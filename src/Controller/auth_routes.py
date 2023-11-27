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
            return redirect(url_for('routes.index')) # TODO: Change to actual student homepage
        elif current_user.user_type == "Professor":
            return redirect(url_for('routes.index')) # TODO: Change to actual prof. homepage
    lform = LoginForm()
    if lform.validate_on_submit():
        user = User.query.filter_by(email = lform.username.data).first()
        if(user is None) or (user.get_password(lform.password.data) == False):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember = lform.remember_me.data)
        flash(f"Welcome, {current_user.firstname}!")
        if current_user.user_type == "Student":
            return redirect(url_for('routes.index')) # TODO: Change to actual student homepage
        elif current_user.user_type == "Professor":
            return redirect(url_for('routes.index')) # TODO: Change to actual prof. homepage
    return render_template('login.html', form=lform)

@auth.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("Successfully logged out.")
    return redirect(url_for("routes.index"))

@auth.route("/register")
def register():
    if current_user.is_authenticated:
        if current_user.user_type == "Student":
            return redirect(url_for('routes.student_homepage')) # TODO: Change to actual student homepage
        elif current_user.user_type == "Professor":
            return redirect(url_for('routes.professor_homepage')) # TODO: Change to actual prof. homepage
    return render_template("Register Pages/index.html")

@auth.route("/register/student", methods=["GET", "POST"])
def register_student():
    if current_user.is_authenticated:
        if current_user.user_type == "Student":
            return redirect(url_for('routes.student_homepage')) # TODO: Change to actual student homepage
        elif current_user.user_type == "Professor":
            return redirect(url_for('routes.professor_homepage')) # TODO: Change to actual prof. homepage
    rform = StudentRegistrationForm()
    if rform.validate_on_submit():
        user = User.query.filter_by(email=rform.email.data).first()
        if user is not None:
            flash("That email is already taken.")
            return redirect(url_for("auth.register_student"))
        # TODO: complete this stuff
        student = Student(
            email=rform.email.data,
            firstname=rform.firstname.data,
            lastname=rform.lastname.data,
            wsu_id=rform.wsu_id.data,
            major=rform.major.data,
            gpa=rform.gpa.data,
            graduationDate=rform.graduationDate.data,
            experience=rform.experience.data,
            phone=rform.phone.data
        )

        for interest in rform.interests.data:
            student.interests.add(interest)

        for language in rform.programming_langs.data:
            student.languages.add(language)

        student.set_password(rform.password.data)
        db.session.add(student)
        db.session.commit()
        flash("Registration successful!")
        return redirect(url_for("auth.login"))
    return render_template("Register Pages/register_student.html", form=rform)

@auth.route("/register/professor", methods=["GET", "POST"])
def register_professor():
    if current_user.is_authenticated:
        if current_user.user_type == "Student":
            return redirect(url_for('routes.student_homepage')) # TODO: Change to actual student homepage
        elif current_user.user_type == "Professor":
            return redirect(url_for('routes.professor_homepage')) # TODO: Change to actual prof. homepage
    rform = ProfessorRegistrationForm()
    # print(rform.validate_on_submit())
    print ("hello")
    if rform.validate_on_submit():
        user = User.query.filter_by(email=rform.email.data).first()
        if user is not None:
            flash("That email is already taken.")
            return redirect(url_for("auth.register_professor"))
        professor = Professor(
            email=rform.email.data,
            firstname=rform.firstname.data,
            lastname=rform.lastname.data,
            title=rform.title.data
        )
        professor.set_password(rform.password.data)
        db.session.add(professor)
        db.session.commit()
        flash("Registration successful!")
        return redirect(url_for("auth.login"))
    return render_template("Register Pages/register_professor.html", form=rform)