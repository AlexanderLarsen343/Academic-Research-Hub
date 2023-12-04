from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request, get_flashed_messages
from config import Config
from flask_login import current_user, login_required

from src import db
from src.Model.models import Position, Application, Student
from src.Controller.forms import PositionForm, ApplicationForm, StudentHomeSortForm, EditStudentForm, EditProfessorForm

routes = Blueprint("routes", __name__)

@routes.route("/", methods=['GET', 'POST'])
def index():
    positions = Position.query.filter_by(accepting_applications=True).all()

    # print("\n")
    # print(current_user.user_type, current_user.firstname)
    # print("\n")


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


@routes.route('/display_profile', methods = ['GET'])
@login_required
def display_profile():
    if current_user.user_type == "Student":
        return render_template('Student Pages/display_student_profile.html', title='Display Profile', student = current_user)
    elif current_user.user_type == "Professor":
        return render_template('Professor Pages/display_professor_profile.html', title='Display Profile', professor = current_user)


@routes.route('/edit_profile', methods = ['GET', 'POST'])
@login_required
def edit_profile():
    if current_user.user_type == "Student":
        eform = EditStudentForm()
        if request.method == 'POST':
            if eform.validate_on_submit():
                current_user.email = eform.email.data
                current_user.set_password(eform.password.data)
                current_user.firstname = eform.firstname.data
                current_user.lastname = eform.lastname.data
                current_user.wsu_id = eform.wsu_id.data
                current_user.major = eform.major.data
                current_user.gpa = eform.gpa.data
                current_user.graduationDate = eform.graduationDate.data
                current_user.interests = eform.interests.data
                current_user.languages = eform.programming_langs.data
                current_user.experience = eform.experience.data
                current_user.phone = eform.phone.data
                db.session.add(current_user)
                db.session.commit()
                flash("Your changes have been saved")
                return redirect(url_for('routes.display_profile'))
        elif request.method == 'GET':
            eform.email.data = current_user.email
            eform.firstname.data = current_user.firstname
            eform.lastname.data = current_user.lastname
            eform.wsu_id.data = current_user.wsu_id
            eform.major.data = current_user.major
            eform.gpa.data = current_user.gpa
            eform.graduationDate.data = current_user.graduationDate
            eform.interests.data = current_user.interests
            eform.programming_langs.data = current_user.languages
            eform.experience.data = current_user.experience
            eform.phone.data = current_user.phone
        return render_template('Student Pages/edit_student_profile.html', title = 'Edit Profile', form = eform)
    elif current_user.user_type == "Professor":
        eform = EditProfessorForm()
        if request.method == 'POST':
            if eform.validate_on_submit():
                current_user.email = eform.email.data
                current_user.set_password(eform.password.data)
                current_user.firstname = eform.firstname.data
                current_user.lastname = eform.lastname.data
                current_user.wsu_id = eform.wsu_id.data
                current_user.title = eform.title.data
                current_user.phone = eform.phone.data
                db.session.add(current_user)
                db.session.commit()
                flash("Your changes have been saved")
                return redirect(url_for('routes.display_profile'))                
        elif request.method == 'GET':
            eform.firstname.data = current_user.firstname
            eform.lastname.data = current_user.lastname
            eform.email.data = current_user.email
            eform.wsu_id.data = current_user.wsu_id
            eform.title.data = current_user.title
            eform.phone.data = current_user.phone
        return render_template('Professor Pages/edit_professor_profile.html', title = 'Edit Profile', form = eform)           
        