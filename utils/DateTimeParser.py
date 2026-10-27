"""
package org.nailyourinterview.lld.parking_lot.utils;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class DateTimeParser {
    public static LocalDateTime parse(String input) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("d MMM h:mm a yyyy", Locale.ENGLISH);
        return LocalDateTime.parse(input, formatter);
    }
}
"""


from datetime import datetime


class DateTimeParser:
    @staticmethod
    def parse(input: str) -> datetime:
        # Expected format example: "21 May 7:30 AM 2025"
        for fmt in ("%d %b %I:%M %p %Y", "%d %B %I:%M %p %Y", "%Y-%m-%d %H:%M:%S"):
            try:
                return datetime.strptime(input.strip(), fmt)
            except ValueError:
                continue
        raise ValueError(f"Unable to parse date time string: '{input}'")

