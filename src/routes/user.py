from flask import current_app, Blueprint, request, jsonify
from src.models import objs_to_json

from src.services import (create_user_in_database,
                          get_user_by_id_in_database,
                          get_user_by_email_in_database,
                          get_all_users_in_database,
                          return_200_response,
                          )

user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/id=<id_>")
def get_user_by_id(id_: int):
    db_session = current_app.config['db'].session
    user_ = get_user_by_id_in_database(db_session, id_)
    return user_.obj_to_json()


@user.route("/email=<email>")
def get_user_by_email(email: str):
    db_session = current_app.config['db'].session
    user_ = get_user_by_email_in_database(db_session, email)
    return user_.obj_to_json()


@user.route("/")
def get_all_users():
    db_session = current_app.config['db'].session
    users = get_all_users_in_database(db_session)
    return jsonify(objs_to_json(users))


@user.route("", methods=['POST'])
def create_user():
    db_session = current_app.config['db'].session
    result = create_user_in_database(db_session, **request.get_json())
    return return_200_response(result)
