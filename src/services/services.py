from http import HTTPStatus
from flask import make_response, jsonify, Response
from typing import Any, List
from src.models import db


def create_new(Model: db.Model, data: dict):
    model = Model(**data)
    model.enrich()
    db.session.add(model)
    db.session.commit()
    return f"{Model.__name__.lower()} created ✅"


def get_by_id(Model: db.Model, id_: int) -> db.Model:
    return db.session.query(Model).filter_by(id=id_).first()


def get_all(Model: db.Model) -> List[db.Model]:
    return db.session.query(Model).all()


def get_by_name(Model: db.Model, name: str) -> List[db.Model]:
    return db.session.query(Model).filter_by(name=name).all()


def return_200_response(message: str) -> Response:
    return make_response(
        jsonify(
            {"message": message}
        ),
        HTTPStatus.OK,
    )
