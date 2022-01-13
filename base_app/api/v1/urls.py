from flask import Blueprint
from flask_restful import Api

from .resources import users

#####################################################
#                   IMPORT ROUTES                   #
#####################################################


#####################################################
#                       ROUTES                      #
#####################################################

v1 = Blueprint("v1", __name__)
api = Api(v1, catch_all_404s=True)


api.add_resource(users.User, "/users", endpoint="users")
