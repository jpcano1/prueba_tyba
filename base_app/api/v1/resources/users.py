from http import HTTPStatus

from flask_restful import Resource, abort
from webargs import fields
from webargs.flaskparser import use_kwargs

from base_app.api.handlers import UsersHandler
from base_app.core.helpers import HandlerException


class User(Resource):
    @use_kwargs(
        {
            "username": fields.String(required=True),
            "password": fields.String(required=True),
        },
        location="json",
    )
    def post(self, **kwargs: dict[str, str]) -> tuple[dict[str, str], int]:
        """
        Create user.

        ---
        tags:
          - Users
        parameters:
          - in: body
            name: body
            required: true
            schema:
                type: object
                properties:
                    username:
                        type: string
                        required: true
                    password:
                        type: string
                        required: true
        responses:
            201:
                description: Movement created
        """
        handler = UsersHandler(**kwargs)
        try:
            handler.handle_post()
        except HandlerException as err:
            abort(err.code, error=err.message)
        return handler.response, HTTPStatus.CREATED


class Login(Resource):
    @use_kwargs(
        {
            "username": fields.String(required=True),
            "password": fields.String(required=True),
        },
        location="json",
    )
    def post(self, **kwargs: dict[str, str]) -> tuple[dict[str, str], int]:
        """
        Login user.

        ---
        tags:
          - Users
        parameters:
          - in: body
            name: body
            required: true
            schema:
                type: object
                properties:
                    username:
                        type: string
                        required: true
                    password:
                        type: string
                        required: true
        responses:
            201:
                description: Logged in
        """
        handler = UsersHandler(**kwargs)
        try:
            handler.handle_login()
        except HandlerException as err:
            abort(err.code, error=err.message)
        return handler.response, HTTPStatus.OK
