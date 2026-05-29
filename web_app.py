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
@app.after_request
def add_header(response):
    """
    Enforces absolute browser security by preventing caching on back-button navigation
    """
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response
app.secret_key = 'super_secret_student_toolkit_key_2026'

init_db()

@app.route('/')
def home():
    if 'email' in session:
        return redirect(url_for('dashboard'))
        
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to Scholar Desk | Your Academic Command Center</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="landing-body">

        <nav class="landing-nav">
            <div class="nav-logo">
                <span>🎓</span> Scholar Desk
            </div>
            <div class="nav-buttons">
                <button onclick="window.location.replace('/login')" class="btn-nav-signin">
                    Sign In
                </button>
                <a href="/register" class="btn-nav-signup">
                    Get Started
                </a>
            </div>
        </nav>

        <header class="hero-section">
            <div class="hero-content">
                <h1>Organize Your Academic Life In One Workspace.</h1>
                <p>Streamline your lecture notes, track course deadlines, auditor class attendance margins, and compute your term grades dynamically with a unified digital campus dashboard.</p>
                <button onclick="window.location.replace('/login')" class="hero-btn-action">
                    Access Your Desk Terminal
                </button>
            </div>
            <div class="hero-badge">📚</div>
        </header>

        <main>
            <h2 class="section-title">Engineered For Peak Academic Productivity</h2>
            <div class="features-grid">
                
                <div class="feature-card">
                    <span class="feature-icon">📝</span>
                    <h3>Notes Engine</h3>
                    <p>Compile core lecture summaries and reference logs cleanly within structural dedicated cloud notebooks.</p>
                </div>

                <div class="feature-card">
                    <span class="feature-icon">📅</span>
                    <h3>Task Scheduler</h3>
                    <p>Map your assignment submissions, project targets, and mid-term exam milestones with intuitive alerts.</p>
                </div>

                <div class="feature-card">
                    <span class="feature-icon">📈</span>
                    <h3>SGPA Calculator</h3>
                    <p>Input course grade points and multi-weighted academic credits to project your semester GPA instantly.</p>
                </div>

                <div class="feature-card">
                    <span class="feature-icon">⏱️</span>
                    <h3>Pomodoro Engine</h3>
                    <p>Maintain consistent academic performance intervals utilizing localized sensory study timers.</p>
                </div>

                <div class="feature-card">
                    <span class="feature-icon">✅</span>
                    <h3>Attendance Auditor</h3>
                    <p>Track your lecture presence rates dynamically to ensure you stay safely above minimum examination thresholds.</p>
                </div>

                <div class="feature-card">
                    <span class="feature-icon">🤖</span>
                    <h3>Saathi AI Chatbot</h3>
                    <p>Consult an advanced, context-aware AI study assistant for rapid curriculum breakdown and summarization.</p>
                </div>

            </div>
        </main>

        <footer class="footer-landing">
            <p style="margin: 0; font-size: 0.95rem;">&copy; 2026 Scholar Desk Core Platforms Systems. All Rights Reserved.</p>
            <div class="developer-credit">
                Designed & Developed with engineered precision by <br>
                <span class="developer-names">Mayur B. Gund</span> & <span class="developer-names">Arjun B. Kadam</span>
            </div>
        </footer>

    </body>
    </html>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    # 🧼 AUTOMATIC SESSION KILLER: Wipes session if user manually returns here via GET
    if request.method == 'GET' and 'email' in session:
        session.clear()

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        is_valid, student = login(email, password)
        
        if is_valid:
            session['email'] = student[0]
            session['name'] = student[1]
            return {"status": "success", "redirect": url_for('dashboard')}
        else:
            return {"status": "error", "message": "Invalid email or password. Please verify your credentials and try again."}
            
    # --- GET REQUEST: RENDER THE INDUSTRY-GRADE UI ---
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sign In | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="auth-bg">
        <div class="auth-wrapper">
            
            <div class="auth-card">
                <div class="auth-header">
                    <span class="auth-brand-icon">🎓</span>
                    <h2>Welcome Back</h2>
                    <p>Enter your credentials to access your academic command center</p>
                </div>
                
                <div id="js-alert-container" class="alert-box">
                    <span class="alert-icon">⚠️</span>
                    <p id="js-error-text"></p>
                </div>
                
                <form id="loginForm">
                    <div class="form-group">
                        <label for="email">Institutional Email Address</label>
                        <input type="email" id="email" name="email" placeholder="name@university.edu" required autocomplete="email">
                    </div>
                    
                    <div class="form-group">
                        <div class="label-row">
                            <label for="password">Password</label>
                            <a href="/reset_password" class="auth-link-alt">Forgot password?</a>
                        </div>
                        <input type="password" id="password" name="password" placeholder="••••••••" required autocomplete="current-password">
                    </div>
                    
                    <div class="form-utility-row">
                        <label class="checkbox-container">
                            <input type="checkbox" name="remember_me">
                            <span class="checkbox-checkmark"></span>
                            <span class="checkbox-label">Keep me logged in</span>
                        </label>
                    </div>
                    
                    <button type="submit" class="btn-auth-submit">
                        <span>Sign In to Workspace</span>
                        <span class="btn-arrow">→</span>
                    </button>
                </form>
                
                <div class="auth-footer">
                    <p>New to the platform? <a href="/register" class="auth-link-highlight">Create a workspace</a></p>
                    
                    <button onclick="window.location.replace('/')" class="btn-history-back">
                        ← Back to Welcome Landing
                    </button>
                </div>
            </div>
            
            <p class="auth-meta-compliance">Secure 256-bit SSL encrypted terminal session</p>
        </div>

        <script>
            document.getElementById('loginForm').addEventListener('submit', async function(e) {{
                e.preventDefault();
                
                const formData = new FormData(this);
                const alertContainer = document.getElementById('js-alert-container');
                const errorText = document.getElementById('js-error-text');
                
                alertContainer.style.display = 'none';
                alertContainer.classList.remove('animated-shake');
                
                try {{
                    const response = await fetch('/login', {{
                        method: 'POST',
                        body: formData
                    }});
                    
                    const data = await response.json();
                    
                    if (data.status === 'success') {{
                        window.location.replace(data.redirect);
                    }} else {{
                        errorText.textContent = data.message;
                        alertContainer.style.display = 'flex';
                        
                        void alertContainer.offsetWidth; 
                        alertContainer.classList.add('animated-shake');
                    }}
                }} catch (err) {{
                    console.error("Authentication communication failure:", err);
                }}
            }});
        </script>
    </body>
    </html>
    '''
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    # If an authenticated user wanders to the sign-up page, clear them out
    if request.method == 'GET' and 'email' in session:
        session.clear()

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        age = request.form.get('age')
        class_ = request.form.get('class')
        contact_info = request.form.get('contact_info')

        # Execute your backend validation function
        is_valid, message = student_Registration(name, email, password, age, class_, contact_info)
        
        if is_valid:
            # 🚀 JSON API SUCCESS BRIDGE
            return {"status": "success", "message": "Account created successfully! Redirecting to login..."}
        else:
            # 🚀 JSON API ERROR BRIDGE
            return {"status": "error", "message": message}

    # --- GET REQUEST: RENDER THE INDUSTRY REGISTRATION WORKSPACE ---
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Create Your Workspace | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="auth-bg">
        <div class="register-container">
            
            <div class="register-card">
                <div class="register-header">
                    <span class="register-brand-logo">🎓</span>
                    <h2>Create Your Workspace</h2>
                    <p>Set up your institutional profile to activate your student desk</p>
                </div>
                
                <div id="js-status-container" class="alert-box">
                    <span id="js-status-icon">⚠️</span>
                    <p id="js-status-text"></p>
                </div>
                
                <form id="registerForm">
                    <div class="form-grid-layout">
                        
                        <div class="form-group">
                            <label for="name">Full Name</label>
                            <input type="text" id="name" name="name" placeholder="John Doe" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="email">Institutional Email</label>
                            <input type="email" id="email" name="email" placeholder="name@university.edu" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="password">Secure Password</label>
                            <input type="password" id="password" name="password" placeholder="••••••••" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="age">Age</label>
                            <input type="number" id="age" name="age" placeholder="20" min="16" max="100" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="class">Class / Batch Division</label>
                            <input type="text" id="class" name="class" placeholder="CS - Division A" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="contact_info">Contact Number</label>
                            <input type="tel" id="contact_info" name="contact_info" placeholder="+91 XXXXX XXXXX" required>
                        </div>
                        
                    </div>
                    
                    <button type="submit" class="btn-auth-submit" style="margin-top: 10px;">
                        <span>Initialize Workspace Profile</span>
                        <span class="btn-arrow">→</span>
                    </button>
                </form>
                
                <div class="auth-footer">
                    <p>Already have a desk assigned? <a href="/login" class="auth-link-highlight">Sign in instead</a></p>
                    
                    <button onclick="window.location.replace('/')" class="btn-history-back">
                        ← Back to Welcome Landing
                    </button>
                </div>
            </div>
            
            <p class="auth-meta-compliance">System Development Lead: Mayur B. Gund & Arjun B. Kadam</p>
        </div>

        <script>
            document.getElementById('registerForm').addEventListener('submit', async function(e) {{
                e.preventDefault();
                
                const formData = new FormData(this);
                const statusContainer = document.getElementById('js-status-container');
                const statusText = document.getElementById('js-status-text');
                const statusIcon = document.getElementById('js-status-icon');
                
                // Clear state
                statusContainer.style.display = 'none';
                statusContainer.className = 'alert-box';
                
                try {{
                    const response = await fetch('/register', {{
                        method: 'POST',
                        body: formData
                    }});
                    
                    const data = await response.json();
                    
                    if (data.status === 'success') {{
                        // Style banner green for visual confirmation
                        statusContainer.style.backgroundColor = '#ecfdf5';
                        statusContainer.style.borderColor = '#a7f3d0';
                        statusContainer.style.borderLeftColor = '#10b981';
                        statusText.style.color = '#065f46';
                        statusIcon.textContent = '✅';
                        
                        statusText.textContent = data.message;
                        statusContainer.style.display = 'flex';
                        
                        // Wait 1.5 seconds so they can read the success message, then replace screen with login
                        setTimeout(() => {{
                            window.location.replace('/login');
                        }}, 1500);
                        
                    }} else {{
                        // Style banner red for error
                        statusContainer.style.backgroundColor = '#fdf2f2';
                        statusContainer.style.borderColor = '#f8b4b4';
                        statusContainer.style.borderLeftColor = '#e74c3c';
                        statusText.style.color = '#c0392b';
                        statusIcon.textContent = '⚠️';
                        
                        statusText.textContent = data.message;
                        statusContainer.style.display = 'flex';
                        
                        void statusContainer.offsetWidth; 
                        statusContainer.classList.add('animated-shake');
                    }}
                }} catch (err) {{
                    console.error("Registration processing error:", err);
                }}
            }});
        </script>
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
@app.route('/logout')
def logout():
    # 1. Completely destroy all session data variables behind the scenes
    session.clear() 
    
    # 2. 🚀 THE HISTORY ERASED RENDERING ENGINE:
    # Instead of a standard redirect, we return a micro-response that forces 
    # the browser to overwrite its history stack with the landing page.
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <script>
            // Completely replace the current history track entry with the clean home page
            window.location.replace("/");
        </script>
    </head>
    <body>
        <p style="font-family: sans-serif; text-align: center; color: #7f8c8d; margin-top: 50px;">
            Securely closing workspace session...
        </p>
    </body>
    </html>
    '''

