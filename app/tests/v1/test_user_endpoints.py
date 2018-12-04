import json
import unittest

from app.api.v1.models.user import UserModel
from app import create_app


class UserTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.user_details = {
            "firstname": "charles",
            "lastname": "kakai",
            "email": "ckakai@gmail.com",
            "username": "ckakai",
            "password": "password",
            "othernames" : "chinungo",
            "phoneNumber" : "0809090"
                }

    def test_user_create(self):
        user_created = UserModel(**self.user_details)
        self.assertEqual(user_created.username, "ckakai")


    def test_encrypt_pass_empty(self):
        user_password = UserModel.encrypt_user_password("")
        self.assertEqual(user_password, None)


    def test_hash_password_and_check_password(self):
        user_created = UserModel(**self.user_details)
        self.assertTrue(user_created.authenticate_password("password"))
        self.assertFalse(user_created.authenticate_password("password1"))