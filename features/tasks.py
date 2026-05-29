import sqlite3
from features.utility import *

def schedule_task(email, task, deadline = None):
    task = (task or '').strip()
    deadline = (deadline or '').strip()

    if not task:
        return f"Task description cannot be empty. Please try again."

    if not deadline:
        return f"Deadline cannot be empty. Please try again."

    if not date_checker(deadline):
        return f"Invalid date format. Please enter the date in DD-MM-YYYY format."
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute('''
        INSERT INTO tasks(student_email,task,deadline) VALUES(?,?,?)
    ''',(email,task,deadline))
    print("Task scheduled successfully!")
    conn.commit()
    conn.close()
    return f"Task scheduled successfully!"

def view_tasks(email):
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE student_email = ?", (email,))
    tasks=cursor.fetchall()
    if tasks:
         conn.commit()
         conn.close()
         return tasks
    conn.close()
    return f"No tasks found."

def delete_tasks(email, task_id=None):
    try:
        task_id = int(task_id)
    except (TypeError, ValueError):
        return f"Invalid task ID. Please try again."

    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE student_email = ?", (email,))
    tasks=cursor.fetchall()
    if tasks:

        print("Tasks found!")
        flag=False
        for task in tasks:
            if task[0] == task_id:
                flag=True
                break
        if flag:
            cursor.execute("DELETE FROM tasks WHERE id = ? AND student_email = ?", (task_id, email))
            conn.commit()
            conn.close()
            return f"Task deleted successfully."
        else:
            conn.commit()
            conn.close()
            return f"Wrong task ID. Please try again."
    else:
        conn.commit()
        conn.close()
        return f"No tasks found."
 
def Completed_tasks(email, task_id=None):
    try:
        task_id = int(task_id)
    except (TypeError, ValueError):
        return f"Invalid task ID. Please try again."

    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE student_email = ? and completed = 0", (email,))
    tasks=cursor.fetchall()
    if tasks:
        flag=False
        for task in tasks:
            if task[0] == task_id:
                flag=True
                break
        if flag:
            cursor.execute("UPDATE tasks SET completed = TRUE WHERE id = ? AND student_email = ?", (task_id, email))
            conn.commit()
            conn.close()
            return f"Task is marked as completed."
        else:
            conn.commit()
            conn.close()
            return f"Wrong task ID. Please try again."
    else:
        conn.commit()
        conn.close()
        return f"No tasks found."
 
def view_completed_tasks(email) :
    conn=sqlite3.connect("student_toolkit.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE student_email = ? and completed = 1", (email,))
    tasks=cursor.fetchall()
    if tasks:
        conn.commit()
        conn.close()
        return tasks
    else:
        conn.commit()
        conn.close()
        return f"No completed tasks found."
 
def view_incomplete_tasks(email):
    conn=sqlite3.connect('student_toolkit.db')
    cursor=conn.cursor()
    cursor.execute('''SELECT * FROM tasks WHERE student_email=? and completed=0''',(email,))
    tasks=cursor.fetchall()
    if tasks:
        conn.commit()
        conn.close()
        return tasks
    else:
        conn.commit()
        conn.close()
        return f"No incomplete tasks found."
     