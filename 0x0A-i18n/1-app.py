#!/usr/bin/env python3
""" Simple message of welcoming
Description:
    to start working models i18n and l10n
"""

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    """ config all objects to translate
    """
    LANGUAGES = ["en", "fr"]

app.config['BABEL_DEFAULT_LOCALE'] = Config.LANGUAGES[0]
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

