import datetime
import json
from typing import Any
from uuid import UUID

import bson
import mongoengine as me

from .parser import clean_dict


class MongoSchemaEncoder(json.JSONEncoder):
    def default(self, object_: Any) -> Any:
        """
        Encode data inside a custom Mongo Schema.

        :param object_: The object to be parsed
        :return:
        """
        if isinstance(object_, me.EmbeddedDocument):
            return clean_dict(object_._data)
        if isinstance(object_, (datetime.datetime, datetime.date, datetime.time)):
            return object_.isoformat()
        if isinstance(object_, UUID):
            return str(object_)
        if isinstance(object_, bson.objectid.ObjectId):
            return str(object_)
        if isinstance(object_, bson.dbref.DBRef):
            return object_.id
        if isinstance(object_, me.Document):
            return object_.id
        return super().default(object_)
