import unittest
from src.models import db, Product
from src.mocks import FlaskSQLAlchemy, populate_db


class TestProductCrud(FlaskSQLAlchemy):
    def test_get_product_by_id_returns_json(self):
        populate_db()
        self.app = self.create_app().test_client()
        response = self.app.get("/product/id=1")
        payload = response.get_json()

        self.assertTrue(response.status_code == 200)
        self.assertIsInstance(payload, dict)
        self.assertEqual(payload.get('name'), "cheese")

    def test_get_product_by_name_returns_list_with_one_element_json(self):
        populate_db()
        self.app = self.create_app().test_client()
        response = self.app.get("/product/name=cheese")
        payload = response.get_json()
        self.assertTrue(response.status_code == 200)
        self.assertIsInstance(payload, list)
        self.assertEqual(payload[0].get('name'), "cheese")

    def test_get_all_products(self):
        populate_db()
        self.app = self.create_app().test_client()
        response = self.app.get("/product/")
        payload = response.get_json()
        self.assertEqual(len(payload), 3)
        self.assertEqual(payload[0].get("name"), 'cheese')
        self.assertEqual(payload[1].get("name"), 'ham')

    def test_create_product(self):
        self.app = self.create_app().test_client()
        response = self.app.post("/product/", json={"name": "cheese", "unit": "each","price": 2})
        msg = response.get_json().get("message")

        self.assertTrue(response.status_code == 200)
        self.assertTrue(msg == "product created ✅")
        new_product = self.app.get("/product/name=cheese").get_json()
        self.assertEqual(new_product[0].get("name"), "cheese")

    def test_create_product_incorrectly_invalid_column_name(self):
        self.app = self.create_app().test_client()
        response = self.app.post("/product/", json={"name": "cheese", "unit": "each", "price1": 2})
        msg = response.get_json().get("message")
        self.assertTrue(response.status_code == 400)
        self.assertTrue(msg == "'price1' is an invalid keyword argument for Product")

    def test_create_product_with_empty_not_nullable_condition_should_respond_with_400_and_informative_error_message(self):
        self.app = self.create_app().test_client()
        response = self.app.post("/product/", json={"name": "cheese", "unit": "each"})
        msg = response.get_json().get("message")
        self.assertTrue(response.status_code == 400)
        self.assertTrue(msg == "Column 'price' cannot be null")

    def test_get_product_by_id_when_id_does_not_exists_should_respond_with_200_and_nice_error_message(self):
        self.app = self.create_app().test_client()
        response = self.app.get("/product/id=1")
        payload = response.get_json()
        self.assertTrue(response.status_code == 200)
        self.assertTrue(payload.get("message") == f"No {Product.__name__} was found")

    def test_get_all_products_when_none_exist_should_respond_with_200_and_nice_response(self):
        self.app = self.create_app().test_client()
        response = self.app.get("/product/")
        payload = response.get_json()
        self.assertTrue(response.status_code == 200)
        self.assertTrue(payload.get("message") == f"No {Product.__name__} was found")

    def test_delete_product_by_id_should_return_200_response_when_successful(self):
        populate_db()
        self.app = self.create_app().test_client()
        response = self.app.delete("/product/id=1")
        msg = response.get_json().get("message")
        self.assertTrue(response.status_code == 200)
        self.assertTrue(msg == f"{Product.__name__.lower()} deleted ✅")

    def test_delete_product_by_id_should_return_400_response_when_unsuccessful_when_product_does_not_exist(self):
        self.app = self.create_app().test_client()
        response = self.app.delete("/product/id=1")
        msg = response.get_json().get("message")
        self.assertTrue(response.status_code == 400)
        self.assertTrue(msg == "No rows to delete")


if __name__ == '__main__':
    unittest.main()
