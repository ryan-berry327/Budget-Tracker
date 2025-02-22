

class Transaction:
    def __init__(self, amount, category, date,description, type):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        self.type = type

    def __str__(self):
        return f"Transaction: {self.description}, Amount: {self.amount}, Category: {self.category}, Date: {self.date}, Type of Transaction: {self.type}"

    