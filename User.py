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
        for amount in self.transactions:
            self.balance += amount
        return f"Your balance is: {self.balance}.2f"
    
    # Maybe I should look at having the categories checked inside the types of transactions?
    def get_transactions(self,filter_type = None, filter_category = None):
        # Returns a list of transactions that match the filter criteria
        if filter_type.lower() = 'income':
            return [t for t in self.transactions if t.type == filter_type]
        elif filter_type.lower() = 'expense':
            return [t for t in self.transactions if t.type == filter_type]
        else:
            return "This type of transaction does not exist, you can only search for income or expense"

        if filter_category is in self.transactions.category:
            return [t for t in self.transactions if t.category == filter_category]
        else: 
            return "This category does not exist within your transactions."
    
    def set_budget(self,category,limit):
        # Sets a budget for a specific category
        self.budget[category] = limit # Sets the limit you have entered into the category you have chosen
        retrun f"You have set the budget limit of: {limit} for the category: {self.budget[category]}"
    
    # Checks if any category is over budget. and returns the categories that are
    def check_all_budgets(self):
        return [bc['current_spent'],bl['limit'] for bc['current_spent'],bl['limit'] in self.budget.items() if bc['current_spent']bl['limit']] # BC is budget categories and BL is budget limits

    # Generates a report of all transactions, including the category, date, description, and amount
    def generate_report(self):
        pass


    # think about it
    def save_data():
        pass

    def load_data():
        pass


