"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;
import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.util.concurrent.atomic.AtomicBoolean;

@Getter
@Setter
@RequiredArgsConstructor
public class ParkingSpot {
    private final String id;
    private final VehicleType allowedType;

    private AtomicBoolean occupied = new AtomicBoolean(false);

    // t1 t2
    // false false
    // _     true
    // false


    public boolean tryOccupy() {
        return occupied.compareAndSet(false, true);
    }

    public void vacate() {
        occupied.set(false);
    }

    public boolean isOccupied() {
        return occupied.get();
    }
}
"""
import threading
from enums.VehicleType import VehicleType


class ParkingSpot:
    def __init__(self, id: str, allowedType: VehicleType):
        self.id = id
        self.allowedType = allowedType
        self.occupied = False
        self._lock = threading.Lock()

    def getId(self) -> str:
        return self.id

    def getAllowedType(self) -> VehicleType:
        return self.allowedType

    def tryOccupy(self) -> bool:
        with self._lock:
            if not self.occupied:
                self.occupied = True
                return True
            return False

    def vacate(self):
        with self._lock:
            self.occupied = False

    def isOccupied(self) -> bool:
        with self._lock:
            return self.occupied