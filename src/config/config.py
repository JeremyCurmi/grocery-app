from dotenv import dotenv_values

env_vars = dotenv_values()
ENV = env_vars.get("ENVIRONMENT")


class Config:
    """Base config."""
    FLASK_RUN_HOST = env_vars.get("API_HOST")
    FLASK_RUN_PORT = env_vars.get("API_PORT")
    SECRET_KEY = env_vars.get("SECRET_KEY")
    MYSQL_USER = env_vars.get("MYSQL_USER")
    MYSQL_HOST = env_vars.get("MYSQL_HOST")
    MYSQL_PORT = env_vars.get("MYSQL_PORT")
    MYSQL_PASSWORD = env_vars.get("MYSQL_PASSWORD")
    MYSQL_DATABASE = env_vars.get("MYSQL_DATABASE")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True


def get_config(is_test: bool = False) -> str:
    path = "src" + "."
    if any([ENV == "debug", is_test]):
        return path + "config.DevConfig"
    return path + "config.ProdConfig"
