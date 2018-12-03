import psycopg2

url = "dbname='ireporter' host='localhost' port='5432' user='charles' password='database'"

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
    pass

def tables():
    db1 = """CREATE TABLE IF NOT EXISTS red_flags(
            id serial PRIMARY KEY NOT NULL,
            incident_type char(40) NOT NULL,
            location char(40) NOT NULL,
            status char(20) NOT NULL,
            image char(120) NOT NULL,
            video char(120) NOT NULL,
            comment char(120) NOT NULL,
            created_by char(120) NOT NULL,
            create_on timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
            );
            """

    db2 = """CREATE TABLE IF NOT EXISTS users (
	    user_id serial PRIMARY KEY NOT NULL,
	    first_name character varying(50) NOT NULL,
	    last_name character varying(50),
        other_names character varying(50),
	    username character varying(50) NOT NULL,
	    email character varying(50),
        phoneNumber numeric NOT NULL,
        isAdmin boolean NOT NULL, 
	    registered timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
	    password character varying(500) NOT NULL
	    )"""
    queries = [db1, db2]
    return queries
