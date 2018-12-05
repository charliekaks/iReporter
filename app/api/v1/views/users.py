import datetime
from flask import make_response, jsonify, request, Response
from flask_restful import Resource, reqparse
from app.api.v1.models.user import UserModel
from flask_jwt_extended import create_access_token

parser = reqparse.RequestParser(bundle_errors=True)



class SignIn(Resource):
    parser.add_argument('username', type=str, required=True, help='This field cannot be left blank!')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank!')
    def post(self):
        request_data = parser.parse_args()

        logged_user = UserModel.find_user(request_data['username'])

        if logged_user and logged_user.authenticate_password(password=request_data["password"]):
            expire_time = datetime.timedelta(minutes=60)
            token = create_access_token(logged_user.username, expires_delta=expire_time, )
            result = {"status": 200,
                    'token': token,
                    "data": [{
                        'message': f'You were successfully'
                        f' logged in {logged_user.username}'
                    }]}
            return make_response(jsonify(result), 200)

        result = {"status": 400,
                "data": [{
                    "message": "A user with that username doesn't exists"
                }]}
        return make_response(jsonify(result), 400)

    def get(self):
        return make_response(jsonify({"users":
                                    [user.json_maker() for user in UserModel.get_users()]
                                    }),200)


class SignUp(Resource):
    parser.add_argument('firstname', type=str, default="", help='This field can be left blank!')
    parser.add_argument('lastname', type=str, default="", help='This field can be left blank!')
    parser.add_argument('othernames', type=str, default="", help='This field can be left blank!')
    parser.add_argument('email', type=str, default="", help='This field can be left blank!')
    parser.add_argument('phoneNumber', type=str, default="", help='This field can be left blank!')
    parser.add_argument('username', type=str, default="",help='This field can be left blank!')
    parser.add_argument('password', type=str, default="",help='This field can be left blank!')

    def post(self):
        request_data = parser.parse_args()
        user_exists = UserModel.check_user(request_data['username'])
        if user_exists == True:
            result = {"status": 400,
                    "data": [{
                        "message": "A user with that username already exists"
                    }]}
            return make_response(jsonify(result), 400)

        user_data = UserModel(**request_data)
        user_data.save()
        result = {"status": 201,
                "data": [{
                    "message": "User created Successfully."
                }]}
        return make_response(jsonify(result), 201)
