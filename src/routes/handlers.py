from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask import make_response, jsonify, Response
from src.models import db, objs_to_json
from typing import Any
from src.services import verify_get_response, create_new, delete_by_id
from src.utils import parse_sqlalchemy_integrity_error_message, DatabaseError


def handle_create_response(Model: db.Model, model: Any) -> Response:
    try:
        result = create_new(Model, model)
        return return_200_response(result)
    except TypeError as err:
        return return_400_response(str(err))
    except IntegrityError as err:
        msg = parse_sqlalchemy_integrity_error_message(err)
        return return_400_response(msg)


def handle_delete_response(Model: db.Model, param: Any) -> Response:
    try:
        result = delete_by_id(Model, param)
        return return_200_response(result)
    except DatabaseError as err:
        return return_400_response(str(err))


def handle_get_response(Model: db.Model, model: Any) -> Response:
    is_ok = verify_get_response(model)
    if is_ok:
        return model.obj_to_json()
    else:
        return return_200_response(f"No {Model.__name__} was found")


def handle_get_multiple_values_response(Model: db.Model, model: Any) -> Response:
    is_ok = verify_get_response(model)
    if is_ok:
        return jsonify(objs_to_json(model))
    else:
        return return_200_response(f"No {Model.__name__} was found")


def return_200_response(message: str) -> Response:
    return make_response(
        jsonify(
            {"message": message}
        ),
        HTTPStatus.OK,
    )


def return_400_response(message: str) -> Response:
    return make_response(
        jsonify(
            {"message": message}
        ),
        HTTPStatus.BAD_REQUEST
    )