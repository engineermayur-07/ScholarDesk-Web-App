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
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Student Toolkit</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body>
            <h1>Welcome to the SCHOLAR DESK!</h1>
            <a href='/login'>LOGIN</a><br>
            <a href='/register'>REGISTER</a>
        </body>
        </html>
        '''
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
    # Find this return inside @app.route('/login')
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login - Student Toolkit</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="form-container">
            <div class="form-card">
                <h2>🔐 Student Sign In</h2>
                <form method="post">
                    <div class="input-group">
                        <label>Email Address</label>
                        <input type="text" name="email" placeholder="Enter your email" required>
                    </div>
                    <div class="input-group">
                        <label>Password</label>
                        <input type="password" name="password" placeholder="Enter your password" required>
                    </div>
                    <input type="submit" value="Login" class="btn-submit">
                </form>
                <p class="form-footer">Forgot password? <a href="/reset_password" class="link-flat">Reset it here</a></p>
            </div>
        </div>
    </body>
    </html>
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
    <!DOCTYPE html>
    <html>
    <head>
        <title>Create Account | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="auth-bg">
        <div class="register-wrapper">
            <div class="brand-header animated-fade-in">
                <span class="brand-logo">🎓</span>
                <h1>Scholar Desk</h1>
                <p>Your ultimate academic command center</p>
            </div>
            
            <div class="register-card animated-slide-up">
                <h2>Create Your Workspace</h2>
                <form method="post">
                    <div class="form-grid">
                        <div class="input-field">
                            <label>Full Name</label>
                            <input type="text" name="name" placeholder="John Doe" required>
                        </div>
                        <div class="input-field">
                            <label>Email Address</label>
                            <input type="email" name="email" placeholder="you@school.com" required>
                        </div>
                        <div class="input-field">
                            <label>Secure Password</label>
                            <input type="password" name="password" placeholder="••••••••" required>
                        </div>
                        <div class="input-field">
                            <label>Age</label>
                            <input type="number" name="age" placeholder="20" required>
                        </div>
                        <div class="input-field">
                            <label>Class / Batch</label>
                            <input type="text" name="class" placeholder="CS - Division A" required>
                        </div>
                        <div class="input-field">
                            <label>Contact Number</label>
                            <input type="text" name="contact_info" placeholder="+91 XXXXX XXXXX" required>
                        </div>
                    </div>
                    
                    <button type="submit" class="btn-register">
                        <span>Initialize Profile</span>
                        <span class="btn-arrow">→</span>
                    </button>
                </form>
                
                <p class="auth-meta">Already have a desk? <a href="/login" class="link-highlight">Sign in here</a></p>
            </div>
        </div>
    </body>
    </html>
    '''
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password_route():
    if request.method == 'POST':
        email = request.form['email']
        contact = request.form['contact']
        new_password = request.form['new_password']

        is_valid, message = reset_password(email, contact, new_password)
        # if is_valid:
        #     return message
        # else:
        #     return message
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Reset Status | Scholar Desk</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body class="auth-bg">
            <div class="register-card animated-slide-up" style="text-align: center; max-width: 400px;">
                <h2>System Notification</h2>
                <p style="font-size: 1.1rem; color: #2c3e50; margin-bottom: 25px;">{message}</p>
                <a href="/login" class="btn-register" style="text-decoration: none;">Go to Sign In</a>
            </div>
        </body>
        </html>
        '''

    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reset Password | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="auth-bg">
        <div class="register-wrapper" style="max-width: 450px;">
            <div class="brand-header animated-fade-in">
                <span class="brand-logo">🔑</span>
                <h1>Scholar Desk</h1>
                <p>Account Recovery Portal</p>
            </div>
            
            <div class="register-card animated-slide-up">
                <h2>Reset Password</h2>
                <p style="color: #7f8c8d; font-size: 0.9rem; margin-top: -20px; margin-bottom: 25px;">
                    Verify your registered mobile number to configure a new access credential.
                </p>
                
                <form method="post">
                    <div class="input-field" style="margin-bottom: 20px;">
                        <label>Email Address</label>
                        <input type="email" name="email" placeholder="you@school.com" required>
                    </div>
                    
                    <div class="input-field" style="margin-bottom: 20px;">
                        <label>Registered Mobile Number</label>
                        <input type="text" name="contact" placeholder="+91 XXXXX XXXXX" required>
                    </div>
                    
                    <div class="input-field" style="margin-bottom: 30px;">
                        <label>New Secure Password</label>
                        <input type="password" name="new_password" placeholder="••••••••" required>
                    </div>
                    
                    <button type="submit" class="btn-register">
                        <span>Update Desk Credentials</span>
                        <span class="btn-arrow">→</span>
                    </button>
                </form>
                
                <p class="auth-meta"><a href="/login" class="link-highlight">← Back to Sign In</a></p>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard - Student Toolkit</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="dashboard-header">
            <h1>🎒 Student Toolkit Workspace</h1>
            <p>Welcome back, <b>{session.get("name")}</b>! What are we focusing on today?</p>
        </div>

        <div class="grid-container">
            
            <div class="card">
                <div class="card-icon">📝</div>
                <h3>Notes Engine</h3>
                <p>Create, manage, and review your academic lecture notebooks.</p>
                <a href="/notes" class="btn-card">Open Notebook</a>
            </div>

            <div class="card">
                <div class="card-icon">📅</div>
                <h3>Task Manager</h3>
                <p>Track assignment deadlines, daily targets, and incomplete schedules.</p>
                <a href="/tasks" class="btn-card">View Schedules</a>
            </div>

            <div class="card">
                <div class="card-icon">📊</div>
                <h3>Academic Tools</h3>
                <p>Compute semester SGPA scores and monitor overall class attendance.</p>
                <a href="/tools" class="btn-card">Launch Tools</a>
            </div>

            <div class="card">
                <div class="card-icon">💳</div>
                <h3>Expense Tracker</h3>
                <p>Monitor your daily student budget ledger and logging histories.</p>
                <a href="/finance" class="btn-card">Check Ledger</a>
            </div>

            <div class="card">
                <div class="card-icon">🤖</div>
                <h3>Saathi AI</h3>
                <p>Chat directly with your interactive context-aware study companion.</p>
                <a href="/chatbot" class="btn-card" style="background-color: #29b6f6;">Talk to Saathi</a>
            </div>

        </div>

        <div style="margin-top: 40px; margin-bottom: 50px;">
            <a href="/logout" class="btn-logout">🔒 Securely Logout</a>
        </div>
    </body>
    </html>
    '''

