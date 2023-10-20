from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField, IntegerField, DateField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length, Email, NumberRange
from src.Model.models import User, Language, Interest
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import CheckboxInput, ListWidget
from flask_login import current_user

def languages():
    return Language.query.all()

def get_language_label(language):
    return language.name

def interests():
    return Interest.query.all()

def get_interest_label(interest):
    return interest.name

class PositionForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(), Length(max=32)]) # not sure if max is right here
	description = TextAreaField('Description', validators=[DataRequired(),Length(max=1500)])
	start_date = DateField('Start Date', validators=[DataRequired()])
	end_date = DateField('End Date', validators=[DataRequired()])
	workload = IntegerField('Hours Per Week', validators=[DataRequired(), NumberRange(1, 168)])
	languages = QuerySelectMultipleField('Languages', query_factory=languages, get_label=get_language_label, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
	research_fields = QuerySelectMultipleField('Research Fields', query_factory=interests, get_label=get_interest_label, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
	submit = SubmitField('Post')