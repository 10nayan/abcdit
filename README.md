# Basic feature app using Flask and deployed in Heroku
<img src="screenshots/Screenshot (72).png">
<img src="screenshots/Screenshot (73).png">
<img src="screenshots/Screenshot (74).png">
<img src="screenshots/Screenshot (75).png">
<img src="screenshots/Screenshot (76).png">
<img src="screenshots/Screenshot (77).png">
<img src="screenshots/Screenshot (78).png">
<img src="screenshots/Screenshot (79).png">
<img src="screenshots/Screenshot (80).png">

## Introduction
This website is built with flask which is a python micro-framework for web development.
You can check out this website clicking here, https://abcdit.herokuapp.com
This application has feature of basic calender, unit converter, advanced mathematics calculator, weather app and chat app.
Any user can signup or register an account to this app and later login  or logout to their account, the user data is stored in postgreSQL database hosted in Heroku app.
User password is stored after hashing so there is no security concern left behind, user other data such as first name or email is used in different features.
This website is styled by using bootstrap CSS framework and all frontend logic is developed using vanilla javascript.
## Files in the project
- **application.py**: This is the main app file and contains the logic of all features and the Flask-SocketIO backend for the app.
- **models.py**: Contains Flask-SQLAlchemy models used for user registration and login in application.py
- **create.py**: optional file only required if repo is to be cloned. *See 'Usage' section below.*
- **Procfile**: file required for Heroku
- **requirements.txt**: list of Python packages installed (also required for Heroku)
- **templates/**: folder with all HTML files
- **static/**: for with all JS scripts and CSS files
## Usage
### Clone/Modify app
1. Modify application.py to replace the secret key *(i.e. os.environ.get('SECRET_KEY'))* with a secret key of your choice and the database link *(i.e. os.environ.get('DATABASE_URL'))* with the link to your own database.

    The two lines to be edited in application.py are shown below:
```python
app.secret_key=os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
```
2. Edit *create.py* to once again replace *os.environ.get('DATABASE_URL')* with the link to your database.

3. Run *create.py* from the terminal to create the table to hold user credentials.
    
```console
C:\Users\private>python create.py
```
## Areas of improvement
1. Style of this website can be improved to another level, I have written very less CSS, most of the time I used bootstrap template. Anyone can add custom CSS to improve the styling.
2. Form validation in server side can be improved, as I have already used bootstrap client side form validation I didn't use Flask-WTForms to server side validation.
## API used
1.https://ipinfo.io for getting users geolocation for weather feature.

2.https://api.weatherapi.com for live weather forecast at users location.
