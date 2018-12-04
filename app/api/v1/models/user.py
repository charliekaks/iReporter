import datetime
from werkzeug.security import generate_password_hash, check_password_hash

User_List = []


class UserModel():
    id = 1
    def __init__(self, firstname=None, lastname=None, password=None, othernames= None, email= None, phoneNumber= None,username=None):
        self.id = UserModel.id
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.registered = datetime.datetime.now()
        self.isAdmin = False
        self.password = UserModel.encrypt_user_password(password)
        UserModel.id +=1

    
    def json_maker(self):
        return{
            "id" : self.id,
            "firstname" : self.firstname,
            "lastname" : self.lastname,
            "othernames" : self.othernames,
            "email" : self.email,
            "phoneNumber" : self.phoneNumber,
            "username" : self.username,
            "registered" : self.registered,
            "isAdmin" : self.isAdmin
        }
    
    @staticmethod
    def check_user(user_name):
        for user in User_List:
            if user.username == user_name:
                return True
        return False

        
    @staticmethod
    def find_user(user_name):
        for user in User_List:
            if user.username == user_name:
                return user
        return None


    def save(self):
        """
        save method
        """
        User_List.append(self)
        return User_List


    @staticmethod
    def get_users():
        """
        get_red_flags method
        """
        return User_List
    
    @classmethod
    def encrypt_user_password(cls, plaintext_password):
        if plaintext_password:
            return generate_password_hash(plaintext_password)
        return None


    def authenticate_password(self, password=''):
        return check_password_hash(self.password, password)


    

