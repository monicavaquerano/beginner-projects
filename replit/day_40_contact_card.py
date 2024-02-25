"""
👉 Day 40 Challenge
Today's challenge is to create a contact card using a dictionary.

Ask the user to input their name, date of birth, telephone number, email and physical address.
Store it all in a dictionary.
Print it out in a nice way once its stored.
Example:

🌟 Contact Card 🌟
Input your name > David Morgan
Input your date of birth > 01/01/1900
Input your telephone number > 01234 567890
Input your email > david@replit.com
Input your address > The Cupboard Under The Stairs, Replit Towers, NY.
"Hi David Morgan. 
Our dictionary says that you were born on 01/01/1900, we can call you on 01234 567890, email david@replit.com, or write to The Cupboard Under The Stairs, Replit Towers, NY."
"""
import os, time

contactDictionary = {}

title = "🌟 Contact Card 🌟"

name = input("Input your name: > ").strip()
dob = input("Input your date of birth: > ").strip()
phone = input("Input your telephone number: > ").strip()
email = input("Input your email: > ").strip()
addresse = input("Input your address: > ").strip()

contactDictionary = {
    "name": name,
    "dob": dob,
    "phone": phone,
    "email": email,
    "address": addresse,
}
while True:
    os.system("clear")
    print(
        f"Hi {contactDictionary['name']}.\nOur dictionary says that you were born on {contactDictionary['dob']},\nwe can call you on {contactDictionary['phone']},\nemail {contactDictionary['email']},\nor write to {contactDictionary['address']}.\n"
    )
    updateInfo = input("Would you like to update some info?: y/n > ").strip().lower()
    if updateInfo == "y":
        key = (
            input(
                "What would you like to update?: name, dob, phone, email or address > "
            )
            .strip()
            .lower()
        )
        if key in contactDictionary.keys():
            newInfo = input(f"Update {key} > ").strip()
            contactDictionary.update({key: newInfo})
            print(f"{key.capitalize()} was updated.")
            time.sleep(2)
        else:
            print(f"Error: {key} can't be updated")
            time.sleep(2)
    else:
        sure = input("Would you like to leave?: > ").strip().lower()
        if sure == "y":
            print(f"Alright! Bye!")
            break
        continue
