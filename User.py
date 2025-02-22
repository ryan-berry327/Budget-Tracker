from Transaction import Transaction
from Budget import Budget

class User:

    def __init__(self, name, transactions, budget, balance):
        self.name = name
        self.transactions = [] # Stores transaction objects
        self.budget = {} # maps Categories to budget objects
        self.balance = balance

    def add_transaction(self, amount,category,date,description,type):
        # Adds a transaction to the user's transactions list
        self.transactions.append(Transaction(amount,category,date,description,type))
    
    def calculate_balance(self):
        for transaction in self.transactions:
            if transaction.type == 'income':
                self.balance += transaction.amount
            elif transaction.type == 'expense':
                self.balance += transaction.amount
        return f"Your balance is: {self.balance}"
    
    # Maybe I should look at having the categories checked inside the types of transactions?
    def get_transactions(self,filter_type = None, filter_category = None):
        for transaction in self.transactions:
            # Che
            if filter_type == 'income' and transaction.type == 'income':
                print(transaction)
            elif filter_type == 'expense' and transaction.type == 'expense':
                print(transaction)

        
    
    def set_budget(self,category,limit):
        # Sets a budget for a specific category
        self.budget[category] = limit # Sets the limit you have entered into the category you have chosen
        return f"You have set the budget limit of: {limit} for the category: {category}"
    
    # Checks if any category is over budget. and returns the categories that are
    def check_all_budgets(self):
        return [(b,c) for b,c in self.budget.items()] # BC is budget categories and BL is budget limits

    # Generates a report of all transactions, including the category, date, description, and amount
    def generate_report(self):
        pass

    # think about it
    def save_data():
        pass

    def load_data():
        pass


