from flask import Blueprint, request
from src.models import User
from . import return_200_response, handle_get_response, handle_get_multiple_values_response
from src.services import (create_new,
                          get_by_id,
                          get_user_by_email,
                          get_all,
                          )

user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/id=<id>")
def get_user_by_id(id: int):
    user_ = get_by_id(User, id)
    return handle_get_response(User, user_)


@user.route("/email=<email>")
def get_user_by_email_(email: str):
    user_ = get_user_by_email(email)
    return handle_get_response(User, user_)


@user.route("/")
def get_all_users():
    users = get_all(User)
    return handle_get_multiple_values_response(User, users)


@user.route("", methods=['POST'])
def create_user():
    result = create_new(User, request.get_json())
    return return_200_response(result)
