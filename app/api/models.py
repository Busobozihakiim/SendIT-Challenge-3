from urllib import parse
import psycopg2
from psycopg2 import Error

class DatabaseOps:
    """Contains methods to create a db connection and create some tables"""

    def connect_to_db(self):
        """Creates a connection to the database"""
        try:
            #using parameters to create a connection to the database
            url = parse.urlparse('postgresql://postgres:th3k1ng@localhost:5432/postgres')
            db = "dbname={} user={} password={} host={} ".format(url.path[1:], \
            url.username, url.password, url.hostname)
            self.conn = psycopg2.connect(db)
            self.cur = self.conn.cursor()
            self.conn.autocommit = True
            print("Success connected to the database - ")
        except (Exception, psycopg2.Error) as error:
            print("Error connecting to the database", error)

    def create_table(self):
        """Creates the users and parcels tables"""
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
            current_location VARCHAR(100) DEFAULT'in transit',
            user_id INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
            )'''
        )
        for sql in queries:
            self.cur.execute(sql)
        print("Table created")

    def create_parcel(self, name, description, pick_up, drop_off, user_id):
        query = ('''INSERT INTO parcel_deliveries (name, description, pick_up, drop_off, user_id)
                    VALUES ('{}','{}','{}','{}','{}')'''.format(name, description, pick_up,
                                                                drop_off, user_id))
        self.cur.execute(query)
        return True
        