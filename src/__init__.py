from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.static_folder = config.STATIC_FOLDER 
    app.template_folder = config.TEMPLATE_FOLDER

    db.init_app(app)

    @app.before_request
    def initBD(*args, **kwargs):
        if app.got_first_request:
            db.create_all()

    # Register Blueprints

    # Auth blueprint
    from src.Controller.auth_routes import auth
    app.register_blueprint(auth)

    # Main routes
    from src.Controller.routes import routes
    app.register_blueprint(routes)

    return app