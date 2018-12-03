
import unittest
import json
from flask import jsonify
from app.api.v1.models.user import UserModel
from app import create_app


class UserTest(unittest.TestCase):
    data = {
            "firstname": "charles",
            "lastname": "kakai",
            "othernames": "Muchai",
            "phoneNumber": 10191010,
            "email": "k@gmail.com",
            "username": "ckakai"
        }


    def test_crude(self):
        """
        Test CRUD functionality of the class
        :return: Item found.
        """
        a_user = UserModel(**UserTest.data)

        a_user.save()

        self.assertEqual(a_user.firstname, 'charles')