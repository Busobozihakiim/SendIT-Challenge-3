from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask import jsonify, request
from app.api import apiv2
from .modals import db_operations
from .auth import UserCredentials

@apiv2.route('auth/signup', methods=['POST'])
def registers_user():
    returned = request.get_json() or {}
    print(returned)

    #check for an empty post
    if not returned:
        return jsonify("You entered nothing")
    
    #check for empty values in post and return missing field
    for key, value in returned.items():
        if value == "":
            return jsonify("You are missing {} in your input".format(key))

    #create an account  
    new_user = UserCredentials()
    new_user.register_user(returned['email'], returned['password'])
    return jsonify('Account created succesfully'), 201

@apiv2.route('auth/login', methods=['POST'])
def login_users():
    returned = request.get_json() or {}
    user = UserCredentials()
    loggedin_user = user.login_user(returned['email'])
    if loggedin_user:
        return jsonify({'token':create_access_token(identity=loggedin_user), 
        'message':'logged in' }), 201
    return jsonify('Wrong Credentials'), 201
