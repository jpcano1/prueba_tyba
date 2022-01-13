import mongoengine as me
from mongoengine import fields


class Location(me.EmbeddedDocument):
    name = fields.StringField()
    latitude = fields.FloatField()
    longitude = fields.FloatField()
