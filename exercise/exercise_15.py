def add_time(start, duration, start_day=None):
    """Add a duration to a start time and return the resulting time string."""

    # Parse start time
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(":"))

    # Convert to 24-hour format for easier calculation
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Parse duration
    dur_hour, dur_minute = map(int, duration.split(":"))

    # Add minutes first
    total_minutes = start_minute + dur_minute
    result_minute = total_minutes % 60
    hour_carry = total_minutes // 60

    # Add hours
    total_hours = start_hour + dur_hour + hour_carry
    result_hour_24 = total_hours % 24
    days_later = total_hours // 24

    # Convert back to 12-hour format
    if result_hour_24 == 0:
        result_hour = 12
        result_period = "AM"
    elif result_hour_24 < 12:
        result_hour = result_hour_24
        result_period = "AM"
    elif result_hour_24 == 12:
        result_hour = 12
        result_period = "PM"
    else:
        result_hour = result_hour_24 - 12
        result_period = "PM"

    # Format the time string
    new_time = f"{result_hour}:{result_minute:02d} {result_period}"

    # Handle day of week if provided
    if start_day:
        days_of_week = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]
        start_day_index = days_of_week.index(start_day.lower())
        result_day_index = (start_day_index + days_later) % 7
        result_day = days_of_week[result_day_index].capitalize()
        new_time += f", {result_day}"

    # Add day information
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
