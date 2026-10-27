"""
package org.nailyourinterview.lld.parking_lot.strategy.pricing;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.temporal.ChronoUnit;

public class TimeBasedPricing implements PricingStrategy {
    // Peak period hours (e.g., 8:00 to 17:00)
    private static final LocalTime PEAK_START = LocalTime.of(8, 0);
    private static final LocalTime PEAK_END = LocalTime.of(17, 0);

    private boolean isPeak(LocalTime time) {
        return !time.isBefore(PEAK_START) && !time.isAfter(PEAK_END);
    }

    @Override
    public double calculateFee(VehicleType type, LocalDateTime entryTime, LocalDateTime exitTime) {
        if (exitTime.isBefore(entryTime)) throw new IllegalArgumentException("Exit time before entry time");

        long durationMinutes = Duration.between(entryTime, exitTime).toMinutes();
        long totalHours = (long) Math.ceil(durationMinutes / 60.0);

        // Count peak hours and non-peak hours by iterating hour by hour
        int peakHours = 0;
        int nonPeakHours = 0;

        LocalDateTime cursor = entryTime.truncatedTo(ChronoUnit.HOURS);
        // If entry time has minutes, consider first hour partially occupied, count as 1 hour anyway (already rounded)
        for (int i = 0; i < totalHours; i++) {
            LocalTime hourStart = cursor.toLocalTime();
            if (isPeak(hourStart)) peakHours++;
            else nonPeakHours++;
            cursor = cursor.plusHours(1);
        }

        double peakRate = switch (type) {
            case CAR -> 30.0;
            case BIKE -> 15.0;
            case TRUCK -> 50.0;
        };

        double nonPeakRate = switch (type) {
            case CAR -> 20.0;
            case BIKE -> 10.0;
            case TRUCK -> 30.0;
        };

        return peakHours * peakRate + nonPeakHours * nonPeakRate;
    }
}
"""
import math
from datetime import datetime, time, timedelta
from enums.VehicleType import VehicleType
from strategy.pricing.PricingStrategy import PricingStrategy


class TimeBasedPricing(PricingStrategy):
    PEAK_START = time(8, 0)
    PEAK_END = time(17, 0)

    def isPeak(self, t: time) -> bool:
        return self.PEAK_START <= t <= self.PEAK_END

    def calculateFee(self, vehicleType: VehicleType, entryTime: datetime, exitTime: datetime) -> float:
        if exitTime < entryTime: raise ValueError("Exit time before entry time")

        durationMinutes = int((exitTime - entryTime).total_seconds() / 60)
        totalHours = math.ceil(durationMinutes / 60.0)

        # Count peak hours and non-peak hours by iterating hour by hour
        peakHours = 0
        nonPeakHours = 0

        cursor = entryTime.replace(minute=0, second=0, microsecond=0)
        for i in range(totalHours):
            hourStart = cursor.time()
            if self.isPeak(hourStart): peakHours += 1
            else: nonPeakHours += 1
            cursor += timedelta(hours=1)

        rates = {
            VehicleType.CAR: (30.0, 20.0),    # (peak, non-peak)
            VehicleType.BIKE: (15.0, 10.0),
            VehicleType.TRUCK: (50.0, 30.0)
        }
        peakRate, nonPeakRate = rates.get(vehicleType, (0.0, 0.0))

        return peakHours * peakRate + nonPeakHours * nonPeakRate