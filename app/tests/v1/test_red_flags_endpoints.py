import unittest
import json
from flask import jsonify
from app import create_app
from mock import Mock

class TestRedFlags(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.data = {
            "id": 1,
            "type": "red-flag",
            'createdBy': 0,
            "createdOn": "11/2/2018",
            'location': '-5.256987e, 30.369854s',
            'status': 'rejected',
            'images': 'http://hi.jpg',
            'video': 'http://looped.mp4',
            'comment': 'Rise of crime in west embakasi'
        }


    def test_redflag_creation(self):
        result = self.client().post('/api/v1/red-flags',data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(result.status_code, 201)


    def test_delete_existing_incident_true(self):
        res = self.client().post('/api/v1/red-flags', data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(res.status_code, 201)
        result = self.client().delete('/api/v1/red-flags/1')
        self.assertEqual(result.status_code, 201)
    

    def test_edit_existing_record_comment_true(self):
        """Test user can edit an incidences."""
        res = self.client().post('/api/v1/red-flags', data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(res.status_code, 201)
        res = self.client().patch('/api/v1/red-flags/1/comment', json={
            "comment": "Clerks are taking bribes"
        })
        self.assertEqual(res.status_code, 201)
    

    def test_edit_existing_record_location_true(self):
        """Test user can edit an incidences."""
        res = self.client().post('/api/v1/red-flags',data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(res.status_code, 201)
        res = self.client().patch('/api/v1/red-flags/1/location', json={
            "Location": "WestGate"
        })
        self.assertEqual(res.status_code, 201)
        
        

    def tearDown(self):
        self.data = {}

if __name__ == '__main__':
    unittest.main() 
     

