import os


class Base:
    """Base config class."""

    SWAGGER = {
        "title": "Base flask app API",
        "uiversion": 3,
        "Description": "API Documentation for base app",
    }


class Development(Base):
    """Development config class."""

    MONGO_DATABASE_URI = os.getenv("MONGO_DATABASE_URI", "")


class Production(Base):
    """Production config class."""

    MONGO_DATABASE_URI = os.getenv("MONGO_DATABASE_URI", "")


class Testing(Base):
    """Testing config class."""

    ...


class Staging(Base):
    """Staging config class."""

    ...
