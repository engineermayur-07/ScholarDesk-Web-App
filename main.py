# Developing a student toolkit for a school management system which has the
# following features:
# 1. Student Registration: Allow students to register by providing their name, age, grade, and contact information.
# 2, Features students to add the tasks they want to accomplish
# 3. View Tasks: Students can view their list of tasks and mark them as completed.
#4.Students can get resources for studying, such as links to educational websites, study materials, and tips for effective studying.
import sqlite3
import sys
import json
import database_setup
from features.auth import *
from features.tasks import *
from features.notes import *
from features.finance import *
from features.tools import *
from features.utility import *
from chatbot import *
import time

database_setup.init_db()

resources_={
         "documentation":{
            "c language":"https://www.cprogramming.com/tutorial/c-tutorial.html",
            "python":"https://www.python.org/doc/",
            "java":"https://docs.oracle.com/en/java/",
            "javascript":"https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
            "html":"https://developer.mozilla.org/en-US/docs/Web/HTML",
            "css":"https://developer.mozilla.org/en-US/docs/Web/CSS",
            "sql":"https://www.w3schools.com/sql/"  ,
            "sqlite":"https://www.sqlite.org/docs.html",
            "git":"https://git-scm.com/doc"
         },
         "notes":{
            "html":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/YouTube/The%20Ultimate%20HTML%20handbook.pdf",
            "css":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/notes/CSS_Complete_Notes.pdf",
            "javascript":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/notes/JS_Chapterwise_Notes.pdf",
            "php":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/cheatsheets/Php%20Cheatsheet.pdf",
            "c programming":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/YouTube/The%20Ultimate%20C%20Handbook.pdf",
            "c++":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/cheatsheets/C%2B%2B%20Cheatsheet.pdf",
            "java":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/notes/Java_Complete_Notes.pdf",
            "python":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/YouTube/The%20Ultimate%20Python%20Handbook.pdf",
            "dsa":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/notes/DSA_CompleteNotes.pdf",
            "sql":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/YouTube/MySQL%20Handbook.pdf",
            "mysql":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/cheatsheets/MySQL%20Cheatsheet.pdf",
            "mongodb":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/YouTube/MongoDB%20Handbook.pdf",
            "django":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/cheatsheets/Django%20Cheatsheet.pdf",
            "flask":"https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/cheatsheets/Flask%20Cheatsheet.pdf"
         }
          
    }
     
while True:
    print("\nWelcome to the Student Toolkit")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1' or choice.lower() == "register":
        student_Registration()
    elif choice == '2' or choice.lower() == "login":
        student,logged_in=login()
        if logged_in:
            print("\n--- Main Application Menu coming next! ---")
            while True:
                print(f"Welcome back {student[1]}! Let's get started with your Student Toolkit.")
                print("1. View Profile")
                print("2. Schedule Tasks")
                print("3. View Tasks")
                print("4. Delete Tasks")
                print("5. Mark Task as Completed")
                print("6. View Completed Tasks")
                print("7. View Incomplete Tasks")
                print("8. Resources")
                print("9. Saathi AI")
                print("10. Pomodoro Timer")
                print("11. Add Notes")
                print("12. View Notes")
                print("13. Delete Notes")
                print("14. SGPA Calculator")
                print("15. Attendance Tracker")
                print("16. Expenses Tracker")
                print("17. View Expenses")
                print("18. Logout")
                sub_choice = input("Enter your choice: ")
                if sub_choice == '1' or sub_choice.lower() == "view profile":
                    profile(student[0])
                elif sub_choice == '2' or sub_choice.lower() == "schedule tasks":
                    schedule_task(student[0])
                elif sub_choice == '3' or sub_choice.lower() == "view tasks":
                    view_tasks(student[0])
                elif sub_choice == '4' or sub_choice.lower() == "delete tasks":
                    delete_tasks(student[0])
                elif sub_choice == '5' or sub_choice.lower() == "mark task as completed":
                    Completed_tasks(student[0])
                elif sub_choice == '6' or sub_choice.lower() == "view completed tasks":
                    view_completed_tasks(student[0])
                elif sub_choice == '7' or sub_choice.lower() == "view incomplete tasks":
                    view_incomplete_tasks(student[0])
                elif sub_choice == '8' or sub_choice.lower() == "resources":
                    resources()
                elif sub_choice == '9' or sub_choice.lower() == "saathi ai":
                    chatbot()
                elif sub_choice == '10' or sub_choice.lower() == "pomodoro timer":
                    pomodoro_timer()
                elif sub_choice == '11' or sub_choice.lower() == "add notes":
                    add_notes(student[0])
                elif sub_choice == '12' or sub_choice.lower() == "view notes":
                    view_notes(student[0])
                elif sub_choice == '13' or sub_choice.lower() == "delete notes":
                    delete_notes(student[0])
                elif sub_choice == '14' or sub_choice.lower() == "sgpa calculator":
                    sgpa_calculator()
                elif sub_choice == '15' or sub_choice.lower() == "attendance tracker":
                    attendance_tracker()
                elif sub_choice == '16' or sub_choice.lower() == "expenses tracker":
                    expenses_tracker(student[0])
                elif sub_choice == '17' or sub_choice.lower() == "view expenses":
                    view_expenses(student[0])
                elif sub_choice == '18' or sub_choice.lower() == "logout":
                    print("Logging out...")
                    break

        else:
            continue

    elif choice == '3' or choice.lower() == "exit":
        print("Exiting the Student Toolkit. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")