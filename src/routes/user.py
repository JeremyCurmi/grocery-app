from flask import Blueprint, request
from src.models import User
from . import handle_create_response, handle_get_response, handle_get_multiple_values_response, handle_delete_response
from src.services import (get_by_id,
                          get_user_by_email,
                          get_all,
                          )


user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/id=<int:id_>")
def get_user_by_id(id_: int):
    user_ = get_by_id(User, id_)
    return handle_get_response(User, user_)


@user.route("/email=<string:email>")
def get_user_by_email_(email: str):
    user_ = get_user_by_email(email)
    return handle_get_response(User, user_)


@user.route("/")
def get_all_users():
    users = get_all(User)
    return handle_get_multiple_values_response(User, users)


@user.route("/", methods=['POST'])
def create_user():
    user_data = request.get_json()
    return handle_create_response(User, user_data)


@user.route("/id=<int:id_>", methods=["DELETE"])
def delete_user(id_: int):
    return handle_delete_response(User, id_)
