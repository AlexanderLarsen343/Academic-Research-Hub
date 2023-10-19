from src import create_app, db
from src.Model.models import User, Student

app = create_app()
app.app_context().push()

for u in User.query.all():
    print(u)