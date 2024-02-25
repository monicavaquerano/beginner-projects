"""
👉 Day 41 Challenge
Create a dictionary that stores the following information about a website: name, URL, description and a star rating (out of 5).
Use a loop to output the names of the keys, ask the user to type in the details and store the input in the dictionary.
Finally, output the whole dictionary (keys and values).
🥳 Extra points for getting all the inputs with just one input command and the split function.

Example:

🌟Website Rating🌟
Input the website name: Replit
Input the URL: replit.com
Input your a description: An awesome online IDE.
Input the a star rating out of 5: *****
name:Replit, URL:replit.com, description:An awesome online IDE, rating:*****

Hints:
When creating your dictionary, you will need to use example = { "MyValue": none} to show a key name and no value.
Use a loop to print the entire dictionary.
Make sure you include both variables (name and value) in your loop and your print statement.

"""
import os, time

rating = {"website name": None, "URL": None, "description": None, "rating": None}

while True:
    os.system("clear")
    for key in rating.keys():
        value = input(f"Input the {key}: > ").strip()
        rating[key] = value

    time.sleep(2)
    os.system("clear")

    print("🌟 Website Rating 🌟\n")

    for key, value in rating.items():
        print(f"{key}: {value}")

    again = input("\nWould you like to change your rating?: y/n > ").strip().lower()
    if again == "y":
        time.sleep(2)
        continue
    else:
        break
