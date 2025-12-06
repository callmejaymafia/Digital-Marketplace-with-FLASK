from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path
from flask_login import LoginManager

login_manager = LoginManager()
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "this-is-secret-fr"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    from app.routes.auth import auth
    from app.routes.admin import admin
    from app.routes.vendor import vendor
    from app.routes.download import download
    from app.routes.checkout import checkout
    from app.routes.marketplace import marketplace

    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(vendor)
    app.register_blueprint(download)
    app.register_blueprint(checkout)
    app.register_blueprint(marketplace)

    create_database(app)

    return app


def create_database(app):
    if not path.exists("app/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created database!")
