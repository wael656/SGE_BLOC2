import psycopg2

def cpnnection_db():
        conn = psycopg2.connect(
            database="the_bear",
            password="admin",
            user="admin",
            host="localhost",
            port="5432"
        )
    
    return conn
