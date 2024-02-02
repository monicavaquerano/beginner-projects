"""
👉 Day 36 Challenge
Create a list of people's names. Ask for first and last name (surname) separately.
Strip any extra spaces.
Store names in a capitalized version.
Create a new string using an fString that combines the tidied up version of the first name and tidied up version of the last name.
Add those new versions to a list.
Do not allow duplicates.
Each time you add a new name, you should print out the full list.
"""
import os, time

nameList = [["Adda", "Lovelace"], ["Alan", "Turning"]]


def printList(list):
    print(f"\n{'--- Name List ---': ^35}\n")
    for i in range(len(list)):
        print(f"{i + 1:02d}. {list[i][0]} {list[i][1]}")
    print()


while True:
    os.system("clear")
    menu = input("Name list:\nadd or view?: > ").strip().lower()
    if menu == "add":
        firstName = input("First Name: > ").strip().capitalize()
        lastName = input("Last Name: > ").strip().capitalize()
        full_name = [firstName, lastName]

        if full_name not in nameList:
            nameList.append(full_name)
        else:
            print(f"Error: {firstName} {lastName} is a duplicated name")
        printList(nameList)
        time.sleep(4)
    elif menu == "view":
        printList(nameList)
        time.sleep(4)
    else:
        continue
