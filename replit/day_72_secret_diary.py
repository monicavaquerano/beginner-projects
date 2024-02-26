"""
👉 Day 72 Challenge
Now that we know about secure passwords, we can really protect our diary program.

Go back 10 days and grab your diary code from Day 62.

When you have it, add the following features:

The first time the diary is run, the user must create a username and password.
Salt & hash the password and store it in the database with the username as the key.
Then proceed to the diary.
The next time that program is run, it should prompt for the username and password, and only allow access if they are correct.
The username, password, and salt should be excluded from diary entry outputs, for obvious reasons.
"""

# from replit import db
import datetime, os, random, time

db = {}


def random_salt(number=4):
    salt = ""
    for _ in range(number):
        salt += str(random.randint(0, 9))
    return salt


def create_user(username, password, confirm_password):
    if username == "" or password == "" or confirm_password == "":
        print("\nYou must enter a valid username and password")
        return

    if password != confirm_password:
        print("\nYour password is not the same. Try again")
        return

    salt = random_salt()
    newPassword = f"{password}{salt}"
    hashedPassword = hash(newPassword)

    if username not in db.keys():
        db[username] = {"password": hashedPassword, "salt": salt}
        print("\nUser successfully created")
    else:
        print("\nUsername already exist")


def loggin(username, user_password):
    try:
        password = db[username]["password"]
        user_password = hash(f"{user_password}{db[username]['salt']}")
        if password == user_password:
            print("\nLogin successful")
            return 1
        else:
            print("\nPassword is incorrect")
            return 0
    except KeyError:
        print("\nUsername is incorrect")
        return 0


def addEntry(user):
    if "entries" not in db[user].keys():
        db[user]["entries"] = {}

    timestamp = datetime.datetime.now()
    entry_key = f"entry{timestamp}"
    entry = input("\nWrite your entry: > ")
    db[user]["entries"][entry_key] = entry
    print("\nEntry added")
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
                print("\nYou reached the end of the entries")
                break
            else:
                continue
        else:
            break


def secret_diary(username):
    while True:
        os.system("clear")
        print(f"🌟 {username}'s Secret Diary 🌟")
        menu = input("\n1. Add entry\n2. View entries\n3. Exit\n> ")
        if menu == "1":
            addEntry(username)
        elif menu == "2":
            while True:
                viewEntries(username)
                again = input("\nView again? y/n > ").strip().lower()
                if again[0] == "y":
                    continue
                else:
                    break
        elif menu == "3":
            break
        else:
            continue


if __name__ == "__main__":

    while True:
        os.system("clear")
        print("🌟 Secret Diary 🌟")
        menuChoice = input("\n1. Create a new user\n2. Login\n3. Exit\n> ").strip()
        if menuChoice == "1":
            os.system("clear")
            print("Create a new user:\n")
            username = input("Username: > ")
            password = input("Password: > ")
            confirm_password = input("Confirm Password: > ")
            create_user(username, password, confirm_password)
            time.sleep(2)
        elif menuChoice == "2":
            os.system("clear")
            print("Login:\n")
            username = input("Username: > ")
            password = input("Password: > ")
            isLogin = loggin(username, password)
            time.sleep(2)
            if isLogin == 1:
                secret_diary(username)
            else:
                continue
        elif menuChoice == "3":
            print("\nSee you later!")
            exit()
        else:
            continue
