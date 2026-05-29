import json
from flask import *
# Imported Flask from flask
from database_setup import init_db
# Import newly organized features!
from features.auth import * 
from features.notes import *
from features.tasks import *
from features.tools import *
from features.finance import *
from chatbot import * 

app = Flask(__name__)
app.secret_key = 'super_secret_student_toolkit_key_2026'

# Initialize the database when the web server starts up
init_db()

# 1. The Home Page Route
@app.route('/') 
@app.route('/home') 
def home():
    # This renders a visual layout instead of a terminal print string
    return render_template('home.html')


# 2. The Login Page Route
@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form.get('email', '')
        password = request.form.get('password', '')

        is_valid, student = login(email, password)

        if is_valid and isinstance(student, tuple) and len(student) >= 2:
            session['email'] = student[0]
            session['name'] = student[1]
            return redirect(url_for('dashboard'))

        return render_template('login.html', error='Invalid email or password. Please try again.')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        age = request.form.get('age', '')
        class_ = request.form.get('class', '')
        contact_info = request.form.get('contact_info', '')

        is_valid, message = student_Registration(name, email, password, age, class_, contact_info)
        if is_valid:
            return render_template('register.html', message=message)
        else:
            return render_template('register.html', message=message)

    return render_template('register.html')


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password_route():
    if request.method == 'POST':
        email = request.form.get('email', '')
        contact = request.form.get('contact', '')
        new_password = request.form.get('new_password', '')

        is_valid, message = reset_password(email, contact, new_password)
        return render_template('forgot_password.html', message=message)

    return render_template('forgot_password.html')

 
@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    return render_template('dashboard.html', name=session.get('name', 'Student'))

@app.route('/notes')
def notes():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    notes_data = view_notes(session['email'])
    notes_list = notes_data if isinstance(notes_data, list) else []
    return render_template('notes.html', notes=notes_list, name=session.get('name', 'Student'))


@app.route('/view_notes')
def web_view_notes():
    if 'email' not in session:
        return redirect(url_for('login_user'))

    notes_data = view_notes(session['email'])

    if not isinstance(notes_data, list) or not notes_data:
        return "<h3>No notes found. <a href='/dashboard'>Go Back</a></h3>"

    html_output = "<h1>Your Saved Notes</h1><hr>"
    for note in notes_data:
        html_output += f"<h3>ID: {note[0]} | Note: {note[2]} | Date: {note[3]}</h3><hr>"

    html_output += "<br><a href='/dashboard'>Back to Dashboard</a>"
    return html_output


@app.route('/add_note', methods=['GET', 'POST'])
def web_add_note():
    if 'email' not in session:
        return redirect(url_for('login_user'))

    if request.method == 'POST':
        note = request.form.get('note', '').strip()
        date = request.form.get('date', '').strip()
        message = add_notes(session['email'], note, date)
        return render_template('notes.html', notes=view_notes(session['email']) if isinstance(view_notes(session['email']), list) else [], message=message, name=session.get('name', 'Student'))

    return redirect(url_for('notes'))

@app.route('/tasks')
def tasks():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    tasks_data = view_tasks(session['email'])
    tasks_list = tasks_data if isinstance(tasks_data, list) else []
    return render_template('tasks.html', tasks=tasks_list, name=session.get('name', 'Student'))


@app.route('/view_tasks')
def view_task():
    if 'email' not in session:
        return redirect(url_for('login_user'))

    tasks = view_tasks(session['email'])
    if not isinstance(tasks, list) or not tasks:
        return "<h3>No tasks found. <a href='/dashboard'>Go Back</a></h3>"

    html_output = "<h1>Your Tasks</h1><hr>"
    for task in tasks:
        html_output += f"<h2>ID: {task[0]} | Task: {task[2]} | Deadline: {task[4]}</h2><hr>"

    html_output += "<br><a href='/dashboard'>Back to Dashboard</a>"
    return html_output


@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if 'email' not in session:
        return redirect(url_for('login_user'))

    if request.method == 'POST':
        task = request.form.get('task', '').strip()
        deadline = request.form.get('deadline', '').strip()
        message = schedule_task(session['email'], task, deadline)
        tasks_data = view_tasks(session['email'])
        return render_template('tasks.html', tasks=tasks_data if isinstance(tasks_data, list) else [], message=message, name=session.get('name', 'Student'))

    return redirect(url_for('tasks'))


@app.route('/tools')
def tools():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    return render_template('tools.html', name=session.get('name', 'Student'))

