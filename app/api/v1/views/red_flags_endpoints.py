from flask import make_response, jsonify, request, Response
from datetime import datetime
from flask_restful import Resource, Api, reqparse
from app.api.v1.models.Red_Flag import RedFlagsModel

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

class UniqueRedFlag(Resource):
    def get(self,id):
        return_value = {}
        for flag in red_flags:
            if flag["id"] == id:
                return_value = {
                    "id": flag['id'],
                    "createdOn": flag['createdOn'],
                    "createdBy" : flag['createdBy'],
                    "type": flag['type'],
                    "location": flag['location'],
                    "status": flag['status'],
                    "images": flag['images'],
                    "video": flag['video'],
                    "comment": flag['comment']
                }
        return make_response(jsonify(return_value),200)
    
    def put(self,id):
        request_data = request.get_json()
        updated_red_flag = {
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
        i = 0
        for flag in red_flags:
            currentFlag = flag["id"]
            if currentFlag == id:
                red_flags[i] = updated_red_flag
            i+=1
        response = {
            "status": 200,
            "data": [{
                        "id": updated_red_flag["id"],
                        "message":  "successfully editted a red-flag record"
                    }]
        }  
        return  make_response(jsonify(response),201)  


    def delete(self,id):
        i=0
        for flag in red_flags:
            if flag["id"] == id:
                red_flags.pop(i)
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
        request_data = request.get_json()
        updated_location = {}
        if "location" in request_data:
            updated_location["location"] = request_data["location"]
        for flag in red_flags:
            if flag["id"] == id:
                flag.update(updated_location)
        
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
        request_data = request.get_json()
        updated_comment = {}
        if "comment" in request_data:
            updated_comment["comment"] = request_data["comment"]
        for flag in red_flags:
            if flag["id"] == id:
                flag.update(updated_comment)
        
        response = {
            "status": 200,
            "data": [{
                        "id": id,
                        "message":  "successfully updated comment of a red-flag record"
                    }]
        }  
        return  make_response(jsonify(response),201)  
