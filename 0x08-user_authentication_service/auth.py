#!/usr/bin/env python3
""" create password encrypted
"""
#import concrete
from db import DB
from user import User

# Universal importation
import bcrypt
import uuid

# from slqalchemy
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """create password encrypted
    """
    psw = password.encode('utf-8')
    hashed = bcrypt.hashpw(psw, bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register a new user
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            psw = _hash_password(password)
            new_user = self._db.add_user(email, psw)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Valid login user authentication
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return False

        if bcrypt.checkpw(password.encode('utf-8'),
                          user.hashed_password) and user:
            return True
        else:
            return False

    def _generate_uuid():
        """ generate a uniq identifier 
        """
        return uuid.uuid4()
