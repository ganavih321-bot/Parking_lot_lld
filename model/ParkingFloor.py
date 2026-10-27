"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.Getter;
import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.util.HashMap;
import java.util.Map;

@Getter
public class ParkingFloor {
    private final String id;
    private final Map<String, ParkingSpot> spots = new HashMap<>();

    public ParkingFloor(String id) { this.id = id; }

    public void addSpot(ParkingSpot spot) {
        spots.put(spot.getId(), spot);
    }

    public ParkingSpot findAvailableSpot(VehicleType vehicleType) {
        for (ParkingSpot spot : spots.values()) {
            if (spot.getAllowedType() == vehicleType && spot.tryOccupy()) {
                return spot;
            }
        }
        return null;
    }
}
"""

from typing import Dict, Optional
from model.ParkingSpot import ParkingSpot
from enums.VehicleType import VehicleType


class ParkingFloor:
    def __init__(self, id: str):
        self.id = id
        self.spots: Dict[str, ParkingSpot] = {}

    def getId(self) -> str:
        return self.id

    def getSpots(self) -> Dict[str, ParkingSpot]:
        return self.spots

    def addSpot(self, spot: ParkingSpot):
        self.spots[spot.getId()] = spot

    def findAvailableSpot(self, vehicleType: VehicleType) -> Optional[ParkingSpot]:
        for spot in self.spots.values():
            if spot.getAllowedType() == vehicleType and spot.tryOccupy():
                return spot
        return None