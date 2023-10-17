from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

studentInterests = db.Table('studentInterests',
                db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
                db.Column('interest_id', db.Integer, db.ForeignKey('interest.id')))

studentLanguages = db.Table('studentLanguages',
                db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
                db.Column('language_id', db.Integer, db.ForeignKey('language.id')))

#Parent class for both Student and Professor
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique = True, index = True)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120),unique = True, index = True)
    phone = db.Column(db.String(11))
    user_type = db.Column(db.String(50))
    
    #Polymorphic attribute
    __mapper_args__ = {
        'polymorphic_identity': 'User',
        'polymorphic_on': user_type
    }

    def __repr__(self):
        return f"User ID is {self.id} and username is {self.username}"
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password_hash, password)

#Student Model with all information
#Note: languages and interests will be from a multiple select field
class Student(User, db.Model):
    __tablename__='student'
    id = db.Column(db.ForeignKey("user.id"), primary_key = True)
    wsu_id = db.Column(db.String(15), unique = True)
    major = db.Column(db.String(50))
    graduation = db.Column(db.String(15))
    gpa = db.Column(db.Integer(4))
    languages = db.Column(db.String(50))
    #interests = db.Column(db.String(150))
    experience = db.Column(db.String(500))
    
    interests = db.relationship('Interest',
                                secondary=studentInterests,
                                primaryjoin=(studentInterests.c.student_id == id),
                                backref=db.backref('studentInterests', lazy='dynamic'),
                                lazy='dynamic')
    languages = db.relationship('Language',
                                secondary=studentLanguages,
                                primaryjoin=(studentLanguages.c.student_id == id),
                                backref=db.backref('studentLanguages', lazy='dynamic'),
                                lazy='dynamic')
    def get_interests(self):
        return self.interests
    
    def get_languages(self):
        return self.languages

    #Designates the identity of user_type
    __mapper_args__ = {
        'polymorphic_identity': 'Student'
    }
    
class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12))
    
class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12))
    
class Professor(User, db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.ForeignKey("user.id"), primary_key=True)
    title = db.Column(db.String(50))


    #Designates the identity of user_type
    __mapper__args__ = {
        'polymorphic_identity': 'Professor',
    }