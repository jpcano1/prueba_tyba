from flask_jwt_extended import get_jwt_identity

from base_app.core.helpers import BaseHandler

from ..executors import TransactionExecutor


class TransactionsHandler(BaseHandler):
    radius: int
    lat: float
    lng: float

    def handle_post(self):
        user_id = get_jwt_identity()

        location_queried = {"lat": self.lat, "lng": self.lng}

        transaction = TransactionExecutor.get_restaurants(
            user_id=user_id,
            radius=self.radius,
            location_queried=location_queried,
        )

        self.response = transaction.to_dict()

    def handle_get(self):
        user_id = get_jwt_identity()

        transactions = TransactionExecutor.get_transactions(user_id)

        self.response = {"transactions": [transaction.to_dict() for transaction in transactions]}
