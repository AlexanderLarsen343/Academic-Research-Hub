from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request, get_flashed_messages
from flask_login import current_user, login_required

from src import db
from src.Model.models import Position, Application, Student
from src.Controller.forms import StudentHomeSortForm
from src.Controller.forms import PositionForm, ApplicationForm

routes = Blueprint("positions", __name__)

@routes.route("/positions", methods=["GET", "POST"])
@login_required
def positions():
    positions = None
    form = StudentHomeSortForm()

    if current_user.user_type == "Professor":
        positions = Position.query.filter_by(professor_id=current_user.id).all()
        return render_template("Position Pages/positions.html", positions=positions)
    elif current_user.user_type == "Student":

        positions = Position.query.filter_by(accepting_applications=True).all()
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
                return render_template("Position Pages/positions.html", positions=positions_to_show, form=form)

            # languages
            elif sort_by == "2":
                student_languages = current_user.get_languages().all()
                for position in positions:
                    for language in student_languages:
                        if (position not in positions_to_show) and (language in position.languages):
                            positions_to_show.append(position)
                return render_template("Position Pages/positions.html", positions=positions_to_show, form=form)


            else:
                positions_to_show = positions
                return render_template("Position Pages/positions.html", positions=positions, form=form)
        return render_template("index.html", title="WSU Research Portal", positions=positions, form=form)

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
            accepting_applications=True,
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
    return render_template('Position Pages/create_position.html', form = pform)

@routes.route("/positions/<position_id>")
def positions_by_id(position_id):
    position = Position.query.filter_by(id=position_id).first()

    if position is None:
        return render_template("errors/404.html"), 404

    if (current_user.user_type != "Student") and (current_user.id != position.professor_id):
        return render_template("errors/403.html"), 403
    
    return render_template("Position Pages/position_page.html", position=position)

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
    return render_template("Position Pages/position_apply.html", form=form, position=position)

@routes.route("/positions/<position_id>/applicants", methods=["GET"]) # View Applicants for current position
def positions_by_id_applicants(position_id):
    position = Position.query.filter_by(id=position_id).first()

    if position is None:
        return render_template("errors/404.html"), 404
    
    if current_user.user_type != "Professor" or current_user.id != position.professor_id:
        return render_template("errors/403.html"), 403

    applicants = {application:Student.query.filter_by(id=application.student_id).first() for application in position.applications}
    recommended_applicants = []
    #Make a list of students with the desired coding skills
    #Find what skills the position wants
    #Go through all students and add them into the list if they have all coding lang in common
    
    required_languages = tuple(language for language in position.languages)
    
    for student in Student.query.all():
        student_languages = tuple(language for language in student.languages)
        if (student not in recommended_applicants) and all([required_language in student_languages for required_language in required_languages]):
            recommended_applicants.append(student)
    
    return render_template("Application Pages/applicants.html", recommended_applicants=recommended_applicants, students=applicants, position=position)

@routes.route("/positions/<position_id>/applicants/<student_id>") # "View Qualifications" button route.
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

    return render_template("Application Pages/application_page.html", position=position, student=student, application=application)

@routes.route("/positions/<position_id>/close", methods=["GET", "POST"])
def positions_by_id_delete(position_id):
    position = Position.query.filter_by(id=position_id).first()
    print(position.accepting_applications)
    if position is None:
        return render_template("errors/404.html"), 404
    
    if current_user.user_type != "Professor" or current_user.id != position.professor_id:
        return render_template("errors/403.html"), 403
    
    if request.method == "POST":
        flash(f"Research position \"{position.title}\" has been closed.")
        position.accepting_applications = False

        for application in position.applications:
            if application.status in ("Pending", "Approved for Interview"):
                application.status = "Position is Unavailable"
                db.session.add(application)

        db.session.add(position)
        db.session.commit()
        return redirect(url_for("positions.positions"))
    
    return render_template("Position Pages/close_position.html", position=position)

@routes.route("/positions/<position_id>/applicants/decline/<student_id>", methods=["GET","POST"])
def decline_applicant(position_id, student_id):
    position = Position.query.filter_by(id=position_id).first()
    student = Student.query.filter_by(id=student_id).first()
    
    if position is None:
        return render_template("errors/404.html"), 404
    
    if current_user.user_type != "Professor" or current_user.id != position.professor_id:
        return render_template("errors/403.html"), 403
    
    applications = [ x for x in position.applications ]
    target_application = None
    for app in applications:
        if app.student_id == student.id:
            target_application = app
    
    
    target_application.status = "Declined"
    target_application.position_id = None # Here we disassociate the target_application from its position.
    db.session.add(target_application)
    db.session.commit()
    
    return redirect(url_for('positions.positions_by_id_applicants', position_id=position_id))

@routes.route("/positions/<position_id>/applicants/accept/<student_id>", methods=["GET","POST"])
def accept_applicant(position_id, student_id):
    position = Position.query.filter_by(id=position_id).first()
    student = Student.query.filter_by(id=student_id).first()
    
    if position is None:
        return render_template("errors/404.html"), 404
    
    if current_user.user_type != "Professor" or current_user.id != position.professor_id:
        return render_template("errors/403.html"), 403
    
    applications = [ x for x in position.applications ]
    target_application = None
    for app in applications:
        if app.student_id == student.id:
            target_application = app
    
    
    target_application.status = "Accepted"
    db.session.add(target_application)
    db.session.commit()
    
    return redirect(url_for('positions.positions_by_id_applicants', position_id=position_id))

@routes.route("/positions/<position_id>/applicants/approve_for_interview/<student_id>", methods=["GET","POST"])
def approve_for_interview(position_id, student_id):
    position = Position.query.filter_by(id=position_id).first()
    student = Student.query.filter_by(id=student_id).first()
    
    if position is None:
        return render_template("errors/404.html"), 404
    
    if current_user.user_type != "Professor" or current_user.id != position.professor_id:
        return render_template("errors/403.html"), 403
    
    applications = [ x for x in position.applications ]
    target_application = None
    for app in applications:
        if app.student_id == student.id:
            target_application = app
    
    
    target_application.status = "Approved for Interview"
    db.session.add(target_application)
    db.session.commit()
    
    return redirect(url_for('positions.positions_by_id_applicants', position_id=position_id))