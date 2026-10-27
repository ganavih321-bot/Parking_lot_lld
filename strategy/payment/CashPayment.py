"""
package org.nailyourinterview.lld.parking_lot.strategy.payment;

import org.nailyourinterview.lld.parking_lot.model.Ticket;

public class CashPayment implements PaymentStrategy {
    @Override
    public boolean processPayment(Ticket ticket, double amount) {
        System.out.println("Paid ₹" + amount + " for ticket " + ticket.getTicketId() + " via Cash.");
        return true;
    }
}
"""
from model.Ticket import Ticket
from strategy.payment.PaymentStrategy import PaymentStrategy


class CashPayment(PaymentStrategy):
    def processPayment(self, ticket: Ticket, amount: float) -> bool:
        try:
            print(f"Paid ₹{amount} for ticket {ticket.getTicketId()} via Cash.")
        except UnicodeEncodeError:
            print(f"Paid Rs. {amount} for ticket {ticket.getTicketId()} via Cash.")
        return True