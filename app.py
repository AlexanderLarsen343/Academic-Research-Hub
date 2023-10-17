from src import create_app, db
from src.Model.models import Language, Interest

app = create_app()

@app.before_request
def initBD(*args, **kwargs):
    if app.got_first_request:

        # Adds all the predetermined fields for interests and languages for students
        db.create_all()
        if Language.query.count() == 0:
            languages = ['Java','C', 'Python', 'C++', 'JavaScript', 'HTML', 'CSS']
            for t in languages:
                db.session.add(Language(name=t))
        db.session.commit()
        if Interest.query.count() == 0:
            interests = ['Software Engineering', 'Artificial intelligence', 'Cyber Security', 'Machine Learning', 'Computer Architecture', 'Data Science']
            for t in interests:
                db.session.add(Interest(name=t))
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)