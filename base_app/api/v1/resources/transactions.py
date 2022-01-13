from http import HTTPStatus
from typing import Any

from flask_restful import Resource, abort
from webargs import fields
from webargs.flaskparser import use_kwargs

from base_app.core.helpers import HandlerException

from ...handlers import TransactionsHandler


class Transaction(Resource):
    @use_kwargs(
        {
            "lat": fields.Float(required=True, data_key="latitude"),
            "lng": fields.Float(required=True, data_key="longitude"),
        },
        location="json",
    )
    def post(self, **kwargs: dict[str, Any]) -> tuple[dict[str, Any], int]:
        handler = TransactionsHandler(**kwargs)
        try:
            handler.handle_post()
        except HandlerException as err:
            abort(err.code, error=err.message)
        return handler.response, HTTPStatus.CREATED
