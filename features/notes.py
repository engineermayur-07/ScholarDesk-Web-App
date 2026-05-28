import sqlite3
from features.utility import *

def add_notes(email):
    note=input("Enter your note: ")
    date=input("Enter the date for the note (DD-MM-YYYY): ").strip()
    if not date_checker(date):
        print("❌ Invalid date format. Please enter the date in DD-MM-YYYY format.")
        return add_notes(email)
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute('''
        INSERT INTO notes(student_email,note,date) VALUES(?,?,?)
    ''',(email,note,date))
    print("✅ Note added successfully!")
    conn.commit()
    conn.close()

def view_notes(email):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE student_email = ?", (email,))
    notes=cursor.fetchall()
    if notes:
        print(50*"=")
        print("\t\t-- Notes --")
        for note in notes:
            print(f"Note: {note[2]}, Date: {note[3]}")
        print(50*"=")
    else:
        print("❌ No notes found.")
    conn.close()

def delete_notes(email):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE student_email = ?", (email,))
    notes=cursor.fetchall()
    if notes:
        print("✅ Notes found!")
        for note in notes:
            print(f"ID: {note[0]}, Note: {note[2]}, Date: {note[3]}")
        note_id=input("Enter the ID of the note you want to delete: ")
        flag=False
        for note in notes:
            if str(note[0])==note_id:
                flag=True
                break
        if flag==False:
            print("❌ Invalid note ID. Please try again.")
            return delete_notes(email)
        cursor.execute("DELETE FROM notes WHERE id = ? AND student_email = ?", (note_id, email))
        conn.commit()
        print("✅ Note deleted successfully.")
    else:
        print("❌ No notes found.")
    conn.close() 