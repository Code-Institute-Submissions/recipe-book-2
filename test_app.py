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


@app.route('/recipes', methods=["POST"])
def recipes():
    if request.method == "POST":
        searchTerm = request.form['search']
        return redirect(url_for('search', searchTerm=searchTerm))
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
    categories=mongo.db.categories.find().sort("category",1),cuisines=mongo.db.cuisines.find().sort("cuisine",1), ratings=mongo.db.ratings.find().sort("rating",1),
    difficulty=mongo.db.levels.find().sort("level",1),serving=mongo.db.serves.find().sort("level",1),main_ings=mongo.db.main_ing.find().sort("level",1))

    
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html",
    categories=mongo.db.categories.find().sort("category",1),cuisines=mongo.db.cuisines.find().sort("cuisine",1), ratings=mongo.db.ratings.find().sort("rating",1),
    difficulty=mongo.db.levels.find().sort("level",1),serving=mongo.db.serves.find().sort("level",1),main_ings=mongo.db.main_ing.find().sort("level",1))


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
        'name':request.form['name'],
        'image':request.form['image'],
        'description':request.form['description'],
        'category': request.form['category'],
        'cuisine': request.form['cuisine'],
        'prep_time':request.form['prep_time'],
        'cooking_time':request.form['cooking_time'],
        'main_ing':request.form['main_ing'],
        'serves':request.form['serves'],
        'rating':request.form['rating'],
        'level':request.form['level'],
        'date_added':request.form['date_added'],
        'added_by':request.form['added_by'],
        'ingredient_1':request.form['ingredient_1'],
        'ingredient_2':request.form['ingredient_2'],
        'ingredient_3':request.form['ingredient_3'],
        'ingredient_4':request.form['ingredient_4'],
        'ingredient_5':request.form['ingredient_5'],
        'ingredient_6':request.form['ingredient_6'],
        'ingredient_7':request.form['ingredient_7'],
        'ingredient_8':request.form['ingredient_8'],
        'ingredient_9':request.form['ingredient_9'],
        'ingredient_10':request.form['ingredient_10'],
        'method_1':request.form['method_1'],
        'method_2':request.form['method_2'],
        'method_3':request.form['method_3'],
        'method_4':request.form['method_4'],
        'method_5':request.form['method_5'],
        'method_6':request.form['method_6'],
        'method_7':request.form['method_7'],
        'method_8':request.form['method_8'],
        'method_9':request.form['method_9'],
        'method_10':request.form['method_10']
        
    })
    return redirect(url_for('recipes'))

@app.route('/insert_category_edit', methods=['POST'])
def insert_category_edit():
    category = mongo.db.categories
    category.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))

@app.route('/insert_cuisine_edit', methods=['POST'])
def insert_cuisine_edit():
    cuisine = mongo.db.cuisines
    cuisine.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))
    
@app.route('/insert_main_ing_edit', methods=['POST'])
def insert_main_ing_edit():
    main_ing = mongo.db.main_ing
    main_ing.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))

@app.route('/insert_category_add', methods=['POST'])
def insert_category_add():
    category = mongo.db.categories
    category.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))

@app.route('/insert_cuisine_add', methods=['POST'])
def insert_cuisine_add():
    cuisine = mongo.db.cuisines
    cuisine.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))

@app.route('/insert_main_ing_add', methods=['POST'])
def insert_main_ing_add():
    main_ing = mongo.db.main_ing
    main_ing.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)