
import unittest
import json
from flask import jsonify
from app.api.v1.models.red_flag import RedFlagsModel
from app import create_app

class IncidentTest(unittest.TestCase):
    data = {
            "comment": "THis hopefully works",
            "image": "wwmkmwmow",
            "incident_type": "red-flag",
            "location": "Ronfgai",
            "status": "investigating",
            "video": "jooncono"
        }


    def test_crude(self):
        """
        Test CRUD functionality of the class
        :return: Item found.
        """
        incident = RedFlagsModel(**IncidentTest.data)

        incident.save()

        self.assertEqual(incident.incident_type, 'red-flag')
        

    