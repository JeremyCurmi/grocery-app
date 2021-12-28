from sqlalchemy.exc import IntegrityError


def parse_sqlalchemy_integrity_error_message(err: IntegrityError) -> str:
    return err.args[0].split('(')[-1].split(',')[-1][:-1].split('"')[1]
