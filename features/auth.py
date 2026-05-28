import sqlite3
from features.utility import *

def student_Registration():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    
    # Connect to check if email exists
    conn = sqlite3.connect('student_toolkit.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT email FROM students WHERE email = ?", (email,))
    if cursor.fetchone():
        print("❌ Email already registered. Please sign in.")
        conn.close()
        return
    password = input("Enter your password: ")
    if not password_checker(password):
        print("❌ Invalid password. Please try again.")
        return student_Registration()
    age = input("Enter your age: ")
    class_ = input("Enter your class: ")
    contact_info = input("Enter your mobile no:  ")
    
    cursor.execute('''
        INSERT INTO students (email, name, password, age, class, contact_info) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (email, name, password, age, class_, contact_info))
    
    conn.commit()
    conn.close()
    print(f"\n🎉 Student '{name}' registered successfully!")

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    conn = sqlite3.connect('student_toolkit.db')
    cursor = conn.cursor()
    
    # Search for a row matching BOTH email and password
    cursor.execute("SELECT * FROM students WHERE email = ? AND password = ?", (email, password))
    student = cursor.fetchone()
    conn.close()
    
    if student:
        print(f"\n✅ Login successful! Welcome back.")
        return student,True  
    else:
        print("❌ Invalid email or password.")
        forgot_password = input("Forgot password? (yes/no): ")
        if forgot_password.lower() == 'yes':
            reset_password(email)
        else:
            return  None,False

def reset_password(email):
    conn = sqlite3.connect('student_toolkit.db')
    cursor = conn.cursor()
    
    # Fetch student details for verification
    cursor.execute("SELECT contact_info FROM students WHERE email = ?", (email,))
    result = cursor.fetchone()
    
    if result:
        db_contact = result[0]
        contact = input("Enter your registered mobile number: ")
        
        if contact != db_contact:
            print("❌ Incorrect contact information. Password reset failed.")
            conn.close()
            return 
            
        new_password = input("Enter your new password: ")
        if not password_checker(new_password):
            print("❌ Invalid password. Please try again.")
            conn.close()
            return reset_password(email)
        # Update the password in the database
        cursor.execute("UPDATE students SET password = ? WHERE email = ?", (new_password, email))
        conn.commit()
        print("✅ Password reset successful.")
    else:
        print("❌ Email not found. Please register first.")
        
    conn.close()

def profile(email):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students WHERE email=?", (email,))
    result=cursor.fetchone()
    if result:
        print(50*"=")
        print("\t\t-- Student Profile --\n")
        print(f"Name :  {result[1]}")
        print(f"Age :  {result[3]}")
        print(f"Class :  {result[4]}")
        print(f"Contact Info : { result[5]}")
        print(50*"=")
    else:
        print("❌ Profile not found.")
    conn.close()
