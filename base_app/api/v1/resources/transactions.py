from http import HTTPStatus
from typing import Any

from flask_jwt_extended import jwt_required
from flask_restful import Resource, abort
from webargs import fields
from webargs.flaskparser import use_kwargs

from base_app.core.helpers import HandlerException

from ...handlers import TransactionsHandler


class Transaction(Resource):
    @jwt_required()
    @use_kwargs(
        {
            "lat": fields.Float(required=True, data_key="latitude"),
            "lng": fields.Float(required=True, data_key="longitude"),
            "radius": fields.Int(missing=200),
        },
        location="json",
    )
    def post(self, **kwargs: dict[str, Any]) -> tuple[dict[str, Any], int]:
        """
        Create transaction.

        ---
        tags:
          - Transactions
        parameters:
          - in: body
            name: body
            required: true
            schema:
                type: object
                properties:
                    latitude:
                        type: number
                        required: true
                    longitude:
                        type: number
                        required: true
                    radius:
                        type: number
                        required: false
        responses:
            201:
                description: Transaction created
        """
        handler = TransactionsHandler(**kwargs)
        try:
            handler.handle_post()
        except HandlerException as err:
            abort(err.code, error=err.message)
        return handler.response, HTTPStatus.CREATED

    @jwt_required()
    def get(self):
        """
        Get transaction list.

        ---
        tags:
          - Transactions
        responses:
            200:
                description: Transactions obtained
        """
        handler = TransactionsHandler()
        try:
            handler.handle_get()
        except HandlerException as err:
            abort(err.code, error=err.message)
        return handler.response, HTTPStatus.CREATED