@app.route('/notes')
def notes():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Notes Hub - Student Toolkit</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="menu-container">
            <div class="menu-header">
                <h1>📚 Lecture Notes Hub</h1>
                <p>Organize your thoughts, archive study materials, and review your classes.</p>
                <a href="/dashboard" class="link-flat">← Return to Main Dashboard</a>
            </div>
            
            <!-- Reusing our clean action-grid structure -->
            <div class="action-grid">
                <a href="/view_notes" class="action-box box-blue">
                    <span class="action-icon">📖</span>
                    <h4>View Notes</h4>
                    <p>Open your full notebook database ledger.</p>
                </a>

                <a href="/add_note" class="action-box box-green">
                    <span class="action-icon">✍️</span>
                    <h4>Add New Note</h4>
                    <p>Jot down fresh concepts and logs.</p>
                </a>

                <a href="/mark_note" class="action-box box-orange">
                    <span class="action-icon">🎯</span>
                    <h4>Complete Note</h4>
                    <p>Mark a study topic revision as done.</p>
                </a>

                <a href="/delete_note" class="action-box box-red">
                    <span class="action-icon">🗑️</span>
                    <h4>Delete Note</h4>
                    <p>Discard unwanted notebooks permanently.</p>
                </a>
            </div>

            <div class="submenu-links">
                <a href="/completed_notes" class="link-flat">✅ Completed Revisions</a> | 
                <a href="/incomplete_notes" class="link-flat">⏳ Pending Backlogs</a>
            </div>
        </div>
    </body>
    </html>
    '''
@app.route('/view_notes')
def web_view_notes():
    if 'email' not in session:
        return redirect(url_for('login_user'))
        
     
    notes_data = view_notes(session['email'])
    
    if not notes_data:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>View Notes | Scholar Desk</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body>
            <div class="data-container" style="text-align: center; max-width: 500px;">
                <h1 style="font-size: 3rem;">📝</h1>
                <h2>No Notes Found</h2>
                <p style="color: #7f8c8d; margin-bottom: 25px;">Your personal study binder is currently empty.</p>
                <a href="/add_note" class="btn-submit" style="text-decoration: none; display: block;">✍️ Create Your First Note</a>
                <br>
                <a href="/notes" class="link-flat">← Back to Notes Hub</a>
            </div>
        </body>
        </html>
        '''
        
    html_output = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Your Notebook | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="data-container">
            <h1>📝 Your Saved Lecture Notes</h1>
            <p style="color: #7f8c8d; margin-top: -5px;">Review, structure, and keep track of your core subject logs.</p>
            <p>
                <a href="/notes" class="link-flat">← Notes Hub Menu</a> | 
                <a href="/add_note" class="link-flat">➕ Add Fresh Note</a>
            </p>
            
            <div class="table-responsive">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th style="width: 15%;">Note ID</th>
                            <th class="text-left" style="width: 60%;">Subject Content / Topic</th>
                            <th style="width: 25%;">Date Logged</th>
                        </tr>
                    </thead>
                    <tbody>
    '''
    for note in notes_data:
        # Assuming note[2] is the Topic and note[3] is the Content
        html_output += f'''
                        <tr>
                            <td><code>#{note[0]}</code></td>
                            <td class="text-left" style="font-weight: 600; color: #2c3e50;">{note[2]}</td>
                            <td><span class="badge badge-date">{note[3]}</span></td>
                        </tr>
        '''
        
    html_output += '''
                    </tbody>
                </table>
            </div>
            <div style="margin-top: 30px;">
                <a href="/dashboard" class="link-flat">← Return to Main Workspace</a>
            </div>
        </div>
    </body>
    </html>
    '''
    return html_output
@app.route('/add_note', methods=['GET', 'POST'])
def web_add_note():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    
    if request.method == 'POST':
        note = request.form['note']
        date = request.form['date']
        add_notes(session['email'],note,date)
        return redirect(url_for('web_view_notes'))
    
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Add Note | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="form-container" style="min-height: 70vh;">
            <div class="form-card" style="max-width: 500px;">
                <h2>📝 Create Fresh Note</h2>
                <p style="color: #7f8c8d; font-size: 0.9rem; margin-top: -20px; margin-bottom: 25px;">
                    Log your ideas, class topics, or reminders directly into your database.
                </p>
                
                <form method="post">
                    <div class="input-field" style="margin-bottom: 20px;">
                        <label>Note Description / Content</label>
                        <textarea name="note" rows="6" placeholder="Type your lecture summary or study reminders here..." required 
                            style="width: 100%; padding: 12px; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 0.95rem; outline: none; font-family: inherit; resize: vertical; box-sizing: border-box; transition: all 0.3s ease;"></textarea>
                    </div>
                    
                    <div class="input-field" style="margin-bottom: 30px;">
                        <label>Date Mentioned (DD-MM-YYYY)</label>
                        <input type="text" name="date" placeholder="29-05-2026" required>
                    </div>
                    
                    <button type="submit" class="btn-register" style="background: linear-gradient(135deg, #34495e, #2c3e50); box-shadow: 0 4px 15px rgba(52, 73, 94, 0.2);">
                        <span>Save to Notebook</span>
                        <span class="btn-arrow">→</span>
                    </button>
                </form>
                
                <p class="auth-meta">
                    <a href="/notes" class="link-highlight" style="color: #34495e;">← Back to Notes Hub</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/tasks')
def tasks():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    if 'email' not in session:
        return redirect(url_for('login_user'))
        
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tasks Control Panel - Student Toolkit</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="menu-container">
            <div class="menu-header">
                <h1>📅 Task Management Hub</h1>
                <p>Track deadlines, prioritize projects, and clear your agenda items.</p>
                <a href="/dashboard" class="link-flat">← Return to Main Dashboard</a>
            </div>
            
            <!-- Quick Action Grid Link Cards -->
            <div class="action-grid">
                <a href="/view_tasks" class="action-box box-blue">
                    <span class="action-icon">👁️‍🗨️</span>
                    <h4>View All Tasks</h4>
                    <p>See your full ongoing schedule log.</p>
                </a>

                <a href="/add_task" class="action-box box-green">
                    <span class="action-icon">➕</span>
                    <h4>Add New Task</h4>
                    <p>Schedule a new assignment deadline.</p>
                </a>

                <a href="/mark_task_completed" class="action-box box-orange">
                    <span class="action-icon">✅</span>
                    <h4>Complete Task</h4>
                    <p>Mark an outstanding item as finished.</p>
                </a>

                <a href="/delete_task" class="action-box box-red">
                    <span class="action-icon">🗑️</span>
                    <h4>Delete Task</h4>
                    <p>Permanently remove records from database.</p>
                </a>
            </div>

            <div class="submenu-links">
                <a href="/view_completed_tasks" class="link-flat">✔️ View Completed History</a> | 
                <a href="/view_incomplete_tasks" class="link-flat">❌ View Pending Backlogs</a>
            </div>
        </div>
    </body>
    </html>
    '''
