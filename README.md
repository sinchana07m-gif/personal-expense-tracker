# personal-expense-tracker
A Python-based personal expense tracker using SQLite to manage, update, delete, search, and analyze daily expenses.
# Personal Expense Tracker

A simple command-line application built using Python and SQLite to record and manage personal expenses.

## Features

* Add new expenses
* View all recorded expenses
* Search expenses by category
* Update existing expenses
* Delete expenses
* Calculate total expenses
* View category-wise expense summary
* Store expense data using SQLite

## Technologies Used

* Python
* SQLite

## Project Structure

```text
Personal-Expense-Tracker/
│
├── expense_tracker.py
├── expenses.db
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
```

### 2. Open the project folder

```bash
cd Personal-Expense-Tracker
```

### 3. Run the program

```bash
python expense_tracker.py
```

The application will display a menu where you can choose different expense management options.

## How It Works

The application uses SQLite to store expense records. Each expense contains:

* Date
* Category
* Description
* Amount

The program provides options to add, view, search, update, and delete records. It also calculates the total amount spent and provides a category-wise summary.

## Future Improvements

* Add a graphical user interface
* Add monthly expense reports
* Add data visualization
* Add income tracking
* Add budget management

## Author

**Sinchana M**

