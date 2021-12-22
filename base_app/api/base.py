"""
File to create base app and other apps
======================================
"""
from flask import Flask
from http import HTTPStatus
from flask_cors import CORS


def init_app() -> Flask:
    """
    Base app initializer
    """
    flask_app = Flask(__name__, instance_relative_config=True)

    @flask_app.route("/")
    def health() -> tuple[str, int]:
        """
        Health check route
        """
        return "Hello World", HTTPStatus.OK

    CORS(flask_app)

    return flask_app
