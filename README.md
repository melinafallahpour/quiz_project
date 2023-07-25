## CS50 Test
This is a final project for HarvardX CS50's Web Programming with Python and JavaScript. CS50 Test is a quiz app. This Web App has been built for CS50 learners who want to test their skills after they take this course. Users are able to create their tests, take them, view the score, and check all of their results.

Video Demo :: https://youtu.be/gR3meOVyF4s


### Distinctiveness and Complexity
  - `Ajax` is used for exchanging data with a web server.
  - `django-crispy-forms` controls the rendering behavior of Django forms.
  - `UserCreationForm` is used for registering a new user.
  - This is a Quiz app.
  - As things have been mentioned above, this app is sufficiently distinct from the other projects in CS50. 
  - This app utilizes Django on the back-end and JavaScript on the front-end.
  - This app is mobile-responsive.

### Files and Directories
This project contains two apps(`users` and `quiz`) and a `static` directory:
  * `quiz_proj` - the actual python package for the project.
    * `settings.py` - settings and configuration for the project.
    * `urls.py` - the URL declarations for the project.
  * `users` - the user authentication app
    * `templates` - contains logout and register templates.
      * `templates/registration` - contains login templates.
        * `login.html` - a template for login form.
        * `register.html` - a template for register form.
        * `logout.html` - a template for logout.
    * `urls.py` - defines a path to register
    * `views.py` - defines login and register views.
  * `quiz` - the main app for the project.
    * `templates/quiz` - contains all templates of the quiz app.
      * `base.html` - all other templates extend this base template.
      * `main.html` - a template that shows all quizzes.
      * `question.html` - a template that shows  questions of the quiz which the user has selected.
      * `result.html` - a template that shows the user results.
    * `admin.py` - imports and registers models.
    * `forms.py` - defines `QuizForm` class with Quiz model and `QuestionForm` class with Question model.
    * `models.py` - defines four models. `Topic`(category of quiz), `Quiz`()
    * `urls.py` - defines paths for the quiz app.
    * `views.py` - defines views for the quiz app.
  * `static` - contains the stylesheet and JavaScript files.
      * `styles.css` - the stylesheet.
      * `favicon.ico` - a favicon for the web page.
      * `functions.js` - handles alert messages.
      * `main.js` - handles creating a quiz and adding questions.
      * `question.js` - handles showing questions, timer, sending answer, and showing score.
  * `requirements.txt` - python packages that need to be installed to run this app.

### Running the app

1. Download all packages from requirements.txt.
```
pip install -r requirements.txt
```
2. Make migrations
```
python manage.py makemigrations
python manage.py migrate
```
3. Create a superuser
```
python manage.py createsuperuser
```
4. Run the django server to start the app.
```
python manage.py runserver
```
