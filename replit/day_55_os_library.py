"""
OS Library

👉 Day 55 Challenge
Back the 'f' up everybody!

'f' is short for 'file', of course. What did you think I meant?

Get your minds out of the gutter, go back and get your auto save/load to do list from Day 51 and use it here.

Your program should:

Create a backup folder.
Create a random filename.
Save a copy of the data to that file.
This should all happen before the auto save.

Hints:
* Use a Boolean variable fileExists set to False to store whether the file has already been created.
* Use if fileExists later on to check the status of the file before creating or writing.
* Use the os.mkdir() function.

# import os

# List a file
# os.listdir() # will allow you to list all the files:

# Create a folder
# os.mkdir("Hello") # Creates a folder called 'Hello'

# Renames a file
# os.rename("myname.txt", "new_name.txt")

# Joins paths
# os.path.join("Hello/","aFile.txt")

# files = os.listdir()
# if "quickSave.txt" not in files:
#     print("Error: QuickSave not found")

"""

import os, time, random

myList = []

# Reads the document if it exists
try:
    f = open("toDoList.txt", "r")
    myList = eval(f.read())
    f.close()
except FileNotFoundError as err:
    print(err)
    pass


def saveList():
    # BackUp Copy First
    files = os.listdir()
    if "55_BackUp" not in files:
        os.mkdir("55_BackUp")

    while True:
        uniqueNumber = ""
        for i in range(10):
            uniqueNumber += str(random.randint(0, 9))

        filename = os.path.join("55_BackUp", f"backup{uniqueNumber}.txt")
        if filename not in os.listdir("55_BackUp"):
            f = open(filename, "w")
            f.write(str(myList))
            f.close()
            break
        else:
            continue

    # Write File
    f = open("toDoList.txt", "w")
    f.write(str(myList))
    f.close()


def colorful(color, word):
    """ANSI color codes"""
    colors = [
        ["BLACK", "\033[0;30m"],
        ["RED", "\033[0;31m"],
        ["GREEN", "\033[0;32m"],
        ["BROWN", "\033[0;33m"],
        ["BLUE", "\033[0;34m"],
        ["PURPLE", "\033[0;35m"],
        ["CYAN", "\033[0;36m"],
        ["LIGHT_GRAY", "\033[0;37m"],
        ["DARK_GRAY", "\033[1;30m"],
        ["LIGHT_RED", "\033[1;31m"],
        ["LIGHT_GREEN", "\033[1;32m"],
        ["YELLOW", "\033[1;33m"],
        ["LIGHT_BLUE", "\033[1;34m"],
        ["LIGHT_PURPLE", "\033[1;35m"],
        ["LIGHT_CYAN", "\033[1;36m"],
        ["LIGHT_WHITE", "\033[1;37m"],
        ["BOLD", "\033[1m"],
        ["FAINT", "\033[2m"],
        ["ITALIC", "\033[3m"],
        ["UNDERLINE", "\033[4m"],
        ["BLINK", "\033[5m"],
        ["NEGATIVE", "\033[7m"],
        ["CROSSED", "\033[9m"],
        ["END", "\033[0m"],
    ]

    for c in colors:
        if color.upper() == c[0]:
            return f"{c[1]}{word}\033[0m"
    return word


def printList(list):
    if len(list) == 0:
        print()
        print(f"{colorful('purple', 'The list is empty!')}")
        print("\033[?25l")
    else:
        print()
        i = 0
        print("\033[0;35m=== MyList ===\033[0m")
        for item in list:
            i += 1
            print(f"\033[0;35m{i:02d}\033[0m - {item: <3}")
    print("\033[?25l")


while True:
    print("\033[?25h", end="")
    os.system("clear")
    title = "\033[7m=== Ultimate To-Do List ===\033[0m"
    print(f"{title: ^35}")
    menu = (
        input(
            f"\n{colorful('purple','1: View')}, {colorful('green','2: Add')}, {colorful('red','3: Remove')}, {colorful('blue','4: Edit')} or {colorful('underline','5: delete all')}?: "
        )
        .lower()
        .strip()
    )
    if menu == "1" or menu[0] == "v":
        printList(myList)
        time.sleep(5)
        os.system("clear")
    elif menu == "2" or menu[0] == "a":
        item = (
            input(f"\n{colorful('green','What should I add to the list?: ')}")
            .lower()
            .strip()
        )
        if item in myList:
            print(f"{colorful('yellow', item)} is already on the list.")
            print("\033[?25l")
            time.sleep(2)
        else:
            myList.append(item)
            print(f"{colorful('green', 'The item was successfully added!')}")
            print("\033[?25l")
            saveList()
            time.sleep(2)
    elif menu == "3" or menu[0] == "r":
        item = (
            input(f"\n{colorful('red','What should I remove from the list?: ')}")
            .lower()
            .strip()
        )
        if item not in myList:
            print(f"{colorful('yellow', item)} not in the list")
            print("\033[?25l")
            time.sleep(2)
        else:
            sure = (
                input(
                    f"Are you sure you want to {colorful('red','remove')} this? {colorful('red','y')}/n > "
                )
                .lower()
                .strip()
            )
            if sure == "y":
                myList.remove(item)
                print(f"{colorful('red', 'The item was successfully removed!')}")
                print("\033[?25l")
                saveList()
                time.sleep(2)
            else:
                print(f"{colorful('yellow', 'The item was not removed!')}")
                print("\033[?25l")
                time.sleep(2)
    elif menu == "4" or menu[0] == "e":
        item = (
            input(f"\n{colorful('blue', 'What should I edit from the list?: ')}")
            .lower()
            .strip()
        )
        if item not in myList:
            print(f"{colorful('yellow',item)} not in the list")
            print("\033[?25l")
            time.sleep(2)
        else:
            i = myList.index(item)
            newItem = input("What should it be?: ").lower().strip()
            myList[i] = newItem
            print(f"{colorful('blue', 'The item was successfully edited!')}")
            print("\033[?25l")
            saveList()
            time.sleep(2)
    elif menu == "5" or menu[0] == "d":
        printList(myList)
        sure = (
            input(
                f"Are you sure you want to {colorful('underline','delete all')}? {colorful('underline','y')}/n\033[?25h > "
            )
            .lower()
            .strip()
        )
        if sure == "y":
            myList = []
            print(f"{colorful('underline', 'The list was successfully deleted!')}")
            print("\033[?25l")
            saveList()
            time.sleep(2)
        else:
            print(f"{colorful('yellow', 'The list was not deleted.')}")
            print("\033[?25l")
            time.sleep(2)
    else:
        continue
