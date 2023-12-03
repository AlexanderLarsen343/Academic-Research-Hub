import os
import pytest
from src import create_app, db
from src.Model.models import *
from config import Config

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SECRET_KEY = "a-very-bad-key"
    WTF_CSRF_ENABLED = False
    DEBUG = True
    TESTING = True

@pytest.fixture(scope="module")
def client():
    # Create flask app and configure it for testing
    app = create_app(config=TestConfig)

    # db.init_app(app)

    testing_client = app.test_client()

    context = app.app_context()

    context.push()

    yield testing_client

    context.pop()

@pytest.fixture
def init_db():
    print("initing database")
    db.create_all()

    if Language.query.count() == 0:
        for l in ['Java','C', 'Python', 'C++', 'JavaScript', 'HTML', 'CSS']:
            db.session.add(Language(name=l))
    
    if Interest.query.count() == 0:
        for i in ['Software Engineering', 'Artificial intelligence', 'Cyber Security', 'Machine Learning', 'Computer Architecture', 'Data Science']:
            db.session.add(Interest(name=i))

    # student = Student(firstname="Marcus", lastname="Horan", email="marcus@wsu.edu", phone="3602732883", wsu_id = "20024881", major = "Computer Science", graduationDate = "May 2025", experience = "TA for Software Engineering for last year Spring")
    # student.interests.add()
    # student.set_password("password")
    
    # db.session.add(student)
    
    db.session.commit()

    yield

    db.drop_all()

def test_register_page(client):
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Student" in response.data
    assert b"Professor" in response.data

def test_register_student_page(client, init_db):
    response = client.get("/register/student")
    assert response.status_code == 200
    assert b"Student" in response.data
    assert b"Professor" not in response.data

def test_register_professor_page(client):
    response = client.get("/register/professor")
    assert response.status_code == 200
    assert b"Student" not in response.data
    assert b"Professor" in response.data

def test_registration_student(client, init_db):
    data = {
        "email": "marcus@wsu.edu",
        "password": "password",
        "password2": "password",
        "firstname": "Marcus",
        "lastname": "Horan",
        "wsu_id": "1234567890",
        "major": "Pre-Dental",
        "gpa": "4.0",
        "phone": "1234567890",
        "graduateionDate": "May 2026",
        "experience": "I like pie"
    }

    response = client.post("/register/student", data=data, follow_redirects=True)
    # print(response.data)
    assert response.status_code == 200
    assert b"Registration successful!" in response.data
    assert b"Sign In" in response.data
    