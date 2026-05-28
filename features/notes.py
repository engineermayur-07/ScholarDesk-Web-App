import sqlite3
from features.utility import *

def add_notes(email,note=None,date=None):
    if not date_checker(date):
        return f"❌ Invalid date format. Please enter the date in DD-MM-YYYY format."
        
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute('''
        INSERT INTO notes(student_email,note,date) VALUES(?,?,?)
    ''',(email,note,date))
    print("✅ Note added successfully!")
    conn.commit()
    conn.close()
    return f"✅ Note added successfully!"

def view_notes(email):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE student_email = ?", (email,))
    notes=cursor.fetchall()
    if notes:
        conn.close()
        return notes
         
    else:
        print("❌ No notes found.")
        conn.commit()
        conn.close()
        return f"❌ No notes found."

def delete_notes(email,note_id=None):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE student_email = ?", (email,))
    notes=cursor.fetchall()
    if notes:
        print("✅ Notes found!")
         
        flag=False
        for note in notes:
            if str(note[0])==note_id:
                flag=True
                break
        if flag==False:
            conn.commit()
            conn.close()
            return f"❌ Invalid note ID. Please try again."
        cursor.execute("DELETE FROM notes WHERE id = ? AND student_email = ?", (note_id, email))
        
        conn.commit()
        conn.close()

        return f"✅ Note deleted successfully."
    else:
        conn.commit()
        conn.close()
        return f"❌ No notes found."