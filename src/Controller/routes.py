from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
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
def createPosition():
    pform = PositionForm()
    if pform.validate_on_submit():
        newPostition = Position(title=pform.title.data, body=pform.body.data, happiness_level = pform.happiness_level.data, user_id = current_user.id)
        for t in pform.languages.data:
            newPostition.languages.append(t)
        for t in pform.requirements.data:
            newPostition.requirements.append(t)
        db.session.add(newPostition)
        db.session.commit()
        flash('New Post: "' + newPostition.title + '" has been uploaded.')
        return redirect(url_for('routes.index'))
    return render_template('createPosition.html', form = pform)