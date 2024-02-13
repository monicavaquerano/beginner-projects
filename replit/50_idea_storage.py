"""
Idea Maker...
Do you have brilliant ideas at inconvenient times? Do you need a handy way of storing those ideas? Have you never heard of smartphone voice note apps? Or pens and paper? Then, today's project is for you!

Head on over to the challenge page for all the amazing details.
------------------------------------------------------------------------
👉 Day 50 Challenge
Day 50! Boy, you are smashing this 100 days! 🎊 To celebrate, here's a project for you.

Your idea storage system should:

1. Prompt the user to add an idea, or load a random one.
2. Choosing 'Add an idea' results in:
    i. A prompt for the user to input their idea.
    ii. Add the idea to a text file called 'my.ideas'.
    iii. Add the idea in append mode, with every new idea on a brand new line.
3. Choosing 'Load random' results in:
    i. Load the list of ideas.
    ii. Choose one at random.
    iii. Display it on screen for a few seconds.
    iv. Return to the menu.

Example:

🌟Idea Storage🌟
Add an idea or see a random idea? a/r. > r
Monkey tennis.
Add an idea or see a ranmdom idea? a/r. > a
Input your idea. > Youth hostelling with Chris Eubank
Nice! Your idea has been stored.

Hints:
* To pick an idea at random, you could use split() to get an array of values. Or you could use random.choice to generate a random number and keep loading lines until you get to the random number line.
* Try implementing your menu as a subroutine, so you can call it whenever you need to return to it.
"""

import os, time, random

mainMenu = "1: Add an idea\n2: Load up a random idea\n3: Exit"


def addIdea():
    f = open("my.ideas", "a+")
    idea = input("Add your idea: > ").strip()
    f.write(f"{idea}\n")
    f.close()
    print("\nYour idea was successfully added.")


def loadIdeas():
    try:
        f = open("my.ideas", "r")
    except FileNotFoundError:
        return
    while True:
        fileContent = f.readline().strip()
        if fileContent == "":
            break
        ideas.append(fileContent)
    f.close()


while True:
    ideas = []
    loadIdeas()
    os.system("clear")
    print("=== Idea Storage System ===")
    print(mainMenu)
    menuInput = input("> ").strip()
    if menuInput == "1":
        os.system("clear")
        print("=== Add Idea ===")
        addIdea()
        time.sleep(2)
    elif menuInput == "2":
        while True:
            os.system("clear")
            print("=== Random Idea ===")
            try:
                randomIdea = random.choice(ideas)
                print(f"\n{randomIdea}")
            except IndexError:
                print("\nIdeas' list is empy. Add an idea first.")
            finally:
                againInput = (
                    input("\nLoad another random idea? y/n? > ").strip().lower()
                )
                if againInput[0] == "y":
                    continue
                else:
                    break
        time.sleep(1)
    elif menuInput == "3":
        break
    else:
        continue
