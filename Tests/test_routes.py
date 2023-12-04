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
    
    student1 = Student(
        firstname="Butch",
        lastname="Cougar",
        email="butch@wsu.edu",
        phone="1879534989"
    )
    student1.set_password("password")
    
    db.session.add(student1)
    
    professor1 = Professor(
        email="sakire@wsu.edu",

        firstname = "Sakire",
        lastname = "Arslan Ay",
        phone = "3609699669",
        title = "Pretty Cool Professor"
    )
    professor1.set_password("123")
    db.session.add(professor1)
    
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
    
def test_login_page(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Sign In" in response.data

def test_login_successful(client, init_db):
    data = {
        "username": "butch@wsu.edu",
        "password": "password"
    }

    response = client.post("/login", data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Hello, Butch" in response.data 

def test_login_failure(client):
    data = {
        "username": "alex@wsu.edu",
        "password": "giant_toe"
    }

    response = client.get("/login", data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Sign In" in response.data

def test_position_creation(client, init_db):
    data = {
        "username": "sakire@wsu.edu",
        "password": "123"
    }

    #Login
    response = client.post('/login', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Hello Professor" in response.data

    #Test get of position creation
    response = client.get('/positions/new')
    assert response.status_code == 200

    #Test Post for position creation

    interests1 = list( map(lambda t: t.id, Interest.query.all()[:2]))
    langs1 =  list( map(lambda t: t.id, Language.query.all()[:2]))

    data = {
        "title": "AI Research",
        "description": "This position requires students to be able to balance lab activity with a mentor and doing research on your own time. Papers on specific AI attributes will be a frequent task along with peer reviewing.",
        "start_date": "May 2024",
        "end_date" : "August 2024",
        "workload" : "20",
        "languages" : langs1,
        "research_fields": interests1
    }

    response = client.post('/positions/new', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"AI Research" in response.data
