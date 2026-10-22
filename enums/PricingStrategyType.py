"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum PricingStrategyType {
    TIME_BASED, EVENT_BASED
}
"""
from enum import Enum
class PricingStrategyType(Enum):
    TIME_BASED="time_based"
    EVENT_BASED="event_based"