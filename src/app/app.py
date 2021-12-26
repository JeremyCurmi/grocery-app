from flask import Flask
from flask_migrate import Migrate

from src.models import db
from src.routes import home


def create_app(env: str):
    app = Flask(__name__,
                template_folder='../frontend/templates',
                static_folder='../frontend/static')
    app.config.from_object(env)

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(home)
    return app
