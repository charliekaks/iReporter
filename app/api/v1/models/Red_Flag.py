"""
red-flags model
"""
import datetime
from ....db_config import init_db

RED_FLAGS_LIST = []

class RedFlagsModel:
    """
    red-flags class
    """
    id = 1
    def __init__(self, incident_type=None, location=None,status=None, image=None, video=None ,comment=None):
        self.id = RedFlagsModel.id
        self.incident_type = incident_type
        self.location = location
        self.status = status
        self.image = image
        self.video = video
        self.createdBy = ""
        self.comment = comment
        self.createdOn = datetime.datetime.now()

        RedFlagsModel.id += 1
        self.db = init_db()

    def json_maker(self):
        return{
            "id":self.id,
            "incident_type": self.incident_type,
            "location": self.location,
            "status": self.status,
            "image": self.image,
            "video": self.video,
            "createdBy":self.createdBy,
            "comment": self.comment,
            "createdOn": self.createdOn
        }
    @staticmethod
    def update_incident_location(location,id):
        for incident in RED_FLAGS_LIST:
            if incident.id == id:
                RED_FLAGS_LIST.remove(incident)
                incident.location = location
                return incident
        return None


    @staticmethod
    def update_incident_comment(comment,id):
        for incident in RED_FLAGS_LIST:
            if incident.id == id:
                RED_FLAGS_LIST.remove(incident)
                incident.comment = comment
                return incident
        return None

        
    def save(self):
        """
        save method
        """
        RED_FLAGS_LIST.append(self)

        return RED_FLAGS_LIST

    @staticmethod
    def get_red_flags():
        """
        get_red_flags method
        """
        return RED_FLAGS_LIST

