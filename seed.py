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
    title, overview, poster_path = (movie['title'],
                                    movie['overview'],
                                    movie['poster_path'])
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

    db_movie = crud.create_movie(title,
                                 overview,
                                 release_date,
                                 poster_path)
    movies_in_db.append(db_movie)