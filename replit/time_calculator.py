def add_time(start, duration, weekday=None):
    WEEKDAYS = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    # Initial hour
    total_hour, meridian = start.split(" ")
    hour, minutes = total_hour.split(":")

    if meridian.lower() == "am":
        hour = int(hour)
    elif meridian.lower() == "pm":
        hour = int(hour) + 12

    # Duration
    duration_hour, duration_minutes = duration.split(":")

    # New time
    new_hour = hour + int(duration_hour)
    new_minutes = int(minutes) + int(duration_minutes)
    new_meridian = ""

    if new_minutes == 60:
        new_hour += 1
        new_minutes = 0
    elif new_minutes > 60:
        new_hour += 1
        new_minutes = int(new_minutes) % 60

    # Days
    days = new_hour // 24

    # New hour
    new_hour = new_hour - (days * 24)

    if 0 <= new_hour < 12:
        new_meridian = "AM"
    elif 12 <= new_hour <= 23:
        new_meridian = "PM"
    elif new_hour == 24:
        new_meridian = "AM"

    if new_hour == 0:
        new_hour = 12
    elif new_hour > 12:
        new_hour = new_hour % 12

    # Weekday
    if weekday:
        day_index = WEEKDAYS.index(weekday.lower())
        new_weekday = WEEKDAYS[(day_index + days) % 7].capitalize()
    else:
        new_weekday = None

    new_minutes = f"{new_minutes:02d}"

    # Return new time
    if days == 1:
        new_time = (
            f"{new_hour}:{new_minutes} {new_meridian}, {new_weekday} (next day)"
            if new_weekday
            else f"{new_hour}:{new_minutes} {new_meridian} (next day)"
        )
    elif days > 1:
        new_time = (
            f"{new_hour}:{new_minutes} {new_meridian}, {new_weekday} ({days} days later)"
            if new_weekday
            else f"{new_hour}:{new_minutes} {new_meridian} ({days} days later)"
        )
    else:
        new_time = (
            f"{new_hour}:{new_minutes} {new_meridian}, {new_weekday}"
            if new_weekday
            else f"{new_hour}:{new_minutes} {new_meridian}"
        )

    return new_time


print(add_time("11:59 PM", "24:05"))
# Returns: 12:04 AM (2 days later)

print(add_time("11:59 PM", "24:05", "Wednesday"))
# Returns: '12:04 AM, Friday (2 days later)

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("3:00 PM", "48:10"))
# Returns: 00:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
