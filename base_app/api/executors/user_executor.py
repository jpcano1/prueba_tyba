from http import HTTPStatus

from mongoengine import errors

from base_app.core.helpers import HandlerException

from ..models import User


class UserExecutor:
    @staticmethod
    def create_user(
        username: str,
        password: str,
    ) -> User:
        """
        Create a new user.

        :param username: The username
        :param password: The password
        :return: The user created
        """
        hashed_password = User.generate_hash(password)
        new_user = User(username=username, password=hashed_password)
        try:
            new_user.save()
            return new_user
        except errors.ValidationError as err:
            raise HandlerException(HTTPStatus.BAD_REQUEST, err.to_dict())

    @staticmethod
    def get_user(username: str) -> User:
        """
        Obtain a user.

        :param username: The username of the user to be found
        :return: The user retrieved
        """
        try:
            user: User = User.objects(username=username).get()
            return user
        except errors.DoesNotExist:
            raise HandlerException(HTTPStatus.NOT_FOUND, "User does not exists")
