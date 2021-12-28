from flask import Blueprint, request
from src.models import Product
from sqlalchemy.exc import IntegrityError
from . import return_200_response, handle_get_response, handle_get_multiple_values_response, return_400_response
from src.services import (create_new,
                        get_by_id,
                        get_by_name,
                        get_all,
                          )
from src.utils import parse_sqlalchemy_integrity_error_message

product = Blueprint("product", __name__, url_prefix="/product")


@product.route("/id=<id>")
def get_product_by_id(id: int):
    product_ = get_by_id(Product, id)
    return handle_get_response(Product, product_)


@product.route("/name=<name>")
def get_product_by_name(name: str):
    products = get_by_name(Product, name)
    return handle_get_multiple_values_response(Product, products)


@product.route("/")
def get_all_products():
    products = get_all(Product)
    return handle_get_multiple_values_response(Product, products)


@product.route("", methods=['POST'])
def create_product():
    user_data = request.get_json()
    try:
        result = create_new(Product, user_data)
        return return_200_response(result)
    except TypeError as err:
        return return_400_response(str(err))
    except IntegrityError as err:
        msg = parse_sqlalchemy_integrity_error_message(err)
        return return_400_response(msg)
