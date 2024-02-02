import random, os, time

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
listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

myWord = random.choice(listOfWords).strip().lower()
tries = []
counter = 0
lives = 6


def printDummy(counter):
    print(HANGMANPICS[counter])


title = "🌟Hangman🌟"

while True:
    os.system("clear")
    # print(myWord)
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
        print(f"\nYou already tried '{guess}'")
        time.sleep(2)
        continue

    tries.append(guess)

    if guess in myWord:
        print("\nCorrect!")
    else:
        counter += 1
        lives -= 1
        print("\nNope, not in there.")

    time.sleep(2)


# i = myList.index(item)
# newItem = input("What should it be?: ").lower().strip()
# myList[i] = newItem
