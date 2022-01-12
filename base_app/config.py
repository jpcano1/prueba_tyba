class Base:
    """Base config class."""

    SWAGGER = {
        "title": "Base flask app API",
        "uiversion": 3,
        "Description": "API Documentation for base app",
    }


class Production(Base):
    """Production config class."""

    ...


class Testing(Base):
    """Testing config class."""

    ...


class Staging(Base):
    """Staging config class."""

    ...
