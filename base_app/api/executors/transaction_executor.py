from datetime import datetime
from http import HTTPStatus

from mongoengine import errors

from base_app.core.helpers import HandlerException
from base_app.core.services import get_restaurants

from ..models import Transaction
from ..models.embedded import Location
from .user_executor import UserExecutor


class TransactionExecutor:
    @staticmethod
    def get_restaurants(
        user_id: str,
        location_queried: dict[str, float],
        radius: int,
    ) -> Transaction:
        """
        Get all nearby restaurants.

        :param user_id: The id of the user
        :param location_queried: The main location
        :param radius: The radius of the query
        :return: The transaction
        """
        transaction = Transaction(
            user_id=user_id,
        )

        locations_found = get_restaurants(
            location=location_queried,
            radius=radius,
            open_now=True if 6 < datetime.now().hour < 20 else False,
        )

        transaction.location_queried = Location(
            latitude=location_queried["lat"],
            longitude=location_queried["lng"],
        )

        for loc in locations_found:
            transaction.locations_found.append(
                Location(
                    name=loc["name"],
                    latitude=loc["location"]["lat"],
                    longitude=loc["location"]["lng"],
                )
            )

        try:
            transaction.save()
            return transaction
        except errors.ValidationError as err:
            raise HandlerException(HTTPStatus.CONFLICT, err.to_dict())

    @staticmethod
    def get_transactions(user_id: str) -> list[Transaction]:
        """
        Obtain all transactions of a user by ID.

        :param user_id: The ID of the user
        :return: All the transactions associated to the user
        """
        transactions: list[Transaction] = Transaction.objects(user_id=user_id)
        return transactions
