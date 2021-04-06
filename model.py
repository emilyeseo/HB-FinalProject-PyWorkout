from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Users"""
    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String, 
                    unique = True)
    password = db.Column(db.String)    

    def __repr__(self):
        return f'<User user_id= {self.user_id} email = {self.email}>'

class Workout_plan(db.Model):
    """A Workout plan. A user can have 0 to many workout plans."""
    __tablename__ = 'workout_plans'

    workout_plan_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer,
                            db.ForeignKey('users.user_id'))

    users = db.relationship('User', backref='workout_plans')

    def __repr__(self):
        return f'<Workout_plan workout_plan_id = {self.workout_plan_id} user_id = {self.user_id}>'

class Workout_plan_exercise(db.Model):
    """A randomized Workout plan. """

    __tablename__ = 'workout_plan_exercises'

    workout_plan_exercise_id = db.Column(db.Integer,
                                        autoincrement = True,
                                        primary_key=True)
    workout_plan_id = db.Column(db.Integer,
                                db.ForeignKey('workout_plans.workout_plan_id'))
    exercise_id = db.Column(db.Integer,
                            db.ForeignKey('exercises.exercise_id'))

    def __repr__(self):
        return f'<Workout_plan_exercise workout_plan_exercise_id = {self.workout_plan_exercise_id}>'

    
    exercises = db.relationship ('Exercise', backref = 'workout_plan_exercises') 
    workout_plans  = db.relationship ('Workout_plan', backref = 'workout_plan_exercises')


class Exercise(db.Model):
    """Exercises.  Information about each exercise."""
    __tablename__ = 'exercises'

    exercise_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
                           
    exercise_name = db.Column(db.String)
    main_muscle_group = db.Column(db.String) 
    type_of_exercise = db.Column(db.String)
    difficulty = db.Column(db.String)
    equipment = db.Column(db.String)
    instructions = db.Column(db.String)
    exercise_img1 = db.Column(db.String)
    exercise_img2 = db.Column(db.String) 
    reps = db.Column(db.Integer)

    def __repr__(self):
        return f'<Exercise exercise_id= {self.exercise_id} exercise_name = {self.exercise_name}>'




    


def connect_to_db(flask_app, db_uri='postgresql:///exercises', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.mm

    connect_to_db(app)
