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

# Initialize the database when the web server starts up
init_db()

# 1. The Home Page Route
@app.route('/')
def home():
    # This renders a visual layout instead of a terminal print string
    return "<h1>Welcome to the Student Toolkit Web Edition!</h1><a href='/login'>LOGIN</a><br><a href='/register'>REGISTER</a>"

# 2. The Login Page Route
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
            Email: <input type="text" name="email"><br>
            Password: <input type="password" name="password"><br>
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
            Name: <input type="text" name="name"><br>
            Email: <input type="text" name="email"><br>
            Password: <input type="password" name="password"><br>
            Age: <input type="number" name="age"><br>
            Class: <input type="text" name="class"><br>
            Contact Info: <input type="text" name="contact_info"><br>
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
            Email: <input type="text" name="email"><br>
            Contact Info: <input type="text" name="contact"><br>
            New Password: <input type="password" name="new_password"><br>
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
        html_output += f"<h3>📌 {note} </h3><hr>"
        
    html_output += "<br><a href='/dashboard'>Back to Dashboard</a>"
    return html_output

@app.route('/add_note', methods=['GET', 'POST'])
def web_add_note():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        note = request.form['note']
        date = request.form['date']
        # Call your existing backend logic function!
        add_notes(session['email'])
        return redirect(url_for('view_notes'))
    
    return '''
        <h1>📝 Add a New Note</h1>
        <form method="post">
            Note: <input type="text" name="note"><br>
            Date (DD-MM-YYYY): <input type="text" name="date"><br>
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
            <a href="/completed_tasks">Completed Tasks</a><br>
            <a href="/incomplete_tasks">Incomplete Tasks</a><br>
            <a href="/mark_task">Mark Task as Completed</a><br>
        '''

@app.route('/tools')
def tools():
    if 'email' not in session:
        return redirect(url_for('login'))
    return '''
            <h1>Tools Section</h1>
            <p>Here you can access all your tools and resources.</p>
            <a href="/sgpacalculator">SGPA calculator</a><br>
            <a href="/pomodoro">Pomodoro Timer</a><br>
            <a href="/attendance">Attendance Tracker</a><br>
            <a href="/chatbot">Saathi AI</a><br>
            <a href="/resources">Resources</a><br>
        '''


if __name__ == '__main__':
    # Start the web server on your local machine
    app.run(debug=True)