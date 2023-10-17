from flask import Blueprint, flash, redirect, url_for, render_template
from flask_login import login_user, current_user, logout_user, login_required

from src.Controller.auth_forms import LoginForm
from src.Model.models import User, Student, Professor

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