@app.route('/dashboard')
def dashboard():
    # Security Guardrail Check
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    # --- GET REQUEST: RENDER ENTERPRISE WORKSPACE ---
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Workspace Dashboard | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
        <script>
            // 🚀 THE PERSISTENCE GUARD: Force fresh server evaluation on back-arrow travel
            window.addEventListener('pageshow', function(event) {{
                if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {{
                    window.location.reload();
                }}
            }});
        </script>
    </head>
    <body class="dashboard-body">

        <div class="workspace-layout">
            
            <aside class="workspace-sidebar">
                <div class="sidebar-brand">
                    <span class="brand-avatar">🎓</span>
                    <div class="brand-text">
                        <h3>Scholar Desk</h3>
                        <span class="system-badge">v2.4 Core</span>
                    </div>
                </div>
                
                <nav class="sidebar-menu">
                    <a href="/dashboard" class="menu-item active">
                        <span class="menu-icon">🎛️</span> Workspace Home
                    </a>
                    <a href="/notes" class="menu-item">
                        <span class="menu-icon">📝</span> Notes Engine
                    </a>
                    <a href="/tasks" class="menu-item">
                        <span class="menu-icon">📅</span> Task Manager
                    </a>
                    <a href="/tools" class="menu-item">
                        <span class="menu-icon">📊</span> Academic Tools
                    </a>
                    <a href="/finance" class="menu-item">
                        <span class="menu-icon">💳</span> Expense Tracker
                    </a>
                    <a href="/chatbot" class="menu-item highlight-ai">
                        <span class="menu-icon">🤖</span> Saathi AI Assistant
                    </a>
                </nav>
                
                <div class="sidebar-footer">
                    <a href="/logout" class="btn-sidebar-logout">
                        <span>🔒 Terminate Session</span>
                    </a>
                </div>
            </aside>
            
            <main class="workspace-main">
                
                <header class="main-header">
                    <div class="header-welcome">
                        <h1>Welcome Back, <span class="user-highlight">{session.get("name", "Scholar")}</span></h1>
                        <p>Academic Hub Command Center Terminal</p>
                    </div>
                    <div class="header-profile-badge">
                        <div class="avatar-circle">{session.get("name", "S")[0].upper()}</div>
                        <span class="status-indicator online"></span>
                    </div>
                </header>
                
                <section class="dashboard-matrix-grid">
                    
                    <div class="matrix-card">
                        <div class="matrix-card-header">
                            <span class="matrix-icon bg-blue">📝</span>
                            <span class="matrix-tag">Active Engine</span>
                        </div>
                        <h3>Notes Engine</h3>
                        <p>Compile core lecture summaries and reference logs cleanly within structural cloud notebooks.</p>
                        <a href="/notes" class="btn-matrix-action">Launch Engine</a>
                    </div>

                    <div class="matrix-card">
                        <div class="matrix-card-header">
                            <span class="matrix-icon bg-purple">📅</span>
                            <span class="matrix-tag">Realtime Sync</span>
                        </div>
                        <h3>Task Manager</h3>
                        <p>Map your assignment submissions, project targets, and mid-term exam milestones with alerts.</p>
                        <a href="/tasks" class="btn-matrix-action">Open Scheduler</a>
                    </div>

                    <div class="matrix-card">
                        <div class="matrix-card-header">
                            <span class="matrix-icon bg-emerald">📊</span>
                            <span class="matrix-tag">Analytical</span>
                        </div>
                        <h3>Academic Tools</h3>
                        <p>Compute multi-weighted course credit parameters and track lecture metrics dynamically.</p>
                        <a href="/tools" class="btn-matrix-action">Compute Metrics</a>
                    </div>

                    <div class="matrix-card">
                        <div class="matrix-card-header">
                            <span class="matrix-icon bg-amber">💳</span>
                            <span class="matrix-tag">Ledger Vault</span>
                        </div>
                        <h3>Expense Tracker</h3>
                        <p>Audit financial overhead allowances, student budget targets, and history statements.</p>
                        <a href="/finance" class="btn-matrix-action">Audit Ledger</a>
                    </div>

                    <div class="matrix-card featured-ai-card">
                        <div class="matrix-card-header">
                            <span class="matrix-icon bg-ai">🤖</span>
                            <span class="matrix-tag tag-ai">Neural Mesh</span>
                        </div>
                        <h3>Saathi AI Workspace</h3>
                        <p>Consult an interactive, context-aware artificial intelligence study assistant for rapid curriculum breakdown.</p>
                        <a href="/chatbot" class="btn-matrix-action btn-ai-action">Initialize Saathi Core</a>
                    </div>

                </section>
                
            </main>
            
        </div>
    </body>
    </html>
    '''
@app.route('/notes')
def notes():
    # Security Guardrail
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    # --- GET REQUEST: RENDER ENTERPRISE NOTES ENGINE ---
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Notes Engine | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
        <script>
            // 🚀 THE PERSISTENCE GUARD: Force fresh evaluation on back-arrow travel
            window.addEventListener('pageshow', function(event) {{
                if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {{
                    window.location.reload();
                }}
            }});
        </script>
    </head>
    <body class="dashboard-body">

        <div class="workspace-layout">
            
            <aside class="workspace-sidebar">
                <div class="sidebar-brand">
                    <span class="brand-avatar">🎓</span>
                    <div class="brand-text">
                        <h3>Scholar Desk</h3>
                        <span class="system-badge">v2.4 Core</span>
                    </div>
                </div>
                
                <nav class="sidebar-menu">
                    <a href="/dashboard" class="menu-item">
                        <span class="menu-icon">🎛️</span> Workspace Home
                    </a>
                    <a href="/notes" class="menu-item active">
                        <span class="menu-icon">📝</span> Notes Engine
                    </a>
                    <a href="/tasks" class="menu-item">
                        <span class="menu-icon">📅</span> Task Manager
                    </a>
                    <a href="/tools" class="menu-item">
                        <span class="menu-icon">📊</span> Academic Tools
                    </a>
                    <a href="/finance" class="menu-item">
                        <span class="menu-icon">💳</span> Expense Tracker
                    </a>
                    <a href="/chatbot" class="menu-item highlight-ai">
                        <span class="menu-icon">🤖</span> Saathi AI Assistant
                    </a>
                </nav>
                
                <div class="sidebar-footer">
                    <a href="/logout" class="btn-sidebar-logout">
                        <span>🔒 Terminate Session</span>
                    </a>
                </div>
            </aside>
            
            <main class="workspace-main">
                
                <header class="main-header">
                    <div class="header-welcome">
                        <h1>📚 Lecture Notes Hub</h1>
                        <p>Organize thoughts, archive study materials, and audit core revisions</p>
                    </div>
                    
                    <div class="header-quick-filters">
                        <a href="/completed_notes" class="btn-filter-tab status-complete">
                            <span class="dot-indicator"></span> Completed Revisions
                        </a>
                        <a href="/incomplete_notes" class="btn-filter-tab status-pending">
                            <span class="dot-indicator"></span> Pending Backlogs
                        </a>
                    </div>
                </header>
                
                <div class="notes-utility-bar">
                    <div class="utility-meta-info">
                        Workspace Session Active: <b>{session.get("name", "Scholar")}</b>
                    </div>
                </div>
                
                <section class="dashboard-matrix-grid">
                    
                    <a href="/view_notes" class="notes-action-card">
                        <div class="notes-card-accent border-blue"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-blue">📖</div>
                            <div class="notes-card-content">
                                <h3>View Notebook Ledger</h3>
                                <p>Open your comprehensive, central repository database to read, search, and parse archived class logs.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                    <a href="/add_note" class="notes-action-card">
                        <div class="notes-card-accent border-emerald"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-emerald">✍️</div>
                            <div class="notes-card-content">
                                <h3>Add New Notebook</h3>
                                <p>Jot down real-time concepts, configure study parameters, and log fresh curricular data insights.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                    <a href="/mark_note" class="notes-action-card">
                        <div class="notes-card-accent border-amber"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-amber">🎯</div>
                            <div class="notes-card-content">
                                <h3>Complete Review Cycle</h3>
                                <p>Flag a curriculum study notebook entry as fully processed, removing it from your active urgent workload.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                    <a href="/delete_note" class="notes-action-card">
                        <div class="notes-card-accent border-red"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-red">🗑️</div>
                            <div class="notes-card-content">
                                <h3>Purge Archive Entries</h3>
                                <p>Permanently remove old backlogs, erroneous notebook modules, or outdated syllabus sheets from disk.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                </section>
                
            </main>
            
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
    # Consolidated Security Check
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    # --- GET REQUEST: RENDER ENTERPRISE TASK TERMINAL ---
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Task Manager | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
        <script>
            // 🚀 THE PERSISTENCE GUARD: Force fresh verification on back-arrow travel
            window.addEventListener('pageshow', function(event) {{
                if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {{
                    window.location.reload();
                }}
            }});
        </script>
    </head>
    <body class="dashboard-body">

        <div class="workspace-layout">
            
            <aside class="workspace-sidebar">
                <div class="sidebar-brand">
                    <span class="brand-avatar">🎓</span>
                    <div class="brand-text">
                        <h3>Scholar Desk</h3>
                        <span class="system-badge">v2.4 Core</span>
                    </div>
                </div>
                
                <nav class="sidebar-menu">
                    <a href="/dashboard" class="menu-item">
                        <span class="menu-icon">🎛️</span> Workspace Home
                    </a>
                    <a href="/notes" class="menu-item">
                        <span class="menu-icon">📝</span> Notes Engine
                    </a>
                    <a href="/tasks" class="menu-item active">
                        <span class="menu-icon">📅</span> Task Manager
                    </a>
                    <a href="/tools" class="menu-item">
                        <span class="menu-icon">📊</span> Academic Tools
                    </a>
                    <a href="/finance" class="menu-item">
                        <span class="menu-icon">💳</span> Expense Tracker
                    </a>
                    <a href="/chatbot" class="menu-item highlight-ai">
                        <span class="menu-icon">🤖</span> Saathi AI Assistant
                    </a>
                </nav>
                
                <div class="sidebar-footer">
                    <a href="/logout" class="btn-sidebar-logout">
                        <span>🔒 Terminate Session</span>
                    </a>
                </div>
            </aside>
            
            <main class="workspace-main">
                
                <header class="main-header">
                    <div class="header-welcome">
                        <h1>📅 Task Management Hub</h1>
                        <p>Track strict deadlines, prioritize academic metrics, and audit schedules</p>
                    </div>
                    
                    <div class="header-quick-filters">
                        <a href="/view_completed_tasks" class="btn-filter-tab status-complete">
                            <span class="dot-indicator"></span> Completed History
                        </a>
                        <a href="/view_incomplete_tasks" class="btn-filter-tab status-pending">
                            <span class="dot-indicator"></span> Pending Backlogs
                        </a>
                    </div>
                </header>
                
                <div class="notes-utility-bar">
                    <div class="utility-meta-info">
                        Schedule Tracking Matrix: <b>{session.get("name", "Scholar")}</b>
                    </div>
                </div>
                
                <section class="dashboard-matrix-grid">
                    
                    <a href="/view_tasks" class="notes-action-card">
                        <div class="notes-card-accent border-indigo"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-indigo">👁️‍🗨️</div>
                            <div class="notes-card-content">
                                <h3>View All Scheduled Tasks</h3>
                                <p>Access your primary timeline grid ledger to monitor operational task lists, notes, and milestones.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                    <a href="/add_task" class="notes-action-card">
                        <div class="notes-card-accent border-emerald"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-emerald">➕</div>
                            <div class="notes-card-content">
                                <h3>Add New Task Entry</h3>
                                <p>Log an upcoming submission requirement, assignment deadline, or specific test block parameter onto your stack.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                    <a href="/mark_task_completed" class="notes-action-card">
                        <div class="notes-card-accent border-amber"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-amber">✅</div>
                            <div class="notes-card-content">
                                <h3>Complete Pending Item</h3>
                                <p>Close an active milestone schedule loop, logging it instantly into your archive as successfully finished.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                    <a href="/delete_task" class="notes-action-card">
                        <div class="notes-card-accent border-red"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-red">🗑️</div>
                            <div class="notes-card-content">
                                <h3>Purge Task Registry</h3>
                                <p>Permanently wipe dropped courses, erroneous deadline logs, or test notes out of your cloud structural platform storage.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                </section>
                
            </main>
            
        </div>
    </body>
    </html>
    '''
