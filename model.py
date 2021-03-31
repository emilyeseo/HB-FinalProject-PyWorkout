from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

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
    """Workout plan."""
    ___tablename__ = 'workout_plans'

    workout_plan_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer)
    first_exercise = db.Column(db.Integer)
    second_exercise = db.Column(db.Integer)
    third_exercise = db.Column(db.Integer)
    fourth_exercise = db.Column(db.Integer)

    def __repr__(self):
        return f'<Workout_plan workout_plan_id= {self.workout_plan_id} workout_plan = {self.workout_plan}>'

class Exercise(db.Model):
    """Workout plan."""
    ___tablename__ = 'exercises'

    exercise_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    exercise_name = db.Column(db.String(15))
    equipment = db.Column(db.String(15))
    intensity = db.Column(db.Integer)
    description = db.Column(db.Text)
    reps = db.Column(db.Integer)
    main_muscle_group = db.Column(db.String(30))
    type_of_exercise = db.Column(db.String(15))

    def __repr__(self):
        return f'<Workout_plan exercise= {self.exercise_id} exercise_name = {self.exercise_name}>'

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
    # query it executes.

    connect_to_db(app)
