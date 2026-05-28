# database_setup.py
import sqlite3

def init_db():
    """Connects to the database and ensures all 4 core tables exist."""
    conn = sqlite3.connect('student_toolkit.db')
    cursor = conn.cursor()
    
    #Students Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            email TEXT PRIMARY KEY,
            name TEXT,
            password TEXT,
            age INTEGER,
            class TEXT,
            contact_info TEXT
        )
    ''')

  
    #Tasks Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_email TEXT,
            task TEXT,
            completed INTEGER DEFAULT 0,
            deadline TEXT,
            FOREIGN KEY (student_email) REFERENCES students (email)
        )
    ''')
    #Expense Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_email TEXT,
            amount FLOAT,
            category TEXT,
            date TEXT,
            FOREIGN KEY (student_email) REFERENCES students (email)
        )
    ''')
    
 
    conn.commit()
    conn.close()
    print("🗄️ Database verification complete. All tables are ready.")