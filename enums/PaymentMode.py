"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum PaymentMode {
    CASH, UPI, CARD
}

"""
from enum import Enum

class PaymentMode(Enum):
    CASH = "cash"
    UPI = "upi"
    CARD = "card"