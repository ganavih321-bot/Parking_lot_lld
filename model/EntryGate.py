"""
package org.nailyourinterview.lld.parking_lot.model;

import org.nailyourinterview.lld.parking_lot.enums.GateType;
import org.nailyourinterview.lld.parking_lot.service.ParkingLot;
import java.time.LocalDateTime;


public class EntryGate extends Gate {

    public EntryGate(String id) {
        super(id);
    }

    @Override
    public GateType getType() {
        return GateType.ENTRY;
    }

    public Ticket parkVehicle(Vehicle vehicle, LocalDateTime entryTime) {
        return ParkingLot.getInstance().parkVehicle(vehicle, entryTime);
    }
}
"""

from datetime import datetime
from typing import Optional
from .Gate import Gate
from ..enums.GateType import GateType
from .Vehicle import Vehicle
from .Ticket import Ticket


class EntryGate(Gate):
    def __init__(self, id: str):
        super().__init__(id)

    def getType(self) -> GateType:
        return GateType.ENTRY

    def parkVehicle(self, vehicle: Vehicle, entryTime: datetime) -> Optional[Ticket]:
        from ..service.ParkingLot import ParkingLot
        return ParkingLot.getInstance().parkVehicle(vehicle, entryTime)