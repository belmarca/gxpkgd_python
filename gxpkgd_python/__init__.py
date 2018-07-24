"""gxpkgd_python app factory"""
from flask import Flask

from gxpkgd_python.app import register_extensions, register_blueprints
from gxpkgd_python.routes import *


def create_app(config_file=None):
    app = Flask(__name__)

    if config_file is not None:
        app.config.from_pyfile(config_file)

    register_extensions(app)
    register_blueprints(app)

    return app
