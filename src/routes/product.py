from flask import Blueprint, request, render_template
from src.models import Product
from . import handle_get_response, handle_get_multiple_values_response, handle_create_response, handle_delete_response
from src.services import (get_by_id,
                        get_by_name,
                        get_all,
                          )

product = Blueprint("product", __name__, url_prefix="/product")


@product.route("")
def index():
    return render_template("product.html",
                           page_title="Products")


@product.route("/id=<int:id_>")
def get_product_by_id(id_: int):
    product_ = get_by_id(Product, id_)
    return handle_get_response(Product, product_)


@product.route("/name=<string:name>")
def get_product_by_name(name: str):
    products = get_by_name(Product, name)
    return handle_get_multiple_values_response(Product, products)


@product.route("/")
def get_all_products():
    products = get_all(Product)
    return handle_get_multiple_values_response(Product, products)


@product.route("/", methods=['POST'])
def create_product():
    product_data = request.get_json()
    return handle_create_response(Product, product_data)


@product.route("/id=<int:id_>", methods=["DELETE"])
def delete_product(id_: int):
    return handle_delete_response(Product, id_)
