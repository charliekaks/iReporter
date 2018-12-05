"""App module: sets the configuration for the flask application"""

# Third party imports
import os
from flask import Flask
from instance.config import config
from flask_restful import Resource, Api
from .api.v1 import v1
from flask_jwt_extended import JWTManager

jwt = JWTManager()





def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config['testing'])
    jwt.init_app(app)
    # register blueprints
    app.register_blueprint(v1)
    app.config.from_pyfile('config.py')
    return app