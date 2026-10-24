"""
package org.nailyourinterview.lld.parking_lot.strategy.payment;

import org.nailyourinterview.lld.parking_lot.model.Ticket;

public class UpiPayment implements PaymentStrategy {
    @Override
    public boolean processPayment(Ticket ticket, double amount) {
        System.out.println("Paid ₹" + amount + " for ticket " + ticket.getTicketId() + " via UPI.");
        return true;
    }
}
"""
from .PaymentStrategy import PaymentStrategy
from ...model.Ticket import Ticket

class UpiPayment(PaymentStrategy):
    def processPayment(self, ticket: Ticket, amount: float) -> bool:
        print(f"Paid ₹{amount} for ticket {ticket.getTicketId()} via UPI.")
        return True
