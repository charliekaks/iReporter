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
        self.user_details2 = {
            "firstname": "charles1",
            "lastname": "kakai1",
            "email": "ckakai1@gmail.com",
            "username": "ckakai1",
            "password": "password1",
            "othernames" : "chinungo1",
            "phoneNumber" : "08090901"
                }
        self.sigin_details = {
            "username": "ckakai",
            "password": "password"  
        }

    def test_user_create(self):
        user_created = UserModel(**self.user_details)
        self.assertEqual(user_created.username, "ckakai")


    def test_if_encrypt_password_is_empty(self):
        user_password = UserModel.encrypt_user_password("")
        self.assertEqual(user_password, None)


    def test_hashing_password(self):
        user_created = UserModel(**self.user_details)
        self.assertTrue(user_created.authenticate_password("password"))
        self.assertFalse(user_created.authenticate_password("password1"))

    def test_get_users(self):
        result = self.client().post('/api/v1/auth/register',data=json.dumps(self.user_details),content_type="application/json")
        self.assertEqual(result.status_code, 201)
        get_result = self.client().get('/api/v1/auth/login')
        self.assertEqual(get_result.status_code, 200)

    def test_user_creations(self):
        result = self.client().post('/api/v1/auth/register',data=json.dumps(self.user_details2),content_type="application/json")
        self.assertEqual(result.status_code, 201)
    
    def test_sign_in(self):
        result = self.client().post('/api/v1/auth/login',data=json.dumps(self.sigin_details),content_type="application/json")
        self.assertEqual(result.status_code, 200)