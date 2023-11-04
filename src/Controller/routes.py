from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request, get_flashed_messages
from config import Config
from flask_login import current_user, login_required

from src import db
from src.Model.models import Position
from src.Controller.forms import PositionForm

routes = Blueprint("routes", __name__)

@routes.route("/", methods=['GET'])
# @routes.route("/index", methods=['GET'])
@login_required
def index():
    positions=Position.query.all()
    return render_template("index.html", title="WSU Research Portal", positions=positions)

@routes.route('/postposition/', methods = ['GET', 'POST'])
@login_required
def create_position():
    pform = PositionForm()
    if pform.validate_on_submit():
        newPostition = Position(
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
        db.session.add(newPostition)
        db.session.commit()
        flash('New Post: "' + newPostition.title + '" has been created.')
        return redirect(url_for('routes.index'))
    else:
        for field, errors in pform.errors.items():
            for error in errors:
                print(f"Field: {field}, Error: {error}")
    return render_template('createPosition.html', form = pform)

@routes.route("/positions", methods=["GET"])
def positions():
    positions = Position.query.all()
    return render_template("positions.html", positions=positions)


# @routes.route('/display_profile', methods = ['GET'])
# @login_required
# def display_profile():
#     return render_template('display_profile.html', title='Display Profile', student = current_user)