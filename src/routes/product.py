from flask import Blueprint, request, jsonify
from src.models import objs_to_json, Product
from src.services import (return_200_response,
                          create_new,
                        get_by_id,
                        get_by_name,
                        get_all,
                          )

product = Blueprint("product", __name__, url_prefix="/product")


@product.route("/id=<id>")
def get_product_by_id(id: int):
    product_ = get_by_id(Product, id)
    return product_.obj_to_json()


@product.route("/name=<name>")
def get_product_by_name(name: str):
    products = get_by_name(Product, name)
    return jsonify(objs_to_json(products))


@product.route("/")
def get_all_products():
    products = get_all(Product)
    return jsonify(objs_to_json(products))


@product.route("", methods=['POST'])
def create_product():
    result = create_new(Product, request.get_json())
    return return_200_response(result)