from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#Student Model with all information
#Note: languages and interests will be from a multiple select field
class Student(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique = True, index = True)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120),unique = True, index = True)
    wsu_id = db.Column(db.String(15), unique = True)
    major = db.Column(db.String(50))
    phone = db.Column(db.String(11))
    graduation = db.Column(db.String(15))
    languages = db.Column(db.String(50))
    interests = db.Column(db.String(150))

    def __repr__(self):
        return f"User ID is {self.id} and username is {self.username}"
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password_hash, password)
