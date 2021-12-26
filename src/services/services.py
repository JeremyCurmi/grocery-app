from http import HTTPStatus
from flask import make_response, jsonify


def return_200_response(message: str):
    return make_response(
        jsonify(
            {"message": message}
        ),
        HTTPStatus.OK,
    )