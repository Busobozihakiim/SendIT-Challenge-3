from urllib import parse
import psycopg2

class DatabaseOps:
    """Contains methods to create a db connection and create some tables"""

    def connect_to_db(self):
        """Creates a connection to the database"""
        try:
            url = parse.urlparse('postgresql://postgres:th3k1ng@localhost:5432/postgres')
            db = "dbname={} user={} password={} host={} ".format(url.path[1:], \
            url.username, url.password, url.hostname)
            self.conn = psycopg2.connect(db)
            self.cur = self.conn.cursor()
            self.conn.autocommit = True
            print("Success connected to the database - ")
        except (Exception, psycopg2.DatabaseError) as error:
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
        """save a delivery order to a database"""
        query = ('''INSERT INTO parcel_deliveries (name, description, pick_up, drop_off, user_id)
                    VALUES ('{}','{}','{}','{}','{}')'''.format(name, description, pick_up,
                                                                drop_off, user_id))
        self.cur.execute(query)
        return True

    def get_from_db(self, user):
        """retreive all delivery orders of a given user id"""
        query = ('''SELECT * FROM parcel_deliveries WHERE user_id = '{}' '''.format(user))
        self.cur.execute(query)
        parcel_records = self.cur.fetchall()
        return parcel_records

    def get_delivery_from_db(self, parcel, user):
        """fetch a delivery order by its id"""
        query = ('''SELECT * FROM parcel_deliveries
                    where parcel_id = '{}' and user_id = '{}' '''.format(parcel, user))
        self.cur.execute(query)
        colnames = [column[0] for column in self.cur.description]
        parcel = self.cur.fetchall()
        for this_parcel in parcel:
            return dict(zip(colnames, this_parcel))
    