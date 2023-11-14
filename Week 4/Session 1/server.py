from flask import Flask , render_template


app = Flask(__name__)

@app.route("/")
def root_route():
    return render_template("home.html")

@app.route("/anotherRoute")
def another_route():
    return "This is a new Route!"

@app.route("/greet/<string:name>")
def greet_route(name):

    pet_list = ["Dog" , "Cat" , "Fish", "Dragon"]

    return render_template("greet.html", username = name , pets = pet_list)



if __name__ == "__main__":
    app.run(debug=True)