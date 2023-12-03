import warnings
warnings.filterwarnings("ignore")

import unittest
from src import create_app, db
from src.Model.models import Student, Interest, Language, Professor, Position, Application
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    
class TestModels(unittest.TestCase):
    def setUp(self):
        #self.cleanApp()
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def cleanApp(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop
        
    def test_password_hashing(self):
        user = Student(email = "gabe@wsu.edu")
        user.set_password("123")
        self.assertFalse(user.get_password("321"))
        self.assertTrue(user.get_password("123"))
        
    def test_applications(self):
        prof1 = Professor(id=1)
        stud1 = Student (id=10)
        stud2 = Student (id=20)
        db.session.add(prof1)
        db.session.add(stud1)
        db.session.add(stud2)
        db.session.commit()
        
        pos1 = Position(id=1,professor_id=1)
        pos2 = Position(id=2,professor_id=1)
        pos3 = Position(id=3,professor_id=1)
        db.session.add(pos1)
        db.session.add(pos2)
        db.session.add(pos3)
        db.session.commit()
        self.assertEqual(len(prof1.positions),3)
        
        application1 = Application(position_id=1, student_id=10)
        application2 = Application(position_id=1, student_id=20)
        application3 = Application(position_id=2, student_id=10)
        db.session.add(application1)
        db.session.add(application2)
        db.session.add(application3)
        db.session.commit()
        
        self.assertEqual(len(pos1.applications), 2)
        self.assertEqual(len(pos2.applications), 1)
        self.assertEqual(len(pos3.applications), 0)
        
    #def test_student_fields(self):
        # interest1  = Interest(id=1, name="C#")
        # interest2  = Interest(id=2, name="Java")
        # language1  = Language(id=1, name="English")
        # language2  = Language(id=2, name="Portuguese")
        # db.session.add(interest1)
        # db.session.add(interest2)
        # db.session.add(language1)
        # db.session.add(language2)
        # db.session.commit()
        # stud1 = Student (id=30, interests=[interest1], languages=[language1])
        # stud2 = Student (id=40, interests=[interest1,interest2], languages=[language1,language2])
        # db.session.add(stud1)
        # db.session.add(stud2)
        # db.session.commit()
        
        
        
        
        
            
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)