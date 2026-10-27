"""
package org.nailyourinterview.lld.parking_lot.model;

import org.nailyourinterview.lld.parking_lot.enums.GateType;
import org.nailyourinterview.lld.parking_lot.enums.PaymentMode;
import org.nailyourinterview.lld.parking_lot.service.ParkingLot;

import java.time.LocalDateTime;

public class ExitGate extends Gate {

    public ExitGate(String id) {
        super(id);
    }

    @Override
    public GateType getType() {
        return GateType.EXIT;
    }

    public void unparkVehicle(String ticketId, LocalDateTime exitTime, PaymentMode paymentMode) {
        ParkingLot.getInstance().unparkVehicle(ticketId, exitTime, paymentMode);
    }
}
"""

from datetime import datetime
from model.Gate import Gate
from enums.GateType import GateType
from enums.PaymentMode import PaymentMode


class ExitGate(Gate):
    def __init__(self, id: str):
        super().__init__(id)

    def getType(self) -> GateType:
        return GateType.EXIT

    def unparkVehicle(self, ticketId: str, exitTime: datetime, paymentMode: PaymentMode):
        from service.ParkingLot import ParkingLot
        ParkingLot.getInstance().unparkVehicle(ticketId, exitTime, paymentMode)