from flask import current_app, Blueprint, request, jsonify
from src.models import objs_to_json, User
from src.services import (create_new,
                          get_by_id,
                          get_user_by_email,
                          get_all,
                          return_200_response,
                          )

user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/id=<id>")
def get_user_by_id(id: int):
    user_ = get_by_id(User, id)
    return user_.obj_to_json()


@user.route("/email=<email>")
def get_user_by_email_(email: str):
    user_ = get_user_by_email(email)
    return user_.obj_to_json()


@user.route("/")
def get_all_users():
    users = get_all(User)
    return jsonify(objs_to_json(users))


@user.route("", methods=['POST'])
def create_user():
    result = create_new(User, request.get_json())
    return return_200_response(result)
