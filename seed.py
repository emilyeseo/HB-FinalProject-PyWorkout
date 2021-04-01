"""Script to seed database."""

import os
import json
from random import choice, randint
# from datetime import datetime

import crud
import model
# import server

os.system('dropdb exercises')
os.system('createdb exercises')

model.connect_to_db(server.app)
model.db.create_all()

# Load exercise data from JSON file
with open('data/exercises.json') as f:
    exercise_data = json.loads(f.read())
    
exercise_in_db = []
for exercise in exercise_data:
    exercise_name, main_muscle_group, type_of_exercise, difficulty, 
    equipment, instructions,exercise_img1, exercise_img2, reps = (exercise['exercise_name'],
                                                                exercise['main_muscle_group'],
                                                                exercise['type_of_exercise'],
                                                                exercise['difficulty'],
                                                                exercise['equipment'],
                                                                exercise['instructions'],
                                                                exercise['exercise_img1'],
                                                                exercise['exercise_img2'],
                                                                exercise['reps'])   

    db_exercise = crud.create_exercise(exercise_name,
                                        main_muscle_group,
                                        type_of_exercise,
                                        difficulty,
                                        equipment,
                                        instructions,
                                        exercise_img1,
                                        exercise_img2,
                                        reps)
    movies_in_db.append(db_movie)