# --- GLOBAL COMPONENT: UNIFIED TASK SIDEBAR CONTEXT ---
def get_tasks_sidebar():
    return f'''
    <aside class="workspace-sidebar">
        <div class="sidebar-brand">
            <span class="brand-avatar">🎓</span>
            <div class="brand-text">
                <h3>Scholar Desk</h3>
                <span class="system-badge">v2.4 Core</span>
            </div>
        </div>
        <nav class="sidebar-menu">
            <a href="/dashboard" class="menu-item"><span class="menu-icon">🎛️</span> Workspace Home</a>
            <a href="/notes" class="menu-item"><span class="menu-icon">📝</span> Notes Engine</a>
            <a href="/tasks" class="menu-item active"><span class="menu-icon">📅</span> Task Manager</a>
            <a href="/tools" class="menu-item"><span class="menu-icon">📊</span> Academic Tools</a>
            <a href="/finance" class="menu-item"><span class="menu-icon">💳</span> Expense Tracker</a>
            <a href="/chatbot" class="menu-item highlight-ai"><span class="menu-icon">🤖</span> Saathi AI Assistant</a>
        </nav>
        <div class="sidebar-footer">
            <a href="/logout" class="btn-sidebar-logout"><span>🔒 Terminate Session</span></a>
        </div>
    </aside>
    '''


