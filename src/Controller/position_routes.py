from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request, get_flashed_messages
from flask_login import current_user, login_required

from src import db
from src.Model.models import Position, Application, Student
from src.Controller.forms import PositionForm, ApplicationForm

routes = Blueprint("positions", __name__)

@routes.route("/positions", methods=["GET"])
def positions():
    positions = None

    if current_user.user_type == "Professor":
        positions = Position.query.filter_by(professor_id=current_user.id).all()
    elif current_user.user_type == "Student":
        positions = Position.query.all()

    return render_template("positions.html", positions=positions)

@routes.route('/positions/new', methods = ['GET', 'POST'])
@login_required
def create_position():
    if current_user.user_type != "Professor":
        return render_template("errors/403.html"), 403
    
    pform = PositionForm()
    if pform.validate_on_submit():
        newPosition = Position(
            title=pform.title.data, 
            description=pform.description.data,
            start_date = pform.start_date.data,
            end_date = pform.end_date.data,
            work_load= pform.workload.data,
            languages = pform.languages.data,
            research_fields = pform.research_fields.data,
            candidates = 0,
            applications = [],
            professor_id = current_user.id
        )
        db.session.add(newPosition)
        db.session.commit()
        flash(f'"{newPosition.title}" has been created.')
        return redirect(url_for('positions.positions_by_id', position_id=newPosition.id))
    else:
        for field, errors in pform.errors.items():
            for error in errors:
                print(f"Field: {field}, Error: {error}")
    return render_template('createPosition.html', form = pform)

@routes.route("/positions/<position_id>")
def positions_by_id(position_id):
    position = Position.query.filter_by(id=position_id).first()

    if position is None:
        return render_template("errors/404.html"), 404

    if (current_user.user_type != "Student") and (current_user.id != position.professor_id):
        return render_template("errors/403.html"), 403
    
    return render_template("position.html", position=position)

@routes.route("/positions/<position_id>/apply", methods=["GET", "POST"])
def positions_by_id_apply(position_id):
    if current_user.user_type != "Student":
        return render_template("errors/403.html"), 403
    
    position = Position.query.filter_by(id=position_id).first()
    form = ApplicationForm()
    if form.validate_on_submit():
        application = Application(
            status="In Review",
            statement=form.statement.data,
            reference=form.reference.data,
            reference_email=form.reference_email.data,
            position_id=position.id,
            student_id=current_user.id
        )
        position.candidates += 1
        db.session.add(application)
        db.session.commit()
        flash(f"Successfully applied for {position.title}!")
        return redirect(url_for("routes.index"))
    return render_template("position_apply.html", form=form, position=position)

@routes.route("/positions/<position_id>/applicants", methods=["GET"])
def positions_by_id_applicants(position_id):
    position = Position.query.filter_by(id=position_id).first()

    if position is None:
        return render_template("errors/404.html"), 404
    
    if current_user.user_type != "Professor" or current_user.id != position.professor_id:
        return render_template("errors/403.html"), 403

    students = [Student.query.filter_by(id=application.student_id).first() for application in position.applications]

    return render_template("applicants.html", students=students, position=position)

@routes.route("/positions/<position_id>/appilcants/<student_id>")
def position_applicant_by_id(position_id, student_id):
    position = Position.query.filter_by(id=position_id).first()
    student = Student.query.filter_by(id=student_id).first()

    if position is None:
        return render_template("errors/404.html"), 404
    
    if current_user.user_type != "Professor" or current_user.id != position.professor_id:
        return render_template("errors/403.html"), 403

    applications = [ x for x in position.applications ]
    application = None
    for app in applications:
        if app.student_id == student.id:
            application = app

    return render_template("application_page.html", position=position, student=student, application=application)