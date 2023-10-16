from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length, Email
from Model.models import Student
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import CheckboxInput, ListWidget
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators = [DataRequired(), Length(1, 50)])
    firstname = StringField('Firstname', validators = [DataRequired(), Length(1, 20)])
    lastname = StringField('Lastname', validators = [DataRequired(), Length(1, 20)])
    wsu_id = StringField('wsu ID', validators = [DataRequired(), Length(1,15)])
    email = StringField('Email', validators = [DataRequired(), Email(), Length(1, 120)])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Password', validators = [DataRequired(), EqualTo('password')])
    # will want to edit graduation in the future to select Term (Sping, Summer, Fall, Winter) and year
    graduationDate = StringField('Graduation Date', valdiators = [DataRequired(), Length(1, 15)])
    # these will both be many to many (because many students can have many interest and many interests can belong to many students)
    interests = QuerySelectMultipleField('Interests', query_factory=get_interests_label, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput() )
    programming_langs = QuerySelectMultipleField('ProgrammingLangs', query_factory=get_programming_langs_label, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput() )
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Student.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('The username already exists! Please use a different username.')
    
    def validate_email(self, email):
        user = Student.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('The email already exists! Please use a different email address.')
        