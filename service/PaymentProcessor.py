"""
package org.nailyourinterview.lld.parking_lot.service;

import org.nailyourinterview.lld.parking_lot.enums.PaymentStatus;
import org.nailyourinterview.lld.parking_lot.model.Ticket;
import org.nailyourinterview.lld.parking_lot.strategy.payment.PaymentStrategy;

public class PaymentProcessor {
    private final PaymentStrategy strategy;

    public PaymentProcessor(PaymentStrategy strategy) {
        this.strategy = strategy;
    }

    public boolean pay(Ticket ticket, double amount) {
        boolean success = strategy.processPayment(ticket, amount);
        if (success) {
            ticket.setPaymentStatus(PaymentStatus.SUCCESS);
        } else {
            ticket.setPaymentStatus(PaymentStatus.FAILED);
            System.out.println("Payment failed for ticket: " + ticket.getTicketId());
        }
        return success;
    }
}
"""

from enums.PaymentStatus import PaymentStatus
from model.Ticket import Ticket
from strategy.payment.PaymentStrategy import PaymentStrategy


class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def pay(self, ticket: Ticket, amount: float) -> bool:
        success = self.strategy.processPayment(ticket, amount)
        if success:
            ticket.setPaymentStatus(PaymentStatus.SUCCESS)
        else:
            ticket.setPaymentStatus(PaymentStatus.FAILED)
            print(f"Payment failed for ticket: {ticket.getTicketId()}")
        return success