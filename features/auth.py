import sqlite3
from features.utility import *

def student_Registration(name=None, email=None, password=None, age=None, class_=None, contact_info=None):
     
    
    # Connect to check if email exists
    conn = sqlite3.connect('student_toolkit.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT email FROM students WHERE email = ?", (email,))
    if cursor.fetchone():
        conn.close()
        return False,f"❌ Email already registered. Please sign in."

    if not password_checker(password):
        return False,f"❌ Weak password. Please try again."
    if not email_checker(email):
        return False,f"Invalid Email"
    if not age_check(age):
        return False,f"This app is not for you"
        
    cursor.execute('''
        INSERT INTO students (email, name, password, age, class, contact_info) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (email, name, password, age, class_, contact_info))
    
    conn.commit()
    conn.close()
    return True,f"\n🎉 Student '{name}' registered successfully!"

def login(email=None, password=None):
    if email is None:
        return False,f"❌ Email is required for login."
    if password is None:
        return False,f"❌ Password is required for login."

    conn = sqlite3.connect('student_toolkit.db')
    cursor = conn.cursor()
    
    # Search for a row matching BOTH email and password
    cursor.execute("SELECT * FROM students WHERE email = ? AND password = ?", (email, password))
    student = cursor.fetchone()
    conn.close()
    
    if student:
        return True,student  
    else:
        return False,None
 
def reset_password(email, contact, new_password):
    conn = sqlite3.connect('student_toolkit.db')
    cursor = conn.cursor()
    
    # Fetch student details for verification
    cursor.execute("SELECT contact_info FROM students WHERE email = ?", (email,))
    result = cursor.fetchone()
    
    if result:
        db_contact = result[0]
         
        if contact != db_contact:
            conn.close()
            return False,f"❌ Incorrect contact information. Password reset failed."

        if not password_checker(new_password):
            conn.close()
            return False,f"❌ Weak password. Please try again."
        # Update the password in the database
        cursor.execute("UPDATE students SET password = ? WHERE email = ?", (new_password, email))
        conn.commit()
        return True,f"✅ Password reset successful."
    else:
        return False,f"❌ Email not found. Please register first."
        
    conn.close()

def profile(email):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students WHERE email=?", (email,))
    result=cursor.fetchone()
    if result:
        conn.close()
        return True,result
    else:
        conn.close()
        return False,f"❌ Profile not found."
    conn.close()

