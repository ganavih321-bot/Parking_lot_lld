"""
package org.nailyourinterview.lld.parking_lot.model;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

public class Bike extends Vehicle {
    public Bike(String number) { super(number, VehicleType.BIKE); }
}
"""

from .Vehicle import Vehicle
from enums.VehicleType import VehicleType

class Bike(Vehicle):
    def __init__(self, number):
        super().__init__(number, VehicleType.BIKE)