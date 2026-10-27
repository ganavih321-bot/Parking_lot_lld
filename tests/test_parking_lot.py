import unittest
import threading
from datetime import datetime, time

from enums.GateType import GateType
from enums.PaymentMode import PaymentMode
from enums.PaymentStatus import PaymentStatus
from enums.PricingStrategyType import PricingStrategyType
from enums.VehicleType import VehicleType

from factory.VehicleFactory import VehicleFactory
from factory.PaymentStrategyFactory import PaymentStrategyFactory
from factory.PricingStrategyFactory import PricingStrategyFactory

from model.Car import Car
from model.Bike import Bike
from model.Truck import Truck
from model.EntryGate import EntryGate
from model.ExitGate import ExitGate
from model.ParkingSpot import ParkingSpot
from model.ParkingFloor import ParkingFloor
from model.Ticket import Ticket

from service.ParkingLot import ParkingLot
from service.PaymentProcessor import PaymentProcessor

from strategy.pricing.TimeBasedPricing import TimeBasedPricing
from strategy.pricing.EventBasedPricing import EventBasedPricing
from strategy.payment.CashPayment import CashPayment
from strategy.payment.CardPayment import CardPayment
from strategy.payment.UpiPayment import UpiPayment

from utils.DateTimeParser import DateTimeParser


