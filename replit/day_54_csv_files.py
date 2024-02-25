"""
CSV
Para el futuro:
print("\t".join(row))

👉 Day 54 Challenge
I've given you a CSV file called 'Day54Totals.csv' (look at your file tree) that contains multiple pieces of data in the fields 'cost' and 'quantity' of items sold. How much money did this shop earn in a day?

Your program should:

Read the CSV file in.
Multiply the cost by the quantity.
Add it all together to calculate how much money the shop made in a day.
Example:

🌟Shop $$ Tracker🌟
Your shop took £592 pounds today.

Hints:
+ Use the dictionary approach to loading your file.
* Take in 2 different values.
* Cast them in 2 different ways.
"""

import csv

total = 0.0

with open("Day54Totals.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        sale = float(row["Cost"]) * int(row["Quantity"])
        total += sale

print("\n🌟 Shop $$ Tracker 🌟")
print(f"Your shop took ${total:,.02f} today.")
