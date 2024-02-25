"""
Ta Daaaa! It's A To Do
Today is a todo list management system. Wait, we did this? Yes, but your last to do list didn't allow you to store dates or anything besides the actual list.

Your program will store a todo list, and allow you to give each task a priority.

So, what are you waiting for? Item 1, top priority. Head on over to the challenge page for details.

Still here? Stop procrastinating!

👉 Day 45 Challenge
Made it? Good! Let's get cracking.

Your system should:

Have a menu that asks if you want to add, view, move or edit a 'to do'.

If you choose 'add' then the system should:

Prompt you to input what the to do is, when it is due by and the priority (high, medium or low).
Add the 'to do' to the list.
'View' should give two options:

View all - shows all 'to dos' with a pretty print.
View priority - allows you to search for high, medium or low priority and only see matching tasks.
'Edit' allows you to change any of the information within one of the 'to dos'.

'Remove' lets you completely remove a 'to do' when it is 'to done'.

Example:

Welcome to the life organizer. Do you want to add, view, edit or remove a to do? > Add
What is the task? > Pay teachers more.
When is it due by? > 11/01/2022
What is the priority? >  High
Thanks, this task has been added.
Do you want to see the menu again or quit? > quit.

Hints:
Use a separate subroutine for add, view, edit, and remove.

Clear the console before viewing a new entry.

Use a while True loop to call the subroutines and display the menu.
"""

import os, time
from datetime import datetime

title = "🌟 Life Organizer System 🌟"
text = "Welcome to the life organizer. Do you want to:"
menu = "1: Add\n2: View\n3: Remove\n4: Edit\n"

toDoList = [
    ["Aniversario <3", datetime(2024, 2, 14), "high"],
    ["Cumple Pollito <3", datetime(2024, 4, 21), "high"],
    ["Navidad", datetime(2024, 12, 24), "medium"],
    ["Año Nuevo", datetime(2024, 12, 31), "medium"],
    ["Esta es una task mas larga de prueba", datetime(2024, 12, 31), "low"],
    ["Esta es una task mas larga de prueba 2", datetime(2024, 5, 1), "low"],
]


def addTask():
    print(f"{'--- Add ---':^35}")
    notInList = True
    task = input("What is the task?: > ").strip()
    try:
        year, month, day = (
            input("When is it due by?: YYY-MM-DD format > ").strip().split("-")
        )
        date = datetime(int(year), int(month), int(day))
    except ValueError:
        date = datetime(
            year=datetime.now().year, month=datetime.now().month, day=datetime.now().day
        )

    priority = input("What is the priority?: High, medium or low > ").strip().lower()
    if priority == "":
        priority = "low"

    rowTask = [task, date, priority]

    for row in toDoList:
        if task == row[0]:
            notInList = False

    if notInList == True:
        toDoList.append(rowTask)
        print(f"\n{task} has been added.")
    else:
        print(f"\n{task} has already been added.")


def viewTask():
    print(f"{'--- View ---':^35}")
    menu = "\n1: View All\n2: View Priority\n"
    print(menu)
    menuInput = input("> ").strip()

    if menuInput == "1":
        os.system("clear")
        print(f"{'--- To Do List ---':^100}")
        for row in toDoList:
            line = f"{row[0]:<70} | {row[1].strftime('%d %B %Y'):<20} | {row[2].capitalize():<10}"
            print(line)
        print()
    elif menuInput == "2":
        priority = input("\nWhich priority?: High, medium or low > ").strip().lower()
        if priority == "":
            priority = "low"
        os.system("clear")
        title = f"--- View {priority.capitalize()} Priority ---"
        print(f"{title:^100}")
        for row in toDoList:
            if priority in row:
                line = f"{row[0]:<70} | {row[1].strftime('%d %B %Y'):<20} | {row[2].capitalize():<10}"
                print(line)
        print()


def removeTask():
    print(f"{'--- Remove ---':^35}")
    task = input("What task should I remove?: > ").strip()
    notInList = True
    for row in toDoList:
        if task in row:
            notInList = False
            menuInput = (
                input(f"Are you sure you want to remove: {task}?: y/n > ")
                .strip()
                .lower()
            )
            if menuInput[0] == "y":
                toDoList.remove(row)
                print(f"\n'{task}' was successfully removed")
            else:
                print(f"\n'{task}' was not removed")
    if notInList == True:
        print(f"\n'{task}' is not in the list")


def editTask():
    print(f"{'--- Edit ---':^35}")
    notInList = True
    oldTask = input("What do you want to edit?:\n> ").strip()

    for row in toDoList:
        if oldTask in row:
            notInList = False
            task = input("New task title: > ").strip()
            try:
                year, month, day = (
                    input("New due date (YYYY-MM-DD format): > ").strip().split()
                )
                date = datetime(int(year), int(month), int(day))
            except ValueError:
                date = datetime(
                    year=datetime.now().year,
                    month=datetime.now().month,
                    day=datetime.now().day,
                )
            priority = input("New priority: High, medium or low > ").strip().lower()
            if priority == "":
                priority = "low"
            row[0], row[1], row[2] = task, date, priority
            print("\nTask was updated.")

    if notInList == True:
        print(f"\n'{oldTask}' is not on the list.")


while True:
    os.system("clear")
    print(f"{title:^35}")
    print(f"{text:^35}")
    print(menu)
    menuInput = input("> ").strip()
    if menuInput == "1":
        addTask()
        time.sleep(2)
    elif menuInput == "2":
        viewTask()
        continueInput = input("Press any key to continue > ").strip()
        if continueInput:
            time.sleep(1)
            continue
    elif menuInput == "3":
        removeTask()
        time.sleep(2)
    elif menuInput == "4":
        editTask()
        time.sleep(2)
    else:
        continue
