"""
Replit's DataBase
"""

import datetime, time, os
from replit import db


def addTweet():
    timestamp = datetime.datetime.now()
    print("Add a Tweet:\n")
    tweet = input("What's going on?: ")
    key = f"tweet{timestamp}"
    db[key] = tweet
    print("\nTweet added!")
    time.sleep(2)


def viewTweets():
    matches = db.prefix("tweet")
    matches = matches[::-1]
    counter = 0
    print("My Tweets:\n")
    for i in matches:
        print(f">> {db[i]}\n")
        time.sleep(0.3)
        counter += 1
        if counter % 10 == 0:
            continueInput = input("Next 10? (y/n): ").strip().lower()
            if continueInput == "y":
                print()
                continue
            else:
                break
    time.sleep(1)


while True:
    os.system("clear")
    print("Tweeter Clone\n")
    menuInput = input("1. Add\n2. View\n3. Exit\n> ").strip()
    if menuInput == "1":
        os.system("clear")
        addTweet()
    elif menuInput == "2":
        while True:
            os.system("clear")
            viewTweets()
            againInput = input("View again? (y/n): ").strip().lower()
            if againInput == "y":
                continue
            else:
                break
    elif menuInput == "3":
        break
    else:
        continue
