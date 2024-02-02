"""
👉 Day 37 Challenge
This is the challenge you're looking for. This program will generate your Star Wars Name.

Ask the user to input their first & last names.
Slice the first 3 letters of the first name.
Slice the first 3 letters of the last name (surname).
Join them together. Ideally change the case so that it looks good - think fStrings or .upper()/.lower(). This is the user's Star Wars first name.
Now ask the user for their mother's maiden name and the city where they were born. (Maiden name is the last name they had before they got married. If you are not sure, make up a last name.)
Combine the first two letters of the maiden name with the last 3 letters of the city to make the user's Star Wars last name. Remember, fStrings and .upper()/.lower().
Finally, print them both as part of a sentence.
🥳 Extra points for getting all the inputs with just one input command and the split function.

Example:

🌟Star Wars Name Generator🌟
Input your first name > David
Input your lastname > Morgan
Input your mother's maiden name > Jones
Input the city where you were born > Cardiff
Your Star Wars name is Davmor Joiff
"""
import os, time

while True:
    os.system("clear")
    firstName = input("Enter your first name: > ").strip().lower()
    time.sleep(1)
    os.system("clear")
    lastName = input("Enter your last name: > ").strip().lower()
    time.sleep(1)
    os.system("clear")
    maidenName = input("Enter your Mom's maiden name: > ").strip().lower()
    time.sleep(1)
    os.system("clear")
    city = input("Enter the city where you were born: > ").strip().lower()
    time.sleep(1)
    os.system("clear")

    starWarsName = (
        (f"{firstName[:3]}{lastName[:2]} {maidenName[:2]}{city[-3:]}").strip().title()
    )
    print(f"Your Star Wars name is {starWarsName}\n")

    again = input("Would you like to try it again?: y/n > ").strip().lower()
    if again == "y":
        continue
    else:
        break
