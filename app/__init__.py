from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes.auth import auth
    from .routes.market import routes

    app.register_blueprint(auth)
    app.register_blueprint(routes)

    return app