@app.route('/view_tasks')
def view_task():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    tasks = view_tasks(session['email'])
    html_output= "<h1> Your Tasks</h1><hr>"
    for task in tasks:
        html_output+=f"<h2> ID :{task[0]} Task :{task[2]} Deadline :{task[4]}"
    html_output += "<br><a href='/dashboard'>Back to Dashboard</a>"
    return html_output
@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if 'email' not in session:
        return redirect(url_for('login_user')) 
        
    if request.method == 'POST':
        task = request.form['task']
        date = request.form['date']
        schedule_task(session['email'], task, date)
        return redirect(url_for('view_task')) # Pointing to your correct view function route
    
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Schedule Task | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="form-container" style="min-height: 70vh;">
            <div class="form-card" style="max-width: 450px;">
                <h2>📅 Schedule New Task</h2>
                <p style="color: #7f8c8d; font-size: 0.9rem; margin-top: -20px; margin-bottom: 25px;">
                    Set assignment targets, project milestones, or study goals.
                </p>
                
                <form method="post">
                    <div class="input-field" style="margin-bottom: 20px;">
                        <label>Task / Assignment Description</label>
                        <input type="text" name="task" placeholder="e.g., Complete Mathematics Assignment 2" required>
                    </div>
                    
                    <div class="input-field" style="margin-bottom: 30px;">
                        <label>Deadline Target (DD-MM-YYYY)</label>
                        <input type="text" name="date" placeholder="e.g., 05-06-2026" required>
                    </div>
                    
                    <button type="submit" class="btn-register" style="background: linear-gradient(135deg, #3498db, #2980b9); box-shadow: 0 4px 15px rgba(52, 152, 219, 0.25);">
                        <span>Add to Schedule</span>
                        <span class="btn-arrow">→</span>
                    </button>
                </form>
                
                <p class="auth-meta">
                    <a href="/tasks" class="link-highlight" style="color: #2980b9;">← Back to Tasks Hub</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    '''
@app.route('/delete_task',methods=['GET','POST'])
def delete_task():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    if request.method == 'POST':
        task_id = request.form['task_id']
        delete_tasks(session['email'],task_id)
        return redirect(url_for('view_task'))
    
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Delete Task | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="form-container" style="min-height: 70vh;">
            <div class="form-card" style="max-width: 400px; border-left: 5px solid #e74c3c;">
                <h2 style="color: #c0392b;">🗑️ Remove Task</h2>
                <p style="color: #7f8c8d; font-size: 0.9rem; margin-top: -20px; margin-bottom: 25px;">
                    Enter the specific database <b>Task ID</b> you want to delete permanently.
                </p>
                
                <form method="post">
                    <div class="input-field" style="margin-bottom: 30px;">
                        <label>Task ID Number</label>
                        <input type="number" name="task_id" placeholder="e.g., 4" min="1" required>
                    </div>
                    
                    <button type="submit" class="btn-register" style="background: linear-gradient(135deg, #e74c3c, #c0392b); box-shadow: 0 4px 15px rgba(231, 76, 60, 0.25);">
                        <span>Delete Permanently</span>
                        <span class="btn-arrow">→</span>
                    </button>
                </form>
                
                <p class="auth-meta">
                    <a href="/tasks" class="link-highlight" style="color: #e74c3c;">← Back to Tasks Hub</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    '''
