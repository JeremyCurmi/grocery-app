from src.models import User
from src.models import db


def get_user_by_email(email: str) -> User:
    return db.session.query(User).filter_by(email=email).first()
