import unittest
import json
from flask import jsonify
from app import create_app

class TestRedFlags(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.data = {
            "comment": "THis hopefully works",
            "createdBy": "",
            "createdOn": "Sat, 01 Dec 2018 13:26:12 GMT",
            "id": 1,
            "image": "wwmkmwmow",
            "incident_type": "red-flag",
            "location": "Ronfgai",
            "status": "investigating",
            "video": "jooncono"
        }
        


    def test_redflag_creation(self):
        result = self.client().post('/api/v1/red-flags',data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(result.status_code, 201)
    
    def test_get_redflag(self):
        result = self.client().post('/api/v1/red-flags',data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(result.status_code, 201)
        get_result = self.client().get('/api/v1/red-flags')
        self.assertEqual(get_result.status_code, 200)
    
    def test_get_specific_redflag(self):
        result = self.client().post('/api/v1/red-flags',data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(result.status_code, 201)
        get_result = self.client().get('/api/v1/red-flags/1')
        self.assertEqual(get_result.status_code, 200)


    def test_delete_existing_incident_true(self):
        res = self.client().post('/api/v1/red-flags', data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(res.status_code, 201)
        result = self.client().delete('/api/v1/red-flags/1')
        self.assertEqual(result.status_code, 201)
    

    def test_get_specific_incident_true(self):
        res = self.client().post('/api/v1/red-flags', data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(res.status_code, 201)
        result = self.client().get('api/v1/red-flags/1')
        self.assertEqual(result.status_code, 200)
    

    def test_edit_existing_record_comment_true(self):
        """Test user can edit an incidences."""
        res = self.client().post('/api/v1/red-flags', data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(res.status_code, 201)
        res = self.client().patch('/api/v1/red-flags/1/comment', data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(res.status_code, 201)
    

    def test_edit_existing_record_location_true(self):
        """Test user can edit an incidences."""
        res = self.client().post('/api/v1/red-flags',data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(res.status_code, 201)
        res = self.client().patch('/api/v1/red-flags/1/location', data=json.dumps(self.data),content_type="application/json")
        self.assertEqual(res.status_code, 201)
        
        

    def tearDown(self):
        self.data = {}

if __name__ == '__main__':
    unittest.main() 
     