@app.route('/mark_task_completed',methods=['GET','POST'])
def mark_task_completed():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    if request.method == 'POST':
        task_id = request.form['task_id']
        Completed_tasks(session['email'],task_id)
        return redirect(url_for('view_task'))
    
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mark Completion | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="form-container" style="min-height: 70vh;">
            <div class="form-card" style="max-width: 400px; border-left: 5px solid #2ecc71;">
                <h2 style="color: #27ae60;">✅ Complete a Task</h2>
                <p style="color: #7f8c8d; font-size: 0.9rem; margin-top: -20px; margin-bottom: 25px;">
                    Ready to cross an assignment off your list? Enter its <b>Task ID</b> below.
                </p>
                
                <form method="post">
                    <div class="input-field" style="margin-bottom: 30px;">
                        <label>Task ID Number</label>
                        <input type="number" name="task_id" placeholder="e.g., 2" min="1" required>
                    </div>
                    
                    <button type="submit" class="btn-register" style="background: linear-gradient(135deg, #2ecc71, #27ae60); box-shadow: 0 4px 15px rgba(46, 204, 113, 0.25);">
                        <span>Mark as Completed</span>
                        <span class="btn-arrow">→</span>
                    </button>
                </form>
                
                <p class="auth-meta">
                    <a href="/tasks" class="link-highlight" style="color: #27ae60;">← Back to Tasks Hub</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    '''
@app.route('/view_completed_tasks',methods=['GET','POST'])
def view_completed_task():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    tasks=view_completed_tasks(session['email'])
    if not tasks:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Completed Tasks | Scholar Desk</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body>
            <div class="data-container" style="text-align: center; max-width: 500px;">
                <h1 style="font-size: 3rem;">⏳</h1>
                <h2>No Completed Tasks Yet</h2>
                <p style="color: #7f8c8d; margin-bottom: 25px;">You haven't checked any tasks off your active list yet.</p>
                <a href="/mark_task_completed" class="btn-submit" style="text-decoration: none; display: block; background-color: #2ecc71;">✅ Complete Your First Task</a>
                <br>
                <a href="/tasks" class="link-flat">← Back to Tasks Hub</a>
            </div>
        </body>
        </html>
        '''
    html_output = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Completed Tasks Archive | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="data-container">
            <div style="border-left: 5px solid #2ecc71; padding-left: 15px; margin-bottom: 25px;">
                <h1 style="color: #27ae60; margin: 0;">🎉 Archive of Completed Tasks</h1>
                <p style="color: #7f8c8d; margin: 5px 0 0 0;">Great job! Here is a log of everything you've accomplished at your desk.</p>
            </div>
            
            <p>
                <a href="/tasks" class="link-flat">← Tasks Hub Menu</a> | 
                <a href="/view_tasks" class="link-flat">📅 View Ongoing Schedule</a>
            </p>
            
            <div class="table-responsive">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th style="width: 15%;">Task ID</th>
                            <th class="text-left" style="width: 60%;">Assignment Description</th>
                            <th style="width: 25%;">Deadline Target</th>
                        </tr>
                    </thead>
                    <tbody>
    '''

    for task in tasks:
        html_output += f'''
                        <tr>
                            <td><code>#{task[0]}</code></td>
                            <td class="text-left" style="text-decoration: line-through; color: #95a5a6;">{task[2]}</td>
                            <td><span class="badge" style="background-color: #d4edda; color: #155724;">Finished</span></td>
                        </tr>
        '''
    html_output += '''
                    </tbody>
                </table>
            </div>
            <div style="margin-top: 30px;">
                <a href="/dashboard" class="link-flat">← Return to Main Workspace</a>
            </div>
        </div>
    </body>
    </html>
    '''
    return html_output
@app.route('/view_incomplete_tasks',methods=['GET','POST'])
def view_incomplete_task():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    tasks=view_incomplete_tasks(session['email'])
    if not tasks:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Pending Backlogs | Scholar Desk</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body>
            <div class="data-container" style="text-align: center; max-width: 500px;">
                <h1 style="font-size: 3rem;">☀️</h1>
                <h2>All Caught Up!</h2>
                <p style="color: #7f8c8d; margin-bottom: 25px;">You have no pending or incomplete tasks on your schedule right now.</p>
                <a href="/tasks" class="btn-submit" style="text-decoration: none; display: block; background-color: #34495e;">Go to Tasks Hub</a>
            </div>
        </body>
        </html>
        '''
    html_output = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pending Backlogs | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="data-container">
            <h1>⏳ Outstanding Pending Tasks</h1>
            <p style="color: #7f8c8d; margin-top: -5px;">These agenda items are currently incomplete and require revision.</p>
            <p>
                <a href="/tasks" class="link-flat">← Tasks Hub Menu</a> | 
                <a href="/mark_task_completed" class="link-flat">✅ Complete an Item</a>
            </p>
            
            <div class="table-responsive">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th style="width: 15%;">Task ID</th>
                            <th class="text-left" style="width: 60%;">Assignment Description</th>
                            <th style="width: 25%;">Target Deadline</th>
                        </tr>
                    </thead>
                    <tbody>
    '''
    for task in tasks:
        html_output += f'''
                        <tr>
                            <td><code>#{task[0]}</code></td>
                            <td class="text-left" style="font-weight: 600; color: #2c3e50;">{task[2]}</td>
                            <td><span class="badge badge-deadline">{task[4]}</span></td>
                        </tr>
        '''
    html_output += '''
                    </tbody>
                </table>
            </div>
            <div style="margin-top: 30px;">
                <a href="/dashboard" class="link-flat">← Return to Main Workspace</a>
            </div>
        </div>
    </body>
    </html>
    '''
    return html_output


@app.route('/finance',methods=['GET','POST'])
def finance():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Expense Hub | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="menu-container">
            <div class="menu-header">
                <h1>💳 Financial Expense Tracker</h1>
                <p>Monitor your daily student budget, manage outlays, and audit your savings ledger.</p>
                <a href="/dashboard" class="link-flat">← Return to Main Dashboard</a>
            </div>
            
            <div class="action-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); max-width: 600px; margin: 0 auto;">
                <a href="/view_expense" class="action-box box-blue">
                    <span class="action-icon">📊</span>
                    <h4>View Expense Logs</h4>
                    <p>Audit your historical financial statement records.</p>
                </a>

                <a href="/add_expense" class="action-box box-green">
                    <span class="action-icon">💸</span>
                    <h4>Add New Expense</h4>
                    <p>Log a fresh transactional cost item into your books.</p>
                </a>
            </div>
            
            <div class="submenu-links" style="margin-top: 40px;">
                <p style="font-size: 0.85rem; color: #95a5a6;">💡 Tip: Log costs instantly to maintain an accurate monthly allowance audit.</p>
            </div>
        </div>
    </body>
    </html>
    '''
