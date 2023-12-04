from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField, IntegerField, DateField, PasswordField, FloatField
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
	start_date = StringField('Start Date', validators=[DataRequired()])
	end_date = StringField('End Date', validators=[DataRequired()])
	workload = IntegerField('Hours Per Week', validators=[DataRequired(), NumberRange(1, 168)])
	languages = QuerySelectMultipleField('Languages', query_factory=languages, get_label=get_language_label, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
	research_fields = QuerySelectMultipleField('Research Fields', query_factory=interests, get_label=get_interest_label, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
	submit = SubmitField('Create Position')
     
class ApplicationForm(FlaskForm):
	statement = TextAreaField('Summary of Qualifications', validators=[DataRequired(),Length(max=1500)])
	reference = StringField('Reference Name', validators=[DataRequired(), Length(max=30)])
	reference_email = StringField('Reference Email', validators=[DataRequired(), Length(max=30)])
	submit = SubmitField("Submit")
      
class StudentHomeSortForm(FlaskForm):
    sort_by = SelectField("Filter By", choices=[(0, "Show All"), (1, "Research Position"), (2, "Languages")])
    submit = SubmitField("Refresh")

class EditStudentForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email(), Length(1, 120)])
	password = PasswordField('Password', validators = [DataRequired()])
	password2 = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
	firstname = StringField('First Name', validators = [DataRequired(), Length(1, 20)])
	lastname = StringField('Last Name', validators = [DataRequired(), Length(1, 20)])
	wsu_id = StringField('WSU ID', validators = [DataRequired(), Length(1,15)])
	major = StringField('Major', validators = [DataRequired(), Length(1,50)])
	gpa = FloatField("GPA", validators=[DataRequired(), NumberRange(0.0, 4.0)])
	graduationDate = StringField('Graduation Date', validators = [DataRequired(), Length(1, 15)])
	interests = QuerySelectMultipleField('Interests', query_factory = interests, get_label=get_interest_label, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput() )
	programming_langs = QuerySelectMultipleField('Programming Languages', query_factory = languages, get_label=get_language_label, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput() )
	experience = StringField('Experience', validators = [DataRequired(), Length(1, 500)])
	phone = StringField('Phone Number', validators= [DataRequired(), Length(1, 10)])
	submit = SubmitField('Submit')

	def validate_email(self, email):
		if not email.data.lower().endswith('@wsu.edu'):
			raise ValidationError('Please use your WSU email.')
		if current_user.email == email.data:
			return
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('The email already exists! Please use a different email address.')

class EditProfessorForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email(), Length(1, 120)])
	firstname = StringField('First Name', validators = [DataRequired(), Length(1, 20)])
	lastname = StringField('Last Name', validators = [DataRequired(), Length(1, 20)])
	wsu_id = StringField('WSU ID', validators = [DataRequired(), Length(1,15)])
	password = PasswordField('Password', validators = [DataRequired()])
	password2 = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
	title = StringField('Title', validators = [DataRequired(), Length(1, 30)])
	phone = StringField('Phone Number', validators= [DataRequired(), Length(1, 10)])
	submit = SubmitField('Submit')
	
	def validate_email(self, email):
		if not email.data.lower().endswith('@wsu.edu'):
			raise ValidationError('Please use your WSU email.')
		if current_user.email == email.data:
			return
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('The email already exists! Please use a different email address.')
     