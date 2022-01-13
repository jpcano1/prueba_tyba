from flask import Blueprint
from flask_restful import Api

from .resources import transactions, users

v1 = Blueprint("v1", __name__)
api = Api(v1, catch_all_404s=True)

"""
Users
"""
api.add_resource(users.User, "/users", endpoint="users")

api.add_resource(users.Login, "/login", endpoint="login")


"""
Transactions
"""

api.add_resource(transactions.Transaction, "/transactions", endpoint="transaction")
