"""TESTING OF ENDPOINTS"""
import json
import pytest
from app import create_app
from flask_jwt_extended import JWTManager
from .test_modals import *

@pytest.fixture()
def set_up_client():
    """Creates app that will be used for testing"""
    app = create_app('testing')
    app.config['JWT_SECRET_KEY'] = 'your-none-typical-secret-string-of-characters'
    JWTManager(app)
    client = app.test_client()
    
    #creating the application context and
    #allowing test functions to run by calling test client
    #and finally cleaning house

    ctx = app.app_context()
    ctx.push()
    yield client
    ctx.pop()

def test_register_users(set_up_client):
    """tests the registration of a user"""
    #testing when nothing is input
    res = set_up_client.post('api/v2/auth/signup',
                             data=json.dumps(empty_post),
                             content_type="application/json")
    assert res.status_code == 200
    assert b"You entered nothing" in res.data

    #testing with empty values
    resp = set_up_client.post('api/v2/auth/signup',
                              data=json.dumps(empty_values),
                              content_type="application/json")
    assert resp.status_code == 200
    assert b"You've entered an empty value" in resp.data
    #testing for wrong keys
    respo = set_up_client.post('api/v2/auth/signup',
                               data=json.dumps(wrong_keys),
                               content_type="application/json")
    assert respo.status_code == 200
    assert b"You've messed up the input" in respo.data

    #testing with an existing email
    respon = set_up_client.post('api/v2/auth/signup',
                                data=json.dumps(existing_email),
                                content_type="application/json")
    assert respon.status_code == 200
    assert b"Email already exists" in respon.data

    #testing with clean data
    response = set_up_client.post('api/v2/auth/signup',
                                  data=json.dumps(good_sign_up),
                                  content_type="application/json")
    assert response.status_code == 201
    assert b"account created succesfully" in response.data

def test_login_user(set_up_client):
    """tests the login of a user"""
    #logging in with clean data
    response = set_up_client.post('api/v2/auth/login',
                                  data=json.dumps(good_sign_up),
                                  content_type="application/json")
    assert response.status_code == 201
    assert b"logged in" in response.data

    #loggin in with an empty post
    respon = set_up_client.post('api/v2/auth/login',
                                data=json.dumps(empty_post),
                                content_type="application/json")
    assert respon.status_code == 200
    assert b"You entered nothing" in respon.data

    #loggin in with empty values
    resp = set_up_client.post('api/v2/auth/login',
                              data=json.dumps(empty_values),
                              content_type="application/json")
    assert respon.status_code == 200
    assert b"You've entered an empty value" in resp.data

    #loggin in with messed up keys
    the_response = set_up_client.post('api/v2/auth/login',
                                 data=json.dumps(wrong_keys),
                                 content_type="application/json")
    assert the_response.status_code == 200
    assert b"You've messed up the input" in the_response.data
