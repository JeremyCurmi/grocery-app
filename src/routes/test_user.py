import unittest
from src.models import db, User
from src.utils import FlaskSQLAlchemy, populate_db


class TestUserCrud(FlaskSQLAlchemy):
    def test_get_user_by_id_returns_json(self):
        populate_db(db.session)
        self.app = self.create_app().test_client()
        response = self.app.get("/user/id=1")
        message = response.get_json()

        self.assertTrue(response.status == "200 OK")
        self.assertIsInstance(message, dict)
        self.assertEqual(message.get('email'), "user1@email.com")

    def test_get_user_by_email_returns_json(self):
        populate_db(db.session)
        self.app = self.create_app().test_client()
        response = self.app.get("/user/email=user2@email.com")
        message = response.get_json()
        self.assertTrue(response.status == "200 OK")
        self.assertIsInstance(message, dict)
        self.assertEqual(message.get('email'), "user2@email.com")

    def test_get_all_users(self):
        populate_db(db.session)
        self.app = self.create_app().test_client()
        response = self.app.get("/user/")
        data = response.get_json()
        self.assertTrue(response.status == "200 OK")
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]["email"], "user1@email.com")
        self.assertEqual(data[1]["email"], "user2@email.com")

    def test_create_user(self):
        self.app = self.create_app().test_client()
        response = self.app.post("/user", json={"name":"name","email":"test@email.com","password":"password"})
        msg = response.get_json().get("message")

        self.assertTrue(response.status == "200 OK")
        self.assertTrue(msg == "user created ✅")
        new_user = self.app.get("/user/email=test@email.com").get_json()
        self.assertEqual(new_user.get("email"), "test@email.com")

    def test_get_user_by_email_when_email_does_not_exists_should_respond_with_200_and_nice_error_message(self):
        self.app = self.create_app().test_client()
        response = self.app.get("/user/email=email_does_not_exist")
        payload = response.get_json()
        self.assertTrue(response.status == "200 OK")
        self.assertTrue(payload.get("message") == f"No {User.__name__} was found")


if __name__ == '__main__':
    unittest.main()