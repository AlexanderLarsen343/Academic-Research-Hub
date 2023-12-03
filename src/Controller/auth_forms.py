from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, FloatField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length, Email, NumberRange
from src.Model.models import User, Language, Interest, Student, Professor
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

class StudentRegistrationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email(), Length(1, 120)])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
    firstname = StringField('First Name', validators = [DataRequired(), Length(1, 20)])
    lastname = StringField('Last Name', validators = [DataRequired(), Length(1, 20)])
    wsu_id = StringField('WSU ID', validators = [DataRequired(), Length(1,15)])
    major = StringField('Major', validators = [DataRequired(), Length(1,50)])
    gpa = FloatField("GPA", validators=[DataRequired(), NumberRange(0.0, 4.0)])
    # will want to edit graduation in the future to select Term (Sping, Summer, Fall, Winter) and year
    graduationDate = StringField('Graduation Date', validators = [DataRequired(), Length(1, 15)])
    # these will both be many to many (because many students can have many interest and many interests can belong to many students)
    interests = QuerySelectMultipleField('Interests', query_factory = interests, get_label=get_interest_label, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput() )
    programming_langs = QuerySelectMultipleField('Programming Languages', query_factory = languages, get_label=get_language_label, widget=ListWidget(prefix_label=False), option_widget=CheckboxInput() )
    experience = StringField('Experience', validators = [DataRequired(), Length(1, 500)])
    phone = StringField('Phone Number', validators= [DataRequired(), Length(1, 10)])

    submit = SubmitField('Register')

    def validate_wsu_id(self, wsu_id):
        print(f"TYPE OF WSU_ID: {type(wsu_id)}")
        student = Student.query.filter_by(wsu_id=wsu_id.data).first()
        if student is not None:
            raise ValidationError("This WSU ID is already registered.")
    
    def validate_email(self, email):
        #make sure email ends with "@wsu.edu"
        if not email.data.lower().endswith('@wsu.edu'):
            raise ValidationError('Please use your WSU email.')
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('The email already exists! Please use a different email address.')
        
    def validate_phone(self, phone):
        professor = Professor.query.filter_by(phone=phone.data)
        if professor is not None:
            raise ValidationError("This phone number already exists! Please use a different phone number.")
        

class ProfessorRegistrationForm(FlaskForm):
    #this should be a wsu email, it will be used as the username. not sure if there is a way to check that it sis a wsu email
    email = StringField('Email', validators = [DataRequired(), Email(), Length(1, 120)])
    firstname = StringField('First Name', validators = [DataRequired(), Length(1, 20)])
    lastname = StringField('Last Name', validators = [DataRequired(), Length(1, 20)])
    wsu_id = StringField('WSU ID', validators = [DataRequired(), Length(1,15)])
    # contact_email = StringField('Email', validators = [DataRequired(), Email(), Length(1, 120)])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
    title = StringField('Title', validators = [DataRequired(), Length(1, 30)])
    phone = StringField('Phone Number', validators= [DataRequired(), Length(1, 10)])
   
    submit = SubmitField('Register')

    def validate_email(self, email):
        #make sure email ends with "@wsu.edu"
        if not email.data.lower().endswith('@wsu.edu'):
            raise ValidationError('Please use your WSU email.')
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('The email already exists! Please use a different email address.')
        
    def validate_phone(self, phone):
        professor = Professor.query.filter_by(phone=phone.data)
        if professor is not None:
            raise ValidationError("This phone number already exists! Please use a different phone number.")
            
    # def validate_contact_email(self, contact_email):
    #     if contact_email.data == self.email.data:
    #         return
    #     else:
    #         user = User.query.filter_by(email=contact_email.data).first()
    #         if user is not None:
    #             raise ValidationError('The contact email already exists! Please use a different email address.')
        
class LoginForm(FlaskForm):
    username = StringField("Email", validators=[DataRequired(), Length(1, 50)])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")