@app.route('/view_tasks')
def view_task():
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    tasks = view_tasks(session['email'])
    
    # Empty State Condition
    if not tasks:
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Active Schedule | Scholar Desk</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body class="dashboard-body">
            <div class="workspace-layout">
                {get_tasks_sidebar()}
                <main class="workspace-main" style="display: flex; align-items: center; justify-content: center;">
                    <div class="empty-state-panel">
                        <span class="empty-state-icon">☀️</span>
                        <h2>No Active Tasks Logged</h2>
                        <p>Your ongoing academic schedule ledger is completely immaculate! No tasks or target assignments pending.</p>
                        <a href="/add_task" class="btn-ledger-primary" style="background: linear-gradient(135deg, #6366f1, #4f46e5); box-shadow: 0 4px 12px rgba(99,102,241,0.2);">➕ Add Your First Task</a>
                    </div>
                </main>
            </div>
        </body>
        </html>
        '''

    # Build Premium Task Item View Cards
    task_cards_html = ""
    for task in tasks:
        task_cards_html += f'''
        <div class="task-registry-row">
            <div class="task-left-meta">
                <span class="task-hash-badge">#{task[0]}</span>
                <p class="task-desc-title">{task[2]}</p>
            </div>
            <div class="task-right-meta">
                <span class="task-deadline-pill">⏰ Target: {task[4]}</span>
            </div>
        </div>
        '''

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Active Tasks | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="dashboard-body">
        <div class="workspace-layout">
            {get_tasks_sidebar()}
            
            <main class="workspace-main">
                <header class="main-header">
                    <div class="header-welcome">
                        <h1>📅 Your Ongoing Academic Schedule</h1>
                        <p>Real-time timeline tracking, milestone management, and assignment queues</p>
                    </div>
                    <div style="display: flex; gap: 12px;">
                        <a href="/add_task" class="btn-ledger-primary" style="background: #6366f1; box-shadow: 0 4px 12px rgba(99,102,241,0.2);">Add New Task</a>
                    </div>
                </header>

                <div class="task-list-wrapper-zone">
                    {task_cards_html}
                </div>

                <div style="margin-top: 25px; display: flex; gap: 15px;">
                    <a href="/tasks" class="btn-ledger-secondary">← Back to Tasks Hub</a>
                </div>
            </main>
        </div>
    </body>
    </html>
    '''


@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    if request.method == 'POST':
        task = request.form.get('task')
        raw_date = request.form.get('date') # Format comes from HTML calendar input as 'YYYY-MM-DD'
        
        # 🚀 THE DATE REARRANGEMENT PARSER: Converts 'YYYY-MM-DD' cleanly to match your string database format 'DD-MM-YYYY'
        if raw_date and '-' in raw_date:
            year, month, day = raw_date.split('-')
            formatted_date = f"{day}-{month}-{year}"
        else:
            formatted_date = raw_date

        schedule_task(session['email'], task, formatted_date)
        return redirect(url_for('view_task'))
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Schedule Task | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="dashboard-body">
        <div class="workspace-layout">
            {get_tasks_sidebar()}

            <main class="workspace-main" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <div class="ledger-form-card">
                    <div class="ledger-form-header">
                        <h2>📅 Schedule New Task</h2>
                        <p>Establish strict course assignments, project scopes, or self-study timelines inside your cluster database.</p>
                    </div>

                    <form method="post">
                        <div class="form-group">
                            <label for="task">Task / Assignment Description</label>
                            <input type="text" id="task" name="task" placeholder="e.g., Complete Advanced Operating Systems Assignment 2" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="date">Deadline Target Date</label>
                            <input type="date" id="date" name="date" required>
                        </div>
                        
                        <button type="submit" class="btn-ledger-submit" style="background: linear-gradient(135deg, #6366f1, #4f46e5); box-shadow: 0 4px 12px rgba(99,102,241,0.2);">
                            <span>Append Task to Schedule</span>
                            <span class="btn-arrow">→</span>
                        </button>
                    </form>
                    
                    <div class="ledger-form-footer">
                        <a href="/tasks" class="btn-ledger-secondary">Cancel and Return</a>
                    </div>
                </div>
            </main>
        </div>
    </body>
    </html>
    '''


@app.route('/delete_task', methods=['GET', 'POST'])
def delete_task():
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    if request.method == 'POST':
        task_id = request.form.get('task_id')
        delete_tasks(session['email'], task_id)
        return redirect(url_for('view_task'))
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Purge Records | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="dashboard-body">
        <div class="workspace-layout">
            {get_tasks_sidebar()}

            <main class="workspace-main" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <div class="ledger-form-card" style="border-top: 4px solid #ef4444;">
                    <div class="ledger-form-header">
                        <h2 style="color: #ef4444;">🗑️ Purge Task Record</h2>
                        <p>Provide the matching mathematical <b>Task ID Token</b> below to wipe this workflow block permanently out of your account file indexes.</p>
                    </div>

                    <form method="post">
                        <div class="form-group">
                            <label for="task_id">Target Task ID Number</label>
                            <input type="number" id="task_id" name="task_id" placeholder="e.g., 4" min="1" required>
                        </div>
                        
                        <button type="submit" class="btn-ledger-submit" style="background: linear-gradient(135deg, #ef4444, #dc2626); box-shadow: 0 4px 12px rgba(239,68,68,0.25);">
                            <span>Confirm Permanent Deletion</span>
                            <span class="btn-arrow">→</span>
                        </button>
                    </form>
                    
                    <div class="ledger-form-footer">
                        <a href="/tasks" class="btn-ledger-secondary">Cancel and Abort</a>
                    </div>
                </div>
            </main>
        </div>
    </body>
    </html>
    '''


