"""
👉 Day 35 Challenge
Build a really cool to do list manager. (I know we did this before...hold on!)

We are going to upgrade the last to do list manager we created:

Create a menu where the user can view, add, or remove an item.
The user should be able to edit the text of an item on the list too.
Don't allow the user to add duplicates.
Double check with the user they want to remove an item from the list before it is actually removed. (Is this the item they really want to remove?)
Give the user the option to completely erase the to do list. (You should be able to do this in one line of code!)
Example:

To Do List Manager:
Do you want to view, add, edit, or remove an item from the to do list?
view
record the video for day 36
Do you want to view, add, edit, or remove an item from the to do list?
remove
What do you want to remove?
record the video for day 36
Are you sure you want to remove this?
yes
"""
import os, time

myList = ["comer", "reir", "rezar"]


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
            f"\n{colorful('purple','View')}, {colorful('green','add')}, {colorful('red','remove')}, {colorful('blue','edit')} or {colorful('underline','delete all')}?: "
        )
        .lower()
        .strip()
    )
    if menu == "view":
        printList(myList)
        time.sleep(5)
        os.system("clear")
    elif menu == "add":
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
            time.sleep(2)
    elif menu == "remove":
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
                time.sleep(2)
            else:
                print(f"{colorful('yellow', 'The item was not removed!')}")
                print("\033[?25l")
                time.sleep(2)
    elif menu == "edit":
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
            time.sleep(2)
    elif menu == "delete all":
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
            time.sleep(2)
        else:
            print(f"{colorful('yellow', 'The list was not deleted.')}")
            print("\033[?25l")
            time.sleep(2)
    else:
        continue
