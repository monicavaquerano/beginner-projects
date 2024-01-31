"""
👉 Day 34 Challenge
Let's extend this program and build option 4: "Get SPAMMING".

Print out the first 10 email addresses with a custom email sent to each of those people.
Print one email at a time, pause, and then clear the screen before the next email is printed.
Example:

Dear john@test.com
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.
Love and hugs,
Ian Spammington III
"""
import os, time

listOfEmail = [
    "andy@test.com",
    "betty@test.com",
    "charlie@test.com",
    "danny@test.com",
    "ellie@test.com",
]


def prettyPrint(list):
    os.system("clear")
    print("List of Emails")
    print()
    counter = 1
    if len(list) == 0:
        print("Empty list")
    else:
        for item in list:  # len counts how many items in a list
            print(f"{counter}: {item}")
            counter += 1
    time.sleep(1)


def spam(list):
    os.system("clear")
    if len(list) == 0:
        print("Empty list")
    elif len(list) < 10:
        for item in list:
            print(f"Dear {item}")
            print(
                """
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. 
If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. 
We might just do that anyway.
Love and hugs,

Ian Spammington III"""
            )
            print()
            time.sleep(2)
            os.system("clear")
    else:
        for i in range(10):  # len counts how many items in a list
            print(f"Dear {list[i]}")
            print(
                """
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. 
If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. 
We might just do that anyway.
Love and hugs,

Ian Spammington III"""
            )
            print()
            time.sleep(2)
            os.system("clear")


while True:
    print("SPAMMER Inc.")
    menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
    if menu == "1":
        email = input("Email > ")
        listOfEmail.append(email)
    elif menu == "2":
        email = input("Email > ")
        if email in listOfEmail:
            listOfEmail.remove(email)
    elif menu == "3":
        prettyPrint(listOfEmail)
    elif menu == "4":
        spam(listOfEmail)
    time.sleep(1)
    os.system("clear")
