import unittest
from src.app import create_app
from src.config import get_config


class TestUserCrud(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app(get_config(is_test=True)).test_client()

    def test_get_user(self):
        self.fail()

    def test_create_user(self):
        response = self.app.post("/user", json={"name":"name","email":"test@email.com","password":"password"})
        message = response.get_json().get("message")
        self.assertTrue(response.status == "200 OK")
        self.assertTrue(message == "user created")
        # assert that row has been included


if __name__ == '__main__':
    unittest.main()
