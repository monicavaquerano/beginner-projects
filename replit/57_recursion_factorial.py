"""
👉 Day 57 Challenge - Recursion
Try to use recursion to build a factorial program.

Yep, it's a math challenge. Recursion is often good for this type of problem.

It could be a real head scratcher, so don't be afraid to use 100 Days of Code Community or the Discord channel for help.

A factorial is the product of all the numbers up to a value, starting from 1.

For example, factorial 5 would be 1 * 2 * 3 * 4 * 5 = 120

Write a function that:
Starts at the highest number.
Multiplies that by factorial of itself minus one
Terminates when it reaches 1 and returns 1
Outputs the factorial.
Example:

🌟Factorial Finder🌟
Input a number > 5
The factorial of 5 is 120.

Hints:
# Don't forget to return 1 in your terminating condition.
# Try multiplying the number by the factorial (n-1) call.
"""


def reverse(value):
    if value <= 0:
        print("Done!")
        return
    else:
        for i in range(value):
            print("🍕", end="")
        print()
        reverse(value - 1)


reverse(5)


def factorial(value):
    if value <= 1:
        return 1
    else:
        return value * factorial(value - 1)


def factorialFinder():
    print("🌟 Factorial Finder 🌟")
    number = int(input("Input a number: > "))
    print(f"The factorial of {number} is {factorial(number)}")


factorialFinder()
