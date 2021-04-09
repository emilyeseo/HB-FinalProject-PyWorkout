from flask import (Flask, render_template, render_template, flash, session, request, redirect)
from jinja2 import StrictUndefined
from model import connect_to_db
from random import choice
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

@app.route('/login')
def login():
    email = request.args.get('email')
    password = request.args.get('password')

    user = crud.get_user_by_email(email)

    if user: 
        session['logged_in_user_id'] = user.user_id
        
        print('***********')
        print(session)

        return redirect('/create_workout_plan_form')
    else: 
        return redirect ('/')

@app.route('/all_exercises')
def all_exercises():
    """View all Exercises."""

    exercises = crud.get_exercises()

    return render_template('all_exercises.html', exercises = exercises)

@app.route('/create_workout_plan_form')
def create_workout_plan_form():

    return render_template('create_workout_plan_form.html')


@app.route('/create_workout_plan', methods = ['POST'])
def create_workout_plan():
    """Create a workout plan of user's choice"""

    if 'logged_in_user_id' in session:
        workout_plan= crud.create_workout_plan(session['logged_in_user_id'])
        main_muscle_group = request.form.get("main_muscle_group")
        
    
        if main_muscle_group == 'back':
            exercises = crud.get_exercises_by_main_group('Back') #list of back exercise objects
            
            for i in range(4):
                random_back_exercise = choice(exercises) #using random library choice
                print('*************')
                print(random_back_exercise)

                random_back_workout = crud.create_workout_plan_exercise(workout_plan.workout_plan_id, random_back_exercise.exercise_id)

            
        # elif main_muscle_group == 'legs':
        #     workout_for_the_day = crud.create_workout_plan_exercise()
        
        # elif main_muscle_group == 'glute':
        #     workout_for_the_day = crud.create_workout_plan_exercise()
        
        # elif main_muscle_group == 'abs':
        #     workout_for_the_day = crud.create_workout_plan_exercise()
    
    return redirect('/')




# @app.route("/my_workout", method = ["GET"])    

#     return redirect('/myworkout')



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', port="5001", debug=True)