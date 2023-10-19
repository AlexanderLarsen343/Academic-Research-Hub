from flask import Blueprint, flash, redirect, url_for, render_template
from flask_login import login_user, current_user, logout_user, login_required

from src.Controller.auth_forms import LoginForm, StudentRegistrationForm, ProfessorRegistrationForm
from src.Model.models import User, Student, Professor
from src import db

auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["GET", "POST"])
def login():
    if current_user.is_authenticated:
        if current_user.user_type == "Student":
            return redirect(url_for('routes.student_homepage')) # TODO: Change to actual student homepage
        elif current_user.user_type == "Professor":
            return redirect(url_for('routes.professor_homepage')) # TODO: Change to actual prof. homepage
    lform = LoginForm()
    if lform.validate_on_submit():
        user = User.query.filter_by(username = lform.username.data).first()
        if(user is None) or (user.get_password(lform.password.data) == False):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember = lform.remmeber_me.data)
        if current_user.user_type == "Student":
            return redirect(url_for('routes.student_homepage')) # TODO: Change to actual student homepage
        elif current_user.user_type == "Professor":
            return redirect(url_for('routes.professor_homepage')) # TODO: Change to actual prof. homepage
    return render_template('login.html', form=lform)

@auth.route("/register")
def register():
    if current_user.is_authenticated:
        if current_user.user_type == "Student":
            return redirect(url_for('routes.student_homepage')) # TODO: Change to actual student homepage
        elif current_user.user_type == "Professor":
            return redirect(url_for('routes.professor_homepage')) # TODO: Change to actual prof. homepage
    return render_template("register/index.html")

@auth.route("/register/student")
def register_student():
    if current_user.is_authenticated:
        if current_user.user_type == "Student":
            return redirect(url_for('routes.student_homepage')) # TODO: Change to actual student homepage
        elif current_user.user_type == "Professor":
            return redirect(url_for('routes.professor_homepage')) # TODO: Change to actual prof. homepage
    rform = StudentRegistrationForm()
    if rform.validate_on_submit():
        user = User.query.filter_by(username=rform.username.data).first()
        if user is not None:
            flash("That username is already taken.")
            return redirect(url_for("auth.register_student"))
        # I think StudentRegForm is missing some fields
        # TODO: complete this stuff
        student = Student(
            email=rform.email.data,
            firstname=rform.firstname.data,
            lastname=rform.lastname.data,
            wsu_id=rform.wsu_id.data,
        )
        student.set_password(rform.password.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("register/student/index.html", form=rform)

@auth.route("/register/professor")
def register_professor():
    if current_user.is_authenticated:
        if current_user.user_type == "Student":
            return redirect(url_for('routes.student_homepage')) # TODO: Change to actual student homepage
        elif current_user.user_type == "Professor":
            return redirect(url_for('routes.professor_homepage')) # TODO: Change to actual prof. homepage
    rform = ProfessorRegistrationForm()
    if rform.validate_on_submit:
        pass
        return redirect(url_for("auth.login"))
    return render_template("register/professor/index.html", form=rform)