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


@app.route('/login', methods = ['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user and password == user.password: 
        
        session['logged_in_user_id'] = user.user_id
        flash('successfully logged in')

        return redirect('/create_workout_plan_form')
    else: 
        print(user)
        print('********')
        flash('User information could not be found')
        return redirect ('/')


@app.route('/logout')
def logout():

    session.pop('logged_in_user_id', None)
    flash("Successfully logged out")
        
    return redirect('/')


@app.route('/register_user')
def register_user():
    """View register user account page"""

    return render_template('create_account_form.html')


@app.route('/register_user', methods = ['POST'])
def create_an_account():
    """ Create a new user. """
    
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user: 
        flash('Sorry. This login email already exists. Please try a different email address to register, or login to your exisiting account.')
        return redirect('/register_user')
    else:
        crud.create_user(firstname,lastname,email,password)
        flash('Account succesfully created. Please proceed and log in to your account.')

    return redirect('/')


@app.route('/all_exercises')
def all_exercises():
    """View all Exercises."""

    exercises = crud.get_exercises()

    return render_template('all_exercises.html', exercises = exercises)

@app.route('/exercise/<exercise_id>')
def exercise_detail(exercise_id):
    """Show details on a particular exercise"""

    exercise = crud.get_exercise_by_id(exercise_id)

    return render_template('exercise_detail.html', exercise = exercise)


@app.route('/create_workout_plan_form')
def create_workout_plan_form():

    if 'logged_in_user_id' in session:

        return render_template('create_workout_plan_form.html')
        
    flash('Please log in or create an account')   

    return redirect('/')


@app.route('/create_workout_plan', methods = ['POST'])
def create_workout_plan():
    """Create a workout plan of user's choice"""

    if 'logged_in_user_id' in session:
        workout_plan= crud.create_workout_plan(session['logged_in_user_id'])
        main_muscle_group = request.form.get("main_muscle_group")
        
        #created workout plan exercise and added to our data base
        if main_muscle_group == 'back':
            exercises = crud.get_exercises_by_main_group('Back') #list of back exercise objects
            
            for i in range(4):
                random_back_exercise = choice(exercises) #using random library choice
                random_back_workout = crud.create_workout_plan_exercise(workout_plan.workout_plan_id, random_back_exercise.exercise_id)
        
        elif main_muscle_group == 'legs':
            exercises = crud.get_exercises_by_main_group('Legs')
            for i in range(4): 
                random_leg_exercise = choice(exercises)
                random_leg_workout = crud.create_workout_plan_exercise(workout_plan.workout_plan_id, random_leg_exercise.exercise_id)

        elif main_muscle_group == 'glutes':
            exercises = crud.get_exercises_by_main_group('Glutes')
            for i in range(4): 
                random_glute_exercise = choice(exercises)
                random_glute_workout = crud.create_workout_plan_exercise(workout_plan.workout_plan_id, random_glute_exercise.exercise_id)
        
        elif main_muscle_group == 'abs':
            exercises = crud.get_exercises_by_main_group('Abs')
            for i in range(4): 
                random_abs_exercise = choice(exercises)
                random_abs_workout = crud.create_workout_plan_exercise(workout_plan.workout_plan_id, random_abs_exercise.exercise_id)    


        #create this crud function
        #list of four workout plan exercises objects (Workout_plan_exercise class) for the workout_plan_id
        user_list_of_random_exercises = crud.get_workout_plan_exercises_by_workout_plan_id(workout_plan.workout_plan_id)
        # print("==================")
        # # print(user_list_of_random_exercises[0]) #first object in our list
        # # print(user_list_of_random_exercises[0].exercises) #view exercises relationship
        # print(user_list_of_random_exercises[0].exercises.exercise_name)
        # print(user_list_of_random_exercises[0].exercises.type_of_exercise)
        # print(user_list_of_random_exercises[0].exercises.difficulty)
        # print(user_list_of_random_exercises[0].exercises.instructions)
        # print("==================")
    
    return render_template("display_workout_plan.html", user_list_of_random_exercises = user_list_of_random_exercises)




# @app.route("/my_workout", method = ["GET"])    

#     return redirect('/myworkout')



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', port="5000", debug=True)