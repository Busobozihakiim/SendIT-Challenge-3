from flask import Flask
from .api import apiv2 as apiv2
from .api.config import configuration

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configuration[config_name])
    app.register_blueprint(apiv2, url_prefix="/api/v2")
    return app