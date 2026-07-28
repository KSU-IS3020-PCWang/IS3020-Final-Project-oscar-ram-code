"""
Oscar Ramirez
IS 3020 Final Project
Personal Budget Tracker

This application allows users to track income and expenses,
view spending by category, calculate their balance,
and save/load financial data using a CSV file.
""" 

import csv
import os

FILE_NAME = "transactions.csv"

transactions = []


def load_data():
    """
    Loads transaction data from the CSV file if it exists.
    """
    global transactions

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["amount"] = float(row["amount"])
                transactions.append(row)


def save_data():
    """
    Saves all transactions to the CSV file.
    """

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = [
            "date",
            "type",
            "category",
            "description",
            "amount"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for transaction in transactions:
            writer.writerow(transaction)


def add_income():
    """
    Adds an income transaction.
    """

    print("\n--- Add Income ---")

    date = input("Date (MM/DD/YYYY): ")
    category = input("Income Category: ")
    description = input("Description: ")

    while True:
        try:
            amount = float(input("Amount: $"))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    transaction = {
        "date": date,
        "type": "Income",
        "category": category,
        "description": description,
        "amount": amount
    }

    transactions.append(transaction)
    save_data()

   print("\n=========================================")
print(f"Income of ${amount:.2f} added successfully!")
print("Transaction has been saved.")
print("=========================================\n")


def add_expense():
    """
    Adds an expense transaction.
    """

    print("\n--- Add Expense ---")

    date = input("Date (MM/DD/YYYY): ")
    category = input("Expense Category: ")
    description = input("Description: ")

    while True:
        try:
            amount = float(input("Amount: $"))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    transaction = {
        "date": date,
        "type": "Expense",
        "category": category,
        "description": description,
        "amount": amount
    }

    transactions.append(transaction)
    save_data()

    print("\n=========================================")
print(f"Expense of ${amount:.2f} added successfully!")
print("Transaction has been saved.")
print("=========================================\n")


def view_transactions():
    """
    Displays every transaction.
    """

    print("\n=========================================")
    print("           ALL TRANSACTIONS")
    print("=========================================")

    if len(transactions) == 0:
        print("No transactions have been recorded yet.\n")
        return

    for i, transaction in enumerate(transactions, start=1):

        print(f"Transaction #{i}")
        print(f"Date: {transaction['date']}")
        print(f"Type: {transaction['type']}")
        print(f"Category: {transaction['category']}")
        print(f"Description: {transaction['description']}")
        print(f"Amount: ${transaction['amount']:.2f}")
        print("-----------------------------------------")

    print(f"\nTotal Transactions: {len(transactions)}\n")


def spending_by_category():
    """
    Displays total spending grouped by category.
    """

    print("\n=========================================")
    print("        SPENDING BY CATEGORY")
    print("=========================================")

    totals = {}

    for transaction in transactions:

        if transaction["type"] == "Expense":

            category = transaction["category"]

            if category not in totals:
                totals[category] = 0

            totals[category] += transaction["amount"]

    if len(totals) == 0:
        print("No expenses have been recorded.\n")
        return

    for category in sorted(totals):
        print(f"{category:<20} ${totals[category]:>8.2f}")

    print()


def calculate_balance():
    """
    Calculates total income,
    total expenses,
    and remaining balance.
    """

    income = 0
    expenses = 0

    for transaction in transactions:

        if transaction["type"] == "Income":
            income += transaction["amount"]
        else:
            expenses += transaction["amount"]

    balance = income - expenses

    print("\n=========================================")
    print("          CURRENT BALANCE")
    print("=========================================")
    print(f"Total Income:        ${income:.2f}")
    print(f"Total Expenses:      ${expenses:.2f}")
    print("-----------------------------------------")
    print(f"Current Balance:     ${balance:.2f}")
    print(f"Transactions Saved:  {len(transactions)}")
    print("=========================================\n")

def menu():
    """
    Displays the main menu.
    """

    print("\n=========================================")
    print("      PERSONAL BUDGET TRACKER")
    print("=========================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. View Spending By Category")
    print("5. Calculate Current Balance")
    print("6. Save Data")
    print("7. Exit")
    print("=========================================")


def main():
    """
    Main program loop.
    """

    load_data()

    while True:

        menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_income()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            view_transactions()

        elif choice == "4":
            spending_by_category()

        elif choice == "5":
            calculate_balance()

        elif choice == "6":
            save_data()
            print("\nData saved successfully!\n")

        elif choice == "7":

            save_data()

            print("\n=========================================")
print("Thank you for using Personal Budget Tracker!")
print("All transactions have been saved successfully.")
print("Goodbye!")
print("=========================================")
            break

        else:
            print("Invalid menu option.\n")


if __name__ == "__main__":
    main()
