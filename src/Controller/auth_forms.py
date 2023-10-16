from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length, Email
from Model.models import User

class RegistrationForm(FlaskForm):
    #this should be a wsu email, it will be used as the username. not sure if there is a way to check that it sis a wsu email
    email = StringField('Email', validators = [DataRequired(), Email(), Length(1, 120)])
    firstname = StringField('Firstname', validators = [DataRequired(), Length(1, 20)])
    lastname = StringField('Lastname', validators = [DataRequired(), Length(1, 20)])
    wsu_id = StringField('Lastname', validators = [DataRequired(), Length(1,15)])
    contact_email = StringField('Email', validators = [DataRequired(), Email(), Length(1, 120)])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Password', validators = [DataRequired(), EqualTo('password')])
   
    #submit = SubmitField('Register')

    def validate_email(self, email):
        #make sure email ends with "@wsu.edu"
        if not email.data.lower().endswith('@wsu.edu'):
            raise ValidationError('Please use your WSU email.')
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('The email already exists! Please use a different email address.')
            
    def validate_contact_email(self, contact_email):
        if contact_email.data == self.email.data:
            return
        else:
            user = User.query.filter_by(email=contact_email.data).frist()
            if user is not None:
                raise ValidationError('The contact email already exists! Please use a different email address.')
        