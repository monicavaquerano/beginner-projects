"""
👉 Mecca Your Nan Very Happy
Today's challenge is to create a bingo card. Oh yes, because programming's not just for you hip, young cats. 😆

Anyway, your challenge is to enable "gambling for the elderly" (aka Bingo), and you'll achieve it like this:

Randomly generate a series of number between 0 and 90.
Allocate each number to a place in a 2D list.
The numbers should be in numerical order, left to right.
Numbers should not be repeated.
The center square should not contain a number. It should contain the word 'BINGO!'.
When the program is run, the bingo card should be displayed on screen.

Hints:
Make sure you include 'prettyprinting'.
Try using a 2D list with each sublist as a row.
Randomly generate the numbers and append each to a list as you do.
Use .sort() to put the list of numbers in order before adding to the card.
"""

import random, os, time


def generateCard():
    title = f"{'Bingo Card':^25}"
    numbers = []
    bn = []
    counter = 0
    i = 0
    while i < 9:
        numb = random.randint(0, 90)
        if numb not in numbers:
            numbers.append(numb)
            i += 1

    numbers.sort()

    for i in range(3):
        row = []
        for j in range(3):
            row.append(numbers[j + counter])
        counter += 3
        bn.append(row)

    bn[1][1] = "BINGO"

    bingoCard = f"""
    {bn[0][0]:02d}  |  {bn[0][1]:02d}   | {bn[0][2]:02d}
    ------------------
    {bn[1][0]:02d}  | {bn[1][1]} | {bn[1][2]:02d}
    ------------------
    {bn[2][0]:02d}  |  {bn[2][1]:02d}   | {bn[2][2]:02d}
    """

    print(title)
    print(bingoCard)


while True:
    os.system("clear")
    generateCard()
    again = input("Generate another card?: y/n\n> ").strip().lower()
    if again[0] == "y":
        time.sleep(1)
        continue
    else:
        break
