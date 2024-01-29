import os, time

myList = []


def printList(list):
    print()
    i = 0
    for item in list:
        i += 1
        print(f"{i:02d} - {item: >3}")
    print()


while True:
    menu = input("\nView, add, remove or edit?: ").lower().strip()
    if menu == "view":
        printList(myList)
    elif menu == "add":
        item = input("\nWhat should I add to the list?: ").lower().strip()
        myList.append(item)
    elif menu == "remove":
        item = input("\nWhat should I remove from the list?: ").lower().strip()
        if item not in myList:
            print(f"\n{item} not in the list")
        else:
            myList.remove(item)
    elif menu == "edit":
        item = input("\nWhat should I edit from the list?: ").lower().strip()
        if item not in myList:
            print(f"\n{item} not in the list")
        else:
            newItem = input("What should it be?: ").lower().strip()
            myList[item] = newItem
    else:
        continue
