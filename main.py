from Transaction import Transaction
from Budget import Budget
from User import User
from BudgetTracker import BudgetTracker

class main():

    # Test transactions for transaction class
    transaction1 = Transaction(100.0, "Groceries", "2023-10-01", "Weekly grocery shopping", "Expense")
    transaction2 = Transaction(500.0, "Salary", "2023-10-05", "Monthly salary", "Income")
    transaction3 = Transaction(50.0, "Entertainment", "2023-10-10", "Movie tickets", "Expense")

    # Print the transactions
    print(transaction1)
    print(transaction2)
    print(transaction3)

    # Test Budget for budget class
    # Create a Budget instance for "Groceries" with a limit of 500 and current spent of 0
    grocery_budget = Budget("Groceries", 500, 0)
    
    # Print the initial budget status
    print(grocery_budget)
    
    # Update the amount spent on groceries
    print(grocery_budget.update_spent(200))
    
    # Check the budget status
    print(grocery_budget.check_budget())
    
    # Spend more money
    print(grocery_budget.update_spent(400))
    
    # Check the budget status again
    print(grocery_budget.check_budget())

    print("----" * 20)
    # Tests User class
    # Create a User instance
    user = User("John Doe", [], {}, 0)

    # Add transactions
    user.add_transaction(1000, "Salary", "2024-02-20", "Monthly salary", "income")
    user.add_transaction(-200, "Groceries", "2024-02-21", "Weekly groceries", "expense")
    user.add_transaction(-50, "Transport", "2024-02-22", "Bus fare", "expense")

    # Print balance
    print(user.calculate_balance())

    # Get transactions filtered by type
    print("\nIncome Transactions:")
    print(user.get_transactions(filter_type="income"))

    print("\nExpense Transactions:")
    print(user.get_transactions(filter_type="expense"))

    # Set budgets
    print(user.set_budget("Groceries", 300))
    print(user.set_budget("Transport", 100))

    # Check budgets
    print("\nBudget Status:")
    print(user.check_all_budgets())

if __name__ == '__main__':
    main()

