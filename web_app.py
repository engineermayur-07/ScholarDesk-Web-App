from flask import Flask, render_template, request, redirect, url_for
from database_setup import init_db
# Import your newly organized features!
from features.auth import login  

app = Flask(__name__)

# Initialize the database when the web server starts up
init_db()

# 1. The Home Page Route
@app.route('/')
def home():
    # This renders a visual layout instead of a terminal print string
    return "<h1>Welcome to the Student Toolkit Web Edition!</h1><a href='/login'>Click here to login</a>"

# 2. The Login Page Route
@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        # Grab what the student typed into the web form fields
        email = request.form['email']
        password = request.form['password']
        
        # Call your existing backend logic function!
        # (Assuming your modular function returns True/False for success)
        if login():
            return f"✅ Success! Welcome back {email}."
        else:
            return "❌ Invalid credentials. Try again."
            
    # If they are just browsing to the page (GET request), show a simple form
    return '''
        <form method="post">
            Email: <input type="text" name="email"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    # Start the web server on your local machine
    app.run(debug=True)