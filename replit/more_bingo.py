"""
👉 Day 44 Challenge
It's time for more bingo! You can reuse your code from day 43, but this time add the following features:

Repeatedly ask the user what number comes up next.
Check the bingo card to see if the number picked matches one on the card.
If the bingo card is all 'X's, then the user has won.

Hints:
Create a subroutine called createCard to clean up some of the code from Day 43.
Use a variable and loop to store how many x's there are on the card. Add one every time a number is replaced.
Check the variable every time to see if it has reached the magic winning number.

#replit100DaysOfCode
#DavidsNanLovesThisCode
#DavidsNanIsGoingToWinAtBingo
"""

import random, os


def generateCard():
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

    return bn


def printBingoCard(bingoCard):
    title = f"{'Bingo Card':^25}"
    bn = bingoCard
    card = f"""
    {bn[0][0]:<2}  |  {bn[0][1]:^2}   | {bn[0][2]:>2}
    ------------------
    {bn[1][0]:<2}  | {bn[1][1]:^2} | {bn[1][2]:>2}
    ------------------
    {bn[2][0]:<2}  |  {bn[2][1]:^2}   | {bn[2][2]:>2}
    """

    print(title)
    print(card)


bingoCard = generateCard()
x = 0

while True:
    os.system("clear")
    printBingoCard(bingoCard)

    if x == 8:
        print("You have won! :D")
        break

    number = int(input("What number was called? > ").strip())

    for row in bingoCard:
        for item in row:
            if number == item:
                x += 1
                rowIndex = bingoCard.index(row)
                itemIndex = row.index(item)
                bingoCard[rowIndex][itemIndex] = "X"


# if again == "y":
#     time.sleep(2)
#     continue
# else:
#     break


# test = [["Monica", 35, "PC"],["Tanya", 37, "Mac"]]

# listOfShame = []

# while True:
#     menu = input("Add or Remove?")

#     if menu.strip().lower()[0] == "a":

#         name = input("What is your name? ")
#         age = input("What is your age? ")
#         pref = input("What is your computer platform? ")

#         row = [name, age, pref]

#         listOfShame.append(row)

#     else:
#         name = input("What is the name of the record to delete?")

#         for row in listOfShame:
#             if name in row:
#                 listOfShame.remove(row)  # remove the whole row if name is in it

#     print(listOfShame)