@app.route('/view_expense',methods=['GET','POST'])
def view_expense():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    expenses=view_expenses(session['email'])
    if not expenses:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Expense Logs | Scholar Desk</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body>
            <div class="data-container" style="text-align: center; max-width: 500px;">
                <h1 style="font-size: 3rem;">📉</h1>
                <h2>No Expenses Logged</h2>
                <p style="color: #7f8c8d; margin-bottom: 25px;">Your budget sheet is completely clean! No outlays recorded yet.</p>
                <a href="/add_expense" class="btn-submit" style="text-decoration: none; display: block; background-color: #2ecc71;">💸 Log Your First Expense</a>
                <br>
                <a href="/finance" class="link-flat">← Back to Finance Hub</a>
            </div>
        </body>
        </html>
        '''
    html_output = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Expense Sheet | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="data-container">
            <h1>💳 Your Personal Expense Logs</h1>
            <p style="color: #7f8c8d; margin-top: -5px;">Track your outlays, maintain budget balances, and audit transactions.</p>
            <p>
                <a href="/finance" class="link-flat">← Finance Hub Menu</a> | 
                <a href="/add_expense" class="link-flat">➕ Log Fresh Outlay</a>
            </p>
            
            <div class="table-responsive">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th style="width: 15%;">Log ID</th>
                            <th style="width: 25%;">Amount</th>
                            <th style="width: 35%;">Category / Label</th>
                            <th style="width: 25%;">Date Incurred</th>
                        </tr>
                    </thead>
                    <tbody>
    '''
    for expense in expenses:
        html_output += f'''
                        <tr>
                            <td><code>#{expense[0]}</code></td>
                            <td class="amount-text" style="color: #e74c3c;">₹{expense[2]}</td>
                            <td><span class="badge badge-category">{expense[3]}</span></td>
                            <td style="color: #7f8c8d; font-size: 0.95rem;">{expense[4]}</td>
                        </tr>
        '''
    html_output += '''
                    </tbody>
                </table>
            </div>
            <div style="margin-top: 30px;">
                <a href="/dashboard" class="link-flat">← Return to Main Workspace</a>
            </div>
        </div>
    </body>
    </html>
    '''
    return html_output
