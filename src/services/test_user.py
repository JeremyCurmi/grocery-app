from flask_testing import TestCase
from src.app import create_app
from src.models import db, User
from .user import create_user_in_database, get_user_by_id_in_database, get_user_by_email_in_database


class FlaskSQLAlchemy(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"

    def create_app(self):
        # pass in test configuration
        return create_app("src.config.DevConfig")

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestUserServices(FlaskSQLAlchemy):

    def test_create_user_in_database(self):
        data = {"name": "name", "email": "test@email.com", "password": "password"}
        msg, err = create_user_in_database(db.session, **data)
        self.assertIsNone(err)

    def test_get_user_by_id_in_database(self):
        data = {"name": "name", "email": "test@email.com", "password": "password"}
        _ = create_user_in_database(db.session, **data)
        user_id = 1
        user = get_user_by_id_in_database(db.session, user_id)
        self.assertIsNotNone(user)

    def test_get_user_by_email_in_database(self):
        data = {"name": "name", "email": "test@email.com", "password": "password"}
        _ = create_user_in_database(db.session, **data)
        email = "test@email.com"
        user = get_user_by_email_in_database(db.session, email)
        self.assertIsNotNone(user)

