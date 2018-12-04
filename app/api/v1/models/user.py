import datetime

User_List = []


class UserModel():
    id = 1
    def __init__(self, firstname=None, lastname=None, othernames= None, email= None, phoneNumber= None,username=None):
        self.id = UserModel.id
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.registered = datetime.datetime.now()
        self.isAdmin = False
        UserModel.id +=1

    
    def json_maker(self):
        return{
            "id" : self.id,
            "firstname" : self.firstname,
            "lastname" : self.lastname,
            "othername" : self.othernames,
            "email" : self.email,
            "phoneNumber" : self.phoneNumber,
            "username" : self.username,
            "registered" : self.registered,
            "isAdmin" : self.isAdmin
        }


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


    

