"""
👉 Day 91 Challenge
Today's challenge is to build a program from this basic principle that will:
1. Give you a random joke.
2. Ask if you want to save it.
3. If you do, it should:
    i. Save the joke ID number to a replit db
4. Ask the user if they want to see the saved jokes and output the contents of the database.

Hints:
* Check out the fetching a specific joke examples on the icanhazdadjoke API.
"""

import csv, json, os, requests, time


def get_joke():
    # API Conection
    result = requests.get(
        "https://icanhazdadjoke.com/", headers={"Accept": "application/json"}
    )
    # get a random dad joke from the site endpoint and assign to a variable. The second argument (the header request) tells the script to return the json data as a string.
    # print(result.content)
    if result.status_code != 200:
        print("An error in the API has ocurred. Try later")
        exit()
    else:
        data = result.json()
        id = data["id"]
        joke = data["joke"]
        return id, joke


def write_joke(id, joke):
    # Creates and/or write document
    if "dad_jokes.csv" in os.listdir():
        with open("dad_jokes.csv", "a+", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([id, joke])
        print("Saved\n")
    else:
        with open("dad_jokes.csv", "w", newline="") as f:
            writer = csv.writer(f)
            headers = ["id", "joke"]
            writer.writerow(headers)

        write_joke(id, joke)


def read_jokes():
    # Read document
    try:
        with open("dad_jokes.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row["joke"])
            print()

    except FileNotFoundError:
        print("Save a joke first.\n")


while True:
    print(f"{'Dad Jokes':=^30}\n")
    id, joke = get_joke()
    print(joke, "\n")
    choice = (
        input("(s)ave joke, (l)oad old jokes, (n)ew joke, (e)xit\n> ").strip().lower()
    )
    if choice[0] == "s":
        write_joke(id, joke)
        time.sleep(1)
        os.system("clear")
    elif choice[0] == "l":
        time.sleep(1)
        os.system("clear")
        print(f"{'Saved Dad Jokes':=^30}\n")
        read_jokes()
    elif choice[0] == "n":
        time.sleep(1)
        os.system("clear")
    elif choice[0] == "e":
        print("Bye!")
        break
