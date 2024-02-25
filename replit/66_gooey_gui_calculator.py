"""
👉 Day 66 Challenge
Your challenge is to create a simple GUI calculator.

Your program should:

Have buttons for the numbers 0 to 9, plus, minus, multiply, divide and equals.
The user should be able to press buttons to create their calculation.
It should output the correct result when they press equals.

Hints:
* Use a grid to lay out the buttons.
* Create a buttonChoice subroutine or similar that takes in the value of the numeric button clicked, casts it to an int and displays it in the label.
* Create an operatorChoice sub that selects which operator to display and use.
* Investigate the lambda command for your buttons.
* Use a calc subroutine with global variables for answer, lastnumber and operator.

"""

import tkinter as tk

window = tk.Tk()
window.title("Gooey GUI Calculator")
window.geometry("300x200")

label = 0
lastNumber = 0
operator = None

# Screen
screen = tk.Label(text=label)
screen.grid(row=0, column=1)


def updateLabel(value):
    global label
    label = f"{label}{value}"
    label = int(label)
    screen["text"] = label


def buttonChoice(button):
    global label, lastNumber, operator
    lastNumber = label
    label = 0
    match button:
        case "+":
            operator = "+"
        case "-":
            operator = "-"
        case "*":
            operator = "*"
        case "/":
            operator = "/"
    screen["text"] = label


def calculate():
    global label, lastNumber, operator
    print(f"{lastNumber}\t{label}\t{operator}")
    match operator:
        case "+":
            total = lastNumber + label
        case "-":
            total = lastNumber - label
        case "*":
            total = lastNumber * label
        case "/":
            total = lastNumber / label

    label = total
    screen["text"] = label


# Buttons
one = tk.Button(text="1", command=lambda: updateLabel(1))
one.grid(row=1, column=1)
two = tk.Button(text="2", command=lambda: updateLabel(2))
two.grid(row=1, column=2)
three = tk.Button(text="3", command=lambda: updateLabel(3))
three.grid(row=1, column=3)
plus = tk.Button(text="+", command=lambda: buttonChoice("+"))
plus.grid(row=1, column=4)
minus = tk.Button(text="-", command=lambda: buttonChoice("-")).grid(row=1, column=5)

four = tk.Button(text="4", command=lambda: updateLabel(4))
four.grid(row=4, column=1)
five = tk.Button(text="5", command=lambda: updateLabel(5))
five.grid(row=4, column=2)
six = tk.Button(text="6", command=lambda: updateLabel(6))
six.grid(row=4, column=3)
multiply = tk.Button(text="*", command=lambda: buttonChoice("*"))
multiply.grid(row=4, column=4)
divide = tk.Button(text="/", command=lambda: buttonChoice("/"))
divide.grid(row=4, column=5)

seven = tk.Button(text="7", command=lambda: updateLabel(7))
seven.grid(row=5, column=1)
eight = tk.Button(text="8", command=lambda: updateLabel(8))
eight.grid(row=5, column=2)
nine = tk.Button(text="9", command=lambda: updateLabel(9))
nine.grid(row=5, column=3)

zero = tk.Button(text="0", command=lambda: updateLabel(0))
zero.grid(row=6, column=2)
equal = tk.Button(text="=", command=calculate)
equal.grid(row=6, column=4)


# hello = tk.Label(text=label)
# hello.grid(row=0, column=1)


# text = tk.Text(window, height=1, width=25)
# text.grid(row=1, column=1)


# button = tk.Button(text="Click me!", command=updateLabel).grid(row=2, column=0)

# button = tk.Button(text="Another Button", command=updateLabel).grid(row=2, column=1)

# button = tk.Button(text="Last one", command=updateLabel).grid(row=2, column=2)

tk.mainloop()


# 7 rows 7 columns
