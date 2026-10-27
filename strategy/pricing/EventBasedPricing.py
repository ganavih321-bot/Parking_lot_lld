"""
package org.nailyourinterview.lld.parking_lot.strategy.pricing;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.time.Duration;
import java.time.LocalDateTime;
import java.util.Map;

public class EventBasedPricing implements PricingStrategy {
    // Event pricing: Higher per-hour rates
    private static final Map<VehicleType, Double> EVENT_HOURLY_RATES = Map.of(
            VehicleType.CAR, 50.0,
            VehicleType.BIKE, 30.0,
            VehicleType.TRUCK, 70.0
    );

    @Override
    public double calculateFee(VehicleType type, LocalDateTime entryTime, LocalDateTime exitTime) {
        long durationMinutes = Duration.between(entryTime, exitTime).toMinutes();
        long hours = (long) Math.ceil(durationMinutes / 60.0); // always round up to next hour

        double ratePerHour = EVENT_HOURLY_RATES.getOrDefault(type, 0.0);
        return ratePerHour * hours;
    }
}
"""

import math
from datetime import datetime
from enums.VehicleType import VehicleType
from strategy.pricing.PricingStrategy import PricingStrategy


class EventBasedPricing(PricingStrategy):
    EVENT_HOURLY_RATES = {
        VehicleType.CAR: 50.0,
        VehicleType.BIKE: 30.0,
        VehicleType.TRUCK: 70.0
    }

    def calculateFee(self, vehicleType: VehicleType, entryTime: datetime, exitTime: datetime) -> float:
        if exitTime < entryTime:
            raise ValueError("Exit time before entry time")
        durationMinutes = int((exitTime - entryTime).total_seconds() / 60)
        hours = math.ceil(durationMinutes / 60.0)
        ratePerHour = self.EVENT_HOURLY_RATES.get(vehicleType, 0.0)
        return ratePerHour * hours

    