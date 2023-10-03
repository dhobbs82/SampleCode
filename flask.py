"""
Derrick Hobbs
4/25/2023
SDEV300
This is a Flask program to create a website
"""
import datetime
from flask import Flask, render_template

lab_6 = Flask(__name__)

# Define the home page route
@lab_6.route('/')
def home():
    return render_template('home.html')

# Define the about page route
@lab_6.route('/about')
def about():
    return render_template('about.html')

# Define the contact page route
@lab_6.route('/contact')
def contact():
    return render_template('contact.html')

# Define a function to get the current date and time
def get_current_datetime():
    return datetime.datetime.now()

# Define a custom filter to format the date and time
@lab_6.template_filter()
def format_datetime(value, format='%Y-%m-%d %H:%M:%S'):
    return value.strftime(format)

# Define the context processor to make the current datetime available to all templates
@lab_6.context_processor
def inject_datetime():
    return {'now': get_current_datetime()}

if __name__ == '__main__':
    lab_6.run(debug=False)
