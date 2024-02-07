"""
👉 Day 46 Challenge
Today, you're going to program a full on Mokébeast Mokédex. Yep, think we're getting away with it so far...
Don't forget, you can reuse your code from Day 42 here.

Your Mokédex should:

Store multiple Mokébeasts using a loop.
Get user input of the beasts' details.
Add the details to a 2D dictionary.
Repeat until the user wants to stop.
Output the full Mokédex using a prettyPrint() function.
Example:

🌟MokeBeast Generator🌟
Input the beast name > PikaWho?
Input the beast element > Air
Input the beast special move > Shaved fish
Input the beast starting HP > 50
Input the beast starting MP > 50
Again? y/n > n
name: PikaWho? |  element: Air  |  special move: Shaved Fish  |  HP: 50  | MP: 50
"""

import os, time


mokeBeasts = {
    "pikachu": {"type": "electric", "hp": "500", "mp": "500"},
    "charmander": {"type": "fire", "hp": "500", "mp": "500"},
    "squirtle": {"type": "water", "hp": "500", "mp": "500"},
    "bulbasaur": {"type": "plant", "hp": "500", "mp": "500"},
}


def addMokebeast():
    print(f"{'--- Add a MokéBeast to the MokéDex ---':^60}\n")
    name = input("Add the name: > ").strip().lower()
    type = input("Add the type: > ").strip().lower()
    hp = input("Add the HP: > ").strip().lower()
    mp = input("Add the MP: > ").strip().lower()
    mokeBeasts[name] = {"type": type, "hp": hp, "mp": mp}


def printMokedex():
    print(f"\n{'MokéDex':^60}\n")
    print(f"|{'Name':^30}|{'Type':^10}|{'HP':^10}|{'MP':^10}|")
    print(f"{'================================================================':^60}")
    for key, value in mokeBeasts.items():
        print(f"|{key.capitalize():^30}", end="|")
        for subvalue in value.values():
            print(f"{subvalue.capitalize():^10}", end="|")
        print()


while True:
    os.system("clear")

    addMokebeast()

    printMokedex()

    again = input("\nAdd another MokeBeast?: y/n > ").strip().lower()
    if again == "y":
        time.sleep(1)
        continue
    else:
        break
