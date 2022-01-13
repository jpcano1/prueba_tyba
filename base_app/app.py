from werkzeug.middleware.dispatcher import DispatcherMiddleware

from .api import init_app

app = init_app()

BASE_PATH = "/app"

app.wsgi_app = DispatcherMiddleware(  # type: ignore
    app.wsgi_app,
    {
        BASE_PATH: app,
    },
)
