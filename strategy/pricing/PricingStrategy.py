"""
package org.nailyourinterview.lld.parking_lot.strategy.pricing;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.time.LocalDateTime;

public interface PricingStrategy {
    double calculateFee(VehicleType type, LocalDateTime entryTime, LocalDateTime exitTime);
}
"""
from abc import ABC, abstractmethod
from enums.VehicleType import VehicleType
from datetime import datetime

class PricingStrategy(ABC):
    @abstractmethod
    def calculateFee(self, vehicleType: VehicleType, entryTime: datetime, exitTime: datetime) -> float:
        pass