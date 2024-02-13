"""
👉 Day 52 Challenge
There's no place like Rome...Or Napoli, Milan, possibly even New York if you must.

Just not the dodgy 2am 'round bread with suspicious toppings' merchants that I definitely do not visit on my way home from a night out.

That's right, you're opening a pizza shop! Try not to get anchovy on your keyboard. Man that stuff never washes out.

Regardless, your program today must:

Prompt the user to input the quantity and size of pizzas.

Multiply the two inputs together to calculate the cost of the pizzas.

Store that in a 2D list with the user's name.

Use try.... except for two reasons:

Include auto-save and auto-load. Use it with the auto-load.
When casting the quantity of pizzas to an integer. Avoid the user crashing the program by typing 'three' instead of '3'. Or any other non-integer input. If they do, then prompt them to try again.

Example:
🌟Dave's Dodgy Pizzas🌟
How many pizzas? > three
You must input a numerical character, try again. > 3
What size? > XXXXXX
Name please > David
Thanks David, your pizzas will cost XXXXX

Hints:
* Use subroutines for 'add' and 'view'
* Use a while.... true loop for the main menu
* Use a 2d list to store the details of each pizza.
* Use selection to decide which subroutine to run, then write the 2d list to the file.
* For add, get all the inputs in variables and append to a list. Append this list to a 2d one that stores all the pizza details.
* For view, get each index from one row of the 2d list at a time.
"""

import os, time

orders = []

sizes = {"s": 6.99, "m": 9.99, "l": 14.99}

# Load
try:
    f = open("pizza.txt", "r")
    orders = eval(f.read())
    f.close()
except FileNotFoundError:
    pass


while True:
    os.system("clear")
    print("🍕 Rominos Pizza 🍕")
    menuInput = input("1: Add Pizza\n2: View Pizzas\n3: Exit\n> ").strip().lower()
    if menuInput == "1" or menuInput[0] == "a":
        os.system("clear")
        print("🍕 Place Your Order 🍕")
        name = input("Your name please?: > ").strip().lower()
        topping = input(f"What would be your topping?: > ").strip().lower()
        while True:
            try:
                size = input("What would be the size? (s/m/l): > ").strip().lower()
                quantity = int(input(f"How many pizzas?: > "))
                total = sizes[size] * quantity
                break
            except ValueError:
                print("You must input a numerical character, try again.")
            except KeyError:
                print("You must input 's', 'm', or 'l', try again.")

        order = [name, topping, size, quantity, total]
        orders.append(order)
        # Write
        f = open("pizza.txt", "w")
        f.write(str(orders))
        f.close()

        print("\nYour order has been successfully placed.")
        time.sleep(2)

    elif menuInput == "2" or menuInput[0] == "v":
        print(f"{'🍕 All Orders 🍕':^70}")
        if len(orders) == 0:
            print("No orders yet.")
        else:
            print(
                f"{'Name':^20}{'Topping':^20}{'Size':^10}{'Quantity':^10} {'Total':^10}"
            )
            for order in orders:
                print(
                    f"{order[0].title():^20}{order[1].title():^20}{order[2].upper():^10}{order[3]:^10} ${order[4]:^10}"
                )
        time.sleep(4)

    elif menuInput == "3" or menuInput[0] == "e":
        print("Ciao! 🍕")
        break
    else:
        continue
