from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length, Email
from Model.models import Student

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators = [DataRequired(), Length(1, 50)])
    firstname = StringField('Firstname', validators = [DataRequired(), Length(1, 20)])
    lastname = StringField('Lastname', validators = [DataRequired(), Length(1, 20)])
    wsu_id = StringField('Lastname', validators = [DataRequired(), Length(1,15)])
    email = StringField('Email', validators = [DataRequired(), Email(), Length(1, 120)])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Password', validators = [DataRequired(), EqualTo('password')])
    graduation = StringField('Graduation Date', valdiators = [DataRequired(), Length(1, 15)])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('The username already exists! Please use a different username.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('The email already exists! Please use a different email address.')
        