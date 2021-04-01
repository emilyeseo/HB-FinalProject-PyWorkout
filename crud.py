"""CRUD OPERATIONS."""

import model

def create_user(firstname,lastname,email,password):
    """Create and return a new user."""

    user = User(firstname = firstname,
                lastname = lastname,
                email=email,
                password = password)

    db.session.add(user)
    db.session.commit()

    return user

def create_exercise(exercise_name, main_muscle_group, type_of_exercise, difficulty, equipment, instructions, exercise_img1, exercise_img2, reps):
    """Create and return a exercise."""

    exercise = Exercise(exercise_name = exercise_name,
                        main_muscle_group = main_muscle_group,
                        type_of_exercise = type_of_exercise,
                        difficulty = difficulty,
                        equipment = equipment,
                        instructions = instructions,
                        exercise_img1 = exercise_img1,
                        exercise_img2 = exercise_img2,
                        reps = reps)

    db.session.add(exercise)
    db.session.commit()

    return exercise

def create_workout_plan(user_id, first_exercise, second_exercise, third_exercise, fourth_exercise):
    """Create and return a workout plan."""
    
    workout_plan = Workout_plan(user_id = user_id,
                                first_exercise = first_exercise,
                                second_exercise = second_exercise,
                                third_exercise = third_exercise,
                                fourth_exercise = fourth_exercise)
    
    db.session.add(workout_plan)
    db.session.commit()

    return workout_plan

if __name__ == '__main__':
    from server import app
    connect_to_db(app)