from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "this-is-secret-fr"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    migrate = Migrate(app, db)

    from .routes import auth, admin, vendor, download, checkout, marketplace

    blueprints = [auth, admin, vendor, download, checkout, marketplace]
    for bp in blueprints:
        app.register_blueprint(bp)

    create_database(app)

    return app


def create_database(app):
    if not path.exists("app/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created database!")
