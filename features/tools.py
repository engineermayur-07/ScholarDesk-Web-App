import sqlite3
from features.utility import *
from chatbot import *
import time

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

def attendance_tracker():
    print("\n--- Attendance Tracker ---")
    lec_attended = int(input("Enter the number of lectures attended: "))
    total_lec = int(input("Enter the total number of lectures: "))
    print(f"\n✅ Your Attendance Percentage is: {(lec_attended/total_lec)*100:.2f}%")
    return

def sgpa_calculator():
    print("\n--- SGPA Calculator ---")
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        total_credits = 0
        total_points = 0
        
        for i in range(num_subjects):
            grade = int(input(f"Enter the grade point for subject {i+1} (10, 9, 8, 7, 6): ") )
            if(grade>10 or grade<1):
                print("❌ Invalid grade point. Please try again.")
                return 
            credits = int(input(f"Enter the credits for subject {i+1}: "))
            total_credits += credits
            total_points += grade * credits

    except ValueError:
        print("❌ Invalid input. Please enter numeric values and try again.")
        return 

    if total_credits == 0:
        print("❌ Total credits cannot be zero.")
        return 

    sgpa = total_points / total_credits
    print(f"\n✅ Your Calculated SGPA is: {sgpa:.2f}")
    return

def pomodoro_timer():
    print("\n--- Pomodoro Timer ---")
    time_=60*25
    print("Pomodoro timer started for 25 minutes. Focus on your work!")
    while time_>0:
        min,sec=divmod(time_,60)
        print(f"{min:02d}:{sec:02d}",end="\r")
        time.sleep(1)
        time_-=1
    print("\n⏰ Time's up! Take a 5-minute break.")

def chatbot():
    print("\n--- Launching Saathi, your AI Study Buddy ---\n")
    Saathi()

def resources():
    print("---RESOURCES---")
    for category in resources_:
        print(f"\n{category.upper()} :")
        for topic  in resources_[category]:
            print(f"{topic} : {resources_[category][topic]}")
        print(20*"-")
