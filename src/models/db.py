from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from typing import Any, List
from datetime import datetime


db = SQLAlchemy()
migrate = Migrate()


def objs_to_json(objs: Any) -> List[Any]:
    return [x.obj_to_json() for x in objs]


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(50))
    date_created = db.Column(db.TIMESTAMP)

    def enrich(self):
        self.date_created = datetime.now()

    def obj_to_json(self):
        return {"id": self.id,
                "name": self.name,
                "email": self.email,
                "password": self.password,
                "date_created": self.date_created,
                }


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    unit = db.Column(db.String(50))
    price = db.Column(db.FLOAT)
    date_created = db.Column(db.TIMESTAMP)

    def enrich(self):
        self.date_created = datetime.now()

    def obj_to_json(self):
        return {"id": self.id,
                "name": self.name,
                "unit": self.unit,
                "price": self.price,
                "date_created": self.date_created,
                }


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    total_price = db.Column(db.FLOAT)
    date_created = db.Column(db.TIMESTAMP)


class OrderProduct(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), primary_key=True)
    unit = db.Column(db.String(50))
    quantity = db.Column(db.Integer)