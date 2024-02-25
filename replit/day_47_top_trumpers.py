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
        "lesbianism": 50,
        "toxicity": 75,
        "crazyness": 75,
        "playerness": 50,
    },
    "bette": {
        "lesbianism": 100,
        "toxicity": 60,
        "crazyness": 50,
        "playerness": 80,
    },
    "carmen": {
        "lesbianism": 95,
        "toxicity": 85,
        "crazyness": 75,
        "playerness": 80,
    },
    "dana": {
        "lesbianism": 100,
        "toxicity": 60,
        "crazyness": 60,
        "playerness": 60,
    },
    "dylan": {
        "lesbianism": random.randint(0, 75),
        "toxicity": random.randint(0, 75),
        "crazyness": random.randint(0, 75),
        "playerness": random.randint(0, 75),
    },
    "helena": {
        "lesbianism": 100,
        "toxicity": 95,
        "crazyness": 85,
        "playerness": 85,
    },
    "kit": {
        "lesbianism": 0,
        "toxicity": 50,
        "crazyness": 60,
        "playerness": 75,
    },
    "jenny": {
        "lesbianism": 75,
        "toxicity": 100,
        "crazyness": 100,
        "playerness": 55,
    },
    "jodi": {
        "lesbianism": random.randint(0, 75),
        "toxicity": random.randint(0, 75),
        "crazyness": random.randint(0, 75),
        "playerness": random.randint(0, 75),
    },
    "lara": {
        "lesbianism": random.randint(0, 75),
        "toxicity": random.randint(0, 75),
        "crazyness": random.randint(0, 75),
        "playerness": random.randint(0, 75),
    },
    "marina": {
        "lesbianism": 75,
        "toxicity": 90,
        "crazyness": 80,
        "playerness": 85,
    },
    "papi": {
        "lesbianism": random.randint(0, 75),
        "toxicity": random.randint(0, 75),
        "crazyness": random.randint(0, 75),
        "playerness": random.randint(0, 75),
    },
    "shane": {
        "lesbianism": 100,
        "toxicity": 40,
        "crazyness": 75,
        "playerness": 100,
    },
    "tasha": {
        "lesbianism": random.randint(0, 75),
        "toxicity": random.randint(0, 75),
        "crazyness": random.randint(0, 75),
        "playerness": random.randint(0, 75),
    },
    "tina": {
        "lesbianism": 60,
        "toxicity": 40,
        "crazyness": 40,
        "playerness": 75,
    },
}


def addCard():
    while True:
        try:
            name = input("What's her name?: ").strip().lower()
            lesbianism = int(input("What's her lesbianism stat?: "))
            toxicity = int(input("What's her toxicity stat?: "))
            crazyness = int(input("What's her crazyness stat?: "))
            playerness = int(input("What's her playerness stat?: "))
            break
        except ValueError:
            print("\nStats must be numbers.\n")
            continue
        except UnboundLocalError:
            print("\nYou must enter a number.\n")
            continue

    if name not in cards:
        cards[name] = {
            "lesbianism": lesbianism,
            "toxicity": toxicity,
            "crazyness": crazyness,
            "playerness": playerness,
        }
        print("\nNew card was added successfully!")
    else:
        print("\nThis character already exist on the list.")


def printCards():
    i = 1
    for key in cards.keys():
        print(f"{i:>2}: {key.capitalize()}")
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

    os.system("clear")

    print(f"========== Ultimate Match ==========")
    print(f"\n******** {card1.capitalize()} vs {card2.capitalize()} ********")
    print(f"********* on {stat} *********\n")

    c1Stat = cards[card1][stat]
    c2Stat = cards[card2][stat]

    time.sleep(1)

    print(f"> {card1.capitalize()} has a {stat} of: {c1Stat:>3}")
    print(f"> {card2.capitalize()} has a {stat} of: {c2Stat:>3}")

    time.sleep(1)

    if c1Stat > c2Stat:
        print(f"\n******** {card1.capitalize()} wins! ********\n")
        return 1
    elif c1Stat < c2Stat:
        print(f"\n******** {card2.capitalize()} wins! ********\n")
        return 2
    else:
        print(f"\n******** It's a tie! ********\n")
        return 0


def fightHandler(human: bool):
    while True:
        try:
            p1 = int(input("\nP1 choose your character? e.g. 2 for Bette > ")) - 1
            if human == True:
                p2 = int(input("\nP2 choose your character? e.g. 15 for Tina > ")) - 1
            else:
                p2 = random.randint(0, len(listOfCards))
            stat = int(input("\nStat? e.g. 1 for lesbianism > ")) - 1
            winner = fight(p1, p2, stat)
            return winner
        except IndexError:
            print("\nInput must a number on the list")
            continue
        except ValueError:
            print("\nInput must be a number e.g. 1 or 2")
            continue


def printMainMenu():
    title = "🌟 Top Trumps 🌟"
    text = "Welcome to the Top Trumps 'Craziest Character in The L Word' Simulator"
    menu = "--- Main Menu ---\n1: Fight a friend!\n2: Fight the computer!\n3: Add a Card Character\n4: Exit"
    print(f"{title:^70}")
    print(f"{text:^70}\n")
    print(f"{menu}")


while True:
    listOfCards = list(cards.items())
    listOfStats = list(listOfCards[0][1])
    counter1 = 0
    counter2 = 0
    winner = 0

    os.system("clear")
    printMainMenu()
    menuInput = (input("> ")).strip()

    if menuInput == "1":
        while True:
            os.system("clear")
            print("--- Fight a friend ---\nChoose from the following Character:")
            printCards()
            print("Choose from the following Stats:")
            printStats()
            winner = fightHandler(True)
            if winner == 1:
                counter1 += 1
            elif winner == 2:
                counter2 += 1
            else:
                pass

            time.sleep(1)
            print(f"Score Player 1: {counter1}\nScore Player 2: {counter2}")
            time.sleep(1)
            againInput = input(
                "\nPlay again or go back to Main Menu?\n1: Play again.\n2: Main menu.\n> "
            )
            if againInput == "1":
                continue
            else:
                break

    elif menuInput == "2":
        while True:
            os.system("clear")
            print("--- Fight the computer ---\nChoose from the following Character:")
            printCards()
            print("Choose from the following Stats:")
            printStats()
            winner = fightHandler(False)
            if winner == 1:
                counter1 += 1
            elif winner == 2:
                counter2 += 1
            else:
                pass

            time.sleep(1)
            print(f"Score Player 1: {counter1}\nScore Player 2: {counter2}")
            time.sleep(1)
            againInput = input(
                "\nPlay again or go back to Main Menu?\n1: Play again.\n2: Main menu.\n> "
            )
            if againInput == "1":
                continue
            else:
                break

    elif menuInput == "3":
        os.system("clear")
        print("--- Fight the computer ---\n")
        addCard()
        time.sleep(2)
        continue
    elif menuInput == "4":
        break
    else:
        continue
