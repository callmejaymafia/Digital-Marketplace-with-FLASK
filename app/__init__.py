from config import Config
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes import auth, admin, vendor, download, checkout, market

    blueprints = [auth, admin, vendor, download, checkout, market]
    for bp in blueprints:
        app.register_blueprint(bp)

    return app
