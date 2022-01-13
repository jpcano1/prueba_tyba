import os


class Base:
    """Base config class."""

    SWAGGER = {
        "title": "Tyba app API",
        "uiversion": 3,
        "Description": "API Documentation for base app",
    }

    MONGO_DATABASE_URI = os.getenv("MONGO_DATABASE_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT")


class Development(Base):
    """Development config class."""

    ...


class Production(Base):
    """Production config class."""

    ...


class Testing(Base):
    """Testing config class."""

    ...


class Staging(Base):
    """Staging config class."""

    ...
