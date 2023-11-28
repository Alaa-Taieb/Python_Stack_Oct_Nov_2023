from flask_app import app
from flask_app.models.User import User
from flask import render_template, request, redirect, session


@app.route('/')
def login_register():
    # This route will return the page containing both the Login and Register Forms
    return render_template('login_registration.html')

@app.route('/register' , methods=['POST'])
def register():
    data = request.form
    # Check if this data respects certain rules
    if User.validate_register(data):
        # Valid data
        # Save the user in the database
        User.create(data)
        pass
    
    # If it does respect those rules => Save the user in database
    # If it doesn't respect those rules => Display Error Messages
    
    return redirect('/')

@app.route('/login' , methods = ['POST'])
def login():
    data = request.form
    print(data)
    if User.validate_login(data):
        session['logged_user_email'] = data['email']
        print(session['logged_user_email'])
        return redirect('/dashboard')
    
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    logged_user = User.get_by_email({'email': session['logged_user_email']})
    # This route will return the dashboard page after the user successfully logs in.
    return render_template('dashboard.html' , logged_user = logged_user)