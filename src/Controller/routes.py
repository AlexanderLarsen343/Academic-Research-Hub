from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request, get_flashed_messages
from config import Config
from flask_login import current_user, login_required

from src import db
from src.Model.models import Position, Application, Student
from src.Controller.forms import PositionForm, ApplicationForm, StudentHomeSortForm

routes = Blueprint("routes", __name__)

@routes.route("/", methods=['GET', 'POST'])
def index():
    positions = Position.query.all()
    form = StudentHomeSortForm()

    positions_to_show = []

    if request.method == "POST":
        sort_by = form.sort_by.data
        # Research positions
        if sort_by == "0":
            positions_to_show = positions
        elif sort_by == "1":
            student_research_interests = current_user.get_interests().all()
            print(student_research_interests)
            for position in positions:
                for interest in student_research_interests:
                    if (position not in positions_to_show) and (interest in position.research_fields):
                        positions_to_show.append(position)

        # languages
        elif sort_by == "2":
            student_languages = current_user.get_languages().all()
            for position in positions:
                for language in student_languages:
                    if (position not in positions_to_show) and (language in position.languages):
                        positions_to_show.append(position)

    else:
        positions_to_show = positions

    if current_user.is_anonymous:
        return render_template("index.html", title="WSU Research Portal", positions=positions_to_show)
    elif current_user.user_type == "Professor":
        return render_template("/Professor Pages/professor_index.html", title="WSU Research Portal", positions=positions_to_show)
    elif current_user.user_type == "Student":
        return render_template("index.html", title="WSU Research Portal", positions=positions_to_show, form=form)        
    
@routes.route("/my_applications", methods=['GET'])
def my_applications():
        if current_user.is_anonymous:
            return render_template("errors/403.html")
        elif current_user.user_type == "Professor":
            return render_template("errors/403.html")
        elif current_user.user_type == "Student":
            pass
        
        applications = current_user.applications
        applied_positions = []
        apps = {}
        for application in applications: #Get a list of positions
            apps[application] = Position.query.filter_by(id=application.position_id).first()
            # applied_positions.append()
        return render_template("Application Pages/my_applications.html", title="My Applications", applications = apps, positions = applied_positions)        
    



# @routes.route('/display_profile', methods = ['GET'])
# @login_required
# def display_profile():
#     return render_template('display_profile.html', title='Display Profile', student = current_user)