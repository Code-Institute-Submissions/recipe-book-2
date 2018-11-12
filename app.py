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
    categories=mongo.db.categories.find().sort("category",1), recipes=mongo.db.recipes.find(), cuisines=mongo.db.cuisines.find().sort("cuisine",1))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)