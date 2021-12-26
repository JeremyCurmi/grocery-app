from unittest import TestCase
from src.app import create_app
from src.config import get_config


class TestHomePage(TestCase):

    def setUp(self) -> None:
        self.app = create_app(get_config(is_test=True)).test_client()

    def test_index_exists_and_returns_200(self):
        response = self.app.get("/")
        self.assertTrue(response.status == "200 OK")