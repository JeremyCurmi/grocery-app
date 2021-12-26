from flask import current_app, Blueprint, request

from src.services import create_user_in_database, return_200_response

user = Blueprint("user", __name__, url_prefix="/user")


@user.route("")
def get_user():
    pass


@user.route("", methods=['POST'])
def create_user():
    db_session = current_app.config['db'].session
    result, err = create_user_in_database(db_session, **request.get_json())
    if err:
        return "I should create error handler here"
    return return_200_response("user created")


