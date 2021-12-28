from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from src.models import User
from . import return_200_response, handle_get_response, handle_get_multiple_values_response, return_400_response
from src.services import (create_new,
                          get_by_id,
                          get_user_by_email,
                          get_all,
                          )
from src.utils import parse_sqlalchemy_integrity_error_message


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
    user_data = request.get_json()
    try:
        result = create_new(User, user_data)
        return return_200_response(result)
    except TypeError as err:
        return return_400_response(str(err))
    except IntegrityError as err:
        msg = parse_sqlalchemy_integrity_error_message(err)
        return return_400_response(msg)