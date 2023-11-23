from flask_app import app
from flask import render_template , request, redirect
from flask_app.models.burger import Burger



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/burger/<int:id>")
def display_burger(id):
    data = {'id': id}
    burger = Burger.get_by_id(data)
    return render_template("display_burger.html" , burger = burger)


@app.route("/burgers" , methods = ["POST"])
def create_burger():
    data = request.form
    Burger.create(data)
    return redirect("/burger")

@app.route("/burger")
def display_all():
    all_burgers = Burger.get_all()
    return render_template("display_all.html" , burgers = all_burgers)


@app.route("/burger/<int:id>/delete")
def delete(id):
    data = {'id': id}
    Burger.delete(data)
    return redirect('/burger')

@app.route("/burger/<int:id>/update")
def go_to_update_page(id):
    data = {'id': id}
    burger = Burger.get_by_id(data)
    return render_template("update_page.html" , burger_to_update = burger)

@app.route("/update" , methods = ['POST'])
def update_burger():
    data = request.form
    Burger.update(data)
    return redirect('/burger')