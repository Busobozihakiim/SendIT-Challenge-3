import psycopg2
from psycopg2 import Error
from urllib import parse

class db_operations:

    def __init__(self):
        try:
            #using parameters to create a connection to the database
            url = parse.urlparse('postgresql://postgres:th3k1ng@localhost:5432/postgres')
            db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
            self.conn = psycopg2.connect(db)
            self.cur = self.conn.cursor()
            self.conn.autocommit = True
            print("Success connected to the database - ")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error connecting to the database", error)

    def create_table(self):
        queries = (
            '''
            CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY NOT NULL,
            email VARCHAR(50) NOT NULL,
            password VARCHAR(20) NOT NULL)
            ''',
            '''
            CREATE TABLE IF NOT EXISTS parcel_deliveries(
            parcel_id serial PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(100) NOT NULL,
            pick_up VARCHAR(100) NOT NULL,
            drop_off VARCHAR(200) NOT NULL,
            status VARCHAR(100) DEFAULT'pending',
            current_location VARCHAR(100) NOT NULL,
            user_id INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE 
            )'''
        )
        for sql in queries:
            self.cur.execute(sql)
        print("Table created")