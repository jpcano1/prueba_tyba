from datetime import datetime
from uuid import uuid4

from mongoengine import fields

from base_app.core.models.base import BaseDocument

from .embedded import Location
from .user import User


class Transaction(BaseDocument):

    transaction_id = fields.UUIDField(default=uuid4, primary_key=True)
    created_at = fields.DateTimeField(default=datetime.utcnow)
    user_id = fields.StringField(required=True)
    location_queried = fields.EmbeddedDocumentField(Location)
    locations_found = fields.EmbeddedDocumentListField(Location)

    meta = {"collection": "transactions", "db_alias": "tyba-db"}
