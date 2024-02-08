"""
👉 Day 47 Challenge
Alright Top Trumpers. Your program should work like this.

Pick a category. Something popular. You know like 'most handsome computer science teachers'. 😆
Store the information of two different objects in a 2D dictionary.
The key field should be name.
The data in the sub dictionary should be some stats about the object. For example:
Intelligence
Handsomeness
L33t c0ding skillz
Baldness level
Use an infinite loop to get the user to pick one of the two cards, then pick a stat from that card.
Display the chosen stat for both cards and output which has won.
🥳 Extra points for:

Making the dictionary dynamic so you can add your own cards.
Using a loop to play the game in a 2 player format, keeping track of points scored.
Example:

🌟Top Trumps🌟
Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator
Choose your card: 1 - Mr. Morgan  2 - Mr.Colley 
> 1
Choose your stat:
1. Intelligence
2. Handsomeness
3. L33t c0ding skillz
4. Baldness level
> 4
Mr. Morgan has a baldness stat of 99
Mr. Colley has a baldness stat of -68
************* Mr Morgan wins! ********
Again? y/n > n
Hints:
If you're adding your own cards dynamically, try using the random.choice() function to 'draw' two cards from the deck.
"""

import os, random, time

cards = {
    "alice": {
        "lesbianisim": 50,
        "toxicity": 75,
        "crazyness": 75,
        "slutness": 50,
    },
    "bette": {
        "lesbianisim": 100,
        "toxicity": 60,
        "crazyness": 50,
        "slutness": 60,
    },
    "carmen": {
        "lesbianisim": 95,
        "toxicity": 85,
        "crazyness": 75,
        "slutness": 75,
    },
    "dana": {
        "lesbianisim": 100,
        "toxicity": 60,
        "crazyness": 60,
        "slutness": 60,
    },
    "dylan": {
        "lesbianisim": random.randint(0, 75),
        "toxicity": random.randint(0, 75),
        "crazyness": random.randint(0, 75),
        "slutness": random.randint(0, 75),
    },
    "helena": {
        "lesbianisim": 100,
        "toxicity": 95,
        "crazyness": 85,
        "slutness": 85,
    },
    "kit": {
        "lesbianisim": 0,
        "toxicity": 50,
        "crazyness": 60,
        "slutness": 50,
    },
    "jenny": {
        "lesbianisim": 75,
        "toxicity": 100,
        "crazyness": 100,
        "slutness": 95,
    },
    "jodi": {
        "lesbianisim": random.randint(0, 75),
        "toxicity": random.randint(0, 75),
        "crazyness": random.randint(0, 75),
        "slutness": random.randint(0, 75),
    },
    "lara": {
        "lesbianisim": random.randint(0, 75),
        "toxicity": random.randint(0, 75),
        "crazyness": random.randint(0, 75),
        "slutness": random.randint(0, 75),
    },
    "marina": {
        "lesbianisim": 75,
        "toxicity": 90,
        "crazyness": 80,
        "slutness": 80,
    },
    "papi": {
        "lesbianisim": random.randint(0, 75),
        "toxicity": random.randint(0, 75),
        "crazyness": random.randint(0, 75),
        "slutness": random.randint(0, 75),
    },
    "shane": {
        "lesbianisim": 100,
        "toxicity": 40,
        "crazyness": 75,
        "slutness": 100,
    },
    "tasha": {
        "lesbianisim": random.randint(0, 75),
        "toxicity": random.randint(0, 75),
        "crazyness": random.randint(0, 75),
        "slutness": random.randint(0, 75),
    },
    "tina": {
        "lesbianisim": 60,
        "toxicity": 40,
        "crazyness": 40,
        "slutness": 60,
    },
}

listOfCards = list(cards.items())

listOfStats = list(listOfCards[0][1])


def addCard():
    name = input("What's her name?: ").strip().lower()
    try:
        lesbianism = int(input("What's her lesbianism stat?: "))
        toxicity = int(input("What's her toxicity stat?: "))
        crazyness = int(input("What's her crazyness stat?: "))
        slutness = int(input("What's her slutness stat?: "))
    except ValueError:
        print("\nStats must be numbers.")
        addCard()

    if name not in cards:
        cards[name] = {
            "lesbianism": lesbianism,
            "toxicity": toxicity,
            "crazyness": crazyness,
            "slutness": slutness,
        }
    else:
        print("This character already exist on the list.")


def printCards():
    i = 1
    for key in cards.keys():
        print(f"{i}: {key.capitalize()}", end="  ")
        i += 1
    print()


def printStats():
    i = 1
    for item in listOfStats:
        print(f"{i}: {item.capitalize()}", end="  ")
        i += 1
    print()


def fight(c1: int, c2: int, s: int):
    card1 = listOfCards[c1][0]
    card2 = listOfCards[c2][0]
    stat = listOfStats[s]

    print(f"{card1} vs {card2}")
    print(stat)

    c1Stat = cards[card1][stat]
    c2Stat = cards[card2][stat]

    print(f"{card1.capitalize()} has a {stat} of {c1Stat}")
    print(f"{card2.capitalize()} has a {stat} of {c2Stat}")

    if c1Stat > c2Stat:
        print(f"{card1.capitalize()} wins!")
        return 1
    elif c1Stat < c2Stat:
        print(f"{card2.capitalize()} wins!")
        return 2
    else:
        print(f"It's a tie!")
        return 0


# title = "🌟 Top Trumps 🌟"
# text = "Welcome to the Top Trumps 'Craziest Character in The L Word' Simulator"
# menu = "1: Fight!\n2: Add a Card Character\n"
# print(menu)
# menuInput = int(input("> "))

# printCards()
# addCard()


counter1 = 0
counter2 = 0
while True:
    printCards()
    printStats()
    x = int(input("Card 1? > ")) - 1
    y = int(input("Card 2? > ")) - 1
    z = int(input("Stat? > ")) - 1

    try:
        winner = fight(x, y, z)
    except IndexError:
        print("Choose from the following Character:")
        printCards()
        print("Choose from the following Stats:")
        printStats()

    if winner == 1:
        counter1 += 1
    elif winner == 2:
        counter2 += 1
    else:
        continue

    print(f"Score Player 1: {counter1}")
    print(f"Score Player 2: {counter2}")

    playAgain = input("Again?: y/n > ").strip().lower()
    if playAgain[0] == "y":
        continue
    else:
        break

# card1 = listOfCards[x][0]
# card2 = listOfCards[y][0]
# stat = listOfStats[z]

# print(f"{card1} vs {card2}")
# print(stat)

# c1Stat = cards[card1][stat]
# c2Stat = cards[card2][stat]

# print(f"{card1.capitalize()} has a {stat} of {c1Stat}")
# print(f"{card2.capitalize()} has a {stat} of {c2Stat}")

# if c1Stat > c2Stat:
#     print(f"{card1.capitalize()} wins!")
# elif c1Stat < c2Stat:
#     print(f"{card2.capitalize()} wins!")
# else:
#     print(f"It's a tie!")
