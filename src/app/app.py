from flask import Flask
from flask_migrate import Migrate

from src.models import db
from src.config import get_config
from src.routes import home


def create_app():
    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
    app.config.from_object(get_config())

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(home)
    return app
