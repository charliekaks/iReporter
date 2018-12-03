from flask import make_response, jsonify, request, Response
from datetime import datetime
from flask_restful import Resource, Api, reqparse
from app.api.v1.models.red_flag import RedFlagsModel
import jwt , datetime
from functools import wraps



parser = reqparse.RequestParser()
parser.add_argument('incident_type', required=True, help='type cannot be blank')
parser.add_argument('location', required=True, help='location cannot be blank')
parser.add_argument('status', required=True, help='status cannot be blank')
parser.add_argument('image', required=True, help='image cannot be blank')
parser.add_argument('video', required=True, help='video cannot be blank')
parser.add_argument('comment', required=True, help='comments cannot be blank')


class RedFlags(Resource):   
    def post(self):
        data = parser.parse_args()

        incident = RedFlagsModel(**data)
        incident.save()
        response = {
            "status": 201,
            "data": [{
                        "id": incident.id,
                        "message":  "Created red-flag record"
                    }]
                }

        return  make_response(jsonify(response),201)
        
    def get(self):
        return make_response(jsonify({"red":
                                    [incident.json_maker() for incident in RedFlagsModel.get_red_flags()]
                                    }),200)

class UniqueRedFlag(Resource):
    def get(self,id):
        for incident in RedFlagsModel.get_red_flags():
            if incident.id == id:
                return make_response(jsonify(incident.json_maker()),200)

    
    def put(self,id):
        data = parser.parse_args()
        incident = RedFlagsModel(**data)
        incident.save()
        updated_red_flag = incident
        i = 0
        for flag in RedFlagsModel.get_red_flags():
            currentFlag = flag.id
            if currentFlag == id:
                RedFlagsModel.get_red_flags()[i] = updated_red_flag.json_maker()
            i+=1
        response = {
            "status": 200,
            "data": [{
                        "id": updated_red_flag.id,
                        "message":  "successfully editted a red-flag record"
                    }]
        }  
        return  make_response(jsonify(response),201)  


    def delete(self,id):
        i=0
        for flag in RedFlagsModel.get_red_flags():
            if flag.id == id:
                RedFlagsModel.get_red_flags().pop(i)
            i+=1
        response = {
            "status": 200,
            "data": [{
                        "id": id,
                        "message":  "successfully deleted a red-flag record"
                    }]
        }  
        return  make_response(jsonify(response),201)  

class LocationRedFlag(Resource):
    def patch(self,id):
        data = parser.parse_args()
        incident = RedFlagsModel(**data)
        for flag in RedFlagsModel.get_red_flags():
            if flag.id == id:
                flag.update_incident_location(incident.location,id)
                flag.save()
        
        response = {
            "status": 200,
            "data": [{
                        "id": id,
                        "message":  "successfully updated location of a red-flag record"
                    }]
        }  
        return  make_response(jsonify(response),201)  


class CommentRedFlag(Resource):
    def patch(self,id):
        data = parser.parse_args()
        incident = RedFlagsModel(**data)
        for flag in RedFlagsModel.get_red_flags():
            if flag == id:
                flag.update_incident_comment(incident.comment,id)
                flag.save()
        
        response = {
            "status": 200,
            "data": [{
                        "id": id,
                        "message":  "successfully updated comment of a red-flag record"
                    }]
        }  
        return  make_response(jsonify(response),201)  
