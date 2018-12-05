"""App module: sets the configuration for the flask application"""

# Third party imports
from flask import Flask
from flask_jwt_extended import JWTManager

from instance.config import config
from .api.v1 import v1
from .api.version2 import v2
from .db_config import create_tables
jwt = JWTManager()





def create_app(config_name="development"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config['development'])
    app.config.from_pyfile('config.py')
    create_tables()
    jwt.init_app(app)
    # register blueprints
    app.register_blueprint(v1)
    app.register_blueprint(v2)
    return app