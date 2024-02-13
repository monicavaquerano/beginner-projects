"""
Saving Files

👉 Day 48 Challenge
Today's challenge is to create a high score table.

Your program should:

Ask the user to input their three letter initials and score (out of about 100,000).
Save both those values into a file called 'high.score'.
This should use append mode. If the file doesn't exist, it should be created. If it does, the score should be added to the end.
Each new entry score should go on a new line as initials space score. Then start a new line for the next entry.
Add 2-3 scores for testing in a loop.
The loop should ask the user if they've finished entering data and stop if they have.
🥳 Extra points for getting all the inputs with just one input command and the split function.

Example:

🌟HIGH SCORE TABLE🌟
Input your initials > DJM
Input your score > 89,764
Added to high score table.
Add another? y/n? y
Input your initials > ACY
Input your score > 5,731
Added to high score table.
Add another? y/n? n

Hints:
Not much here that you can't get from the examples.
Don't forget to put a new line character at the end of each write command.

"""

import os


def addScore():
    f = open("high.score", "a+")
    initials = input("Enter your initials: > ").strip().upper()
    score = input("Enter your score: > ").strip()
    text = f"{initials} {score}"
    f.write(f"{text}\n")
    f.close()
    print("\nAdded to high score table.")


while True:
    os.system("clear")
    print("🌟 HIGH SCORE TABLE 🌟")
    addScore()
    addInput = input("\nAdd another? y/n? > ").strip().lower()
    if addInput[0] == "y":
        continue
    else:
        break
