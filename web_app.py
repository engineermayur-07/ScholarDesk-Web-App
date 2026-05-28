from flask import *
from database_setup import init_db
# Import your newly organized features!
from features.auth import * 
from features.notes import *
from features.tasks import *
from features.tools import *
from features.finance import *
from chatbot import * 

app = Flask(__name__)
app.secret_key = 'super_secret_student_toolkit_key_2026'

init_db()

@app.route('/')
def home():
     return "<h1>Welcome to the Student Toolkit Web Edition!</h1><a href='/login'>LOGIN</a><br><a href='/register'>REGISTER</a>"

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        # Grab what the student typed into the web form fields
        email = request.form['email']
        password = request.form['password']
        # Call your existing backend logic function!
        # (Assuming your modular function returns True/False for success)
        is_valid, student = login(email,password)
        session['email'] = student[0]
        session['name'] = student[1]
        if is_valid:
            return redirect(url_for('dashboard'))  # Redirect to dashboard on successful login
        else:
            return '''
                <p>❌ Invalid email or password. Please try again.</p>
                <p>Forgot password? <a href="/reset_password">Reset it here</a></p>
            '''
    # If they are just browsing to the page (GET request), show a simple form
    return '''
        <form method="post">
            Email: <input type="text" name="email" required><br>
            Password: <input type="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    '''
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        # Grab what the student typed into the web form fields
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        age = request.form['age']
        class_ = request.form['class']
        contact_info = request.form['contact_info']

        # Call your existing backend logic function!
        is_valid, message = student_Registration(name, email, password, age, class_, contact_info)
        if is_valid:
            return message
        else:
            return message

    # If they are just browsing to the page (GET request), show a simple form
    return '''
        <form method="post">
            Name: <input type="text" name="name" required><br>
            Email: <input type="text" name="email" required><br>
            Password: <input type="password" name="password" required><br>
            Age: <input type="number" name="age" required><br>
            Class: <input type="text" name="class" required><br>
            Contact Info: <input type="text" name="contact_info" required><br>
            <input type="submit" value="Register">
        </form>
    '''
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password_route():
    if request.method == 'POST':
        email = request.form['email']
        contact = request.form['contact']
        new_password = request.form['new_password']

        is_valid, message = reset_password(email, contact, new_password)
        if is_valid:
            return message
        else:
            return message

    return '''
        <form method="post">
            Email: <input type="text" name="email" required><br>
            Contact Info: <input type="text" name="contact" required><br>
            New Password: <input type="password" name="new_password" required><br>
            <input type="submit" value="Reset Password">
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        return redirect(url_for('login'))
    return f"Welcome to your Dashboard, {session.get('name')}!" '''
            <p>Here you can access all your tools and resources.</p>
            <ul>
                <li><a href="/notes">Notes</a></li>
                <li><a href="/tasks">Tasks</a></li>
                <li><a href="/tools">Tools</a></li>
                <li><a href="/finance">Expense Tracker</a></li>
                <li><a href="/chatbot">Saathi AI</a></li>
            </ul>
            <h6><a href="/login">Logout</a></h6>
        
    '''

@app.route('/notes')
def notes():
    if 'email' not in session:
        return redirect(url_for('login'))
    return '''
            <h1>Notes Section</h1>
            <p>Here you can create, view, and manage your notes.</p>
            <a href="/view_notes">View Notes</a><br>
            <a href="/add_note">Add Note</a><br>
            <a href="/delete_note">Delete Note</a><br>
            <a href="/completed_notes">Completed Notes</a><br>
            <a href="/incomplete_notes">Incomplete Notes</a><br>
            <a href="/mark_note">Mark Note as Completed</a><br>
        '''
@app.route('/view_notes')
def web_view_notes():
    if 'email' not in session:
        return redirect(url_for('login'))
        
     
    notes_data = view_notes(session['email'])
    
    if not notes_data:
        return "<h3>📝 No notes found. <a href='/dashboard'>Go Back</a></h3>"
        
    html_output = "<h1>📝 Your Saved Notes</h1><hr>"
    for note in notes_data:
        # Assuming note[2] is the Topic and note[3] is the Content
        html_output += f"<h3>📌 ID : {note[0]}, Note :{note[2]}, DateMentioned :{note[3]} </h3><hr>"
        
    html_output += "<br><a href='/dashboard'>Back to Dashboard</a>"
    return html_output
@app.route('/add_note', methods=['GET', 'POST'])
def web_add_note():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        note = request.form['note']
        date = request.form['date']
        add_notes(session['email'],note,date)
        return redirect(url_for('web_view_notes'))
    
    return '''
        <h1>📝 Add a New Note</h1>
        <form method="post">
            Note: <input type="text" name="note" required><br>
            Date (DD-MM-YYYY): <input type="text" name="date" required><br>
            <input type="submit" value="Add Note">
        </form>
        <br><a href='/dashboard'>Back to Dashboard</a>
    '''

@app.route('/tasks')
def tasks():
    if 'email' not in session:
        return redirect(url_for('login'))
    return '''
            <h1>Tasks Section</h1>
            <p>Here you can create, view, and manage your tasks.</p>
            <a href="/view_tasks">View Tasks</a><br>
            <a href="/add_task">Add Task</a><br>
            <a href="/delete_task">Delete Task</a><br>
            <a href="/view_completed_tasks">Completed Tasks</a><br>
            <a href="/view_incomplete_tasks">Incomplete Tasks</a><br>
            <a href="/mark_task_completed">Mark Task as Completed</a><br>
        '''
@app.route('/view_tasks')
def view_task():
    if 'email' not in session:
        return redirect(url_for('login'))
    tasks = view_tasks(session['email'])
    html_output= "<h1> Your Tasks</h1><hr>"
    for task in tasks:
        html_output+=f"<h2> ID :{task[0]} Task :{task[2]} Deadline :{task[4]}"
    html_output += "<br><a href='/dashboard'>Back to Dashboard</a>"
    return html_output
@app.route('/add_task',methods=['GET','POST'])
def add_task():
    if 'email' not in session:
        return redirect(url_for('login')) 
    if request.method == 'POST':
        task = request.form['task']
        date = request.form['date']
        schedule_task(session['email'],task,date)
        return redirect(url_for('view_task'))
    
    return '''
        <h1>📝 Add a New Task</h1>
        <form method="post">
            Task: <input type="text" name="task" required><br>
            Deadline (DD-MM-YYYY): <input type="text" name="date" required><br>
            <input type="submit" value="Add Task">
        </form>
        <br><a href='/dashboard'>Back to Dashboard</a>
    '''
@app.route('/delete_task',methods=['GET','POST'])
def delete_task():
    if 'email' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        task_id = request.form['task_id']
        delete_tasks(session['email'],task_id)
        return redirect(url_for('view_task'))
    
    return '''
        <h1>📝 Delete Task</h1>
        <form method="post">
            Task ID: <input type="text" name="task_id" required><br>
            <input type="submit" value="Delete Task">
        </form>
        <br><a href='/dashboard'>Back to Dashboard</a>
    '''
@app.route('/mark_task_completed',methods=['GET','POST'])
def mark_task_completed():
    if 'email' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        task_id = request.form['task_id']
        Completed_tasks(session['email'],task_id)
        return redirect(url_for('view_task'))
    
    return '''
        <h1>📝 Mark Task Completion</h1>
        <form method="post">
            Task ID: <input type="text" name="task_id" required><br>
            <input type="submit" value="Mark Task">
        </form>
        <br><a href='/dashboard'>Back to Dashboard</a>
    '''
@app.route('/view_completed_tasks',methods=['GET','POST'])
def view_completed_task():
    if 'email' not in session:
        return redirect(url_for('login'))
    html_output=f"<h1>Completed Tasks</h1>"
    tasks=view_completed_tasks(session['email'])
    for task in tasks:
        html_output+=f"<h2> ID :{task[0]}  Task :{task[2]}  Deadline :{task[4]}"
    html_output += "<br><a href='/dashboard'>Back to Dashboard</a>"
    return html_output
@app.route('/view_incomplete_tasks',methods=['GET','POST'])
def view_incomplete_task():
    if 'email' not in session:
        return redirect(url_for('login'))
    html_output=f"<h1>Inomplete Tasks</h1>"
    tasks=view_incomplete_tasks(session['email'])
    for task in tasks:
        html_output+=f"<h2> ID :{task[0]}  Task :{task[2]}  Deadline :{task[4]}"
    html_output += "<br><a href='/dashboard'>Back to Dashboard</a>"
    return html_output


@app.route('/finance',methods=['GET','POSt'])
def finance():
    if 'email' not in session:
        return redirect(url_for('login'))
    return '''
            <h1>Expense Tracker</h1>
            <a href="/view_expense">View Expense Logs </a><br>
            <a href="/add_expense">Add Expense </a><br>
           '''
@app.route('/view_expense',methods=['GET','POST'])
def view_expense():
    if 'email' not in session:
        return redirect(url_for('login'))
    expenses=view_expenses(session['email'])
    html_output=f"<h1>Your Expense Log</h1>"
    for expense in expenses:
        html_output+=f"<h2>ID :{expense[0]}  Amount :{expense[2]}  Category :{expense[3]}  Date :{expense[4]}</h2><hr>"
    html_output += "<br><a href='/dashboard'>Back to Dashboard</a>"
    return html_output
@app.route('/add_expense',methods=['GET','POST'])
def add_expense():
    if 'email' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        amount = request.form['amount']
        category=request.form['category']
        date = request.form['date']
        expenses_tracker(session['email'],amount,category,date)
        return redirect(url_for('view_expense'))
    
    return '''
        <h1>📝 Add an Expense</h1>
        <form method="post">
            Amount: <input type="text" name="amount" required><br>
            Category (Bus,Food,Shopping,etc) : <input type="text" name="category" required><br>
            Date (DD-MM-YYYY): <input type="text" name="date" required><br>
            <input type="submit" value="Add Expense">
        </form>
        <br><a href='/dashboard'>Back to Dashboard</a>
    '''    


@app.route('/pomodoro')
def web_pomodoro():
    if 'email' not in session:
        return redirect(url_for('web_login'))
        
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
@app.route('/attendance_calc',methods=['GET','POST'])
def attendance_calc():
    if 'email' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        lec_attended= request.form['lec_attended']
        total_lec=request.form['total_lec']
        result=attendance_tracker(lec_attended,total_lec)
        return f"<h2>{result}</h2><br><a href='/dashboard'>Back to Dashboard</a>"

    return '''
        <h1>📝 Add No. Of Lectures</h1>
        <form method="post">
            Lectures Attended : <input type="text" name="lec_attended" required><br>
            Total Lectures Conducted : <input type="text" name="total_lec" required><br>
            <input type="submit" value="Calculate">
        </form>
        <br><a href='/dashboard'>Back to Dashboard</a>
    '''    
@app.route('/sgpa_calculator', methods=['GET', 'POST'])
def web_sgpa_calculator():
    if 'email' not in session:
        return redirect(url_for('login'))
        
    # Dynamically read how many subject rows to display (defaults to 5)
    num_subjects = request.args.get('subjects', default=5, type=int)
    
    if request.method == 'POST':
        try:
            # 🌟 THE SECRET SAUCE: request.form.getlist() collects all inputs with identical names
            raw_grades = request.form.getlist('grades')
            raw_credits = request.form.getlist('credits')
            
            # Convert the list of strings sent by the browser into clean lists of integers
            grades_list = [int(g) for g in raw_grades]
            credits_list = [int(c) for c in raw_credits]
            
            # 🔥 Call your backend function directly!
            sgpa_result, error_message = calculate_sgpa(grades_list, credits_list)
            
            if error_message:
                return f"<h2>❌ Error: {error_message}</h2><br><a href='/sgpa_calculator'>Try Again</a>"
                
            return f'''
                <h2>📊 SGPA Calculation Complete!</h2>
                <h3>Your Calculated SGPA is: <b style="color: #2ecc71;">{sgpa_result:.2f}</b></h3>
                <hr>
                <a href="/sgpa_calculator">Calculate Another Semester</a> | <a href="/dashboard">Back to Dashboard</a>
            '''
        except ValueError:
            return "<h2>❌ Error: Please ensure all input fields contain valid numbers.</h2><a href='/sgpa_calculator'>Try Again</a>"

    # --- GENERATING THE SINGLE FORM WITH MULTIPLE FIELDS ---
    input_rows = ""
    for i in range(num_subjects):
        input_rows += f'''
            <div style="margin-bottom: 15px;">
                <label><b>Subject {i+1}:</b></label> 
                Grade Point (1-10): <input type="number" name="grades" min="1" max="10" style="width: 60px;" required> 
                Credits: <input type="number" name="credits" min="1" max="8" style="width: 60px;" required>
            </div>
        '''
        
    return f'''
        <h1>📊 SGPA Academic Calculator</h1>
        <p>Change number of subjects: 
            <a href="/sgpa_calculator?subjects=3">3</a> | 
            <a href="/sgpa_calculator?subjects=4">4</a> | 
            <a href="/sgpa_calculator?subjects=5">5</a> | 
            <a href="/sgpa_calculator?subjects=6">6</a> | 
            <a href="/sgpa_calculator?subjects=7">7</a>
        </p>
        <hr>
        <form method="post">
            {input_rows}
            <input type="submit" value="Compute SGPA">
        </form>
        <br><a href="/dashboard">Back to Dashboard</a>
    '''
@app.route('/resources')
def resource():
    if 'email' not in session:
        return redirect(url_for('login'))

    resources_=resources()   
    html_output=f"<h1>Resources</h1>"
    for category in resources_:
        html_output+=f"<h2>{category.upper()}<hr>"
        for topic  in resources_[category]:
            html_output+=f"<h3>{topic} : <a href='{resources_[category][topic]}'>{resources_[category][topic]}</a></h3><br>"
    html_output += "<br><a href='/dashboard'>Back to Dashboard</a>"
    return html_output
    

@app.route('/tools')
def tools():
    if 'email' not in session:
        return redirect(url_for('login'))
    return '''
            <h1>Tools Section</h1>
            <p>Here you can access all your tools and resources.</p>
            <a href="/sgpa_calculator">SGPA calculator</a><br>
            <a href="/pomodoro">Pomodoro Timer</a><br>
            <a href="/attendance_calc">Attendance Calculator</a><br>
            <a href="/chatbot">Saathi AI</a><br>
            <a href="/resources">Resources</a><br>
        '''

if __name__ == '__main__':
     app.run(debug=True)