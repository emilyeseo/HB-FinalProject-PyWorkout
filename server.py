from flask import (Flask, render_template, render_template, flash, session)
from jinja2 import StrictUndefined
from model import connect_to_db
import crud





app = Flask(__name__)
app.secret_key = "SecretKey"
app.jinja_env.undefined = StrictUndefined

#to check the homepage is working 
@app.route('/')
def homepage():
    """View homepage"""
    return render_template('homepage.html')

# @app.route('/about')
# def index():
#     """take me to about page. project details"""
#     return render_template('about.html')

@app.route('/exercises')
def all_exercises(): 
    exercises = crud.get_exercises()

    return render_template('all_exercises.html', exercises = exercises)

@app.route('/create_workout_plan')
def create_workout_plan():

    return render_template('create_workout_plan_form.html')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)