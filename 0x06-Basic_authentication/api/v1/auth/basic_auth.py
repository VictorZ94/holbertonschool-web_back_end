#!/usr/bin/env python3
""" Implement a class for basic authentication
"""
from api.v1.auth.auth import Auth
from base64 import b64decode


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ it returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        elif not isinstance(base64_authorization_header, str):
            return None
        try:
            b64decode(base64_authorization_header)
        except Exception:
            return None
        return str(b64decode(base64_authorization_header), 'utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        elif not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        try:
            decoded_base64_authorization_header.split(":")[1]
            decode_base64 = decoded_base64_authorization_header.split(":")
            return (decode_base64[0], decode_base64[1])
        except Exception:
            return (None, None)
