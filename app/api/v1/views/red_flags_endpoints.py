from flask import make_response, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse

from app.api.v1.models.incident import IncidentModel

parser = reqparse.RequestParser()
parser.add_argument('incident_type', required=True, help='type cannot be blank')
parser.add_argument('location', required=True, help='location cannot be blank')
parser.add_argument('status', required=True, help='status cannot be blank')
parser.add_argument('image', required=True, help='image cannot be blank')
parser.add_argument('video', required=True, help='video cannot be blank')
parser.add_argument('comment', required=True, help='comments cannot be blank')


class RedFlags(Resource):
    @jwt_required
    def post(self):
        data = parser.parse_args()

        incident = IncidentModel(**data)
        incident.save()
        response = {
            "status": 201,
            "data": [{
                        "id": incident.id,
                        "message":  "Created red-flag record"
                    }]
                }

        return  make_response(jsonify(response),201)

    @jwt_required    
    def get(self):
        return make_response(jsonify({"red":
                                    [incident.json_maker() for incident in IncidentModel.get_incident()]
                                    }),200)



class UniqueRedFlag(Resource):
    @jwt_required
    def get(self,id):
        for incident in IncidentModel.get_incident():
            if incident.id == id:
                return make_response(jsonify(incident.json_maker()),200)

    @jwt_required
    def delete(self,id):
        i=0
        for flag in IncidentModel.get_incident():
            if flag.id == id:
                IncidentModel.get_incident().pop(i)
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
    @jwt_required
    def patch(self,id):
        data = parser.parse_args()
        incident = IncidentModel(**data)
        for flag in IncidentModel.get_incident():
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
    @jwt_required
    def patch(self,id):
        data = parser.parse_args()
        incident = IncidentModel(**data)
        for flag in IncidentModel.get_incident():
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
