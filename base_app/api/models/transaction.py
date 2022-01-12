from datetime import datetime

from mongoengine import fields

from base_app.core.models.base import BaseDocument

from .embedded import Location
from .user import User


class Transaction(BaseDocument):

    id = fields.UUIDField()
    created_at = fields.DateTimeField(default=datetime.utcnow)
    user_id = fields.ReferenceField(User, reverse_delete_rule=2)
    location_queried = fields.EmbeddedDocumentField(Location)
    locations_found = fields.EmbeddedDocumentListField(Location)

    meta = {"collection": "transactions"}
