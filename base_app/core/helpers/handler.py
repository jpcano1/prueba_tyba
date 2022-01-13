from typing import Any


class BaseHandler:
    def __init__(self, **kwargs):
        self._kwargs: dict[str, Any] = kwargs
        self.response: dict[str, Any] = {}
        self.__parse_kwargs()

    def handle_post(self):
        """Handle Post."""
        ...

    def handle_get(self):
        """Handle Get."""
        ...

    def __parse_kwargs(self):
        for key, value in self._kwargs.items():
            setattr(self, key, value)
