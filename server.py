from flask import (Flask, render_template, render_template,
                   flash, session, request, redirect)
from jinja2 import StrictUndefined
from model import connect_to_db
from random import choice
import crud
from send_sms import client


app = Flask(__name__)
app.secret_key = "SecretKey"
app.jinja_env.undefined = StrictUndefined

# to check the homepage is working
@app.route('/')
def homepage():
    """View homepage"""
    return render_template('homepage.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    # new message: email is correct and password is wrong

    if user and password == user.password:

        session['logged_in_user_id'] = user.user_id
        # flash('successfully logged in')
        return ('successfully logged in')

    elif user and password != user.password:
        # flash('User information could not be found')
        return ('Wrong password. Try again.')


@app.route('/logout')
def logout():

    session.pop('logged_in_user_id', None)
    flash("Successfully logged out")

    return redirect('/')


@app.route('/register_user')
def register_user():
    """View register user account page"""

    return render_template('create_account_form.html')


@app.route('/register_user', methods=['POST'])
def create_an_account():
    """ Create a new user. """

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        # flash('Sorry. This login email already exists. Please try a different email address to register, or login to your exisiting account.')
        return ('Sorry. This login email already exists. Please try a different email address to register, or login to your exisiting account.')
    else:
        user = crud.create_user(firstname, lastname, email, password)
        return ('Account succesfully created. Please proceed and log in to your account.')


@app.route('/all_exercises')
def all_exercises():
    """View all Exercises."""

    exercises = crud.get_exercises()

    return render_template('all_exercises.html', exercises=exercises)


@app.route('/exercise/<exercise_id>')
def exercise_detail(exercise_id):
    """Show details on a particular exercise"""

    exercise = crud.get_exercise_by_id(exercise_id)

    return render_template('exercise_detail.html', exercise=exercise)


@app.route('/create_workout_plan_form')
def create_workout_plan_form():

    if 'logged_in_user_id' in session:

        return render_template('create_workout_plan_form.html')

    flash('Please log in or create an account')

    return redirect('/')


@app.route('/create_workout_plan', methods=['POST'])
def create_workout_plan():
    """Create a workout plan of user's choice"""

    if 'logged_in_user_id' in session:
        workout_plan = crud.create_workout_plan(session['logged_in_user_id'])
        main_muscle_group = request.form.get("main_muscle_group")

        # created workout plan exercise and added to our data base
        if main_muscle_group == 'back':
            exercises = crud.get_exercises_by_main_group(
                'Back')  # list of back exercise objects
            for i in range(1, 4):
                # using random library choice
                random_back_exercise = choice(exercises)
                random_workout_plan = crud.create_workout_plan_exercise(
                    workout_plan.workout_plan_id, random_back_exercise.exercise_id)

        elif main_muscle_group == 'legs':
            exercises = crud.get_exercises_by_main_group('Legs')
            for i in range(1, 4):
                random_leg_exercise = choice(exercises)
                random_workout_plan = crud.create_workout_plan_exercise(
                    workout_plan.workout_plan_id, random_leg_exercise.exercise_id)

        elif main_muscle_group == 'glutes':
            exercises = crud.get_exercises_by_main_group('Glutes')
            for i in range(1, 4):
                random_glute_exercise = choice(exercises)
                random_workout_plan = crud.create_workout_plan_exercise(
                    workout_plan.workout_plan_id, random_glute_exercise.exercise_id)

        elif main_muscle_group == 'abs':
            exercises = crud.get_exercises_by_main_group('Abs')
            for i in range(1, 4):
                random_abs_exercise = choice(exercises)
                random_workout_plan = crud.create_workout_plan_exercise(
                    workout_plan.workout_plan_id, random_abs_exercise.exercise_id)

        user_list_of_random_exercises = crud.get_workout_plan_exercises_by_workout_plan_id(
            random_workout_plan.workout_plan_id)

        return render_template("display_workout_plan.html", user_list_of_random_exercises=user_list_of_random_exercises)
    else:
        return redirect("/")


@app.route('/send-sms', methods=['POST'])
def send_text_message():
    """Send workout plan to user's cell phone"""

    # import pdb
    # pdb.set_trace()

    exercise_plan = request.form.getlist('names[]')

    exercise_names = "\n".join(exercise_plan)

    client.messages.create(
        body=exercise_names, from_='+12143937243', to='+12146095612')
    # workout_plan_id will already be stored in this route

    # things to do
    ## use .join
    # make the route connected to the button.
    # make sure button can determine which "workout_plan_id" is calling.

    return "success"


@app.route('/your_account')
def display_workout_plan():
    """Return and display workout plan by user id"""

    if 'logged_in_user_id' in session:
        workout_plans_by_user_id = crud.get_workout_plan_by_user_id(
            session['logged_in_user_id'])
        workout_history = []

        for user_workout_plan in workout_plans_by_user_id:
            exercise_list = crud.get_workout_plan_exercises_by_workout_plan_id(
                user_workout_plan.workout_plan_id)

            workout_dict = {}
            workout_dict['date'] = user_workout_plan.date_created
            workout_dict['main_muscle'] = exercise_list[1].exercises.main_muscle_group
            workout_dict['exercises'] = exercise_list

            workout_history.append(workout_dict)

            # workout_history.append(exercise_list)

        user = crud.get_user_by_user_id(session['logged_in_user_id'])

        firstname = user.firstname
        lastname = user.lastname
        email = user.email

        return render_template('my_account.html',
                               workout_history=workout_history,
                               firstname=firstname,
                               lastname=lastname,
                               email=email)
    else:
        return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', port="5000", debug=True)
