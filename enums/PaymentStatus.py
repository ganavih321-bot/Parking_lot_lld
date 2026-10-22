"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum PaymentStatus {
    PENDING,
    SUCCESS,
    FAILED
}
"""
from enum import Enum
class PaymentStatus(Enum):
    PENDING="pending"
    SUCCESS="success"
    FAILED="failed"