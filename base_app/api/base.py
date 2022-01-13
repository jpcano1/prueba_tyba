"""
File to create base app and other apps.

======================================
"""
from http import HTTPStatus
import os

from flasgger import Swagger
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from mongoengine import connect
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from ..config import Development, Production, Testing
from ..swagger import swagger_config, swagger_template


def init_app() -> Flask:
    """Initialize of base app."""
    flask_app = Flask(__name__, instance_relative_config=True)

    @flask_app.route("/")
    def health() -> tuple[str, int]:
        """
        Health check route.

        ---
        tags:
            - Health check
        responses:
            200:
                description: Hello world!
        """
        return "Hello World", HTTPStatus.OK

    if flask_app.env == "production":
        sentry_sdk.init(
            dsn=os.getenv("SENTRY_DSN"),
            integrations=[FlaskIntegration()],
            traces_sample_rate=0.01,
            environment=flask_app.env,
        )

        flask_app.config.from_object(Production)
    elif flask_app.env == "testing":
        flask_app.config.from_object(Testing)
    else:
        flask_app.config.from_object(Development)

    CORS(flask_app)
    Bcrypt(flask_app)
    JWTManager(flask_app)

    connect(host=flask_app.config["MONGO_DATABASE_URI"], alias="tyba-db")

    from .v1 import v1

    flask_app.register_blueprint(v1, url_prefix="/v1")

    Swagger(
        flask_app,
        template=swagger_template({}),
        config=swagger_config(),
    )

    return flask_app
