#!/usr/bin/env python3
""" Session authentication
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create session ID by user ID
        """
        if user_id is None and not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id