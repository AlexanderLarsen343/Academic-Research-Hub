from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request, get_flashed_messages
from config import Config
from flask_login import current_user, login_required

from src import db
from src.Model.models import Position, Application
from src.Controller.forms import PositionForm, ApplicationForm

routes = Blueprint("routes", __name__)

@routes.route("/", methods=['GET'])
def index():
    positions=Position.query.all()
    if current_user.is_anonymous:
        return render_template("index.html", title="WSU Research Portal", positions=positions)
    elif current_user.user_type == "Professor":
        return render_template("/Professor Pages/professor_index.html", title="WSU Research Portal", positions=positions)
    elif current_user.user_type == "Student":
        return render_template("index.html", title="WSU Research Portal", positions=positions)        

# @routes.route('/display_profile', methods = ['GET'])
# @login_required
# def display_profile():
#     return render_template('display_profile.html', title='Display Profile', student = current_user)