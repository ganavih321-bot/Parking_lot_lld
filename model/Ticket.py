"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.Builder;
import lombok.Data;
import org.nailyourinterview.lld.parking_lot.enums.PaymentStatus;

import java.time.LocalDateTime;

@Data
@Builder
public class Ticket {
    private String ticketId;
    private LocalDateTime entryTime;
    private Vehicle vehicle;
    private String floorId;
    private String spotId;
    private PaymentStatus paymentStatus = PaymentStatus.PENDING;
}
"""
from datetime import datetime
from enums.PaymentStatus import PaymentStatus
from model.Vehicle import Vehicle


class Ticket:
    def __init__(self, ticketId: str, entryTime: datetime, vehicle: Vehicle, floorId: str, spotId: str, paymentStatus: PaymentStatus = PaymentStatus.PENDING):
        self.ticketId = ticketId
        self.entryTime = entryTime
        self.vehicle = vehicle
        self.floorId = floorId
        self.spotId = spotId
        self.paymentStatus = paymentStatus

    def getTicketId(self) -> str:
        return self.ticketId

    def getEntryTime(self) -> datetime:
        return self.entryTime

    def getVehicle(self) -> Vehicle:
        return self.vehicle

    def getFloorId(self) -> str:
        return self.floorId

    def getSpotId(self) -> str:
        return self.spotId

    def getPaymentStatus(self) -> PaymentStatus:
        return self.paymentStatus

    def setPaymentStatus(self, paymentStatus: PaymentStatus):
        self.paymentStatus = paymentStatus