class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=""):
        """
        A deposit method that accepts an amount and description.
        If no description is given, it should default to an empty string.
        The method should append an object to the ledger list in the form of
        {"amount": amount, "description": description}.
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        A withdraw method that is similar to the deposit method,
        but the amount passed in should be stored in the ledger
        as a negative number. If there are not enough funds, nothing
        should be added to the ledger. This method should return True
        if the withdrawal took place, and False otherwise.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -abs(amount), "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for transaction in self.ledger:
            amount = transaction["amount"]
            total += amount
        return total

    def transfer(self, amount, other):
        """
        A transfer method that accepts an amount and another budget category as
        arguments. The method should add a withdrawal with the amount and the
        description "Transfer to [Destination Budget Category]".
        The method should then add a deposit to the other budget category
        with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
        """
        if self.check_funds(amount):
            other.deposit(amount, f"Transfer from {self.name}")
            self.withdraw(amount, f"Transfer to {other.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        """
        A check_funds method that accepts an amount as an argument.
        It returns False if the amount is greater than the balance of the budget
        category and returns True otherwise. This method should be used by both
        the withdraw method and transfer method.
        """
        total = 0

        for transaction in self.ledger:
            total += transaction["amount"]

        if abs(amount) > total:
            return False
        else:
            return True

    def __str__(self) -> str:
        asterics = (30 - len(self.name)) // 2 * "*"
        title = f"{asterics}{self.name}{asterics}"
        title = title if len(title) == 30 else title + "*"

        balance = ""
        for transaction in self.ledger:
            description = transaction["description"]
            description = description if len(description) < 24 else description[:23]

            amount = transaction["amount"]
            str_amount = f"{amount:.2f}"
            str_amount = str_amount if len(str_amount) < 7 else str_amount[:7]

            balance += f"{description:<23}{str_amount:>7}\n"

        return f"{title}\n{balance}Total: {self.get_balance():.2f}"


def create_spend_chart(categories):
    pass


food = Category("Food")
# food.deposit(1000, "deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# print(food)
# print(clothing)

"""
Calling food.deposit(900, "deposit") and 
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread") 
should return a balance of 854.33.
"""
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
print(food)
print(food.get_balance())
