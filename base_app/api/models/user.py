from typing import Any
from uuid import uuid4

from flask_bcrypt import check_password_hash, generate_password_hash
import mongoengine as me

from base_app.core.models.base import BaseDocument


class User(BaseDocument):
    id_ = me.UUIDField(default=uuid4, primary_key=True)
    username = me.StringField(required=True, unique=True)
    password = me.StringField(required=True)

    @staticmethod
    def generate_hash(password: str) -> Any:
        """
        Generate hash for the password in order to encrypt the hash.

        :param password: The password to be encrypted
        :return: The encrypted password
        """
        return generate_password_hash(password).decode("utf-8")

    @staticmethod
    def verify_hash(hash_: str, password: str) -> Any:
        """
        Verify the hash from the password in database.

        :param hash_: The hashed password
        :param password: The password to be verified
        :return: The verification
        """
        return check_password_hash(hash_, password)

    meta = {"collection": "users"}