@app.route('/mark_task_completed', methods=['GET', 'POST'])
def mark_task_completed():
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    if request.method == 'POST':
        task_id = request.form.get('task_id')
        Completed_tasks(session['email'], task_id)
        return redirect(url_for('view_task'))
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Resolve Milestone | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="dashboard-body">
        <div class="workspace-layout">
            {get_tasks_sidebar()}

            <main class="workspace-main" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <div class="ledger-form-card" style="border-top: 4px solid #10b981;">
                    <div class="ledger-form-header">
                        <h2 style="color: #10b981;">✅ Cross Off Active Task</h2>
                        <p>Ready to log a finished item? Enter its distinct database <b>Task ID</b> below to dispatch it straight into your historical archive boards.</p>
                    </div>

                    <form method="post">
                        <div class="form-group">
                            <label for="task_id">Target Task ID Number</label>
                            <input type="number" id="task_id" name="task_id" placeholder="e.g., 2" min="1" required>
                        </div>
                        
                        <button type="submit" class="btn-ledger-submit" style="background: linear-gradient(135deg, #10b981, #059669); box-shadow: 0 4px 12px rgba(16,185,129,0.25);">
                            <span>Settle and Mark As Completed</span>
                            <span class="btn-arrow">→</span>
                        </button>
                    </form>
                    
                    <div class="ledger-form-footer">
                        <a href="/tasks" class="btn-ledger-secondary">Cancel</a>
                    </div>
                </div>
            </main>
        </div>
    </body>
    </html>
    '''


@app.route('/view_completed_tasks', methods=['GET', 'POST'])
def view_completed_task():
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    tasks = view_completed_tasks(session['email'])
    
    if not tasks:
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Completed History | Scholar Desk</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body class="dashboard-body">
            <div class="workspace-layout">
                {get_tasks_sidebar()}
                <main class="workspace-main" style="display: flex; align-items: center; justify-content: center;">
                    <div class="empty-state-panel">
                        <span class="empty-state-icon">⏳</span>
                        <h2>No Completed Records Found</h2>
                        <p>You haven't checked any active items off your scheduler tracker list for this evaluation block cycle yet.</p>
                        <a href="/mark_task_completed" class="btn-ledger-primary" style="background: #10b981;">✅ Complete Your First Task</a>
                    </div>
                </main>
            </div>
        </body>
        </html>
        '''

    table_rows = ""
    for task in tasks:
        table_rows += f'''
        <tr>
            <td><span class="ledger-id-hash">#{task[0]}</span></td>
            <td class="task-resolved-line-text">{task[2]}</td>
            <td><span class="task-status-badge-complete">Finished Archive</span></td>
        </tr>
        '''

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Completed Archive | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="dashboard-body">
        <div class="workspace-layout">
            {get_tasks_sidebar()}
            
            <main class="workspace-main">
                <header class="main-header">
                    <div class="header-welcome">
                        <h1>🎉 Archive of Resolved Milestones</h1>
                        <p>Historical audit trails showcasing finished deliverables and past task operations</p>
                    </div>
                </header>

                <div class="table-card-wrapper">
                    <table class="enterprise-data-table">
                        <thead>
                            <tr>
                                <th style="width: 15%;">Task ID</th>
                                <th style="width: 65%;">Assignment Description</th>
                                <th style="width: 20%;">Operational State</th>
                            </tr>
                        </thead>
                        <tbody>
                            {table_rows}
                        </tbody>
                    </table>
                </div>

                <div style="margin-top: 25px;">
                    <a href="/tasks" class="btn-ledger-secondary">← Back to Tasks Control Hub</a>
                </div>
            </main>
        </div>
    </body>
    </html>
    '''


@app.route('/view_incomplete_tasks', methods=['GET', 'POST'])
def view_incomplete_task():
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    tasks = view_incomplete_tasks(session['email'])
    
    if not tasks:
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Pending Logs | Scholar Desk</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body class="dashboard-body">
            <div class="workspace-layout">
                {get_tasks_sidebar()}
                <main class="workspace-main" style="display: flex; align-items: center; justify-content: center;">
                    <div class="empty-state-panel">
                        <span class="empty-state-icon">☀️</span>
                        <h2>All Backlogs Cleared!</h2>
                        <p>Excellent performance! There are currently zero pending or delayed task objectives registered under this profile container.</p>
                        <a href="/tasks" class="btn-ledger-secondary" style="text-decoration: underline;">← Return to Main Console</a>
                    </div>
                </main>
            </div>
        </body>
        </html>
        '''

    table_rows = ""
    for task in tasks:
        table_rows += f'''
        <tr>
            <td><span class="ledger-id-hash">#{task[0]}</span></td>
            <td class="task-pending-heavy-text">{task[2]}</td>
            <td><span class="task-status-badge-pending">{task[4]}</span></td>
        </tr>
        '''

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pending Schedule | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="dashboard-body">
        <div class="workspace-layout">
            {get_tasks_sidebar()}
            
            <main class="workspace-main">
                <header class="main-header">
                    <div class="header-welcome">
                        <h1>⏳ Current Outstanding Task Backlogs</h1>
                        <p>Active items that are un-executed and require operational attention</p>
                    </div>
                </header>

                <div class="table-card-wrapper">
                    <table class="enterprise-data-table">
                        <thead>
                            <tr>
                                <th style="width: 15%;">Task ID</th>
                                <th style="width: 65%;">Assignment Description</th>
                                <th style="width: 20%;">Target Deadline</th>
                            </tr>
                        </thead>
                        <tbody>
                            {table_rows}
                        </tbody>
                    </table>
                </div>

                <div style="margin-top: 25px;">
                    <a href="/tasks" class="btn-ledger-secondary">← Back to Tasks Control Hub</a>
                </div>
            </main>
        </div>
    </body>
    </html>
    '''
@app.route('/finance', methods=['GET', 'POST'])
def finance():
    # Security Guardrail Check
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    # --- GET REQUEST: RENDER ENTERPRISE LEDGER MODULE ---
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Expense Tracker | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
        <script>
            // 🚀 THE PERSISTENCE GUARD: Force fresh server evaluation on back-arrow travel
            window.addEventListener('pageshow', function(event) {{
                if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {{
                    window.location.reload();
                }}
            }});
        </script>
    </head>
    <body class="dashboard-body">

        <div class="workspace-layout">
            
            <aside class="workspace-sidebar">
                <div class="sidebar-brand">
                    <span class="brand-avatar">🎓</span>
                    <div class="brand-text">
                        <h3>Scholar Desk</h3>
                        <span class="system-badge">v2.4 Core</span>
                    </div>
                </div>
                
                <nav class="sidebar-menu">
                    <a href="/dashboard" class="menu-item">
                        <span class="menu-icon">🎛️</span> Workspace Home
                    </a>
                    <a href="/notes" class="menu-item">
                        <span class="menu-icon">📝</span> Notes Engine
                    </a>
                    <a href="/tasks" class="menu-item">
                        <span class="menu-icon">📅</span> Task Manager
                    </a>
                    <a href="/tools" class="menu-item">
                        <span class="menu-icon">📊</span> Academic Tools
                    </a>
                    <a href="/finance" class="menu-item active">
                        <span class="menu-icon">💳</span> Expense Tracker
                    </a>
                    <a href="/chatbot" class="menu-item highlight-ai">
                        <span class="menu-icon">🤖</span> Saathi AI Assistant
                    </a>
                </nav>
                
                <div class="sidebar-footer">
                    <a href="/logout" class="btn-sidebar-logout">
                        <span>🔒 Terminate Session</span>
                    </a>
                </div>
            </aside>
            
            <main class="workspace-main">
                
                <header class="main-header">
                    <div class="header-welcome">
                        <h1>💳 Financial Expense Tracker</h1>
                        <p>Monitor student budgets, manage daily outlays, and audit your savings ledger</p>
                    </div>
                </header>
                
                <div class="notes-utility-bar">
                    <div class="utility-meta-info">
                        <span style="color: #e67e22;">💡 Premium Tip:</span> Log transactional data costs immediately to preserve accurate monthly allowance analytics.
                    </div>
                    <div style="font-size: 0.85rem; font-weight: 600; color: #475569;">
                        Account Profile: {session.get("name", "Scholar")}
                    </div>
                </div>
                
                <section class="dashboard-matrix-grid">
                    
                    <a href="/view_expense" class="notes-action-card">
                        <div class="notes-card-accent border-amber-gold"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-amber-gold">📊</div>
                            <div class="notes-card-content">
                                <h3>View Expense Logs</h3>
                                <p>Audit your comprehensive historic financial statements, evaluate line items, and trace overall spending curves.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                    <a href="/add_expense" class="notes-action-card">
                        <div class="notes-card-accent border-rose-mint"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-rose-mint">💸</div>
                            <div class="notes-card-content">
                                <h3>Add New Budget Expense</h3>
                                <p>Instantly document a fresh debit item, classify budget categories, and append specific cost points onto your active ledger.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                </section>
                
            </main>
            
        </div>
    </body>
    </html>
    '''
