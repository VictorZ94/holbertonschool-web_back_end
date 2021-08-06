#!/usr/bin/env python3
""" Implement a class for basic authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Implement a class for basic authentication
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ It returns the Base64 part of the Authorization
        """
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        elif not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header.split()[1]
