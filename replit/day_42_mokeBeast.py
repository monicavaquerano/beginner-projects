"""
Gotta Catch 'Em All....
And Put Them In A Dictionary
This challenge is all about using dictionaries to create a game about small creatures that you have captured, enslaved, and forced to fight for your amusement. You monster.

This game works in a completely non-copyright and totally lawyer friendly way. Pika-who? I have absolutely no idea what you mean..... officer.

👉 Day 42 Challenge
"Some trainers have no fear. To them, this is just one more challenge".

Create a dictionary to store the details of your, ahem, MokéBeast.
Ask the user to input the following details: name, type (earth, fire, air, water or spirit), special move, starting HP and starting MP. For now we're just taking in one set of values for one beast.
Output the beast's details.
Check the beast's type and change the color of the text accordingly. Fire is red, water is blue, air is white. You decide on the others.
🥳 Extra points for getting all the inputs with just one input command and the split function.

👉 IMPORTANT INFO - keep a note of where this Repl is, you'll need it in a couple of lessons' time.

Example:

👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾
Input your beast's name > Brian
Input your beast's type > Earth
Input your beast's special move > Flying bellyflop
Input your beast's staring HP > 50
Input your beast's staring MP > 20
# This text outputs in green
Your beast is called Brian. It is an earth beast with a special move of Flying bellyflop

Hints:
Start with your dictionary.
You will need a for loop.
Change the font color for the beast's type by using if statements.
Change font color using print("\033[XXm", end="") - replace the XX with a color code.
"""
import os, time


mokeBeast = {"name": None, "type": None, "special move": None, "hp": None, "mp": None}


def typeColor(str):
    types = [
        ["normal", "\033[0;30m"],
        ["fire", "\033[0;31m"],
        ["plant", "\033[0;32m"],
        ["ground", "\033[0;33m"],
        ["water", "\033[0;34m"],
        ["poison", "\033[0;35m"],
        ["ice", "\033[0;36m"],
        ["steel", "\033[0;37m"],
        ["rock", "\033[1;30m"],
        ["fight", "\033[1;31m"],
        ["insect", "\033[1;32m"],
        ["electric", "\033[1;33m"],
        ["dragon", "\033[1;34m"],
        ["ghost", "\033[1;35m"],
        ["psychic", "\033[1;36m"],
        ["fly", "\033[1;37m"],
        ["dark", "\033[7m"],
        ["END", "\033[0m"],
    ]

    for type in types:
        if mokeBeast["type"] == type[0]:
            return f"{type[1]}{str}\033[0m"
    return str


while True:
    os.system("clear")
    for key in mokeBeast.keys():
        if key == "hp" or key == "mp":
            print(f"{'--- Mokedex ---':^35}")
            mokeBeast[key] = (
                input(f"Input your beast's {key.upper()}: > ").strip().lower()
            )
            time.sleep(1)
            os.system("clear")
        else:
            print(f"{'--- Mokedex ---':^35}")
            mokeBeast[key] = (
                input(f"Input your beast's {key.title()}: > ").strip().lower()
            )
            time.sleep(1)
            os.system("clear")

    print(f"{typeColor('--- Mokedex ---'):^35}")
    for key, value in mokeBeast.items():
        if key == "hp" or key == "mp":
            print(typeColor(f"{key.upper():<15}: {value.title():}"))
        else:
            print(typeColor(f"{key.title():<15}: {value.title():}"))

    again = input("\nAdd another MokeBeast?: y/n > ").strip().lower()

    if again == "y":
        time.sleep(1)
        continue
    else:
        break


# types = {
#     {"normal": "\033[0;30m"},
#     {"fire": "\033[0;31m"},
#     {"plant": "\033[0;32m"},
#     {"ground": "\033[0;33m"},
#     {"water": "\033[0;34m"},
#     {"poison": "\033[0;35m"},
#     {"ice": "\033[0;36m"},
#     {"steel": "\033[0;37m"},
#     {"rock": "\033[1;30m"},
#     {"fight": "\033[1;31m"},
#     {"insect": "\033[1;32m"},
#     {"electric": "\033[1;33m"},
#     {"dragon": "\033[1;34m"},
#     {"ghost": "\033[1;35m"},
#     {"psychic": "\033[1;36m"},
#     {"fly": "\033[1;37m"},
#     {"dark": "\033[7m"},
#     {"END": "\033[0m"},
# }
