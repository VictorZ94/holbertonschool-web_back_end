#!/usr/bin/env python3
""" log message obfuscated
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ password encrypted
    """
    password = password.encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed
