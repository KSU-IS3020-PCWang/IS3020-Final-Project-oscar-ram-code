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

    print("Income added successfully.\n")


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

    print("Expense added successfully.\n")


def view_transactions():
    """
    Displays every transaction.
    """

    print("\n========== ALL TRANSACTIONS ==========")

    if len(transactions) == 0:
        print("No transactions found.\n")
        return

    for transaction in transactions:

        print(f"""
Date: {transaction['date']}
Type: {transaction['type']}
Category: {transaction['category']}
Description: {transaction['description']}
Amount: ${transaction['amount']:.2f}
-------------------------------
""")


def spending_by_category():
    """
    Displays total spending grouped by category.
    """

    print("\n====== Spending By Category ======")

    totals = {}

    for transaction in transactions:

        if transaction["type"] == "Expense":

            category = transaction["category"]

            if category not in totals:
                totals[category] = 0

            totals[category] += transaction["amount"]

    if len(totals) == 0:
        print("No expenses recorded.\n")
        return

    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")

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

    print("\n========== CURRENT BALANCE ==========")
    print(f"Total Income : ${income:.2f}")
    print(f"Total Expenses : ${expenses:.2f}")
    print(f"Current Balance : ${balance:.2f}\n")


def menu():
    """
    Displays the main menu.
    """

    print("====================================")
    print("     PERSONAL BUDGET TRACKER")
    print("====================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. View Spending By Category")
    print("5. Calculate Current Balance")
    print("6. Save Data")
    print("7. Exit")
    print("====================================")


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
            print("Data saved successfully.\n")

        elif choice == "7":

            save_data()

            print("\nThank you for using Personal Budget Tracker!")
            print("Your data has been saved.")

            break

        else:
            print("Invalid menu option.\n")


if __name__ == "__main__":
    main()
