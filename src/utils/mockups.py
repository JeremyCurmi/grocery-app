from flask_testing import TestCase
from src.app import create_app
from src.models import db, User, Product
from flask_sqlalchemy import SQLAlchemy
from src.services import create_new


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
             {"name": "user2", "email": "user2@email.com", "password": "password2"},
             {"name": "user2", "email": "user3@email.com", "password": "password3"}]

    products = [{"name": "cheese","unit": "each","price": 2},
                {"name": "ham","unit": "kg","price": 1},
                {"name": "ham","unit": "kg","price": 1}]
    for user in users:
        _ = create_new(User, user)

    for product in products:
        _ = create_new(Product, product)