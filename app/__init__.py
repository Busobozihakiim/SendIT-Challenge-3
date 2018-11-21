from flask import Flask
from app.api.models import DatabaseOps
from .api import apiv2
from .api.config import configuration

def create_app(config_name):
    """create flask app and create the table"""
    app = Flask(__name__)
    app.config.from_object(configuration[config_name])
    app.register_blueprint(apiv2, url_prefix="/api/v2")
    database = DatabaseOps()
    database.connect_to_db()
    database.create_table()
    return app
