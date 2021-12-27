from typing import Any
from flask_testing import TestCase
from src.app import create_app
from src.models import db
from flask_sqlalchemy import SQLAlchemy
from src.services import create_user_in_database


class FlaskSQLAlchemy(TestCase):
    def create_app(self):
        return create_app("src.config.TestConfig")

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


def populate_db(session: SQLAlchemy):
    users = [{"name": "user1", "email": "user1@email.com", "password": "password1"},
             {"name": "user2", "email": "user2@email.com", "password": "password2"}]

    for user in users:
        _ = create_user_in_database(session, **user)