#!/usr/bin/env python3
""" create password encrypted
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """create password encrypted
    """
    psw = password.encode('utf-8')
    hashed = bcrypt.hashpw(psw, bcrypt.gensalt())
    return hashed
