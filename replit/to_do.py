import os, time
from colorful import colorful

myList = []


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
    title = "\033[7m=== To-Do List ===\033[0m"
    print(f"{title: ^35}")
    menu = (
        input(
            f"\n{colorful('purple','View')}, {colorful('green','add')}, {colorful('red','remove')} or {colorful('blue','edit')}?: "
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
            print(f"\n{item} not in the list")
            print("\033[?25l")
            time.sleep(2)
        else:
            myList.remove(item)
            print(f"{colorful('red', 'The item was successfully removed!')}")
            print("\033[?25l")
            time.sleep(2)
    elif menu == "edit":
        item = (
            input(f"\n{colorful('blue', 'What should I edit from the list?: ')}")
            .lower()
            .strip()
        )
        if item not in myList:
            print(f"\n{item} not in the list")
            print("\033[?25l")
            time.sleep(2)
        else:
            i = myList.index(item)
            newItem = input("What should it be?: ").lower().strip()
            myList[i] = newItem
            print(f"{colorful('blue', 'The item was successfully edited!')}")
            print("\033[?25l")
            time.sleep(2)
    else:
        continue
