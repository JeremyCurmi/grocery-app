from src.app import init_app

if __name__ == "__main__":
    app = init_app()
    app.run(host=app.config["FLASK_RUN_HOST"],port=app.config["FLASK_RUN_PORT"])