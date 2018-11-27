from flask import make_response, jsonify, request, Response
from datetime import datetime
from flask_restful import Resource, Api, reqparse

red_flags = []


class RedFlags(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True, help='id cannot be blank')
        parser.add_argument('createdOn', required=True, help='createdOn cannot be blank')
        parser.add_argument('createdBy', required=True, help='createdby cannot be blank')
        parser.add_argument('type', required=True, help='type cannot be blank')
        parser.add_argument('location', required=True, help='location cannot be blank')
        parser.add_argument('Status', required=True, help='status cannot be blank')
        parser.add_argument('images', required=True, help='image cannot be blank')
        parser.add_argument('video', required=True, help='video cannot be blank')
        parser.add_argument('comments', required=True, help='comments cannot be blank')
        
    def post(self):
        request_data = request.get_json()
        new_red_flag = {
          "id": request_data['id'],
          "createdOn": request_data['createdOn'],
          "createdBy" : request_data['createdBy'],
          "type": request_data['type'],
          "location": request_data['location'],
          "status": request_data['status'],
          "images": request_data['images'],
          "video": request_data['video'],
          "comment": request_data['comment']
        }
        red_flags.insert(0,new_red_flag)
        response = {
            "status": 200,
            "data": [{
                        "id": new_red_flag["id"],
                        "message":  "Created red-flag record"
                    }]
                }

        return  make_response(jsonify(response),201)
    def get(self):
        return make_response(jsonify({"red-flags":red_flags}), 201)
    
