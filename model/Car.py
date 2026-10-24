"""
package org.nailyourinterview.lld.parking_lot.model;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

public class Car extends Vehicle {
    public Car(String number) { super(number, VehicleType.CAR); }
}
"""
from .Vehicle import Vehicle
from enums.VehicleType import VehicleType

class Car(Vehicle):
    def __init__(self, number):
        super().__init__(number, VehicleType.CAR)