from flask import Flask

from src.models import db, migrate
from src.routes import home, user, product
from src.config import get_config


def create_app(env: str = get_config()):
    app = Flask(__name__,
                template_folder='../frontend/templates',
                static_folder='../frontend/static')
    app.config.from_object(env)

    db.init_app(app)
    migrate.init_app(app, db)

    app.config["db"] = db

    app.register_blueprint(home)
    app.register_blueprint(user)
    app.register_blueprint(product)
    return app
