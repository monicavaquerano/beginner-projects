class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=""):
        """
        A deposit method that accepts an amount and description.
        If no description is given, it should default to an empty string.
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        A withdraw method that is similar to the deposit method,
        but the amount passed in should be stored in the ledger
        as a negative number.
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
        arguments.
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
        """
        total = 0

        for transaction in self.ledger:
            total += transaction["amount"]

        if abs(amount) > total:
            return False
        else:
            return True

    def __str__(self) -> str:
        title = f"{self.name:*^30}"
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
    if len(categories) > 4:
        return "Too many categories"

    chart_string = "Percentage spent by category\n"
    minus_no = (len(categories) * 2) + 4
    lower_line = f"{'': <4}{'-' * minus_no}\n"
    max_length = max(len(category.name) for category in categories)

    # Calculate the percentage spent for each category
    spendings = [
        sum(item["amount"] for item in category.ledger if item["amount"] < 0)
        for category in categories
    ]
    total_spent = sum(spendings)
    percentages = [int(spending / total_spent * 100) for spending in spendings]

    # Categories percentages
    for i in range(100, -1, -10):
        line = str(i).rjust(3) + "| "
        for j in range(len(percentages)):
            if i <= percentages[j]:
                # line += " " + "o" + " "
                line += "o  "
            else:
                line += "   "
        chart_string += f"{line}\n"

    chart_string += lower_line

    # Categories names
    labels = []
    for i in range(max_length):
        label = "     "
        for category in categories:
            if i < len(category.name):
                label += category.name[i] + "  "
            else:
                label += "   "
        labels.append(label)
    for label in labels:
        if label == labels[-1]:
            chart_string += f"{label}"
        else:
            chart_string += f"{label}\n"

    return chart_string


if __name__ == "__main__":
    # Test
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")

    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")

    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)

    # solution = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
    # print(solution)
    print((create_spend_chart([business, food, entertainment])))
