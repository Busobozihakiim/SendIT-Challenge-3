from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask import jsonify, request
from app.api import apiv2
from app.api.auth import UserCredentials

@apiv2.route('auth/signup', methods=['POST'])
def registers_user():
    """Function to create users"""
    returned = request.get_json() or {}
    new_user = UserCredentials()

    #check for an empty post
    if not returned:
        return jsonify({"message":"You entered nothing", "status":"failure"})

    #check for empty values in post and return missing field
    #check for wrong input format
    for key, value in returned.items():
        if value == "":
            return jsonify({"message":"You've entered an empty value ",
                            "status":"failure",
                            "Empty":"{}".format(key)})
        if 'email' not in key and 'password' not in key:
            return jsonify({"message":"You've messed up the input",
                            "status":"failure",
                            "Error":"{}".format(key)})

    #check for existing email
    already_exits = new_user.login_user(returned['email'])
    if already_exits:
        return jsonify({"message":"Email already exists",
                        "status":"failure",
                        "data":"{}".format(returned['email'])})

    #create an account
    new_user.register_user(returned['email'], returned['password'])
    return jsonify({"message":"account created succesfully", "status":"success"}), 201

@apiv2.route('auth/login', methods=['POST'])
def login_users():
    """Function that logs in users
    :return Jason Web Token"""
    returned = request.get_json() or {}
    user = UserCredentials()

    #check for an empty post
    if not returned:
        return jsonify({"message":"You entered nothing", "status":"failure"})

    #check for empty values in post and return missing field
    #check for wrong input format
    for key, value in returned.items():
        if value == "":
            return jsonify({"message":"You've entered an empty value ",
                            "status":"failure",
                            "Empty":"{}".format(key)})
        if 'email' not in key and 'password' not in key:
            return jsonify({"message":"You've messed up the input",
                            "status":"failure",
                            "Error":"{}".format(key)})

    loggedin_user = user.login_user(returned['email'])
    if loggedin_user:
        return jsonify({'token':create_access_token(identity=loggedin_user),
                        'message':'logged in'}), 201
    return jsonify({"message":"Wrong credentials", "status":"failure"}), 201
