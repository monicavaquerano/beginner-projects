from replit import db
import os, time, datetime

# db["david"] = {"password": "password"}
# db["monica"] = {"password": "1234"}


def loggin(user, user_password):
    try:
        password = db[user]["password"]
        if password == user_password:
            print("\nLogin successful")
            time.sleep(1)
            return 1
        else:
            print("\nPassword is incorrect")
            time.sleep(1)
            return 0
    except KeyError:
        print("\nUser is incorrect")
        time.sleep(1)
        return 0


def addEntry(user):
    if "entries" not in db[user].keys():
        db[user]["entries"] = {}

    timestamp = datetime.datetime.now()
    entry_key = f"entry{timestamp}"
    entry = input("Write your entry: > ")
    db[user]["entries"][entry_key] = entry
    print("Entry added")
    time.sleep(1)


def viewEntries(user):
    entries = db[user]["entries"]
    entry_list = list(entries.items())
    entry_list.sort(key=lambda x: x[0], reverse=True)
    counter = 0
    for _ in range(len(entry_list)):
        os.system("clear")
        print(f"{entry_list[counter][0][5:]}\n\n{entry_list[counter][1]}\n")
        next = input("Next entry? y/n > ")
        if next == "y":
            counter += 1
            if counter == len(entry_list):
                print("You reached the end of the entries")
                break
            else:
                continue
        else:
            break


user = input("Username: > ")
user_password = input("Password: > ")

if loggin(user, user_password) == 1:
    while True:
        os.system("clear")
        print("--- Private diary ---")
        menu = input("1. Add entry\n2. View entries\n3. Exit\n> ")
        if menu == "1":
            addEntry(user)
        elif menu == "2":
            while True:
                viewEntries(user)
                again = input("\nView again? y/n > ").strip().lower()
                if again[0] == "y":
                    continue
                else:
                    break
        elif menu == "3":
            break
        else:
            continue
