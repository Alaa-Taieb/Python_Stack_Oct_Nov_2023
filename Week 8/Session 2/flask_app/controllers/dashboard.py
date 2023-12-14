from flask_app import app
from flask import render_template , session , redirect , request , url_for
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect(url_for('index'))
    # Get user id from session
    # logged_user_id = session['user_id']
    # Get the user with that id
    logged_user = User.get_by_id({'id': session['user_id']})

    recipes = Recipe.get_all()
    print(recipes)

    return render_template('dashboard.html' , user = logged_user , recipes = recipes)

@app.route('/recipe/create')
def create_recipe():
    if not 'user_id' in session:
        return redirect(url_for('index'))
    
    return render_template("create_recipe.html")


@app.route('/recipe/add' , methods = ['POST'])
def add_recipe():
    if not 'user_id' in session:
        return redirect(url_for('index'))
    data = request.form
    Recipe.create(data)
    return redirect(url_for('dashboard'))

@app.route('/recipe/<int:id>/edit')
def edit_recipe(id):

    recipe = Recipe.get_by_id({'id': id})
    return render_template("edit_recipe.html" , recipe = recipe)

@app.route('/recipe/update' , methods = ['POST'])
def update_recipe():
    data = request.form
    Recipe.edit(data)
    return redirect(url_for('dashboard'))


@app.route('/recipe/<int:id>/delete')
def delete_recipe(id):
    Recipe.delete({'id': id})
    return redirect(url_for('dashboard'))


@app.route('/recipe/<int:id>')
def view_recipe(id):
    recipe = Recipe.get_by_id({'id': id})
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template("view_recipe.html" , recipe = recipe , user = logged_user)