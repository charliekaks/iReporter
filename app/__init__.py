"""App module: sets the configuration for the flask application"""

# Third party imports
from flask import Flask
from instance.config import app_config
from flask_restful import Api, Resource

from .api.v1.views.red_flags_endpoints import RedFlags, UniqueRedFlag



def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(RedFlags, '/red-flags')
    api.add_resource(UniqueRedFlag,'/red-flags/<int:id>')
    return app