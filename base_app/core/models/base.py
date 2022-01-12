# import json
from typing import Any

import mongoengine as me

# import pydash as py_


class BaseDocument(me.Document):

    meta: dict[str, Any] = {"abstract": True}

    # def to_dict(self):
    #     to_pick = self.__class__._fields.keys()
    #
    #     to_omit = []
    #     for field_key, field_value in self.__class__._fields.items():
    #         if hasattr(field_value, "dump") and (not field_value.dump):
    #             to_omit.append(field_key)
    #     return json.loads(
    #         json.dumps(
    #             py_.omit(
    #                 py_.pick(clean)
    #             )
    #         )
    #     )
