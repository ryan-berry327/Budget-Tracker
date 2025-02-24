from Transaction import Transaction
from Budget import Budget
import json
import os


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
    

    def get_transactions(self, filter_type=None, filter_category=None):
        filter_results = []

        for transaction in self.transactions:
            # If filter type is provided, ensure it matches
            if filter_type and transaction.type != filter_type:
                continue  # Skip this transaction if type doesn't match

            # If filter category is provided, ensure it matches
            if filter_category and transaction.category != filter_category:
                continue  # Skip this transaction if category doesn't match

            # If the transaction meets the conditions, add it to results
            filter_results.append(transaction)

        return filter_results  # Return all filtered transactions

    
    def set_budget(self,category,limit):
        # Sets a budget for a specific category
        self.budget[category] = limit # Sets the limit you have entered into the category you have chosen
        return f"You have set the budget limit of: {limit} for the category: {category}"
    
    # Checks if any category is over budget. and returns the categories that are
    def check_all_budgets(self):
        return [(b,c) for b,c in self.budget.items()] # BC is budget categories and BL is budget limits

    # Generates a report of all transactions, including the category, date, description, and amount
    def generate_report(self):
        for transaction in self.transactions:
            print(f"Category: {transaction.category}, Date: {transaction.date}, Description: {transaction.description}")

    # think about it
    def save_data():
        with open("budget_data.json","w") as file:
            json.dump(self.transactions,file,indent=4)

    def load_data():
        if os.path.exists("budget_data.json","r") as file:
            self.transactions = json.load(file)


