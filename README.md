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

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

![database_schema](https://user-images.githubusercontent.com/28737216/48314730-5f994b80-e5c5-11e8-9d8f-1f68f6d6f451.png)

### Wireframes / Mockups:

Still to be inserted

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea


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

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

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
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from https://myfoodbook.com.au/recipes/categories
