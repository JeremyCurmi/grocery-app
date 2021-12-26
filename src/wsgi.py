from src.app import create_app
from src.config import get_config

if __name__ == "__main__":
    app = create_app(get_config())
    app.run(host=app.config["FLASK_RUN_HOST"],port=app.config["FLASK_RUN_PORT"])