import psycopg2


url = "dbname='ireporter' host='localhost' port='5432' user='charles' password='database'"
url_test = "dbname='ireporter-test' host='localhost' port='5432' user='charles' password='database'"

#creating connection
def connection(url):
    con = psycopg2.connect(url)
    return con


def init_db():
    con = connection(url)
    return con


def create_tables():
    con = connection(url)
    curr = con.cursor()
    queries = tables()

    for query in queries:
        curr.execute(query)
    con.commit()


def destroy_tables():
    conn = connection(url_test)
    curr = conn.cursor()
    incidents = "DROP TABLE IF EXISTS incidents CASCADE"
    users = "DROP TABLE IF EXISTS users CASCADE"
    queries = [incidents, users]
    try:
        for query in queries:
            curr.execute(query)
        conn.commit()
    except:
        print("Fail")

def tables():
    db1 = """CREATE TABLE IF NOT EXISTS incident (
            id serial PRIMARY KEY NOT NULL,
            incident_type char(40) NOT NULL,
            location char(40) NOT NULL,
            status char(20) NOT NULL,
            image char(120) NOT NULL,
            video char(120) NOT NULL,
            comment char(120) NOT NULL,
            created_by char(120) NOT NULL,
            created_on timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
            );
            """

    db2 = """CREATE TABLE IF NOT EXISTS users (
	    user_id serial PRIMARY KEY NOT NULL,
	    first_name character varying(50) NOT NULL,
	    last_name character varying(50),
        other_names character varying(50),
	    username character varying(50) NOT NULL,
	    email character varying(50),
        phonenumber numeric NOT NULL,
        isadmin boolean NOT NULL, 
	    registered timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
	    password character varying(500) NOT NULL
	    )"""
    queries = [db1, db2]
    return queries
