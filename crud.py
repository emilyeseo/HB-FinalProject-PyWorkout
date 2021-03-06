"""CRUD OPERATIONS."""
from model import db, User, Exercise, Workout_plan_exercise, Workout_plan, connect_to_db
from random import choice, randint
from datetime import date


def create_user(firstname, lastname, email, password):
    """Create and return a new user."""

    user = User(firstname=firstname,
                lastname=lastname,
                email=email,
                password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):
    """Return a user """

    return User.query.filter_by(email=email).first()


def get_user_by_user_id(user_id):

    return User.query.filter_by(user_id=user_id).first()


def create_exercise(exercise_name, main_muscle_group, type_of_exercise, difficulty, equipment, instructions, exercise_img1, exercise_img2, reps):
    """Create and return a exercise."""

    exercise = Exercise(exercise_name=exercise_name,
                        main_muscle_group=main_muscle_group,
                        type_of_exercise=type_of_exercise,
                        difficulty=difficulty,
                        equipment=equipment,
                        instructions=instructions,
                        exercise_img1=exercise_img1,
                        exercise_img2=exercise_img2,
                        reps=reps)

    db.session.add(exercise)
    db.session.commit()

    return exercise


def get_exercises():
    """Display and return all exercises"""

    return Exercise.query.all()


def get_exercise_by_id(exercise_id):
    """Return a exercise by exercise id"""

    return Exercise.query.get(exercise_id)


def create_workout_plan(user_id, date_created=date.today()):
    """Create and return a workout plan."""

    workout_plan = Workout_plan(user_id=user_id, date_created=date_created)

    db.session.add(workout_plan)
    db.session.commit()

    return workout_plan


def create_workout_plan_exercise(workout_plan_id, exercise_id):
    """Create and return a workout plan exercise."""

    workout_plan_exercise = Workout_plan_exercise(workout_plan_id=workout_plan_id,
                                                  exercise_id=exercise_id)

    db.session.add(workout_plan_exercise)
    db.session.commit()

    return workout_plan_exercise


def get_exercises_by_main_group(main_muscle_group):
    """Display and return exercises by main muscle group"""

    return Exercise.query.filter_by(main_muscle_group=main_muscle_group).all()


def get_workout_plan_exercises_by_workout_plan_id(workout_plan_id):
    """Display and return exercises by workout plan id"""

    # from database, we are using workout plan exercise class to find the exercise by using workout plan id
    return Workout_plan_exercise.query.filter_by(workout_plan_id=workout_plan_id).all()


def get_workout_plan_by_user_id(user_id):
    """Display and return workout plan by user id"""

    return Workout_plan.query.filter_by(user_id=user_id).all()


def get_number_of_workouts_by_user_id(user_id):

    return Workout_plan.query.filter_by(user_id=user_id).count()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
