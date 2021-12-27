import unittest
from src.models import db
from src.utils import FlaskSQLAlchemy, populate_db


class TestProductCrud(FlaskSQLAlchemy):
    def test_get_product_by_id_returns_json(self):
        populate_db(db.session)
        self.app = self.create_app().test_client()
        response = self.app.get("/product/id=1")
        payload = response.get_json()

        self.assertTrue(response.status == "200 OK")
        self.assertIsInstance(payload, dict)
        self.assertEqual(payload.get('name'), "cheese")

    def test_get_product_by_name_returns_list_with_one_element_json(self):
        self.fail()
    #
    # def test_get_all_products(self):
    #     self.fail()
    #
    # def test_create_product(self):
    #     self.fail()


if __name__ == '__main__':
    unittest.main()
