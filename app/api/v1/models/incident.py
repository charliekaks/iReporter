"""
incident model
"""
import datetime

Incident_List = []

class IncidentModel():
    """
    incident class
    """
    id = 1
    def __init__(self, incident_type=None, location=None,status=None, image=None, video=None ,comment=None):
        self.id = IncidentModel.id
        self.incident_type = incident_type
        self.location = location
        self.status = status
        self.image = image
        self.video = video
        self.createdBy = ""
        self.comment = comment
        self.createdOn = datetime.datetime.now()
        IncidentModel.id += 1
    

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
        for incident in Incident_List:
            if incident.id == id:
                Incident_List.remove(incident)
                incident.location = location
                return incident
        return None


    @staticmethod
    def update_incident_comment(comment,id):
        for incident in Incident_List:
            if incident.id == id:
                Incident_List.remove(incident)
                incident.comment = comment
                return incident
        return None

        
    def save(self):
        """
        save method
        """
        Incident_List.append(self)

        return Incident_List


    @staticmethod
    def get_incident():
        """
        get_all incidents method
        """
        return Incident_List

