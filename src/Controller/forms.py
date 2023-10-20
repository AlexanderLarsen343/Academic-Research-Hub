from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length, Email
from src.Model.models import User, Language, Interest
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import CheckboxInput, ListWidget
from flask_login import current_user

# from src.Model.models import Language

# def get_tags():
# 	return 

class PositionForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(), Length(max=32)]) # not sure if max is right here
	description = TextAreaField('Description', validators=[DataRequired(),Length(max=1500)])
	start_date = SelectField('Start Date',)
	end_date = SelectField('End Date',)
	workload = StringField('Workload', validators=[DataRequired()])
	research_field =  StringField('Research Field', validators=[DataRequired(), Length(max=32)])
	#languages = QuerySelectMultipleField('Tag', query_factory=get_tags, get_label=get_tag_label, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
	#requirements = QuerySelectMultipleField('Tag', query_factory=get_tags, get_label=get_tag_label, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
	submit = SubmitField('Post')