@app.route('/view_expense', methods=['GET', 'POST'])
def view_expense():
    # Security Token Check
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    expenses = view_expenses(session['email'])
    
    # Base Layout Sidebar Navigation Segment
    sidebar_html = f'''
    <aside class="workspace-sidebar">
        <div class="sidebar-brand">
            <span class="brand-avatar">🎓</span>
            <div class="brand-text">
                <h3>Scholar Desk</h3>
                <span class="system-badge">v2.4 Core</span>
            </div>
        </div>
        <nav class="sidebar-menu">
            <a href="/dashboard" class="menu-item"><span class="menu-icon">🎛️</span> Workspace Home</a>
            <a href="/notes" class="menu-item"><span class="menu-icon">📝</span> Notes Engine</a>
            <a href="/tasks" class="menu-item"><span class="menu-icon">📅</span> Task Manager</a>
            <a href="/tools" class="menu-item"><span class="menu-icon">📊</span> Academic Tools</a>
            <a href="/finance" class="menu-item active"><span class="menu-icon">💳</span> Expense Tracker</a>
            <a href="/chatbot" class="menu-item highlight-ai"><span class="menu-icon">🤖</span> Saathi AI Assistant</a>
        </nav>
        <div class="sidebar-footer">
            <a href="/logout" class="btn-sidebar-logout"><span>🔒 Terminate Session</span></a>
        </div>
    </aside>
    '''

    # SCENARIO A: NO DATABASE TRANSACTIONS FOUND
    if not expenses:
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Ledger Logs | Scholar Desk</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body class="dashboard-body">
            <div class="workspace-layout">
                {sidebar_html}
                <main class="workspace-main" style="display: flex; align-items: center; justify-content: center;">
                    <div class="empty-state-panel">
                        <span class="empty-state-icon">📉</span>
                        <h2>No Transactions Logged</h2>
                        <p>Your institutional ledger tracking sheet is completely vacant. No debit entries recorded for this account profile cycle yet.</p>
                        <a href="/add_expense" class="btn-ledger-primary">💸 Document First Outlay</a>
                    </div>
                </main>
            </div>
        </body>
        </html>
        '''

    # SCENARIO B: ACTIVE DATABASE TRANSACTIONS COMPILING
    table_rows = ""
    for expense in expenses:
        table_rows += f'''
        <tr>
            <td><span class="ledger-id-hash">#{expense[0]}</span></td>
            <td class="ledger-val-negative">₹{float(expense[2]):,.2f}</td>
            <td><span class="ledger-category-badge">{expense[3]}</span></td>
            <td class="ledger-date-stamp">{expense[4]}</td>
        </tr>
        '''

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ledger Statement | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="dashboard-body">
        <div class="workspace-layout">
            {sidebar_html}
            
            <main class="workspace-main">
                <header class="main-header">
                    <div class="header-welcome">
                        <h1>💳 Personal Expense Logs</h1>
                        <p>Real-time audit trailing, statement indexing, and categorical ledger tracking</p>
                    </div>
                    <div>
                        <a href="/add_expense" class="btn-ledger-primary">➕ Log Fresh Outlay</a>
                    </div>
                </header>

                <div class="table-card-wrapper">
                    <table class="enterprise-data-table">
                        <thead>
                            <tr>
                                <th>Transaction ID</th>
                                <th>Amount Incurred</th>
                                <th>Category Classification</th>
                                <th>Value Date</th>
                            </tr>
                        </thead>
                        <tbody>
                            {table_rows}
                        </tbody>
                    </table>
                </div>

                <div style="margin-top: 25px;">
                    <a href="/finance" class="btn-ledger-secondary">← Return to Finance Control Hub</a>
                </div>
            </main>
        </div>
    </body>
    </html>
    '''


# --- SHARED GLOBAL COMPONENTS FOR THE TOOLS ECOSYSTEM ---
def get_tools_sidebar():
    return f'''
    <aside class="workspace-sidebar">
        <div class="sidebar-brand">
            <span class="brand-avatar">🎓</span>
            <div class="brand-text">
                <h3>Scholar Desk</h3>
                <span class="system-badge">v2.4 Core</span>
            </div>
        </div>
        <nav class="sidebar-menu">
            <a href="/dashboard" class="menu-item"><span class="menu-icon">🎛️</span> Workspace Home</a>
            <a href="/notes" class="menu-item"><span class="menu-icon">📝</span> Notes Engine</a>
            <a href="/tasks" class="menu-item"><span class="menu-icon">📅</span> Task Manager</a>
            <a href="/tools" class="menu-item active"><span class="menu-icon">📊</span> Academic Tools</a>
            <a href="/finance" class="menu-item"><span class="menu-icon">💳</span> Expense Tracker</a>
            <a href="/chatbot" class="menu-item highlight-ai"><span class="menu-icon">🤖</span> Saathi AI Assistant</a>
        </nav>
        <div class="sidebar-footer">
            <a href="/logout" class="btn-sidebar-logout"><span>🔒 Terminate Session</span></a>
        </div>
    </aside>
    '''


