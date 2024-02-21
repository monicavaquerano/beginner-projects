"""
A Man A Plan A Canal Panama!
Today's challenge is all about palindromes.

A palindrome is a word that is symmetrical, (i.e. it reads the same backwards as forwards).

For example:

racecar
madam
radar
Now that you know what a palindrome is, just go back and have a look at this page title. The one that made you go, huh?! Got it now? Sweet!

Hop over to the challenge page for details.

👉 Day 59 Challenge
You're going to write a program that checks a string to see if it is a palindrome.

Yes. We know that Python has the built in function string.reverse() that you could use.

Zero points for that today, we want you to think hard and utilize your skills in:

* recursion
* string slicing
* looping

Your program should:

1. Prompt the user to input a word.
2. Analyze the word to see if it is a palindrome.
3. Output a relevant 'yes/no message.

Example:
🌟Palindrome Checker🌟
Input a word > Racecar
Racecar is a palindrome. Yay!

Hints:
This is a tough one, so I've given you some hints about the algorithmic thinking needed for a problem like this:
* Don't forget to standardize the case on input.
* Think about which characters in a word are compared first. Check if they are the same.
* If they've been compared and are the same, remove them and repeat the process with the shorter string.
* Keep going until you're down to a string of length 1 or 0 (depending on whether the original word had an odd/even number of characters. If you get to this point, then you've got a palindrome.
"""


def is_palindrom(string):
    base_string = ""
    for char in string.strip().lower():
        if not char.isalpha():
            base_string += ""
        else:
            base_string += char

    reversed_string = base_string[-1::-1]

    print("🌟 Palindrome Checker 🌟")

    if base_string == reversed_string:
        print(f"{string} is a palindrome. Yay!")
        return True
    else:
        print(f"{string} is not a palindrome. :(")
        return False


def main():
    is_palindrom("Race Car")
    is_palindrom("A Man A Plan A Canal Panama!")
    is_palindrom("Anona")
    is_palindrom("Apopa")
    is_palindrom("No soy un palindrome???")

    # Usando recursion
    def palindrome(word):
        if len(word) <= 1:
            return True
        if word[0] != word[-1]:
            return False
        return palindrome(word[1:-1])

    print(palindrome("racecar"))


if __name__ == "__main__":
    main()
