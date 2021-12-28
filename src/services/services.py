from typing import Any, List, Union
from src.models import db


def create_new(Model: db.Model, data: dict) -> str:
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


def delete_by_id(Model: db.Model, id_: int) -> Union[Exception, str]:
    rows_affected = db.session.query(Model).filter_by(id=id_).delete()
    db.session.commit()
    if rows_affected == 0:
        return Exception("No rows to delete")
    return f"{Model.__name__.lower()} deleted ✅"


def verify_get_response(model: Any) -> bool:
    if any([model is None, model == []]):
        return False
    return True
