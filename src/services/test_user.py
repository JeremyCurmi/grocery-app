from src.models import db, User
from .user import create_user_in_database, get_user_by_id_in_database, get_user_by_email_in_database, get_all_users_in_database
from sqlalchemy.exc import IntegrityError
from src.utils import FlaskSQLAlchemy, populate_db


class TestUserServices(FlaskSQLAlchemy):
    def test_create_user_in_database_duplicate_error(self):
        populate_db(db.session)
        data = {"name": "user1", "email": "user1@email.com", "password": "password1"}
        try:
            _ = create_user_in_database(db.session, **data)
        except Exception as err:
            self.assertIsInstance(err, IntegrityError)

    def test_create_user_in_database(self):
        data = {"name": "user1", "email": "user1@email.com", "password": "password1"}
        msg = create_user_in_database(db.session, **data)
        self.assertTrue(msg == "user created ✅")

    def test_get_user_by_id_in_database(self):
        populate_db(db.session)
        user_id = 1
        user = get_user_by_id_in_database(db.session, user_id)
        self.assertIsNotNone(user)
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "user1")
        self.assertEqual(user.email, "user1@email.com")

    def test_get_user_by_email_in_database(self):
        populate_db(db.session)
        email = "user1@email.com"
        user = get_user_by_email_in_database(db.session, email)
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "user1")

    def test_get_all_users_in_database(self):
        populate_db(db.session)
        users = get_all_users_in_database(db.session)
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].name, 'user1')
        self.assertEqual(users[1].name, 'user2')



