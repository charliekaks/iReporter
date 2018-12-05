import datetime
import json
import re

from flask import request, jsonify, make_response
from flask_jwt_extended import create_access_token
# third party imports
from flask_restful import Resource
from werkzeug.exceptions import BadRequest, Unauthorized

# local Imports
from ..models.user import UserModel


class UserSignup(Resource):
    def post(self):
        user_details = request.get_json()
        user = {
            "username" : user_details['username'].strip(),
            "firstname" : user_details['firstname'].strip(),
            "lastname" : user_details['lastname'].strip(),
            "phoneNumber" : user_details['phoneNumber'].strip(),
            "othernames" : user_details['othernames'].strip(),
            "email" : user_details['email'].strip(),
            "password" : user_details['password'].strip()  
        }
        user_model = UserModel(**user)
        user_model.save_user()
        resp = {
            "message": "User signed up successfully",
            "username": user_model.username
        }
        return make_response(jsonify(resp), 201)



class UserLogin(Resource):
    def post(self):
        req_data = request.get_json()
        login_details = {
            "username": req_data['username'],
            "password": req_data['password']
        }
        # locate user in db
        user = UserModel(**login_details)
        user_record = user.get_by_username(login_details["username"])
        if not user_record:
            raise Unauthorized('Your details were not found, please sign up')
        firstname = user.get_first_name(login_details["username"])
        lastname = user.get_last_name(login_details["username"])
        registered = user.get_date_created(login_details["username"])
        if not user.authenticate_password(login_details["password"]):
            raise Unauthorized("The username or password is incorrect")
        name = "{}{}".format(lastname, firstname)
        expire_time = datetime.timedelta(minutes=75)
        token = create_access_token(user.username, expires_delta=expire_time)   
        resp ={
            "message":"success",
            "AuthToken":token,
            "name":name,
            "date_created":registered
        }
        return make_response(jsonify(resp), 200)