@app.route('/pomodoro')
def web_pomodoro():
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pomodoro Focus Timer | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="dashboard-body">
        <div class="workspace-layout">
            {get_tools_sidebar()}
            
            <main class="workspace-main" style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
                <div class="tool-workspace-card text-center">
                    <span class="tool-main-icon text-orange-timer" style="background: #fff7ed; padding: 15px; border-radius: 50%;">🍅</span>
                    <h2 style="margin: 15px 0 5px 0;">Pomodoro Engine</h2>
                    <div class="pomodoro-status-badge" id="status-text">Focus Mode: Deep Concentration</div>
                    
                    <div class="pomodoro-timer-digits" id="timer">25:00</div>
                    
                    <div style="display: flex; gap: 15px; justify-content: center;">
                        <button id="start-btn" class="btn-tool-action bg-orange-timer" onclick="toggleTimer()">Start Focus</button>
                    </div>
                </div>
            </main>
        </div>

        <script>
            let timeLeft = 25 * 60; 
            let timerInterval = null;
            let isRunning = false;
            let isFocusMode = true;

            function updateDisplay() {{
                let minutes = Math.floor(timeLeft / 60);
                let seconds = timeLeft % 60;
                let displayMin = minutes < 10 ? "0" + minutes : minutes;
                let displaySec = seconds < 10 ? "0" + seconds : seconds;
                document.getElementById("timer").innerText = displayMin + ":" + displaySec;
            }}

            function toggleTimer() {{
                if (isRunning) {{
                    clearInterval(timerInterval);
                    document.getElementById("start-btn").innerText = "Resume";
                    isRunning = false;
                }} else {{
                    isRunning = true;
                    document.getElementById("start-btn").innerText = "Pause";
                    
                    timerInterval = setInterval(() => {{
                        if (timeLeft > 0) {{
                            timeLeft--;
                            updateDisplay();
                        }} else {{
                            clearInterval(timerInterval);
                            isRunning = false;
                            alert("⏰ Interval complete!");
                            
                            if (isFocusMode) {{
                                isFocusMode = false;
                                timeLeft = 5 * 60; 
                                document.getElementById("status-text").innerText = "☕ Break Mode: Rest & Recharge";
                                document.getElementById("status-text").style.background = "#e0f2fe";
                                document.getElementById("status-text").style.color = "#0369a1";
                                document.getElementById("start-btn").innerText = "Start Break";
                            }} else {{
                                isFocusMode = true;
                                timeLeft = 25 * 60; 
                                document.getElementById("status-text").innerText = "Focus Mode: Deep Concentration";
                                document.getElementById("status-text").style.background = "#ffe4e6";
                                document.getElementById("status-text").style.color = "#b91c1c";
                                document.getElementById("start-btn").innerText = "Start Focus";
                            }}
                            updateDisplay();
                        }}
                    }}, 1000);
                }}
            }}
        </script>
    </body>
    </html>
    '''


@app.route('/attendance_calc', methods=['GET', 'POST'])
def attendance_calc():
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    if request.method == 'POST':
        try:
            lec_attended = int(request.form['lec_attended'])
            total_lec = int(request.form['total_lec'])
            result = attendance_tracker(lec_attended, total_lec)
            
            return f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Auditor Result | Scholar Desk</title>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <body class="dashboard-body">
                <div class="workspace-layout">
                    {get_tools_sidebar()}
                    <main class="workspace-main" style="display: flex; align-items: center; justify-content: center;">
                        <div class="tool-workspace-card text-center" style="max-width: 460px;">
                            <span style="font-size: 3rem;">📊</span>
                            <h2 style="margin: 10px 0;">Analysis Complete</h2>
                            <div class="tool-result-panel border-emerald-auditor">
                                <p style="margin:0; font-size:1.05rem; color:#1e293b; line-height:1.6;">{result}</p>
                            </div>
                            <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 20px;">
                                <a href="/attendance_calc" class="btn-ledger-primary" style="background: #10b981;">Recalculate Metrics</a>
                                <a href="/tools" class="btn-ledger-secondary">← Back to Tools Hub</a>
                            </div>
                        </div>
                    </main>
                </div>
            </body>
            </html>
            '''
        except (ValueError, ZeroDivisionError):
            return f'''
            <!DOCTYPE html>
            <html>
            <head>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <body class="dashboard-body">
                <div class="workspace-layout">
                    {get_tools_sidebar()}
                    <main class="workspace-main" style="display: flex; align-items: center; justify-content: center;">
                        <div class="tool-workspace-card text-center" style="max-width: 440px; border-top: 4px solid #ef4444;">
                            <h3>❌ Execution Error</h3>
                            <p style="color:#64748b; font-size:0.95rem;">Please ensure input fields contain non-zero, valid matching entries.</p>
                            <a href="/attendance_calc" class="btn-ledger-primary" style="background:#ef4444; margin-top:10px;">Try Again</a>
                        </div>
                    </main>
                </div>
            </body>
            </html>
            '''

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Attendance Auditor | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="dashboard-body">
        <div class="workspace-layout">
            {get_tools_sidebar()}
            
            <main class="workspace-main" style="display: flex; align-items: center; justify-content: center;">
                <div class="tool-workspace-card">
                    <div class="ledger-form-header">
                        <h2>📝 Attendance Monitor</h2>
                        <p>Audit current classroom logs to preserve core minimum threshold eligibility margins.</p>
                    </div>
                    
                    <form method="post">
                        <div class="form-group">
                            <label for="lec_attended">Lectures Attended</label>
                            <input type="number" id="lec_attended" name="lec_attended" min="0" placeholder="e.g., 45" required>
                        </div>
                        <div class="form-group">
                            <label for="total_lec">Total Conducted Lectures</label>
                            <input type="number" id="total_lec" name="total_lec" min="1" placeholder="e.g., 60" required>
                        </div>
                        <button type="submit" class="btn-ledger-submit" style="background: linear-gradient(135deg, #10b981, #059669); box-shadow: 0 4px 12px rgba(16,185,129,0.2);">
                            Analyze Threshold Ratios
                        </button>
                    </form>
                    <div class="ledger-form-footer">
                        <a href="/tools" class="btn-ledger-secondary">← Cancel and Return</a>
                    </div>
                </div>
            </main>
        </div>
    </body>
    </html>
    '''


@app.route('/sgpa_calculator', methods=['GET', 'POST'])
def web_sgpa_calculator():
    if 'email' not in session or not session['email']:
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
                    <link rel="stylesheet" href="/static/style.css">
                </head>
                <body class="dashboard-body">
                    <div class="workspace-layout">
                        {get_tools_sidebar()}
                        <main class="workspace-main" style="display: flex; align-items: center; justify-content: center;">
                            <div class="tool-workspace-card text-center" style="max-width: 440px; border-top: 4px solid #ef4444;">
                                <h2 style="color: #ef4444; margin: 0 0 10px 0;">Calculation Blocked</h2>
                                <p style="color:#64748b; margin-bottom: 20px;">{error_message}</p>
                                <a href="/sgpa_calculator" class="btn-ledger-primary" style="background:#ef4444;">Modify Matrix Data</a>
                            </div>
                        </main>
                    </div>
                </body>
                </html>
                '''
                
            return f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>SGPA Matrix Evaluator | Scholar Desk</title>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <body class="dashboard-body">
                <div class="workspace-layout">
                    {get_tools_sidebar()}
                    <main class="workspace-main" style="display: flex; align-items: center; justify-content: center;">
                        <div class="tool-workspace-card text-center" style="max-width: 460px;">
                            <span>📈</span>
                            <h2 style="margin: 10px 0 5px 0;">Evaluation Complete</h2>
                            <p style="color: #64748b; font-size: 0.9rem; margin-bottom: 20px;">Your semester performance metric has been successfully calculated.</p>
                            
                            <div class="sgpa-display-panel">
                                <span style="font-size: 0.75rem; color: #0891b2; text-transform: uppercase; font-weight: 700; letter-spacing: 1px;">Term SGPA Score</span>
                                <h1 style="font-size: 3.8rem; color: #0891b2; margin: 5px 0; font-family: monospace; font-weight:700;">{sgpa_result:.2f}</h1>
                            </div>
                            
                            <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 20px;">
                                <a href="/sgpa_calculator" class="btn-ledger-primary" style="background: #06b6d4; box-shadow: 0 4px 12px rgba(6,182,212,0.2);">Compute New Term Matrix</a>
                                <a href="/tools" class="btn-ledger-secondary">← Back to Tools Hub</a>
                            </div>
                        </div>
                    </main>
                </div>
            </body>
            </html>
            '''
        except ValueError:
            return f'''
            <!DOCTYPE html>
            <html>
            <head><link rel="stylesheet" href="/static/style.css"></head>
            <body class="dashboard-body"><div class="workspace-layout">{get_tools_sidebar()}<main class="workspace-main" style="display: flex; align-items: center; justify-content: center;"><div class="tool-workspace-card text-center" style="max-width: 440px; border-top: 4px solid #ef4444;"><h3>❌ Structural Input Error</h3><p style="color:#64748b;">Verify score integers contain valid configurations and re-submit.</p><a href="/sgpa_calculator" class="btn-ledger-primary" style="background:#ef4444;">Return</a></div></main></div></body>
            </html>
            '''

    # Generate Dynamic Data Inputs Map Row Sets
    input_rows = ""
    for i in range(num_subjects):
        input_rows += f'''
        <div class="sgpa-input-row">
            <span class="course-row-index">Course Module {i+1:02d}</span>
            <div class="sgpa-fields-wrap">
                <input type="number" name="grades" min="1" max="10" placeholder="Grade (1-10)" required class="sgpa-mini-input">
                <input type="number" name="credits" min="1" max="8" placeholder="Credits" required class="sgpa-mini-input">
            </div>
        </div>
        '''
        
    # Compile Navigation Pills Matrix
    pill_links = []
    for n in range(3, 8):
        is_active = (n == num_subjects)
        bg = "#06b6d4" if is_active else "#ffffff"
        color = "#ffffff" if is_active else "#475569"
        pill_links.append(f'<a href="/sgpa_calculator?subjects={n}" class="sgpa-nav-pill" style="background: {bg}; color: {color}; border-color: {"#06b6d4" if is_active else "#e2e8f0"};">{n} Modules</a>')
    pills_html = " ".join(pill_links)

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>SGPA Calculator | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="dashboard-body">
        <div class="workspace-layout">
            {get_tools_sidebar()}
            
            <main class="workspace-main" style="display: flex; align-items: center; justify-content: center;">
                <div class="tool-workspace-card" style="max-width: 540px; width:100%;">
                    <div class="ledger-form-header">
                        <h2>📊 SGPA Academic Calculator</h2>
                        <p>Configure curriculum size options below to evaluate terminal grade indexes.</p>
                    </div>

                    <div class="sgpa-pills-container">
                        {pills_html}
                    </div>

                    <form method="post">
                        <div class="sgpa-table-header">
                            <span>Module Description</span>
                            <div class="header-label-group">
                                <span>Grade Point</span>
                                <span>Credits</span>
                            </div>
                        </div>

                        <div class="sgpa-fields-scroll-zone">
                            {input_rows}
                        </div>
                        
                        <button type="submit" class="btn-ledger-submit" style="background: linear-gradient(135deg, #06b6d4, #0891b2); box-shadow: 0 4px 12px rgba(6,182,212,0.2); margin-top: 20px;">
                            Evaluate Academic Performance Index
                        </button>
                    </form>
                    
                    <div class="ledger-form-footer">
                        <a href="/tools" class="btn-ledger-secondary">← Back to Tools Hub</a>
                    </div>
                </div>
            </main>
        </div>
    </body>
    </html>
    '''


