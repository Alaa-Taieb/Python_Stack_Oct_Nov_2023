# Importing Classes Methods from flask module
from flask import Flask , render_template, request , redirect , session


# Constructing an instance of the Flask Class
app = Flask(__name__)

# Setting the Secret_key for the entire application (used internally by the server to hash/encrypt data in sessions)
app.secret_key = "sdjufhiesjdnfe"

# Root Route
@app.route('/')
def index():
    # Returning the home.html page
    return render_template("home.html")

# Route that the form is submitting data to | form in home.html
@app.route('/submit_info' , methods = ['POST'])
def submit_route():
    # Pulling the form data (Data sent by the form) and saving them in 'data' variable
    data = request.form

    # Save name from 'data' variable in session using the key 'name'
    session['name'] = data['name']
    # Save email from 'data' variable in session using the key 'email'
    session['email'] = data['email']

    # Redirecting back to the '/display' route
    return redirect("/display")

# Route to display data stored in session
@app.route("/display")
def display():
    # Initiating two variable with "None" as values
    name = "None"
    email = "None"
    # Checking if the key 'name' exists in session
    if 'name' in session:
        # Override the default value 'None' by the new Value from the session
        name = session['name']
    
    # Checking if the key 'email' exists in session
    if 'email' in session:
        # Override the default value 'None' by the new Value from the session
        email = session['email']

    # Returning the "display_info.html" page with name and email as parameters
    return render_template("display_info.html", name = name , email = email)

# Route to clear session storage
@app.route('/clear')
def clear():
    # Clearing the session storage AKA deleting all the information saved in session
    session.clear()
    return redirect('/')

# Checking if this file was ran directly AKA => "Python server.py"
if __name__ == "__main__":
    # Starting the server
    app.run(debug=True)