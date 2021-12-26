from datetime import datetime
from typing import Any, Tuple
from src.models import User


def add_user_to_database(db_session: Any, user: User):
    db_session.add(user)
    db_session.commit()


def create_user_in_database(db: Any, name, email, password: str) -> Tuple[str, Any]:
    try:
        user = User(name=name, email=email, password=password, date_created=datetime.now())
        add_user_to_database(db, user)
        return "user created", None
    except Exception as err:
        return "failed to create user", err


def get_user_by_id_in_database(db_session: Any, id: int) -> User:
    return db_session.query(User).filter_by(id=id).first()


def get_user_by_email_in_database(db_session: Any, email: int) -> User:
    return db_session.query(User).filter_by(email=email).first()
