import sqlite3
from features.utility import *

def expenses_tracker(email,amount=None,category=None,date=None):
    print("\n--- Expenses Tracker ---")
    if amount is None:
        return f"❌ Amount cannot be empty. Please try again."
    if category is None:
        return f"❌ Category cannot be empty. Please try again."
    if date is None:
        return f"❌ Date cannot be empty. Please try again."
    if not date_checker(date):
        return f"❌ Invalid date format. Please enter the date in DD-MM-YYYY format."
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute('''
        INSERT INTO expenses(student_email,amount,category,date) VALUES(?,?,?,?)
    ''',(email,amount,category,date))
    conn.commit()
    conn.close()
    return f"✅ Expense added successfully!"

def view_expenses(email):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE student_email = ?", (email,))
    expenses=cursor.fetchall()
    if expenses:
        conn.commit()
        conn.close()
        return expenses
    else:
        conn.commit()
        conn.close()
        return f"❌ No expenses found."