@app.route('/finance')
def finance():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    expenses_data = view_expenses(session['email'])
    expenses_list = expenses_data if isinstance(expenses_data, list) else []
    return render_template('finance.html', expenses=expenses_list, name=session.get('name', 'Student'))

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if 'email' not in session:
        return redirect(url_for('login_user'))

    if request.method == 'POST':
        amount = request.form.get('amount', '').strip()
        category = request.form.get('category', '').strip()
        date = request.form.get('date', '').strip()
        message = expenses_tracker(session['email'], amount, category, date)
        expenses_data = view_expenses(session['email'])
        return render_template('finance.html', expenses=expenses_data if isinstance(expenses_data, list) else [], message=message, name=session.get('name', 'Student'))

    return redirect(url_for('finance'))

@app.route('/attendance', methods=['GET', 'POST'])
def attendance_page():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    result = None
    if request.method == 'POST':
        result = attendance_tracker(int(request.form.get('lectures_attended', 0)), int(request.form.get('total_lectures', 0)))
    return render_template('attendance.html', result=result, name=session.get('name', 'Student'))

@app.route('/sgpa')
@app.route('/sgpacalculator', methods=['GET', 'POST'])
def sgpa_page():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    result = None
    if request.method == 'POST':
        grades = [float(x) for x in request.form.get('grades', '').split(',') if x.strip()]
        credits = [float(x) for x in request.form.get('credits', '').split(',') if x.strip()]
        sgpa, error = calculate_sgpa(grades, credits)
        result = f"SGPA: {sgpa}" if sgpa is not None else error
    return render_template('sgpa.html', result=result, name=session.get('name', 'Student'))

@app.route('/resources')
def resources_page():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    with open('resources.json', 'r', encoding='utf-8') as f:
        data = json.load(f)['resources']
    return render_template('resources.html', resources=data, name=session.get('name', 'Student'))

@app.route('/chatbot')
def chatbot_page():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    return render_template('chatbot.html', name=session.get('name', 'Student'))

from flask import Flask, render_template, redirect, url_for, session

@app.route('/pomodoro')
def web_pomodoro():
    if 'email' not in session:
        return redirect(url_for('login_user'))
        
    # We send an HTML page containing JavaScript to handle the countdown countdown
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🍅 Pomodoro Timer</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #fcf8f8; }
            .timer-box { border: 2px solid #e74c3c; display: inline-block; padding: 30px; border-radius: 15px; background: white; }
            #timer { font-size: 60px; font-weight: bold; color: #e74c3c; margin: 20px 0; }
            button { padding: 10px 20px; font-size: 18px; cursor: pointer; background-color: #e74c3c; color: white; border: none; border-radius: 5px; }
            button:hover { background-color: #c0392b; }
            .status { font-size: 20px; color: #555; }
        </style>
    </head>
    <body>

        <div class="timer-box">
            <h1>🍅 Student Toolkit Pomodoro </h1>
            <div class="status" id="status-text">Focus Mode: Concentrate on your work!</div>
            <div id="timer">25:00</div>
            <button id="start-btn" onclick="toggleTimer()">Start Timer</button>
            <br><br>
            <a href="/dashboard">Back to Dashboard</a>
        </div>

        <script>
            let timeLeft = 25 * 60; // 25 minutes in seconds
            let timerInterval = null;
            let isRunning = false;
            let isFocusMode = true;

            function updateDisplay() {
                let minutes = Math.floor(timeLeft / 60);
                let seconds = timeLeft % 60;
                
                // Formats numbers nicely (adds leading zero if less than 10)
                let displayMin = minutes < 10 ? "0" + minutes : minutes;
                let displaySec = seconds < 10 ? "0" + seconds : seconds;
                
                document.getElementById("timer").innerText = displayMin + ":" + displaySec;
            }

            function toggleTimer() {
                if (isRunning) {
                    // Pause functionality
                    clearInterval(timerInterval);
                    document.getElementById("start-btn").innerText = "Resume";
                    isRunning = false;
                } else {
                    // Start functionality
                    isRunning = true;
                    document.getElementById("start-btn").innerText = "Pause";
                    
                    timerInterval = setInterval(() => {
                        if (timeLeft > 0) {
                            timeLeft--;
                            updateDisplay();
                        } else {
                            // When time hits 00:00
                            clearInterval(timerInterval);
                            isRunning = false;
                            alert("⏰ Time is up!");
                            
                            if (isFocusMode) {
                                // Switch to break mode
                                isFocusMode = false;
                                timeLeft = 5 * 60; // 5 minute break
                                document.getElementById("status-text").innerText = "☕ Break Mode: Relax and rest!";
                                document.getElementById("start-btn").innerText = "Start Break";
                            } else {
                                // Switch back to focus mode
                                isFocusMode = true;
                                timeLeft = 25 * 60; // 25 minute focus
                                document.getElementById("status-text").innerText = "Focus Mode: Concentrate on your work!";
                                document.getElementById("start-btn").innerText = "Start Focus";
                            }
                            updateDisplay();
                        }
                    }, 1000); // Ticks exactly every 1000ms (1 second)
                }
            }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    # Start the web server on your local machine
    app.run(debug=True)