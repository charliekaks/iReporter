"""Create api version two blueprint."""
from flask import Blueprint
from flask_restful import Api
from .views.users import UserLogin, UserSignup
from .views.red_flag_endpoints import RedFlagsV2, UniqueRedFlagV2, LocationRedFlagV2, CommentRedFlagV2


v2 = Blueprint('v2', __name__, url_prefix='/api/v2')


api = Api(v2)
api.add_resource(RedFlagsV2, '/red-flags')
api.add_resource(UniqueRedFlagV2,'/red-flags/<int:id>')
api.add_resource(LocationRedFlagV2,'/red-flags/<int:id>/location')
api.add_resource(CommentRedFlagV2,'/red-flags/<int:id>/comment')
api.add_resource(UserLogin, "/auth/login")
api.add_resource(UserSignup, "/auth/register")



