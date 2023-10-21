from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request, get_flashed_messages
from config import Config
from flask_login import current_user, login_required

from src import db
from src.Model.models import Position
from src.Controller.forms import PositionForm

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template("index.html")

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
        )
        db.session.add(newPostition)
        db.session.commit()
        flash('New Post: "' + newPostition.title + '" has been created.')
        return redirect(url_for('routes.index'))
    return render_template('createPosition.html', form = pform)