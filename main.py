"""
package org.nailyourinterview.lld.parking_lot;

import org.nailyourinterview.lld.parking_lot.enums.*;
import org.nailyourinterview.lld.parking_lot.factory.*;
import org.nailyourinterview.lld.parking_lot.model.*;
import org.nailyourinterview.lld.parking_lot.service.*;
import org.nailyourinterview.lld.parking_lot.utils.DateTimeParser;

import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;

public class Main {
    public static void main(String[] args) {
        ParkingLot lot = ParkingLot.getInstance();
        EntryGate entryGate = new EntryGate("EG1");
        ExitGate exitGate = new ExitGate("XG1");

        lot.setPricingStrategy(PricingStrategyFactory.get(PricingStrategyType.valueOf("EVENT_BASED")));

        ParkingFloor floor1 = new ParkingFloor("Floor1");
        floor1.addSpot(new ParkingSpot("F1S1", VehicleType.BIKE));
        floor1.addSpot(new ParkingSpot("F1S2", VehicleType.CAR));
        floor1.addSpot(new ParkingSpot("F1S3", VehicleType.TRUCK));
        floor1.addSpot(new ParkingSpot("F1S4", VehicleType.CAR));
        lot.addFloor(floor1);

        System.out.println("--------------------------");

        Vehicle bike1 = VehicleFactory.create("KA01AB1234", VehicleType.BIKE);
        Vehicle bike2 = VehicleFactory.create("KA01AB5678", VehicleType.BIKE);
        LocalDateTime entryTime = DateTimeParser.parse("21 May 7:30 AM 2025");
        System.out.println(entryTime.truncatedTo(ChronoUnit.HOURS));

        Thread t1 = new Thread(() -> entryGate.parkVehicle(bike1, entryTime));
        Thread t2 = new Thread(() -> entryGate.parkVehicle(bike2, entryTime));

        t1.start();
        t2.start();

//        Vehicle car = VehicleFactory.create("KA01AB1234", VehicleType.SEDAN);
//
//        LocalDateTime entryTime = DateTimeParser.parse("21 May 7:30 AM 2025");
//        Ticket ticket = entryGate.parkVehicle(car, entryTime);
//
//        System.out.println("--------------------------");
//
//        lot.printStatus();
//
//        System.out.println("--------------------------");
//
//        LocalDateTime exitTime = DateTimeParser.parse("21 May 1:15 PM 2025");
//        exitGate.unparkVehicle(ticket.getTicketId(), exitTime, PaymentMode.UPI);
//
//        System.out.println("--------------------------");
//
//        lot.printStatus();
    }
}

/*

 */
"""

import threading
from datetime import datetime

from enums.PaymentMode import PaymentMode
from enums.PricingStrategyType import PricingStrategyType
from enums.VehicleType import VehicleType
from factory.PricingStrategyFactory import PricingStrategyFactory
from factory.VehicleFactory import VehicleFactory
from model.EntryGate import EntryGate
from model.ExitGate import ExitGate
from model.ParkingFloor import ParkingFloor
from model.ParkingSpot import ParkingSpot
from model.Ticket import Ticket
from model.Vehicle import Vehicle
from service.ParkingLot import ParkingLot
from utils.DateTimeParser import DateTimeParser


class Main:
    @staticmethod
    def main():
        lot = ParkingLot.getInstance()
        entryGate = EntryGate("EG1")
        exitGate = ExitGate("XG1")

        lot.setPricingStrategy(PricingStrategyFactory.get(PricingStrategyType["EVENT_BASED"]))

        floor1 = ParkingFloor("Floor1")
        floor1.addSpot(ParkingSpot("F1S1", VehicleType.BIKE))
        floor1.addSpot(ParkingSpot("F1S2", VehicleType.CAR))
        floor1.addSpot(ParkingSpot("F1S3", VehicleType.TRUCK))
        floor1.addSpot(ParkingSpot("F1S4", VehicleType.CAR))
        lot.addFloor(floor1)

        print("--------------------------")

        bike1 = VehicleFactory.create("KA01AB1234", VehicleType.BIKE)
        bike2 = VehicleFactory.create("KA01AB5678", VehicleType.BIKE)
        entryTime = DateTimeParser.parse("21 May 7:30 AM 2025")
        print(entryTime.replace(minute=0, second=0, microsecond=0))

        thread1 = threading.Thread(target=entryGate.parkVehicle, args=(bike1, entryTime))
        thread2 = threading.Thread(target=entryGate.parkVehicle, args=(bike2, entryTime))

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        # Demo for car parking, unparking, and status as present in Java commented code:
        # car = VehicleFactory.create("KA01AB1234", VehicleType.CAR)
        # ticket = entryGate.parkVehicle(car, entryTime)
        # print("--------------------------")
        # lot.printStatus()
        # print("--------------------------")
        # exitTime = DateTimeParser.parse("21 May 1:15 PM 2025")
        # if ticket:
        #     exitGate.unparkVehicle(ticket.getTicketId(), exitTime, PaymentMode.UPI)
        # print("--------------------------")
        # lot.printStatus()


if __name__ == "__main__":
    Main.main()

