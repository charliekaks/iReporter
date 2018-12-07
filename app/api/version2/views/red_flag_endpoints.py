from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import  jwt_required

from app.api.version2.models.incident import IncidentModel

parser = reqparse.RequestParser()
parser.add_argument('incident_type', required=True, help='type cannot be blank')
parser.add_argument('location', required=True, help='location cannot be blank')
parser.add_argument('status', required=True, help='status cannot be blank')
parser.add_argument('image', required=True, help='image cannot be blank')
parser.add_argument('video', required=True, help='video cannot be blank')
parser.add_argument('comment', required=True, help='comments cannot be blank')


class RedFlagsV2(Resource): 
    @jwt_required  
    def post(self):
        data = parser.parse_args()
        incident = IncidentModel(**data)
        incident.save_incident()
        resp = {
            "status": 201,
            "data": [{
                        "id": incident.id,
                        "message":  "Created red-flag record"
                    }]
                }

        return  make_response(jsonify(resp),201)

    @jwt_required    
    def get(self):
        incident = IncidentModel()
        all_incidents = incident.get_all_incidents()
        return make_response(jsonify({"flags":all_incidents}), 200)
        



class UniqueRedFlagV2(Resource):
    @jwt_required
    def get(self,id):
        incident = IncidentModel()
        incident_searched = incident.get_specific_incident(id)
        return dict(incident=incident_searched, status="ok"), 200
        

    @jwt_required
    def delete(self,id):
        check = IncidentModel.find_if_user_exists_by_id(id)
        if check:
            IncidentModel.delete_flag(id)
            response = {
            "status": 200,
            "data": [{
                        "id": id,
                        "message":  "successfully deleted a red-flag record"
                    }]
            }  
            return  make_response(jsonify(response),201)
        response = {
            "status" : 404,
            "data": [{
                        "id": id,
                        "message":  "red_flag not found in the database"
                    }]
            }  
        return  make_response(jsonify(response),404)
        

class LocationRedFlagV2(Resource):
    @jwt_required
    def patch(self,id):
        check = IncidentModel.find_if_user_exists_by_id(id)
        if check:
            data = parser.parse_args()
            IncidentModel.update_location(data, id)
            response = {
            "status": 200,
            "data": [{
                        "id": id,
                        "message":  "successfully updated location of a red-flag record"
                    }]
            }  
            return  make_response(jsonify(response),201)  



class CommentRedFlagV2(Resource):
    @jwt_required
    def patch(self,id):
        check = IncidentModel.find_if_user_exists_by_id(id)
        if check:
            data = parser.parse_args()
            IncidentModel.update_comment(data, id)
            response = {
            "status": 200,
            "data": [{
                        "id": id,
                        "message":  "successfully updated comment of a red-flag record"
                    }]
            }  
            return  make_response(jsonify(response),201)  

