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
    positions = Position.query.filter_by(accepting_applications=True).all()

    if current_user.is_anonymous:
        return render_template("index.html", title="WSU Research Portal", positions=positions)
    elif current_user.user_type == "Professor":
        return render_template("/Professor Pages/professor_index.html", title="WSU Research Portal", positions=positions)
    elif current_user.user_type == "Student":
        positions_to_show = []
        student_languages = current_user.get_languages().all()
        student_interests = current_user.get_interests().all()
        for position in positions: #Not the most efficient manner of ensuring both language and interest
                    for language in student_languages:
                        if ((position not in positions_to_show) and (language in position.languages)):
                            for interest in student_interests:
                                if ((position not in positions_to_show) and (interest in position.research_fields)):
                                    positions_to_show.append(position)

        #Take first three positons from list
        if (len(positions_to_show) >= 3):
            positions = [positions_to_show[0], positions_to_show[1], positions_to_show[2]]
        elif (len(positions_to_show) == 2):
            positions = [positions_to_show[0], positions_to_show[1]]
        elif (len(positions_to_show) == 1):
            positions = [positions_to_show[0]]
        else: #If they don't have any matches, just show all positions
             positions = positions
             return render_template("index.html", title="WSU Research Portal", positions=positions)
        return render_template("index.html", title="WSU Research Portal", positions=positions_to_show)        
    
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
    
@routes.route("/<application_id>/application_deletion", methods=['GET', 'POST'])
def application_deletion(application_id):
    application = Application.query.filter_by(id=application_id).first()
    if request.method == "POST":
        flash(f"Application has been withdrawn")
        application.status = "Withdrawn"
        db.session.add(application)
        db.session.commit()
        return redirect(url_for("positions.positions"))
    
    #Get Request
    return render_template("Application Pages/application_deletion.html", title="WSU Research Portal")


# @routes.route('/display_profile', methods = ['GET'])
# @login_required
# def display_profile():
#     return render_template('display_profile.html', title='Display Profile', student = current_user)