"""
Code the rainbow!

Ask the user to input any sentence (string).
Now we'll rainbow-ize (nope, me neither) it.
As soon as the string contains an 'r', every letter from that point on should be red.
When the computer encounters a 'b', 'g', 'p' or 'y', from there the output should be blue for 'b', green for 'g'...you get the idea.
Loop through the string and output it (so the color continues through the loop).
The output should change color every time it encounters a new r,g,b,p or y.
🥳 Extra points for resetting the output color back to default every time there's a space.

Hints:
You can use a lot of your code from Day 31 to get started.
Use an if... elif... else to check for key letters.
Use the print("\033[31m", end="") to change the font color.
Try implementing the color change as a subroutine.
"""
import os, time


def rainbowify(letter):
    if letter.lower() == "r":
        print(f"\033[0;31m", end="")
    elif letter.lower() == "c":
        print(f"\033[0;36m", end="")
    elif letter.lower() == "b":
        print(f"\033[0;34m", end="")
    elif letter.lower() == "g":
        print(f"\033[0;32m", end="")
    elif letter.lower() == "p":
        print(f"\033[0;35m", end="")
    elif letter.lower() == "y":
        print(f"\033[1;33m", end="")
    elif letter.lower() == " ":
        print(f"\033[0m", end="")
    print(letter, end="")


while True:
    os.system("clear")
    print("\033[1;33m--- \033[0;31mRain\033[0;34mbow\033[0;32mify \033[0;36m---\033[0m")

    myString = input(
        "\033[0;32mWhat sentence do you want to rainbowify?:\n > \033[1;33m"
    )
    print(f"\033[0m")
    time.sleep(2)
    os.system("clear")

    print(
        "\033[1;33m--- \033[0;31mRain\033[0;34mbow \033[0;32mMagic! \033[0;36m---\033[0m"
    )
    for c in myString:
        rainbowify(c)
    print(f"\033[0m")

    again = (
        input(
            "\n\033[0;31mRain\033[0;34mbow\033[0;32mify \033[0;36magain?: \033[1;33my/n > \033[0m"
        )
        .strip()
        .lower()
    )
    if again == "y":
        continue
    else:
        break
