import datetime

from werkzeug.security import generate_password_hash, check_password_hash

# local imports
from ....db_config import init_db


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
        self.db = init_db()
        UserModel.id +=1


    def get_by_username(self, username):
        """return a user from the database given a username"""
        database = self.db
        curr = database.cursor()
        curr.execute(
            """SELECT user_id, first_name, last_name, password \
            FROM users WHERE username = '%s'""" % (username))
        data = curr.fetchone()
        curr.close()
        return data


    def get_first_name(self, username):
        database = self.db
        curr = database.cursor()
        curr.execute(
            """SELECT  first_name  \
            FROM users WHERE username = '%s'""" % (username))
        data = curr.fetchone()
        curr.close()
        return data
    
    def get_last_name(self, username):
        database = self.db
        curr = database.cursor()
        curr.execute(
            """SELECT  last_name \
            FROM users WHERE username = '%s'""" % (username))
        data = curr.fetchone()
        curr.close()
        return data

    def get_date_created(self, username):
        database = self.db
        curr = database.cursor()
        curr.execute(
            """SELECT  registered\
            FROM users WHERE username = '%s'""" % (username))
        data = curr.fetchone()
        curr.close()
        return data
    

    def check_exists(self, username):
        """Check if the records exist"""
        curr = self.db.cursor()
        query = "SELECT username FROM users WHERE username = '%s'" % (username)
        curr.execute(query)
        return curr.fetchone() is not None


    def save_user(self):
        """Add user details to the database"""
        user = {
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "othernames" : self.othernames,
            "phoneNumber" : self.phoneNumber,
            "isAdmin"    : self.isAdmin,
            "password": self.password
        }
        # check if user exists
        if self.check_exists(user['username']):
            return False
        database = self.db
        curr = database.cursor()
        query = """INSERT INTO users (first_name, last_name, username, email, password, isadmin, other_names, registered, phonenumber) \
            VALUES ( %(firstname)s, %(lastname)s,\
            %(username)s, %(email)s, %(password)s, %(isAdmin)s, %(othernames)s, ('now'), %(phoneNumber)s) RETURNING user_id;
            """
        curr.execute(query, user)
        user_id = curr.fetchone()[0]
        database.commit()
        curr.close()
        return int(user_id)
    

    def close_db(self):
        """This function closes the database"""
        self.db.close()

    @classmethod
    def encrypt_user_password(cls, plaintext_password):
        if plaintext_password:
            return generate_password_hash(plaintext_password)
        return None


    def authenticate_password(self, password=''):
        return check_password_hash(self.password, password)

    
