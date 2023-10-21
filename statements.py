from src import create_app, db
from src.Model.models import User, Student, Professor, Position

app = create_app()
app.app_context().push()

print("Students: ")
for student in Student.query.all():
    print(f"\t{student.email}")

print("Professors: ")
for prof in Professor.query.all():
    print(f"\t{prof.email}")

print("Positions: ")
for pos in Position.query.all():
    print(f"\t{pos.title}")