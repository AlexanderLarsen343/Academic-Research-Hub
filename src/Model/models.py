from src import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# Establishes the table for the relationship between Student model and Interest model
studentInterests = db.Table('studentInterests',
                db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
                db.Column('interest_id', db.Integer, db.ForeignKey('interest.id')))

# Establishes the table for the relationship between Student model and Language model
studentLanguages = db.Table('studentLanguages',
                db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
                db.Column('language_id', db.Integer, db.ForeignKey('language.id')))

# Establishes table for relationship between Position model and Interest model
positionInterests = db.Table(
    "positionInterests",
    db.Column("position_id", db.Integer, db.ForeignKey("position.id")),
    db.Column("interest_id", db.Integer, db.ForeignKey("interest.id"))    
)

# Establishes table for relationship between Position model and Language model
positionLanguages = db.Table(
    "positionLanguages",
    db.Column("position_id", db.Integer, db.ForeignKey("position.id")),
    db.Column("language_id", db.Integer, db.ForeignKey("language.id"))  
)
    
#Parent class for both Student and Professor
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120),unique = True, index = True)
    phone = db.Column(db.String(11),unique = True)
    user_type = db.Column(db.String(50))
    
    #Polymorphic attribute
    __mapper_args__ = {
        'polymorphic_identity': 'User',
        'polymorphic_on': user_type
    }

    def __repr__(self):
        return f"<User id={self.id} email={self.email}>"
    
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
    gpa = db.Column(db.Integer())
    graduationDate = db.Column(db.String(15))
    experience = db.Column(db.String(500))
    applications = db.relationship('Application', backref='applicant')
    
    # Establishes a many-to-many relationship between students and interests
    # The relationship will store the associations between student profiles and the interests associated with them.
    # Note: A student can have multiple interests associated with them, and a interest can be associated with many students.
    interests = db.relationship('Interest',
                                secondary=studentInterests,
                                primaryjoin=(studentInterests.c.student_id == id),
                                lazy='dynamic',
                                overlaps='studentInterests')
    # Establishes a many-to-many relationship between students and languages
    # The relationship will store the associations between student profiles and the languages associated with them.
    # Note: A student can have multiple languages associated with them, and a language can be associated with many students.
    languages = db.relationship('Language',
                                secondary=studentLanguages,
                                primaryjoin=(studentLanguages.c.student_id == id),
                                lazy='dynamic',
                                overlaps='studentLanguages')
    
          
    def get_interests(self):
        return self.interests
    
    def get_languages(self):
        return self.languages
    
    def get_application_by_position(self, position):
        for application in self.applications:
            if application.position_id == position.id:
                return application
            
        return None

    #Designates the identity of user_type
    __mapper_args__ = {
        'polymorphic_identity': 'Student'
    }

# Students will be able to associate interests to their user profile.
class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    studentInterests = db.relationship(
        'Student',
        secondary=studentInterests,
        primaryjoin=(studentInterests.c.interest_id == id),
        lazy='dynamic',
        overlaps='interests'
    )
    positionInterests = db.relationship(
        'Position',
        secondary = positionInterests,
        primaryjoin = (positionInterests.c.interest_id == id),
        lazy = 'dynamic',
        overlaps = 'interests'
    )

# Students will be able to associate languages to their user profile.
class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12))
    studentLanguages = db.relationship(
        'Student',
        secondary=studentLanguages,
        primaryjoin=(studentLanguages.c.language_id == id),
        lazy='dynamic',
        overlaps='languages'
    )
    positionLanguages = db.relationship(
        'Position',
        secondary = positionLanguages,
        primaryjoin = (positionLanguages.c.language_id == id),
        lazy = 'dynamic',
        overlaps='languages'
    )
    
class Professor(User, db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.ForeignKey("user.id"), primary_key=True)
    wsu_id = db.Column(db.String(15), unique = True)
    title = db.Column(db.String(50))
    positions = db.relationship('Position', backref='professor') # Establishes one-to-many relationship between Professor and Position.

    # Designates the identity of user_type
    __mapper_args__ = {
        'polymorphic_identity': 'Professor'
    }
    
# Defines the model for a research position post made by a faculty user.
# Position -> form -> application
class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), unique=True)
    description = db.Column(db.String(256))
    # start_date = db.Column(db.DateTime(timezone=True))
    # end_date = db.Column(db.DateTime(timezone=True))
    accepting_applications = db.Column(db.Boolean)
    start_date = db.Column(db.String(256))
    end_date = db.Column(db.String(256))
    work_load = db.Column(db.Integer) # Time commitment.
    languages = db.relationship(
        'Language',
        secondary = positionLanguages,
        primaryjoin = (positionLanguages.c.position_id == id),
        lazy='dynamic',
        overlaps='languages'
    )
    # TODO: Finish relationships
    research_fields = db.relationship(
        'Interest',
        secondary=positionInterests,
        primaryjoin=(positionInterests.c.position_id == id),
        lazy='dynamic',
        overlaps='interests'
    )
    candidates = db.Column(db.Integer) # Stores the ID's of the current candidates for the position.
    applications = db.relationship('Application', backref='position') # A position has multiple applications associated to it.
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id')) # Every position has one professor associated to it.
    
    
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(16))
    statement = db.Column(db.String(500))
    reference = db.Column(db.String(40))
    reference_email = db.Column(db.String(30))
    position_id = db.Column(db.Integer, db.ForeignKey('position.id')) # Every application has one position associated to it.
    student_id = db.Column(db.Integer, db.ForeignKey('student.id')) # Every application has one student associated to it.
