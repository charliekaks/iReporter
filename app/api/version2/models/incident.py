import datetime
import json
from flask import jsonify

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
            "comment": self.comment
        }
        database = self.db
        curr = database.cursor()
        query = """INSERT INTO incident (incident_type, id, location, status, created_on, image, video, created_by, comment)  VALUES ( %(incident_type)s,
                   %(id)s, %(location)s, %(status)s,('now'), %(image)s, %(video)s, %(created_by)s, %(comment)s) RETURNING id;"""
        query_2 = """ SELECT  REGEXP_REPLACE(cast(incident_type AS text), '\s+$', '') FROM incident;"""
        query_3 = """ SELECT  REGEXP_REPLACE(cast(id AS text), '\s+$', '') FROM incident;"""
        query_4 = """ SELECT  REGEXP_REPLACE(cast(location AS text), '\s+$', '') FROM incident;"""
        query_5 = """ SELECT  REGEXP_REPLACE(cast(status AS text), '\s+$', '') FROM incident;"""
        query_6 = """ SELECT  REGEXP_REPLACE(cast(created_on AS text), '\s+$', '') FROM incident;"""
        query_7 = """ SELECT  REGEXP_REPLACE(cast(image AS text), '\s+$', '') FROM incident;"""
        query_8 = """ SELECT  REGEXP_REPLACE(cast(video AS text), '\s+$', '') FROM incident;"""
        query_9 = """ SELECT  REGEXP_REPLACE(cast(created_by AS text), '\s+$', '') FROM incident;"""
        query_10 = """ SELECT  REGEXP_REPLACE(cast(comment AS text), '\s+$', '') FROM incident;"""
        queries =[ query_2,query_3,query_4,query_5,query_6,query_7,query_8,query_9,query_10]
        curr.execute(query, incident)
        for query in queries:
            curr.execute(query, incident)
        database.commit()
        curr.close()
        
    

    def get_specific_incident(self ,id):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""SELECT * FROM incident WHERE \
                     id = %d ;""" % (int(id)))
        data = curr.fetchall()
        dbconn.commit()
        curr.close()
        incidents_list = []
        for row in data:
            incident = {
                "incident_type": row[1],
                "id" : row[0],
                "location": row[2],
                "status": row[3],
                "image": row[4],
                "video": row[5],
                "created_by": row[7],
                "comment": row[6],
                "created_on": row[8].__str__()
                        }
            incidents_list.append(incident)

        return json.dumps(incidents_list)
        
    @staticmethod
    def get_all_incidents():
        """Product Class method to fetch all incident"""
        dbconn = init_db()
        curr = dbconn.cursor()
        curr.execute("""SELECT * FROM incident;""" )
        incident = curr.fetchall()
        dbconn.commit()
        curr.close()
        incidents = []
        for row in incident:
            incident = {
                "incident_type": row[1],
                "id" : row[0],
                "location": row[2],
                "status": row[3],
                "image": row[4],
                "video": row[5],
                "created_by": row[7],
                "comment": row[6],
                "created_on": row[8].__str__()
                        }
            incidents.append(incident)
        return json.dumps(incidents)
        
    @staticmethod
    def check_type(incident_type="red-flag"):
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""SELECT * FROM incident WHERE \
                     incident_type = %s;""" % (incident_type))
        data = curr.fetchall()
        dbconn.commit()
        curr.close()
        return data



    @staticmethod
    def update_comment(comment, id):
        dbconn = init_db()
        curr = dbconn.cursor()
        query = """ UPDATE incident
                SET comment = %s
                WHERE id = %s"""
        curr.execute(query, (comment, id))
        dbconn.commit()
        curr.close()
    
    @staticmethod
    def update_location(location, id):
        dbconn = init_db()
        curr = dbconn.cursor()
        query = """ UPDATE incident
                SET comment = %s
                WHERE id = %s"""
        curr.execute(query, (location, id))
        dbconn.commit()
        curr.close()
        
    @staticmethod
    def find_if_user_exists_by_id(id):
        dbconn = init_db()
        curr = dbconn.cursor()
        curr.execute("""SELECT * FROM incident WHERE \
                     id = %d;""" % (int(id)))
        data = curr.fetchone()
        dbconn.commit()
        curr.close()
        if data:
            return True
        return False

    @staticmethod
    def find_by_type(incident_type):
        dbconn = init_db()
        curr = dbconn.cursor()
        curr.execute("""SELECT * FROM incident WHERE \
                     incident_type = %s;""" % (incident_type))
        data = curr.fetchall()
        return data

    @staticmethod
    def delete_flag(id):
        dbconn = init_db()
        curr = dbconn.cursor()
        curr.execute("""DELETE FROM incident WHERE \
                     id = %d;""" % (int(id)))
        dbconn.commit()
        curr.close()
    
    
