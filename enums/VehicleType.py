"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum VehicleType {
    CAR, BIKE, TRUCK
}
"""
from enum import Enum
class VehicleType(Enum):
    CAR="car"
    BIKE="bike"
    TRUCK="truck"