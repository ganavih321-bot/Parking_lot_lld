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

class Ticket:
    def __init__(self, ticketId, entryTime, vehicle, floorId, spotId, paymentStatus):
        self.ticketId = ticketId
        self.entryTime = entryTime
        self.vehicle = vehicle
        self.floorId = floorId
        self.spotId = spotId
        self.paymentStatus = paymentStatus