# Data Centric Milestone Project

## Basic Recipe Book

This is a basic online recipe book for various users.  Features include viewing, editing and adding recipes - additional features may be added in the future.  The full application can be viewed <a href="https://basic-recipe-book.herokuapp.com/" target="_blank" >here</a>.
 
## UX

This website is for a range of people, from those who are looking for quick and easy recipes due to a busy lifestyle, those who have a bit more time to browse and contribute, to those who simply love cooking and want to share their ideas and favourite recipes with the rest of the world!

### User Stories:

![recipe_user_story_1](https://user-images.githubusercontent.com/28737216/48661085-90193380-ea64-11e8-9caa-e2a98376aab3.PNG)

![recipe_user_story_2](https://user-images.githubusercontent.com/28737216/48661185-1c782600-ea66-11e8-89fe-3492de14ab1d.PNG)

![recipe_user_story_3](https://user-images.githubusercontent.com/28737216/48661190-27cb5180-ea66-11e8-8213-1e6a4fe3c82e.PNG)

![recipe_user_story_4](https://user-images.githubusercontent.com/28737216/48661158-880dc380-ea65-11e8-9d88-5ccceab2c4dd.PNG)

### Data Schema:

The following shows the basic set-up of the MongoDB database, which is hosted on the cloud-based Mlab DaaS:

![mlab](https://user-images.githubusercontent.com/28737216/48978923-61760b00-f0ab-11e8-8a58-1016b8bc4819.png)

The following collections are used for the drop-down/select menus throughout:

| ![categories](https://user-images.githubusercontent.com/28737216/48978364-8ca82c80-f0a2-11e8-9c7e-7336369d0efd.png) | ![cuisines](https://user-images.githubusercontent.com/28737216/48978368-9d58a280-f0a2-11e8-9ea1-2b2759481d1c.png) | ![main_ing](https://user-images.githubusercontent.com/28737216/48978395-fa545880-f0a2-11e8-8c8a-eed2f5d0d7a1.png)
|:---:|:---:|:---:|
| categories | cuisines | main_ing |

The following collections would ideally be implemented through nested Arrays, but to simply the data structure and avoid the need for inserting and editing into a nested data, this approach was adopted:

| ![levels](https://user-images.githubusercontent.com/28737216/48978901-fcbab080-f0aa-11e8-87ae-9929298e5e71.png) | ![ratings](https://user-images.githubusercontent.com/28737216/48978905-0a703600-f0ab-11e8-88f2-7b7574d27b85.png) | ![serves](https://user-images.githubusercontent.com/28737216/48978909-14923480-f0ab-11e8-9408-2b1948c72eb0.png)
|:---:|:---:|:---:|
| levels | ratings | serves |

The following collection is the main category within the database that holds all the Recipe records/documents:

![recipes](https://user-images.githubusercontent.com/28737216/48978327-08ee4000-f0a2-11e8-9107-60f417a5da23.png)

Nested data had initially been used, but this was proving diffcult to manipulate through standard CRUD operations (particularly creating and updating)  Previous set-up was as follows:

~~~~
"ingredients": [
        {
            "ing_name": "white wine vinegar",
            "measure": "3 tbsp"
        },
        {
            "ing_name": "large free range eggs",
            "measure": "x 4"
        },
        {
            "ing_name": "toasting muffins",
            "measure": "x 2"
        },
        {
            "ing_name": "batch hot hollandaise sauce",
            "measure": "x 1"
        },
        {
            "ing_name": "Parma ham (or Serrano or Bayonne)",
            "measure": "4 slices"
        }
    ],  
~~~~

### Wireframes / Mockups:

The following are the initial mockups, based on the Materialize *Parallax* template that was used:

#### Index / Landing Page:

![recipe_main](https://user-images.githubusercontent.com/28737216/48676633-5417c880-eb61-11e8-9e9d-f11b0035ef79.png)

#### Recipes Page:

![recipes_cards](https://user-images.githubusercontent.com/28737216/48676660-b1ac1500-eb61-11e8-8573-a557f7a01067.png)

#### View Recipe Page <recipe_id>:

![view_recipe](https://user-images.githubusercontent.com/28737216/48676664-be306d80-eb61-11e8-9cbe-6a98c486bb2b.png)

#### Edit Recipe Page <recipe_id>:

![edit_recipe](https://user-images.githubusercontent.com/28737216/48676667-c688a880-eb61-11e8-84c9-c65730569f31.png)

#### Add/Insert Recipe Page:

![add_recipe](https://user-images.githubusercontent.com/28737216/48676670-cdafb680-eb61-11e8-978f-b9be04cd847d.png)

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features

The main features of the application are the following:

- View full list of all recipes contained in the database
- Search Function to allow users to search recipes containing specfic words (e.g. chicken)
  - Funciton to allow users to Reset the search function and return them to the full list of recipes
- Users are currently allowed to edit recipes (in full implementation this would require user registration / login)
- Users are currently allowed to add recipes (in full implementation this would require user registration / login)
  - When adding new recipes / editing recipes users can also add New Categories / Cuisine Types / Main Ingredients

### Features Left to Implement

Ideally, User Registration would be used on such an application for the CRUD operations within the database.  This would require Account Authentication / Login functionaility also

Another issue noted is the fact that if a user wishes to add a New Category / Cuisine Type / Main Ingredient, then they must do so before they begin adding/editing current attributes of a recipe (as the page will refresh and any new/amended data will not be committed to the database)

## Technologies used

Technologies used in this project include:

* Materialize: Materializecss was used for a basic HTML templates and styling.
* HTML5/CSS: Used for the layout and styling of the application.
* Python 3.4.3: The back end functionality of the application was written entirely in python 3.0.
  Was originally running on Python 2, following code was executed to upgrade:
  ~~~~
  jagger81:~/workspace (master) $ sudo mv /usr/bin/python /usr/bin/python2
  jagger81:~/workspace (master) $ sudo ln -s /usr/bin/python3 /usr/bin/python
  jagger81:~/workspace (master) $ python --version
  Python 3.4.3
  ~~~~
* Flask Microframework: Flask was used to extend pythons functionality to the frond end.
* Balsamiq: Used to create the below wireframes.
* Cloud9 IDE used as development environment workspace
* The project uses **JQuery** to simplify DOM manipulation.


## Testing

Mainly manual testing used throughout - for routing and checking if data is properly rendered in the correct template and format, "test_app.py" was used, whereby on satisfactory completion, the clean functional code would then be transferred to the "app.py" file

Basic testing included:

- DB Connection
- Editing Recipes
- Adding Recipes
- Adding new Categories / Main Ingredients / Cuisine Type
- Rendering data / images

Many GitHub commits will contain the prefix `TESTING`

Pep 8 was used to assist with cleaning the data - indentation, whitespaces, non-spaces, 2 lines expected

http://pep8online.com/

## Deployment

Full project is deployed on Heroku at this <a href="https://basic-recipe-book.herokuapp.com/" target="_blank" >location</a>.

**_Method of Deployment:_**
1. New Heroku Python App created, entitled "basic-recipe-book"
2. Launched Heroku in the C9 environment
3. Git repo was already initiated, so ran **```git remote add heroku https://git.heroku.com/basic-recipe-book.git```** to allow a push to the Heroku server
4. To prevent a "push fail", the requirements.txt was updated using the following command **```sudo pip3 freeze --local >requirements.txt```** to keep track of dependancies
5. A Procfile was created using the following code: **```echo web: python run.py > Procfile```** to inform Heroku which file to run for initiating the app
6. To esnure that Web Processes are running the following command line was run in C9: **```heroku ps:scale web=1```**
7. Config Vars set as follows: **IP=0.0.0.0 and PORT=5000**
8. Lastly, dynos were restarted in Heroku app
9. Code added, committed and pushed to both GitHub and Heroku
10. App launched successfully

In addition, you can clone or download the code from this GitHub repository.


## Credits

### Content
- The details of the recipes was taken from https://www.bbcgoodfood.com

### Media
- The photos used for the recipes were sourced from https://www.bbcgoodfood.com
- Logo was created using https://logojoy.com

### Acknowledgements

- I received inspiration for this project from https://myfoodbook.com.au and https://www.bbcgoodfood.com
- I would also like to acknowledge and thank Heather Olcot (@Heather) who was of grateful assistance on getting the Search function to  work.  Without her help, I may have never figured it out!
