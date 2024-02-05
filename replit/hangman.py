import random, os, time, requests


listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

response = requests.get("https://random-word-api.herokuapp.com/word")

if response.status_code == 200:
    data = response.json()
    myWord = data[0].strip().lower()
else:
    myWord = random.choice(listOfWords).strip().lower()

tries = []
counter = 0
lives = 6


def printDummy(counter):
    HANGMANPICS = [
        """
  +---+
  |   |
      |
      |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
        """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
    ]
    print(HANGMANPICS[counter])


title = "🌟 Hangman 🌟"

while True:
    os.system("clear")
    print(title)
    printDummy(counter)
    all = True

    for letter in myWord:
        if letter in tries:
            print(letter, end="")
        else:
            print("_", end="")
            all = False

    print(f"\n\nSo far you have used these letters: {tries}")

    if counter == 6:
        print(f"\nYou lost!\nThe word was:\t{myWord.capitalize()}")
        exit()
    elif all == True:
        print(f"\nYou won with {lives} lives still")
        exit()

    guess = input("\nChoose a letter:\n > ").strip().lower()

    if guess in tries:
        print(f"You already tried '{guess}'")
        time.sleep(2)
        continue

    tries.append(guess)

    if guess in myWord:
        print("Correct!")
    else:
        counter += 1
        lives -= 1
        print("Nope, not in there.")

    time.sleep(2)
