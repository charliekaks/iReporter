import datetime
# local imports
from ....db_config import init_db

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
        self.createdBy = "charlie"
        self.comment = comment
        self.createdOn = datetime.datetime.now()
        self.db = init_db()
        IncidentModel.id += 1

    def save_incident(self):
        """Add incident details to the database"""
        incident = {
            "incident_type": self.incident_type,
            "id" : self.id,
            "location": self.location,
            "status": self.status,
            "image": self.image,
            "video": self.video,
            "created_by":self.createdBy,
            "comment": self.comment,
        }
        database = self.db
        curr = database.cursor()
        query = """INSERT INTO incident (incident_type, id, location, status, created_on, image, video, created_by, comment) VALUES (%(incident_type)s,\
                   %(id)s, %(location)s, %(status)s,('now'), %(image)s, %(video)s, %(created_by)s, %(comment)s) RETURNING id;"""
        curr.execute(query, incident)
        id = curr.fetchone()[0]
        database.commit()
        curr.close()
        return int(id)

    def get_specific_incident(self, id):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""SELECT * FROM incident WHERE \
                     id = %d;""" % (int(id)))
        data = curr.fetchall()
        data_items = []
        if not isinstance(data, list):
            data_items.append(data)
        else:
            data_items = data[:]
        resp = []
        for i, items in enumerate(data):
            incident_type, id, location, status, date, image, video, created_by, comment = items
            incident = dict(
                incident_type=incident_type,
                id=int(id),
                location=location,
                status=status,
                created_on = date,
                image = image,
                video = video,
                created_by = created_by,
                comment = comment
            )
            resp.append(incident)
        return resp
    
    def get_all_incidents(self):
        """This function returns a list of all the incidents"""
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""SELECT * FROM incident;""")
        data = curr.fetchall()
        resp = []

        for i, items in enumerate(data):
            incident_type, id, location, status, date, image, video, created_by, comment = items
            incident = dict(
                incident_type=incident_type,
                id=int(id),
                location=location,
                status=status,
                created_on = date,
                image = image,
                video = video,
                created_by = created_by,
                comment = comment
            )
            resp.append(incident)
        return resp


    def update_comment(self):
        pass
    

    def update_location(self):
        pass
    
    
