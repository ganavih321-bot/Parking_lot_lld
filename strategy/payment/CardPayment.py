"""
package org.nailyourinterview.lld.parking_lot.strategy.payment;

import org.nailyourinterview.lld.parking_lot.model.Ticket;

public class CardPayment implements PaymentStrategy {
    @Override
    public boolean processPayment(Ticket ticket, double amount) {
        System.out.println("Paid ₹" + amount + " for ticket " + ticket.getTicketId() + " via Card.");
        return true;
    }
}
"""
from model.Ticket import Ticket
from strategy.payment.PaymentStrategy import PaymentStrategy

class CardPayment(PaymentStrategy):
    def processPayment(self, ticket: Ticket, amount: float) -> bool:
        try:
            print(f"Paid ₹{amount} for ticket {ticket.getTicketId()} via Card.")
        except UnicodeEncodeError:
            print(f"Paid Rs. {amount} for ticket {ticket.getTicketId()} via Card.")
        return True