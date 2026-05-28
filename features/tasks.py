import sqlite3
from features.utility import *

def schedule_task(email):
    task=input("Enter the task you want to schedule :- ")
    deadline=input("Enter the deadline for the task (DD-MM-YYYY): ").strip()
    if not date_checker(deadline):
        print("❌ Invalid date format. Please enter the date in DD-MM-YYYY format.")
        return schedule_task(email)
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute('''
        INSERT INTO tasks(student_email,task,deadline) VALUES(?,?,?)
    ''',(email,task,deadline))
    print("✅ Task scheduled successfully!")
    conn.commit()
    conn.close()

def view_tasks(email):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE student_email = ?", (email,))
    tasks=cursor.fetchall()
    if tasks:
        print(50*"=")
        print("\t\t-- Tasks --")
        for task in tasks:
            print(f"Task: {task[2]}, Deadline: {task[4]}")
        print(50*"=")
    else:
        print("❌ No tasks found.")
    conn.close()

def delete_tasks(email):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE student_email = ?", (email,))
    tasks=cursor.fetchall()
    if tasks:
        
        print("✅ Tasks found!")
        
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[2]}, Deadline: {task[4]}")
        task_id=input("Enter the ID of the task you want to delete: ")
        cursor.execute("DELETE FROM tasks WHERE id = ? AND student_email = ?", (task_id, email))
        conn.commit()
        print("✅ Task deleted successfully.")
    else:
        print("❌ No tasks found.")
    conn.close()

def Completed_tasks(email):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE student_email = ? and completed = 0", (email,))
    tasks=cursor.fetchall()
    if tasks:
        print("✅ Following are incomplete Tasks!")
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[2]}, Deadline: {task[4]}, Completed: {task[3]}")
        task_id=input("Enter the ID of the task you want to mark as completed: ")
        cursor.execute("UPDATE tasks SET completed = TRUE WHERE id = ? AND student_email = ?", (task_id, email))
        conn.commit()
        print("✅ Task is marked as completed.")
    else:
        print("❌ No tasks found.")
    conn.close()

def view_completed_tasks(email):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE student_email = ? and completed = 1", (email,))
    tasks=cursor.fetchall()
    if tasks:
        print(50*"=")
        print("✅ Following are completed Tasks!")
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[2]}, Deadline: {task[4]}, Completed: {task[3]}")
        print(50*"=")
    else:
        print("❌ No completed tasks found.")
    conn.close()

def view_incomplete_tasks(email):
    conn=sqlite3.connect('student_toolkit.db')
    cursor=conn.cursor()
    cursor.execute('''SELECT * FROM tasks WHERE student_email=? and completed=0''',(email,))
    tasks=cursor.fetchall()
    if tasks:
        print(50*"=")
        print("✅ Following are incomplete Tasks!")
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[2]}, Deadline: {task[4]}, Completed: {task[3]}")
        print(50*"=")
    else:
        print("❌ No incomplete tasks found.")
    conn.close()