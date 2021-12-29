class Error(Exception):
    """Base class for all exceptions"""
    pass


class DataError(Error):
    """Raised for any error related to data issue"""
    pass


class DatabaseError(Error):
    """Raised for any error related to database issue"""
    pass
