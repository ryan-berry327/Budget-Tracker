# Budget Tracker CLI

## Overview
The **Budget Tracker CLI** is a command-line application designed to help users manage their personal finances efficiently. Users can track income and expenses, set budgets for specific categories, and generate financial reports.

## Features
- Add and categorize transactions (income/expenses)
- Set and monitor spending limits per category
- View detailed financial reports
- Check if spending exceeds budget limits
- Save and load financial data for future use

## Project Structure
The project follows an **object-oriented programming (OOP)** approach with well-defined classes:

### 1. `Transaction`
- Represents a single income or expense.
- Stores amount, category, date, and description.

### 2. `Budget`
- Tracks spending limits for a specific category.
- Updates spending and checks for budget exceedance.

### 3. `User`
- Manages all transactions and budgets.
- Calculates balance, filters transactions, and generates reports.

### 4. `BudgetTracker`
- Handles CLI interactions and user inputs.
- Provides a menu-driven interface for easy navigation.


## Usage
1. Choose an option from the menu.
2. Add transactions and categorize them.
3. Set budgets to monitor spending.
4. Generate reports for financial insights.

## Future Enhancements
- Graphical User Interface (GUI) version.
- Integration with databases for persistent storage.
- Automated financial insights and recommendations.


