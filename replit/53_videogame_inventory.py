"""
Video Game Inventory
Oh yes! It's classic RPG inventory system time.

Chug a 'stamina potion' and head to the challenge page for full details.

👉 Day 53 Challenge
Your video game inventory system should:

Have a menu that allows the user to:
Add
View
Remove
Adding an item saves it to a file using captalize mode. Duplicates are allowed.
Removing an item deletes it from the file.
View is trickier. It should output the name of the item and tell you how many of those items you have.
Use auto-save and auto-load with try... except.
Example:

🌟RPG Inventory🌟
1: Add  2: Remove  3: View  > 1
Input the item to add: > Mana potion
Mana potion has been added to your inventory.
1: Add  2: Remove  3: View  > 2
Input the item to remove: > Sword
Sword has been removed from your inventory.
1: Add  2: Remove  3: View  > 3
Input the item to view: > Wizard's sleeve
You have 2 Wizard's sleeve

Hints:
* Use the count() function when viewing an item.
"""

import os, time

inventory = []
# Load
try:
    f = open("inventory.txt", "r")
    inventory = eval(f.read())
    f.close()
except FileNotFoundError:
    pass

while True:
    os.system("clear")
    print("🌟 RPG Inventory 🌟\n")
    menuInput = input("1: Add  2: Remove  3: View  > ").strip().lower()
    if menuInput == "1" or menuInput[0] == "a":
        item = input("Input the item to add: > ").strip().lower()
        inventory.append(item)
        # Write
        f = open("inventory.txt", "w")
        f.write(str(inventory))
        f.close()
        print(f"\n{item.title()} has been added to your inventory.")
        time.sleep(2)
    elif menuInput == "2" or menuInput[0] == "r":
        item = input("Input the item to remove: > ").strip().lower()
        if item in inventory:
            inventory.remove(item)
            # Write
            f = open("inventory.txt", "w")
            f.write(str(inventory))
            f.close()
            print(f"\n{item.title()} has been removed from your inventory.")
        else:
            print(f"\n{item.title()} not in your inventory.")
        time.sleep(2)
    elif menuInput == "3" or menuInput[0] == "w":
        item = input("Input the item to view: > ").strip().lower()
        quantity = inventory.count(item)
        print(f"You have {quantity} {item.title()}")
        time.sleep(2)
    else:
        print("Bye!")
        break
