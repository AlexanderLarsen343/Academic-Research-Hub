from flask import Flask
from flask_login import LoginManager
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
bootstrap = Bootstrap()

login = LoginManager()
login.login_view = 'auth.login'

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.static_folder = config.STATIC_FOLDER 
    app.template_folder = config.TEMPLATE_FOLDER

    db.init_app(app)
    bootstrap.init_app(app)
    login.init_app(app)

    # Register Blueprints

    # Auth blueprint
    from src.Controller.auth_routes import auth
    app.register_blueprint(auth)

    # Main routes
    from src.Controller.routes import routes as main
    app.register_blueprint(main)

    # Position routes
    from src.Controller.position_routes import routes as position
    app.register_blueprint(position)

    return app