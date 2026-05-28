import sqlite3
from features.utility import *

def expenses_tracker(email):
    print("\n--- Expenses Tracker ---")
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category of expense (e.g., Food, Transport, Books): ")
    date = input("Enter the date of expense (DD-MM-YYYY): ").strip()
    if not date_checker(date):
        print("❌ Invalid date format. Please enter the date in DD-MM-YYYY format.")
        return 
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute('''
        INSERT INTO expenses(student_email,amount,category,date) VALUES(?,?,?,?)
    ''',(email,amount,category,date))
    print("✅ Expense added successfully!")
    conn.commit()
    conn.close()

def view_expenses(email):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE student_email = ?", (email,))
    expenses=cursor.fetchall()
    if expenses:
        print(50*"=")
        print("\t\t-- Expenses --")
        for expense in expenses:
            print(f"Amount: {expense[2]}, Category: {expense[3]}, Date: {expense[4]}")
        print(50*"=")
    else:
        print("❌ No expenses found.")
    conn.close()