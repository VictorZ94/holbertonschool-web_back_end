#!/usr/bin/env python3
""" set up a basic Flask app
"""
from flask import (
                   Flask, jsonify, request, abort,
                   make_response,
                   redirect
)
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def welcome():
    """Create simple route
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def users():
    """Create User application
    """
    email = request.form.get('email')
    pwd = request.form.get('password')

    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def session():
    """ Create a session per user
    """
    email = request.form.get('email')
    pwd = request.form.get('password')
    check = AUTH.valid_login(email, pwd)
    if check:
        session_id = AUTH.create_session(email)
        result = make_response()
        result = jsonify({"email": f"{email}", "message": "logged in"})
        result.set_cookie("session_id", session_id)
        return result
    return abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Destroy session from API REST - logout
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user and session_id:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user and session_id:
        return jsonify({"email": f"{user.email}"})
    else:
        abort(403)


@app.route("/reset_password", methods=['POST'], strict_slashes=False)
def get_reset_password_token ():
    """ get reset password token
    """
    try:
        email = request.form.get('email')
        token = AUTH.get_reset_password_token(email)
    except Exception:
        abort(403)

    if token and email:
        return jsonify({"email": f"{email}", "reset_token": f"{token}"}), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
