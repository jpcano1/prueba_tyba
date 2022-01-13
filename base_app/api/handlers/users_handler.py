from base_app.core.helpers import BaseHandler

from ..executors import UserExecutor


class UsersHandler(BaseHandler):

    username: str
    password: str

    def handle_post(self) -> None:
        """POST create user."""
        UserExecutor.create_user(self.username, self.password)

        self.response = {"response": "User created! Please login"}

    def handle_login(self) -> None:
        """POST login user."""
        access_token = UserExecutor.login(self.username, self.password)

        self.response = {
            "access_token": access_token,
        }
