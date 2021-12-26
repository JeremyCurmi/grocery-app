from flask import Flask
from flask_migrate import Migrate

from src.config import get_config
from src.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    db.init_app(app)
    Migrate(app, db)

    @app.route('/')
    def index():
        return ""

    return app