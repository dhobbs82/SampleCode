"""
Derrick Hobbs
5/2/2023
SDEV300
This is a Flask program to add functionality to a website
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
import re
import datetime


lab_7 = Flask(__name__)

# Set a secret key to enable sessions
lab_7.secret_key = 'supersecretkey'

# Define the home page route
@lab_7.route('/')
def home():
    return render_template('home.html')

# Define the about page route
@lab_7.route('/about')
def about():
    return render_template('about.html')

# Define the contact page route
@lab_7.route('/contact')
def contact():
    return render_template('contact.html')

# Define the registration page route
@lab_7.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the user input from the registration form
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Ensure the password meets the complexity requirements
        password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{12,}$"
        if not re.match(password_regex, password):
            flash('Password should be at least 12 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character.')
            return redirect(url_for('register'))

        # Register the user by saving their username and password to the session
        session['username'] = username
        session['password'] = password
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Define the login page route
@lab_7.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the user input from the login form
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists and the password matches
        if 'username' in session and 'password' in session and session['username'] == username and session['password'] == password:
            # Log the user in by saving their username to the session
            session['logged_in'] = True
            flash('Logged in successfully!')
            return redirect(url_for('secure'))
        else:
            flash('Invalid username or password. Please try again.')
            return redirect(url_for('login'))
    return render_template('login.html')

# Define a function to get the current date and time
def get_current_datetime():
    return datetime.datetime.now()

# Define a custom filter to format the date and time
@lab_7.template_filter()
def format_datetime(value, format='%Y-%m-%d %H:%M:%S'):
    return value.strftime(format)

# Define the context processor to make the current datetime available to all templates
@lab_7.context_processor
def inject_datetime():
    return {'now': get_current_datetime()}

# Define the secure page route
@lab_7.route('/secure')
def secure():
    if 'logged_in' in session and session['logged_in']:
        return render_template('secure.html')
    else:
        flash('You need to log in first.')
        return redirect(url_for('login'))

if __name__ == '__main__':
    lab_7.run(debug=False)
