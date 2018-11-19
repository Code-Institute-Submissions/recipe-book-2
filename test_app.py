import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe-book'
app.config["MONGO_URI"] = 'mongodb://admin:Jagger198!@ds121182.mlab.com:21182/recipe-book'

mongo = PyMongo(app)


"""
Routing for Index.html
"""

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/recipes')
def recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())


@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    this_recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe=this_recipe)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    this_recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=this_recipe,
    categories=mongo.db.categories.find().sort("category",1),cuisines=mongo.db.cuisines.find().sort("cuisine",1),
    difficulty=mongo.db.levels.find().sort("level",1),serves=mongo.db.serves.find().sort("level",1),main_ing=mongo.db.main_ing.find().sort("level",1))

    
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html",
    categories=mongo.db.categories.find().sort("category",1),cuisines=mongo.db.cuisines.find().sort("cuisine",1),
    difficulty=mongo.db.levels.find().sort("level",1),serves=mongo.db.serves.find().sort("level",1),main_ing=mongo.db.main_ing.find().sort("level",1))


"""
Data Functions
"""

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'name':request.form.get['name'],
        'image':request.form.get['image'],
        'description':request.form.get['description'],
        'category': request.form.get['category'],
        'cuisine': request.form.get['cuisine'],
        'prep_time':request.form.get['prep_time'],
        'cooking_time':request.form.get['cooking_time'],
        'main_ing':request.form.get['main_ing'],
        'serves':request.form.get['serves'],
        'rating':request.form.get['rating'],
        'date_added':request.form.get['date_added'],
        'added_by':request.form.get['added_by']
    })
    return redirect(url_for('view_recipe'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)