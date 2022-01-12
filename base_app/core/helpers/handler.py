import abc
from abc import ABC


class BaseHandler(ABC):
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.response = None

    @abc.abstractmethod
    def handle_post(self):
        """Handle Post."""
        ...

    @abc.abstractmethod
    def handle_get(self):
        """Handle Get."""
        ...

    def __parse_kwargs(self):
        for key, value in self._kwargs.items():
            setattr(self, key, value)
