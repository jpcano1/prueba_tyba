from base_app.core.helpers import BaseHandler

from ..executors import UserExecutor


class UsersHandler(BaseHandler):

    username: str
    password: str

    def handle_post(self) -> None:
        user_created = UserExecutor.create_user(self.username, self.password)

        self.response = user_created.to_json()
