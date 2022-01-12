class HandlerException(Exception):
    """Base class for exception handling."""

    def __init__(self, code: int, message: str):
        super().__init__(message)
        self.code = code
        self.message = message
