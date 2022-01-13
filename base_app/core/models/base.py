import json
from typing import Any

import mongoengine as me
import pydash as py_

from ..extensions import MongoSchemaEncoder, clean_dict


class BaseDocument(me.Document):

    meta: dict[str, Any] = {"abstract": True}

    def to_dict(self) -> dict[str, Any]:
        """
        Convert to dictionary a mongo object.

        :return: The mongo object converted to dictionary
        """
        to_pick = self.__class__._fields.keys()
        to_omit = []
        for field_name, field in self.__class__._fields.items():
            if hasattr(field, "dump") and (not field.dump):
                to_omit.append(field_name)

        mongo_dict_object: dict[str, Any] = json.loads(
            json.dumps(
                py_.omit(
                    py_.pick(clean_dict(self._data), *to_pick),
                    *to_omit,
                ),
                cls=MongoSchemaEncoder,
            )
        )
        return mongo_dict_object
