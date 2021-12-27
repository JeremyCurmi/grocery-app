from http import HTTPStatus
from flask import make_response, jsonify, Response


def return_200_response(message: str) -> Response:
    return make_response(
        jsonify(
            {"message": message}
        ),
        HTTPStatus.OK,
    )