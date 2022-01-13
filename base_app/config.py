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
    SECRET_KEY = "insecure_SLCFQf0rvt"
    SECURITY_PASSWORD_SALT = "insecure_d8GrdsUCCw"


class Production(Base):
    """Production config class."""

    MONGO_DATABASE_URI = os.getenv("MONGO_DATABASE_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT")


class Testing(Base):
    """Testing config class."""

    ...


class Staging(Base):
    """Staging config class."""

    ...
