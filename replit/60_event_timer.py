"""
👉 Day 60 Challenge - Datetime
Today's challenge is an events countdown timer.

Your program should:

1. Automatically work out today's date.
2. Prompt the user to input the name and date of their event (year, month and day).
3. Work out the number of days until the event and output it.
4. If the event is happening today, insert some party emojis.
5. If the event was in the past, sad face emojis and tell the user how many days ago it was.

Example:
🌟Event Countdown Timer🌟
Input the event > Nan's 100th birthday
Input the year > 2022
Input the month > 10
Input the day > 16
🎉🎉Nan's 100th birthday is today! 🎉🎉

Hints:
* Subtract today's date from the delta.
* What type of number will you get if the date has passed?
"""

import datetime


def eventTimer():
    today = datetime.date.today()
    print("🎉🎉🌟 Event Countdown Timer 🌟🎉🎉")
    name_event = input("Input the event > ").strip()
    while True:
        try:
            year = int(input("Input the year > "))
            month = int(input("Input the month > "))
            day = int(input("Input the day > "))
            break
        except ValueError:
            print("Dates must be integers (numbers).")

    event_date = datetime.date(year, month, day)
    difference = abs(today - event_date)

    if today > event_date:
        print(f"\n{name_event} was {difference.days} day(s) ago. Hope you enjoyed it.")
    elif today < event_date:
        print(
            f"\n{name_event} is coming soon. Only {difference.days} day(s) left to go."
        )
    else:
        print(f"\n🎉🎉 {name_event} 🎉🎉 is today.")


eventTimer()


# myDate = datetime.date(year=2022, month=12, day=7)

# today = datetime.date.today()
# difference = datetime.timedelta(days=365)
# # difference = datetime.timedelta(weeks=4)
# newDate = today + difference

# print(myDate)
# print(today)
# print(newDate)
