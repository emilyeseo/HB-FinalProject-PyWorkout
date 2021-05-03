from unittest import TestCase
from server import app
from flask import session
import crud
from model import User, Exercise, Workout_plan, Workout_plan_exercise
import os
import json
