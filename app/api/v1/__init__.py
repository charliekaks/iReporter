"""Create api version one blueprint."""
from flask import Blueprint

from flask_restful import Api

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
from .views.red_flags_endpoints import RedFlags, UniqueRedFlag, LocationRedFlag, CommentRedFlag
from .views.users import SignIn, SignUp

api = Api(v1)

api.add_resource(RedFlags, '/red-flags')
api.add_resource(UniqueRedFlag,'/red-flags/<int:id>')
api.add_resource(LocationRedFlag,'/red-flags/<int:id>/location')
api.add_resource(CommentRedFlag,'/red-flags/<int:id>/comment')
api.add_resource(SignIn, "/auth/login")
api.add_resource(SignUp, "/auth/register")
