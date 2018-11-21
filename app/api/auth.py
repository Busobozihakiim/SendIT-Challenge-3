from app.api.models import DatabaseOps

class UserCredentials:
    """Contains methods used in sign up and login"""

    def __init__(self):
        """create connection to the database"""
        self.connect = DatabaseOps()
        self.connect.connect_to_db()

    def register_user(self, email, password):
        """add into the database user the email and password"""
        self.connect.cur.execute('''
                                    INSERT INTO users (email, password) VALUES('{}','{}')
                                 '''.format(email, password))

    def login_user(self, email):
        """Get all from the database when email exists"""
        self.connect.cur.execute('''SELECT * FROM users where email='{}' '''.format(email))
        user = self.connect.cur.fetchone()
        return user
