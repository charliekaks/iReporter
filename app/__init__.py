"""App module: sets the configuration for the flask application"""

# Third party imports
from flask import Flask
from instance.config import app_config
from flask_restful import Resource, Api
from .api.v1 import v1
#from db_config import create_tables



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    # register blueprints
    app.register_blueprint(v1)
    app.config.from_pyfile('config.py')
    return app