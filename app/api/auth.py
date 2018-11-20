from app.api.modals import db_operations
from flask import current_app as app

class UserCredentials:

    def __init__(self):
        self.connect = db_operations()
        self.connect.create_table()

    def register_user(self, email, password):
        self.connect.cur.execute('''INSERT INTO users (email, password) VALUES('{}','{}')'''.format(email, password))        

    def login_user(self, email):
        self.connect.cur.execute('''SELECT * FROM users where email='{}' '''.format(email))
        user = self.connect.cur.fetchone()
        return user
 