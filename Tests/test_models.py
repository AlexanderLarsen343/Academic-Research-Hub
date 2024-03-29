import warnings
warnings.filterwarnings("ignore")

import os
basedir = os.path.abspath(os.path.dirname(__file__))

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
        
    def test_student_relationships(self):
        interest1  = Interest(id=1, name="C#")
        interest2  = Interest(id=2, name="Java")
        language1  = Language(id=1, name="English")
        language2  = Language(id=2, name="Portuguese")
        db.session.add(interest1)
        db.session.add(interest2)
        db.session.add(language1)
        db.session.add(language2)
        db.session.commit()
        stud1 = Student (id=30, interests=[interest1], languages=[language1])
        stud2 = Student (id=40, interests=[interest1,interest2], languages=[language1,language2])
        db.session.add(stud1)
        db.session.add(stud2)
        db.session.commit()
        
        stud1_interests = []
        stud1_languages = []
        stud2_interests = []
        stud2_languages = []
        for interest in stud1.interests:
            stud1_interests.append(interest)
        for language in stud1.languages:
            stud1_languages.append(language)
        for interest in stud2.interests:
            stud2_interests.append(interest)
        for language in stud2.languages:
            stud2_languages.append(language)
        
        self.assertEqual(len(stud1_interests),1)
        self.assertEqual(len(stud1_languages),1)
        self.assertEqual(len(stud2_interests),2)
        self.assertEqual(len(stud2_languages),2)
        
        self.assertEqual(stud1_interests[0].id, 1)
        self.assertEqual(stud1_languages[0].id, 1)
        
        self.assertEqual(stud2_interests[0].id, 1)
        self.assertEqual(stud2_interests[1].id, 2)
        self.assertEqual(stud2_languages[0].id, 1)
        self.assertEqual(stud2_languages[1].id, 2)
        
    def test_position_relationships(self):
        interest1  = Interest(id=1, name="C#")
        interest2  = Interest(id=2, name="Java")
        language1  = Language(id=1, name="English")
        language2  = Language(id=2, name="Portuguese")
        db.session.add(interest1)
        db.session.add(interest2)
        db.session.add(language1)
        db.session.add(language2)
        db.session.commit()
        pos1 = Position (id=30, research_fields=[interest1], languages=[language1])
        pos2 = Position (id=40, research_fields=[interest1,interest2], languages=[language1,language2])
        db.session.add(pos1)
        db.session.add(pos2)
        db.session.commit()
        
        pos1_research_fields = []
        pos1_languages = []
        pos2_research_fields = []
        pos2_languages = []
        for research_field in pos1.research_fields:
            pos1_research_fields.append(research_field)
        for language in pos1.languages:
            pos1_languages.append(language)
        for research_field in pos2.research_fields:
            pos2_research_fields.append(research_field)
        for language in pos2.languages:
            pos2_languages.append(language)
        
        self.assertEqual(len(pos1_research_fields),1)
        self.assertEqual(len(pos1_languages),1)
        self.assertEqual(len(pos2_research_fields),2)
        self.assertEqual(len(pos2_languages),2)
        
        self.assertEqual(pos1_research_fields[0].id, 1)
        self.assertEqual(pos1_languages[0].id, 1)
        
        self.assertEqual(pos2_research_fields[0].id, 1)
        self.assertEqual(pos2_research_fields[1].id, 2)
        self.assertEqual(pos2_languages[0].id, 1)
        self.assertEqual(pos2_languages[1].id, 2)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)