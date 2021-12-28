from src.models import db, User, Product
from . import create_new, get_by_id, get_all, get_user_by_email, get_by_name, delete_by_id
from sqlalchemy.exc import IntegrityError
from src.mocks import FlaskSQLAlchemy, populate_db


class TestUserServices(FlaskSQLAlchemy):
    def test_create_user_duplicate_error(self):
        populate_db()
        data = {"name": "user1", "email": "user1@email.com", "password": "password1"}
        try:
            _ = create_new(User, data)
        except Exception as err:
            self.assertIsInstance(err, IntegrityError)

    def test_create_user(self):
        data = {"name": "user1", "email": "user1@email.com", "password": "password1"}
        msg = create_new(User, data)
        self.assertTrue(msg == "user created ✅")

    def test_get_user_by_id(self):
        populate_db()
        user_id = 1
        user = get_by_id(User, user_id)
        self.assertIsNotNone(user)
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "user1")
        self.assertEqual(user.email, "user1@email.com")

    def test_get_user_by_email(self):
        populate_db()
        email = "user1@email.com"
        user = get_user_by_email(email)
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "user1")

    def test_get_all_users(self):
        populate_db()
        users = get_all(User)
        self.assertEqual(len(users), 3)
        self.assertEqual(users[0].name, 'user1')
        self.assertEqual(users[1].name, 'user2')

    def test_get_user_by_name_when_name_is_unique(self):
        populate_db()
        name = "user1"
        users = get_by_name(User, name)
        self.assertIsNotNone(users)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, "user1")

    def test_get_user_by_name_when_name_is_not_unique(self):
        populate_db()
        name = "user2"
        users = get_by_name(User, name)
        self.assertIsNotNone(users)
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].email, "user2@email.com")
        self.assertEqual(users[1].email, "user3@email.com")


class TestProductServices(FlaskSQLAlchemy):
    def test_create_product(self):
        data = {"name": "cheese5","unit": "each","price": 2}
        msg = create_new(Product, data)
        self.assertTrue(msg == "product created ✅")

    def test_get_product_by_id(self):
        populate_db()
        product_id = 1
        product = get_by_id(Product, product_id)
        self.assertIsNotNone(product)
        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, "cheese")
        self.assertEqual(product.price, 2.0)

    def test_get_all_products(self):
        populate_db()
        products = get_all(Product)
        self.assertEqual(len(products), 3)
        self.assertEqual(products[0].name, 'cheese')
        self.assertEqual(products[1].name, 'ham')

    def test_get_product_by_name_when_name_is_unique(self):
        populate_db()
        name = "cheese"
        products = get_by_name(Product, name)
        self.assertIsNotNone(products)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, name)

    def test_get_product_by_name_when_name_is_not_unique(self):
        populate_db()
        name = "ham"
        products = get_by_name(Product, name)
        self.assertIsNotNone(products)
        self.assertEqual(len(products), 2)
        self.assertEqual(products[0].name, name)
        self.assertEqual(products[1].name, name)

    def test_delete_product_by_id(self):
        populate_db()
        product = get_by_id(Product, 1)
        self.assertIsNotNone(product)
        msg = delete_by_id(Product, 1)
        product = get_by_id(Product, 1)
        self.assertIsNone(product)

    def test_delete_product_by_id_when_id_does_not_exist(self):
        product = get_by_id(Product, 10)
        self.assertIsNone(product)
        msg = delete_by_id(Product, 10)
        self.assertIsInstance(msg, Exception)
        self.assertEqual(str(msg), "No rows to delete")