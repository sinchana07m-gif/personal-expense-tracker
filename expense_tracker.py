import sqlite3

# Connect to database
conn = sqlite3.connect("expenses.db")

# Create cursor
cursor = conn.cursor()

# Create expenses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT NOT NULL,
    amount REAL NOT NULL
)
""")

conn.commit()
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    cursor.execute("""
    INSERT INTO expenses (date, category, description, amount)
    VALUES (?, ?, ?, ?)
    """, (date, category, description, amount))

    conn.commit()

    print("\nExpense added successfully!")
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n---------- ALL EXPENSES ----------")

    for expense in expenses:
        print(
            f"ID: {expense[0]} | "
            f"Date: {expense[1]} | "
            f"Category: {expense[2]} | "
            f"Description: {expense[3]} | "
            f"Amount: ₹{expense[4]:.2f}"
        )
def search_by_category():
    category = input("Enter category to search: ")

    cursor.execute(
        "SELECT * FROM expenses WHERE category = ?",
        (category,)
    )

    expenses = cursor.fetchall()

    if not expenses:
        print("\nNo expenses found for this category.")
        return

    print(f"\n---------- {category.upper()} EXPENSES ----------")

    for expense in expenses:
        print(
            f"ID: {expense[0]} | "
            f"Date: {expense[1]} | "
            f"Description: {expense[3]} | "
            f"Amount: ₹{expense[4]:.2f}"
        )
def total_expenses():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print(f"\nTotal Expenses: ₹{total:.2f}")
def category_summary():
    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)

    results = cursor.fetchall()

    if not results:
        print("\nNo expenses found.")
        return

    print("\n---------- CATEGORY SUMMARY ----------")

    for category, amount in results:
        print(f"{category}: ₹{amount:.2f}")
def update_expense():
    expense_id = int(input("Enter expense ID to update: "))

    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    )

    expense = cursor.fetchone()

    if not expense:
        print("\nExpense not found.")
        return

    print("\nEnter new details:")

    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    cursor.execute("""
    UPDATE expenses
    SET date = ?, category = ?, description = ?, amount = ?
    WHERE id = ?
    """, (date, category, description, amount, expense_id))

    conn.commit()

    print("\nExpense updated successfully!")
def delete_expense():
    expense_id = int(input("Enter expense ID to delete: "))

    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    )

    expense = cursor.fetchone()

    if not expense:
        print("\nExpense not found.")
        return

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()

    print("\nExpense deleted successfully!")
def main():
    while True:
        print("\n==============================")
        print("     PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Total Expenses")
        print("7. Category Summary")
        print("8. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_by_category()

        elif choice == "4":
            update_expense()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            total_expenses()

        elif choice == "7":
            category_summary()

        elif choice == "8":
            print("\nThank you for using Personal Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()

conn.close()