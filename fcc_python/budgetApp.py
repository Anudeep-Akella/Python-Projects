"""A Buget App that calculates how much amount of money was allocated and spent on each category of daily necessities. """
class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description = ""):
        """Let's you allocate an amount to the category."""
        self.ledger.append({'amount': amount, 'description': description})


    def withdraw(self,amount,description=""):
        """Let's you withdraw amount for that category."""
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description':description})
            return True
        return False

    def get_balance(self):
        """Shows how much amount of money was present after repeated deposits and withdraws for each category."""
        balance = 0
        for ledger in self.ledger:
            balance += ledger['amount']
        return balance

    def transfer(self,amount,other):
        """Let's you transfer amount of money from one category to another category."""
        if self.withdraw(amount,f"Transfer to {other.name}"):
            other.deposit(amount,f"Transfer from {self.name}")
            return True
        return False
        

    def check_funds(self,amount):
        """Let's you check the amount of money before performing any type of transaction"""
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        """Let's you print the class object in the form of a custimized string."""
        output = f"{self.name.center(30,'*')}\n"
        for ledger in self.ledger:
            desc = ledger['description'][:23]
            amount = f"{ledger['amount']:.2f}"
            output += f"{desc:<23}{amount:>7}\n"

        output += f"Total: {self.get_balance():.2f}"

        return output

def create_spend_chart(categories):
    """A simple chart will be shown for the amount of money allocated and spent for each category."""
    spent_per_category = []
    total_spent = 0

    for category in categories:
        category_spent = 0
        for item in category:
            if item['amount']<0:
                category_spent += abs(item['amount'])
        spent_per_category.append(category_spent)
        total_spent += category_spent

    
    percentages = []
    for spent in spent_per_category:
        if total_spent > 0:
            percent = (spent / total_spent) * 100
            percentages.append((percent // 10) * 10)

        else:
            percentages.appned(0)

    
    chart = 'Percentage spent per category'

    for i in range(100,-1,-10):
        
        chart += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    chart += "     " + "-" * (len(categories) * 3 +1) + "\n"

    max_len = max(len(category.name) for category in categories)

    padded_names = [category.name.ljust(max_len) for category in categories]

    for i in range(max_len):
        chart += "     "
        for name in padded_names:
            chart += f"{name[i]}  "
        if i < max_len - 1:
            chart += "\n"

    return chart
            
    
