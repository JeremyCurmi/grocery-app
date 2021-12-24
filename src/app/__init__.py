from flask import Flask
from src.config import get_config


def init_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    @app.route('/')
    def index():
        return ""

    return app