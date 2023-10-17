from flask import Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from src.Controller.auth_forms import LoginForm
from src.Model.models import User, Student, Professor

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    if current_user.is_authenticated:
        if current_user.user_type == "Student":
            return redirect(url_for('routes.student_homepage')) # TODO: Change to actual student homepage
        elif current_user.user_type == "Professor":
            return redirect(url_for('routes.professor_homepage')) # TODO: Change to actual prof. homepage
    lform = LoginForm()
    if lform.validate_on_submit():
        user = User.query.filter_by(username = lform.usernmae)