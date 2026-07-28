# IS 3020 Final Project

## Student and Project Information

- Student name: Oscar Ramirez
- GitHub username: oscar-ram-code
- Project title: Personal Budget Tracker
- Application purpose: The Personal Budget Tracker is a Python command-line application that helps users keep track of their personal finances in one simple place. Users can record their income and expenses, organize transactions into different categories, check their current balance, and view summaries of where their money is being spent. The program saves all transaction data to a CSV file, so users can close the application and come back later without losing any of their budget information.

## How to Run the Application

Python Version
Python 3.10 or newer is recommended.

Required Files

The project should contain the following files:

- budget_tracker.py
- transactions.csv (created automatically the first time the program is used if it does not already exist)

1. Running the Program in PyCharm
2. Open PyCharm.
3. Open the project folder.
4. Make sure Python 3.10 or later is selected as the project interpreter.
5. Open budget_tracker.py.
6. Click the Run button or press Shift + F10.
7. The main menu will appear in the console, allowing the user to select different budgeting options.

## Major Features

The application includes the following features:

- Add new income transactions.
- Add new expense transactions.
- View all recorded transactions.
- View total spending grouped by category.
- Calculate total income, total expenses, and current balance.
- Automatically save transaction data to a CSV file.
- Automatically load previously saved transaction data when the application starts.
- Validate numeric input and prevent invalid amounts from being entered.

## Python Concepts Used
The application demonstrates several Python concepts learned throughout IS 3020.

- **Functions:** The application is organized into multiple functions, each responsible for a specific task such as adding income, calculating balances, saving data, or displaying reports.
- **Variables:** Variables are used to store user input, balances, transaction information, and menu selections.
- **Collections:** A list stores all transactions while each transaction is represented as a dictionary containing the transaction date, type, category, description, and amount.
- **Conditionals:** 'if', 'elif', and 'else' statements are used to process menu choices, determine transaction types, and validate user input.
- **Loops:** A while loop keeps the application running until the user chooses to exit, while for loops process transaction records when displaying information or calculating totals.
- **File Persistence:** The application uses the Python csv module to save transaction information to a CSV file and reload it whenever the application starts.
- **Exception Handling:** try and except blocks prevent the program from crashing when users enter invalid numeric values or when file-related errors occur.

## Data Files

## Data Files

### `transactions.csv`

This file stores all financial transactions entered by the user.

Each row represents one transaction and contains the following fields:

| Field | Description |
|-------|-------------|
| Date | The transaction date entered by the user. |
| Type | Indicates whether the transaction is **Income** or **Expense**. |
| Category | The spending or income category (Food, Housing, Utilities, Paycheck, etc.). |
| Description | A short description of the transaction. |
| Amount | The dollar amount of the transaction. |

The application automatically loads this file when it starts and updates it whenever new transactions are added.

## Testing Summary

## Testing Summary

The following scenarios were tested during development:

- Added multiple income transactions.
- Added multiple expense transactions.
- Viewed all saved transactions.
- Viewed spending totals by category.
- Calculated the current account balance.
- Closed and restarted the application to verify that saved transactions loaded correctly.
- Entered invalid numeric values to confirm that exception handling prevented the program from crashing.
- Entered negative or zero dollar amounts to verify input validation.
- Started the program when no `transactions.csv` file existed to verify that a new CSV file was created automatically.

## AI Use

## AI Use

Artificial intelligence was used only after creating an original working version of the application.

AI assistance included:

- Improving the organization and readability of the code.
- Adding function docstrings and helpful comments.
- Improving input validation using `try/except`.
- Refining the menu structure and overall function organization.
- Reviewing the program to ensure it met the IS 3020 project requirements.

All AI-generated suggestions were reviewed, tested in PyCharm, and modified as needed to ensure they worked correctly. I made sure I understood how the code worked before including it in my final submission.
