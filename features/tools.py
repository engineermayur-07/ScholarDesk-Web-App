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

def attendance_tracker(lec_attended=None, total_lec=None):
    print("\n--- Attendance Tracker ---")
    try:
        lec_attended=int(lec_attended)
        total_lec=int(total_lec)
    except ValueError:
        return f"The lectures must be in integer type"
    if lec_attended is None:
        return f"❌ Number of lectures attended cannot be empty. Please try again."
    if total_lec is None:
        return f"❌ Total number of lectures cannot be empty. Please try again."
    if lec_attended > total_lec:
        return f"❌ Lectures attended cannot be greater than total lectures. Please try again."
    return f"\n✅ Your Attendance Percentage is: {(lec_attended/total_lec)*100:.2f}%"   
    

# features/academics.py

def calculate_sgpa(grades_list, credits_list):
    """
    Accepts two lists of integers.
    Returns (sgpa, error_message)
    """
    total_credits = 0
    total_points = 0
    
    for grade, credits in zip(grades_list, credits_list):
        if grade > 10 or grade < 1:
            return None, "Invalid grade point found. Must be between 1 and 10."
            
        total_credits += credits
        total_points += grade * credits

    if total_credits == 0:
        return None, "Total credits cannot be zero."

    sgpa = total_points / total_credits
    return round(sgpa, 2), None

 
def chatbot():
    print("\n--- Launching Saathi, your AI Study Buddy ---\n")
    Saathi()

def resources():
    return resources_    