@app.route('/web_resources')
def web_resource():
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))

    resources_ = resources() 
    
    cards_html = ""
    for category in resources_:
        topic_rows = ""
        for topic in resources_[category]:
            link_target = resources_[category][topic]
            topic_rows += f'''
            <div class="resource-item-row">
                <div class="resource-item-meta">
                    <span class="resource-topic-tag">Topic Block</span>
                    <h4>{topic}</h4>
                </div>
                <a href="{link_target}" target="_blank" class="btn-resource-launch">Launch Asset 🔗</a>
            </div>
            '''
            
        cards_html += f'''
        <div class="resource-folder-card">
            <div class="resource-folder-header">
                <span class="folder-icon">📁</span>
                <h3>{category}</h3>
            </div>
            <div class="resource-folder-contents">
                {topic_rows}
            </div>
        </div>
        '''

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reference Library | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body class="dashboard-body">
        <div class="workspace-layout">
            {get_tools_sidebar()}
            
            <main class="workspace-main">
                <header class="main-header">
                    <div class="header-welcome">
                        <h1>📚 Academic Reference Library</h1>
                        <p>Access curated class syllabi records, external source links, and open textbook data vaults</p>
                    </div>
                </header>

                <div class="resource-library-masonry">
                    {cards_html}
                </div>
            </main>
        </div>
    </body>
    </html>
    '''
@app.route('/tools')
def tools():
    # Security Guardrail Check
    if 'email' not in session or not session['email']:
        return redirect(url_for('login_user'))
        
    # --- GET REQUEST: RENDER UTILITY MATRIX HUB ---
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Academic Tools Hub | Scholar Desk</title>
        <link rel="stylesheet" href="/static/style.css">
        <script>
            // 🚀 THE PERSISTENCE GUARD: Force fresh server evaluation on back-arrow travel
            window.addEventListener('pageshow', function(event) {{
                if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {{
                    window.location.reload();
                }}
            }});
        </script>
    </head>
    <body class="dashboard-body">

        <div class="workspace-layout">
            
            <aside class="workspace-sidebar">
                <div class="sidebar-brand">
                    <span class="brand-avatar">🎓</span>
                    <div class="brand-text">
                        <h3>Scholar Desk</h3>
                        <span class="system-badge">v2.4 Core</span>
                    </div>
                </div>
                
                <nav class="sidebar-menu">
                    <a href="/dashboard" class="menu-item">
                        <span class="menu-icon">🎛️</span> Workspace Home
                    </a>
                    <a href="/notes" class="menu-item">
                        <span class="menu-icon">📝</span> Notes Engine
                    </a>
                    <a href="/tasks" class="menu-item">
                        <span class="menu-icon">📅</span> Task Manager
                    </a>
                    <a href="/tools" class="menu-item active">
                        <span class="menu-icon">📊</span> Academic Tools
                    </a>
                    <a href="/finance" class="menu-item">
                        <span class="menu-icon">💳</span> Expense Tracker
                    </a>
                    <a href="/chatbot" class="menu-item highlight-ai">
                        <span class="menu-icon">🤖</span> Saathi AI Assistant
                    </a>
                </nav>
                
                <div class="sidebar-footer">
                    <a href="/logout" class="btn-sidebar-logout">
                        <span>🔒 Terminate Session</span>
                    </a>
                </div>
            </aside>
            
            <main class="workspace-main">
                
                <header class="main-header">
                    <div class="header-welcome">
                        <h1>📊 Academic Tools & Utilities</h1>
                        <p>Boost productivity, calculate credit thresholds, and navigate institutional repositories</p>
                    </div>
                </header>
                
                <div class="notes-utility-bar">
                    <div class="utility-meta-info">
                        Engine Environment Deployment Mode: <span style="color: #38bdf8; font-weight: 600;">Active Platform Grid</span>
                    </div>
                    <div style="font-size: 0.85rem; color: #64748b; font-weight: 500;">
                        Operator ID: {session.get("name", "Scholar")}
                    </div>
                </div>
                
                <section class="dashboard-matrix-grid">
                    
                    <a href="/sgpa_calculator" class="notes-action-card">
                        <div class="notes-card-accent border-cyan"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-cyan">📈</div>
                            <div class="notes-card-content">
                                <h3>SGPA Calculator</h3>
                                <p>Compute semester grade performance indicators dynamically by processing multi-weighted course credit profiles.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                    <a href="/pomodoro" class="notes-action-card">
                        <div class="notes-card-accent border-orange-timer"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-orange-timer">⏱️</div>
                            <div class="notes-card-content">
                                <h3>Pomodoro Focus Timer</h3>
                                <p>Lock into high-efficiency learning bursts with structural sensory intervals, tracking work blocks flawlessly.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                    <a href="/attendance_calc" class="notes-action-card">
                        <div class="notes-card-accent border-emerald-auditor"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-emerald-auditor">📝</div>
                            <div class="notes-card-content">
                                <h3>Attendance Auditor</h3>
                                <p>Audit course presence indices dynamically to preserve your safety margins above standard university criteria.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                    <a href="/web_resources" class="notes-action-card">
                        <div class="notes-card-accent border-crimson"></div>
                        <div class="notes-card-body">
                            <div class="notes-icon-wrapper text-crimson">📚</div>
                            <div class="notes-card-content">
                                <h3>Digital Resources Library</h3>
                                <p>Browse curated institutional documentation sheets, external academic links, reference keys, and file databases.</p>
                            </div>
                        </div>
                        <span class="notes-action-arrow">→</span>
                    </a>

                </section>
                
            </main>
            
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
     app.run(debug=True)