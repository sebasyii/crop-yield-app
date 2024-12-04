from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

from app.config import Config
from app.middleware import PrefixMiddleware
from app.routes import register_routes


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    Bootstrap5(app)
    CSRFProtect(app)

    # set voc=False if you run on local computer
    app.wsgi_app = PrefixMiddleware(app.wsgi_app, voc=False)

    # Register routes
    register_routes(app)

    return app
