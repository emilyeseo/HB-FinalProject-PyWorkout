"""CRUD OPERATIONS."""

import model

def create_user(email,password):
    """Create and return a new user."""

    user = User(email=email, password = password)

    db.session.add(user)
    db.session.commit()

    return user

def create_exercise(exercise_name, equipment, difficulty, instruction, reps, main_muscle_group, type_of_exercise)
    """create and return a exercise"""

    exercise = Exercise(exercise_name = exercise_name,
                        equipment = equipment,
                        difficulty = difficulty,
                        instruction = instruction,
                        reps = reps,
                        main_muscle_group = main_muscle_group,
                        type_of_exercise = type_of_exercise)

    db.session.add(exercise)
    db.session.commit()

    return exercise

def create_workout_plan(exercise, exierercise):
    """Create and return a workout plan"""
    
    workout_plan = Workout_plan(first_exercise = first_exercise
                                second_exercise = second_exercise
                                third_exercise = third_exercise
                                fourth_exercise = fourth_exercise)
    
    db.session.add(workout_plan)
    db.session.commit()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)