@app.route('/add_expense',methods=['GET','POST'])
def add_expense():
    if 'email' not in session:
        return redirect(url_for('login_user'))
    if request.method == 'POST':
        amount = request.form['amount']
        category=request.form['category']
        date = request.form['date']
        expenses_tracker(session['email'],amount,category,date)
        return redirect(url_for('view_expense'))
    
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Log Expense | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="form-container" style="min-height: 75vh;">
            <div class="form-card" style="max-width: 450px;">
                <h2>💸 Record New Outlay</h2>
                <p style="color: #7f8c8d; font-size: 0.9rem; margin-top: -20px; margin-bottom: 25px;">
                    Keep your budget balanced. Log your daily transactions instantly.
                </p>
                
                <form method="post">
                    <div class="input-field" style="margin-bottom: 20px;">
                        <label>Transaction Amount (₹)</label>
                        <input type="number" name="amount" placeholder="e.g., 150" min="1" step="any" required>
                    </div>
                    
                    <div class="input-field" style="margin-bottom: 20px;">
                        <label>Category / Label</label>
                        <input type="text" name="category" placeholder="e.g., Food, Bus, Books, Utilities" required>
                    </div>
                    
                    <div class="input-field" style="margin-bottom: 30px;">
                        <label>Date of Transaction (DD-MM-YYYY)</label>
                        <input type="text" name="date" placeholder="29-05-2026" required>
                    </div>
                    
                    <button type="submit" class="btn-register" style="background: linear-gradient(135deg, #2ecc71, #27ae60); box-shadow: 0 4px 15px rgba(46, 204, 113, 0.25);">
                        <span>Securely Log Expense</span>
                        <span class="btn-arrow">→</span>
                    </button>
                </form>
                
                <p class="auth-meta">
                    <a href="/finance" class="link-highlight" style="color: #27ae60;">← Back to Finance Hub</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    '''


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
@app.route('/attendance_calc', methods=['GET', 'POST'])
def attendance_calc():
    if 'email' not in session:
        return redirect(url_for('login_user'))
        
    if request.method == 'POST':
        try:
            # Explicit integer conversion to prevent backend math errors
            lec_attended = int(request.form['lec_attended'])
            total_lec = int(request.form['total_lec'])
            
            # Call your mathematical logic engine
            result = attendance_tracker(lec_attended, total_lec)
            
            # Displaying the calculation result inside a clean feedback card
            return f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Attendance Result | Scholar Desk</title>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <body>
                <div class="form-container" style="min-height: 70vh;">
                    <div class="form-card" style="max-width: 450px; text-align: center;">
                        <h2>📊 Analysis Complete</h2>
                        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #3498db;">
                            <p style="font-size: 1.1rem; color: #2c3e50; line-height: 1.6; margin: 0;">{result}</p>
                        </div>
                        <a href="/attendance_calc" class="btn-register" style="text-decoration: none; background: #34495e;">Calculate Again</a>
                        <br>
                        <a href="/tools" class="link-flat">← Back to Academic Tools</a>
                    </div>
                </div>
            </body>
            </html>
            '''
        except ValueError:
            return "<h2>❌ Error: Please ensure all inputs are valid numbers.</h2><a href='/attendance_calc'>Try Again</a>"
        except ZeroDivisionError:
            return "<h2>❌ Error: Total conducted lectures cannot be zero.</h2><a href='/attendance_calc'>Try Again</a>"

    # If they are just browsing to the page (GET request)
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Attendance Calculator | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="form-container" style="min-height: 70vh;">
            <div class="form-card" style="max-width: 450px;">
                <h2>📝 Attendance Monitor</h2>
                <p style="color: #7f8c8d; font-size: 0.9rem; margin-top: -20px; margin-bottom: 25px;">
                    Enter your lecture tallies to audit your overall criteria status.
                </p>
                
                <form method="post">
                    <div class="input-field" style="margin-bottom: 20px;">
                        <label>Lectures Attended</label>
                        <input type="number" name="lec_attended" min="0" placeholder="e.g., 45" required>
                    </div>
                    
                    <div class="input-field" style="margin-bottom: 30px;">
                        <label>Total Lectures Conducted</label>
                        <input type="number" name="total_lec" min="1" placeholder="e.g., 60" required>
                    </div>
                    
                    <button type="submit" class="btn-register" style="background: linear-gradient(135deg, #6c5ce7, #a29bfe); box-shadow: 0 4px 15px rgba(108, 92, 231, 0.25);">
                        <span>Analyze Attendance</span>
                        <span class="btn-arrow">→</span>
                    </button>
                </form>
                
                <p class="auth-meta">
                    <a href="/tools" class="link-highlight" style="color: #6c5ce7;">← Back to Tools Hub</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    '''
@app.route('/sgpa_calculator', methods=['GET', 'POST'])
def web_sgpa_calculator():
    if 'email' not in session:
        return redirect(url_for('login_user'))
        
    num_subjects = request.args.get('subjects', default=5, type=int)
    
    if request.method == 'POST':
        try:
            raw_grades = request.form.getlist('grades')
            raw_credits = request.form.getlist('credits')
            
            grades_list = [int(g) for g in raw_grades]
            credits_list = [int(c) for c in raw_credits]
            
            sgpa_result, error_message = calculate_sgpa(grades_list, credits_list)
            
            if error_message:
                return f'''
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Calculator Error | Scholar Desk</title>
                    <link rel="stylesheet" href="/static/style.css">
                </head>
                <body>
                    <div class="form-container" style="min-height: 70vh;">
                        <div class="form-card" style="max-width: 450px; text-align: center; border-left: 5px solid #e74c3c;">
                            <h2 style="color: #c0392b;">❌ Calculation Error</h2>
                            <p style="color: #2c3e50; margin: 20px 0;">{error_message}</p>
                            <a href="/sgpa_calculator" class="btn-register" style="text-decoration: none; background: #e74c3c;">Try Again</a>
                        </div>
                    </div>
                </body>
                </html>
                '''
                
            return f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>SGPA Result | Scholar Desk</title>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <body>
                <div class="form-container" style="min-height: 70vh;">
                    <div class="form-card" style="max-width: 450px; text-align: center; border-left: 5px solid #2ecc71;">
                        <h2>📊 Calculation Complete!</h2>
                        <p style="color: #7f8c8d; font-size: 0.95rem; margin-top: -10px;">Your semester performance index has been compiled.</p>
                        
                        <div style="background-color: #f4fbf7; padding: 25px; border-radius: 10px; margin: 25px 0; border: 1px dashed #2ecc71;">
                            <span style="font-size: 0.9rem; color: #7f8c8d; text-transform: uppercase; font-weight: 600; letter-spacing: 1px;">Your Calculated SGPA</span>
                            <h1 style="font-size: 3.5rem; color: #27ae60; margin: 5px 0; font-family: monospace;">{sgpa_result:.2f}</h1>
                        </div>
                        
                        <a href="/sgpa_calculator" class="btn-register" style="text-decoration: none; background: linear-gradient(135deg, #9b59b6, #8e44ad);">Calculate New Term</a>
                        <p class="auth-meta"><a href="/tools" class="link-highlight" style="color: #8e44ad;">← Back to Tools Hub</a></p>
                    </div>
                </div>
            </body>
            </html>
            '''
        except ValueError:
            return f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Input Error | Scholar Desk</title>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <body>
                <div class="form-container" style="min-height: 70vh;">
                    <div class="form-card" style="max-width: 450px; text-align: center;">
                        <h2 style="color: #c0392b;">❌ Data Entry Error</h2>
                        <p style="color: #7f8c8d; margin-bottom: 25px;">Please make sure all input fields contain valid numerical scores.</p>
                        <a href="/sgpa_calculator" class="btn-register" style="text-decoration: none; background: #34495e;">Return to Form</a>
                    </div>
                </div>
            </body>
            </html>
            '''

    # --- GENERATING THE SINGLE FORM WITH MULTIPLE FIELDS ---
    input_rows = ""
    for i in range(num_subjects):
        input_rows += f'''
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #f1f2f6;">
            <label style="font-weight: 600; color: #34495e; font-size: 0.95rem;">Subject {i+1}</label> 
            <div style="display: flex; gap: 15px;">
                <div class="input-field" style="width: 110px; margin: 0;">
                    <input type="number" name="grades" min="1" max="10" placeholder="Grade (1-10)" required style="padding: 8px 10px; text-align: center;">
                </div> 
                <div class="input-field" style="width: 90px; margin: 0;">
                    <input type="number" name="credits" min="1" max="8" placeholder="Credits" required style="padding: 8px 10px; text-align: center;">
                </div>
            </div>
        </div>
        '''
        
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>SGPA Calculator | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="form-container" style="margin: 40px auto; padding: 20px;">
            <div class="form-card" style="max-width: 500px; width: 100%;">
                <h2>📊 SGPA Academic Calculator</h2>
                <p style="color: #7f8c8d; font-size: 0.9rem; margin-top: -20px; margin-bottom: 20px;">
                    Select your course load layout below to adjust the calculation grid:
                </p>
                
                <div style="display: flex; gap: 8px; margin-bottom: 25px; flex-wrap: wrap; background: #f8f9fa; padding: 6px; border-radius: 8px; justify-content: center;">
                    <span style="font-size: 0.85rem; color: #7f8c8d; align-self: center; font-weight: 600; margin-right: 5px;">Subjects:</span>
                    {" | ".join([f'<a href="/sgpa_calculator?subjects={n}" style="text-decoration:none; padding: 5px 12px; border-radius: 5px; font-size: 0.85rem; font-weight: bold; background: {"#9b59b6" if n == num_subjects else "white"}; color: {"white" if n == num_subjects else "#7f8c8d"}; border: 1px solid #e2e8f0;">{n}</a>' for n in range(3, 8)])}
                </div>
                
                <form method="post">
                    <div style="display: flex; justify-content: space-between; padding-bottom: 5px; border-bottom: 2px solid #eaeded; margin-bottom: 5px;">
                        <span style="font-size: 0.8rem; font-weight: bold; color: #bdc3c7; text-transform: uppercase;">Course ID</span>
                        <div style="display: flex; gap: 15px; width: 215px; justify-content: space-between; padding-right: 5px;">
                            <span style="font-size: 0.8rem; font-weight: bold; color: #bdc3c7; text-transform: uppercase; text-align: center; width: 110px;">Grade Pt</span>
                            <span style="font-size: 0.8rem; font-weight: bold; color: #bdc3c7; text-transform: uppercase; text-align: center; width: 90px;">Credits</span>
                        </div>
                    </div>

                    {input_rows}
                    
                    <button type="submit" class="btn-register" style="background: linear-gradient(135deg, #9b59b6, #8e44ad); box-shadow: 0 4px 15px rgba(155, 89, 182, 0.25); margin-top: 30px;">
                        <span>Compute Semester SGPA</span>
                        <span class="btn-arrow">→</span>
                    </button>
                </form>
                
                <p class="auth-meta">
                    <a href="/tools" class="link-highlight" style="color: #9b59b6;">← Back to Tools Hub</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    '''
@app.route('/web_resources')
def web_resource():
    if 'email' not in session:
        return redirect(url_for('login_user'))

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
        return redirect(url_for('login_user'))
    return '''
            <h1>Tools Section</h1>
            <p>Here you can access all your tools and resources.</p>
            <a href="/sgpa_calculator">SGPA calculator</a><br>
            <a href="/pomodoro">Pomodoro Timer</a><br>
            <a href="/attendance_calc">Attendance Calculator</a><br>
            <a href="/chatbot">Saathi AI</a><br>
            <a href="/web_resources">Resources</a><br>
        '''

if __name__ == '__main__':
     app.run(debug=True)