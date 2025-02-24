from User import User

class BudgetTracker:
    def __init__(self):
        """Initializes the BudgetTracker application with a User instance."""
        user_name = input("Enter your name: ")
        self.user = User(user_name, [], {}, 0.0)  # Initializes User with empty transactions, budgets, and zero balance

    def display_menu(self):
        """Displays the main menu options for the user."""
        print("\n--- Budget Tracker Menu ---")
        print("1. Add a Transaction")
        print("2. Set a Budget")
        print("3. View Transactions")
        print("4. Check Budget Status")
        print("5. Generate Report")
        print("6. Save & Exit")

    def handle_input(self, choice):
        """Handles user input and executes the corresponding function."""
        if choice == "1":
            self.add_transaction_flow()
        elif choice == "2":
            self.set_budget_flow()
        elif choice == "3":
            self.show_transactions_flow()
        elif choice == "4":
            self.show_budget_status()
        elif choice == "5":
            self.generate_report()
        elif choice == "6":
            self.exit_application()
        else:
            print("Invalid choice. Please enter a number between 1-6.")

    def add_transaction_flow(self):
        """Guides the user through adding a new transaction."""
        amount = float(input("Enter transaction amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        transaction_type = input("Is this an 'income' or 'expense'? ").lower()

        if transaction_type not in ["income", "expense"]:
            print("Invalid transaction type. Please enter 'income' or 'expense'.")
            return

        self.user.add_transaction(amount, category, date, description, transaction_type)
        print("Transaction added successfully!")

    def set_budget_flow(self):
        """Guides the user through setting a budget for a specific category."""
        category = input("Enter the category for the budget: ")
        limit = float(input("Enter the budget limit: "))

        self.user.set_budget(category, limit)
        print(f"Budget of {limit} set for category '{category}'.")

    def show_transactions_flow(self):
        """Allows the user to filter and view transactions."""
        filter_type = input("Filter by 'income' or 'expense' (or press Enter for all): ").lower() or None
        filter_category = input("Enter category to filter (or press Enter for all): ") or None

        transactions = self.user.get_transactions(filter_type, filter_category)

        if transactions:
            print("\n--- Transactions ---")
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions found matching the criteria.")

    def show_budget_status(self):
        """Displays the budget status for all categories."""
        print("\n--- Budget Status ---")
        for category, budget in self.user.budget.items():
            status = "Exceeded" if budget.is_exceeded() else "Within Limit"
            print(f"{category}: {status}")

    def generate_report(self):
        """Generates a financial report summarizing transactions and budget status."""
        print("\n--- Financial Report ---")
        self.user.generate_report()

    def exit_application(self):
        """Saves data before exiting the application."""
        self.user.save_data()
        print("Data saved successfully. Exiting the application.")
        exit()

# Running the Budget Tracker application
if __name__ == "__main__":
    app = BudgetTracker()
    while True:
        app.display_menu()
        choice = input("Enter your choice: ")
        app.handle_input(choice)
