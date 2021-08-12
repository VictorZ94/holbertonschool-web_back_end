#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
if getenv("AUTH_TYPE") == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()

if getenv("AUTH_TYPE") == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

if getenv("AUTH_TYPE") == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()

if getenv("AUTH_TYPE") == 'session_exp_auth':
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(unauthorized) -> str:
    """ Not authorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(forbidden) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_method():
    """ validate before request
    """
    list_path = ['/api/v1/status/',
                 '/api/v1/unauthorized/',
                 '/api/v1/forbidden/',
                 '/api/v1/auth_session/login/']
    if auth is None:
        return
    if not auth.require_auth(request.path, list_path):
        return
    if auth.authorization_header(request) is None \
       and auth.session_cookie(request) is None:
        return abort(401)

    user = auth.current_user(request)
    if user is None:
        return abort(403)
    else:
        request.current_user = user


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
