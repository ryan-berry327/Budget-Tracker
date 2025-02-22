

class User:

    def __init__(self, name, transactions, budget, balance):
        self.name = name
        self.transactions = [] # Stores transaction objects
        self.budget = {} maps Categories to budget objects
        self.balance = balance

    def add_transaction(self, amount,category,date,description,type):
        # Adds a transaction to the user's transactions list
        self.transactions.append(Transaction(amount,category,date,description,type))
    
    def calculate_balance(self):
        
        pass
    
    # Maybe I should look at having the categoryies checked inside the types of transactions?
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
        pass

    def check_all_budgets(self):
        pass

    def generate_report(self):
        pass

    # think about it
    def save_data():
        pass

    def load_data():
        pass


