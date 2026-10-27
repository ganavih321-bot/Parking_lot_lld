"""
package org.nailyourinterview.lld.parking_lot.factory;

import org.nailyourinterview.lld.parking_lot.enums.PaymentMode;
import org.nailyourinterview.lld.parking_lot.strategy.payment.*;

public class PaymentStrategyFactory {
    public static PaymentStrategy get(PaymentMode mode) {
        return switch (mode) {
            case CASH -> new CashPayment();
            case UPI -> new UpiPayment();
            case CARD -> new CardPayment();
        };
    }
}
"""
from enums.PaymentMode import PaymentMode
from strategy.payment.PaymentStrategy import PaymentStrategy
from strategy.payment.CashPayment import CashPayment
from strategy.payment.UpiPayment import UpiPayment
from strategy.payment.CardPayment import CardPayment


class PaymentStrategyFactory:
    @staticmethod
    def get(mode: PaymentMode) -> PaymentStrategy:
        if mode == PaymentMode.CASH:
            return CashPayment()
        elif mode == PaymentMode.UPI:
            return UpiPayment()
        elif mode == PaymentMode.CARD:
            return CardPayment()
        else:
            raise ValueError("Invalid payment mode")