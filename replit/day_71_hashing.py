"""
👉 Day 71 Challenge
Today's challenge is to build a simple login system.

Your program should:
1. Display a menu with the ability to add a user or login.
2. 'Add' user should:
    i. Ask for a username and password.
    ii. Create a new password and a randomly generated 4 digit salt.
    iii. Append the salt to the password and hash it.
    iv. Store the hash and the salt in a repl db with the username as the key.
3. 'Login' should:
    i. Get username and password input.
    ii. Display a success message if details are correct.
4. This system should work with multiple users.

Hints:
* Try implementing the two menu options as subroutines. You'll be able to port them to other programs more easily.

Example:

🌟Login System🌟
1: Add User, 2: Login >  1

Username: > Kenny
Password: > L0gg1ns

Details stored.

1: Add User, 2: Login >  2

Username: > Kenny
Password: > L0gg1ns

Login successful
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


if __name__ == "__main__":

    while True:
        os.system("clear")
        print("🌟 Login System 🌟")
        menuChoice = (
            input("\n1. Create a new user\n2. Login\n3. Exit\n> ").strip().lower()
        )
        if menuChoice == "1" or menuChoice[0] == "c":
            os.system("clear")
            print("Create a new user:\n")
            username = input("Username: > ")
            password = input("Password: > ")
            confirm_password = input("Confirm Password: > ")
            create_user(username, password, confirm_password)
            time.sleep(2)
        elif menuChoice == "2" or menuChoice[0] == "l":
            os.system("clear")
            print("Login:\n")
            username = input("Username: > ")
            password = input("Password: > ")
            isLogin = loggin(username, password)
            time.sleep(2)
            if isLogin == 1:
                break
        elif menuChoice == "3" or menuChoice[0] == "e":
            print("\nSee you later")
            break
        else:
            continue

    # password = "1234"
    # salt = 5489

    # newPassword = f"{password}{salt}"
    # newPassword = hash(newPassword)

    # ask = input("Password?: > ")
    # login = f"{ask}{salt}"

    # user = input("Username: > ")
    # user_password = input("Password: > ")

    # if loggin(user, user_password) == 1:
    #     while True:
    #         os.system("clear")
    #         print("--- Private diary ---")
    #         menu = input("1. Add entry\n2. View entries\n3. Exit\n> ")
    #         if menu == "1":
    #             addEntry(user)
    #         elif menu == "2":
    #             while True:
    #                 viewEntries(user)
    #                 again = input("\nView again? y/n > ").strip().lower()
    #                 if again[0] == "y":
    #                     continue
    #                 else:
    #                     break
    #         elif menu == "3":
    #             break
    #         else:
    #             continue