class TestParkingLotLLD(unittest.TestCase):

    def test_enums(self):
        self.assertEqual(GateType.ENTRY.value, "ENTRY")
        self.assertEqual(GateType.EXIT.value, "EXIT")
        self.assertEqual(PaymentMode.CASH.value, "CASH")
        self.assertEqual(PaymentMode.UPI.value, "UPI")
        self.assertEqual(PaymentMode.CARD.value, "CARD")
        self.assertEqual(PaymentStatus.PENDING.value, "PENDING")
        self.assertEqual(PaymentStatus.SUCCESS.value, "SUCCESS")
        self.assertEqual(PaymentStatus.FAILED.value, "FAILED")
        self.assertEqual(VehicleType.CAR.value, "CAR")
        self.assertEqual(VehicleType.BIKE.value, "BIKE")
        self.assertEqual(VehicleType.TRUCK.value, "TRUCK")
        self.assertEqual(PricingStrategyType.TIME_BASED.value, "TIME_BASED")
        self.assertEqual(PricingStrategyType.EVENT_BASED.value, "EVENT_BASED")

    def test_vehicle_factory_and_models(self):
        car = VehicleFactory.create("KA011234", VehicleType.CAR)
        self.assertIsInstance(car, Car)
        self.assertEqual(car.getNumber(), "KA011234")
        self.assertEqual(car.getType(), VehicleType.CAR)

        bike = VehicleFactory.create("KA015678", VehicleType.BIKE)
        self.assertIsInstance(bike, Bike)
        self.assertEqual(bike.getNumber(), "KA015678")
        self.assertEqual(bike.getType(), VehicleType.BIKE)

        truck = VehicleFactory.create("KA019999", VehicleType.TRUCK)
        self.assertIsInstance(truck, Truck)
        self.assertEqual(truck.getNumber(), "KA019999")
        self.assertEqual(truck.getType(), VehicleType.TRUCK)

    def test_parking_spot_and_concurrency(self):
        spot = ParkingSpot("S1", VehicleType.CAR)
        self.assertEqual(spot.getId(), "S1")
        self.assertEqual(spot.getAllowedType(), VehicleType.CAR)
        self.assertFalse(spot.isOccupied())

        # Test atomic occupation
        results = []
        def try_occupy():
            results.append(spot.tryOccupy())

        t1 = threading.Thread(target=try_occupy)
        t2 = threading.Thread(target=try_occupy)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        # Exactly one thread must succeed
        self.assertEqual(results.count(True), 1)
        self.assertEqual(results.count(False), 1)
        self.assertTrue(spot.isOccupied())

        spot.vacate()
        self.assertFalse(spot.isOccupied())

    def test_parking_floor(self):
        floor = ParkingFloor("F1")
        self.assertEqual(floor.getId(), "F1")

        spot1 = ParkingSpot("S1", VehicleType.CAR)
        spot2 = ParkingSpot("S2", VehicleType.BIKE)
        floor.addSpot(spot1)
        floor.addSpot(spot2)

        self.assertEqual(len(floor.getSpots()), 2)

        available_car_spot = floor.findAvailableSpot(VehicleType.CAR)
        self.assertIsNotNone(available_car_spot)
        self.assertEqual(available_car_spot.getId(), "S1")
        self.assertTrue(available_car_spot.isOccupied())

        # No more car spot available now
        self.assertIsNone(floor.findAvailableSpot(VehicleType.CAR))

        # Truck spot doesn't exist
        self.assertIsNone(floor.findAvailableSpot(VehicleType.TRUCK))

    def test_ticket_model(self):
        car = Car("KA011111")
        now = datetime.now()
        ticket = Ticket("T1", now, car, "F1", "S1")
        self.assertEqual(ticket.getTicketId(), "T1")
        self.assertEqual(ticket.getEntryTime(), now)
        self.assertEqual(ticket.getVehicle(), car)
        self.assertEqual(ticket.getFloorId(), "F1")
        self.assertEqual(ticket.getSpotId(), "S1")
        self.assertEqual(ticket.getPaymentStatus(), PaymentStatus.PENDING)

        ticket.setPaymentStatus(PaymentStatus.SUCCESS)
        self.assertEqual(ticket.getPaymentStatus(), PaymentStatus.SUCCESS)

    def test_time_based_pricing(self):
        pricing = TimeBasedPricing()
        self.assertTrue(pricing.isPeak(time(8, 0)))
        self.assertTrue(pricing.isPeak(time(12, 0)))
        self.assertTrue(pricing.isPeak(time(17, 0)))
        self.assertFalse(pricing.isPeak(time(7, 59)))
        self.assertFalse(pricing.isPeak(time(18, 0)))

        # 7:30 to 10:30 (3 hours: 7:00-8:00 non-peak, 8:00-9:00 peak, 9:00-10:00 peak)
        entry = datetime(2025, 5, 21, 7, 30)
        exit_time = datetime(2025, 5, 21, 10, 30)
        # Car rate: peak 30, non-peak 20 -> 2*30 + 1*20 = 80
        fee_car = pricing.calculateFee(VehicleType.CAR, entry, exit_time)
        self.assertEqual(fee_car, 80.0)

        # Bike rate: peak 15, non-peak 10 -> 2*15 + 1*10 = 40
        fee_bike = pricing.calculateFee(VehicleType.BIKE, entry, exit_time)
        self.assertEqual(fee_bike, 40.0)

        # Invalid entry/exit time
        with self.assertRaises(ValueError):
            pricing.calculateFee(VehicleType.CAR, exit_time, entry)

    def test_event_based_pricing(self):
        pricing = EventBasedPricing()
        entry = datetime(2025, 5, 21, 10, 0)
        exit_time = datetime(2025, 5, 21, 12, 15)  # 2 hours 15 mins -> 3 hours
        # Car: 50 * 3 = 150
        self.assertEqual(pricing.calculateFee(VehicleType.CAR, entry, exit_time), 150.0)
        # Bike: 30 * 3 = 90
        self.assertEqual(pricing.calculateFee(VehicleType.BIKE, entry, exit_time), 90.0)
        # Truck: 70 * 3 = 210
        self.assertEqual(pricing.calculateFee(VehicleType.TRUCK, entry, exit_time), 210.0)

    def test_payment_strategies_and_processor(self):
        car = Car("KA011111")
        ticket = Ticket("T1", datetime.now(), car, "F1", "S1")

        cash_strat = PaymentStrategyFactory.get(PaymentMode.CASH)
        upi_strat = PaymentStrategyFactory.get(PaymentMode.UPI)
        card_strat = PaymentStrategyFactory.get(PaymentMode.CARD)

        self.assertIsInstance(cash_strat, CashPayment)
        self.assertIsInstance(upi_strat, UpiPayment)
        self.assertIsInstance(card_strat, CardPayment)

        processor = PaymentProcessor(upi_strat)
        success = processor.pay(ticket, 100.0)
        self.assertTrue(success)
        self.assertEqual(ticket.getPaymentStatus(), PaymentStatus.SUCCESS)

    def test_full_parking_lot_flow(self):
        lot = ParkingLot.getInstance()
        floor = ParkingFloor("TestFloor")
        spot_bike = ParkingSpot("TB1", VehicleType.BIKE)
        spot_car = ParkingSpot("TC1", VehicleType.CAR)
        floor.addSpot(spot_bike)
        floor.addSpot(spot_car)
        lot.addFloor(floor)

        entry_gate = EntryGate("EG_TEST")
        exit_gate = ExitGate("XG_TEST")

        entry_time = DateTimeParser.parse("21 May 7:30 AM 2025")
        bike = VehicleFactory.create("KA01BIKE", VehicleType.BIKE)

        ticket = entry_gate.parkVehicle(bike, entry_time)
        self.assertIsNotNone(ticket)
        self.assertEqual(ticket.getSpotId(), "TB1")
        self.assertTrue(spot_bike.isOccupied())

        # Second bike cannot park on same spot
        bike2 = VehicleFactory.create("KA02BIKE", VehicleType.BIKE)
        ticket2 = entry_gate.parkVehicle(bike2, entry_time)
        self.assertIsNone(ticket2)

        # Unpark bike
        exit_time = DateTimeParser.parse("21 May 9:30 AM 2025")
        exit_gate.unparkVehicle(ticket.getTicketId(), exit_time, PaymentMode.CARD)
        self.assertFalse(spot_bike.isOccupied())

    def test_date_time_parser(self):
        dt1 = DateTimeParser.parse("21 May 7:30 AM 2025")
        self.assertEqual(dt1.year, 2025)
        self.assertEqual(dt1.month, 5)
        self.assertEqual(dt1.day, 21)
        self.assertEqual(dt1.hour, 7)
        self.assertEqual(dt1.minute, 30)

        dt2 = DateTimeParser.parse("2025-05-21 14:00:00")
        self.assertEqual(dt2.hour, 14)

        with self.assertRaises(ValueError):
            DateTimeParser.parse("invalid-date-string")


if __name__ == "__main__":
    unittest.main()
