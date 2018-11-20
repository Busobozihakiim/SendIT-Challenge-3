from app import create_app
from flask_jwt_extended import JWTManager

app = create_app('development')
app.config['JWT_SECRET_KEY'] = 'your-none-typical-secret-string-of-characters'
jwt = JWTManager(app)
if __name__ == '__main__':
    app.run()