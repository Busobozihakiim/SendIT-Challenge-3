from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request
from app.api import apiv2
from app.api.auth import UserCredentials

@apiv2.route('/parcels/<int:parcel_id>/presentLocation', methods=['PUT'])
@jwt_required
def change_location(parcel_id):
    pass

@apiv2.route('/parcels/<parcelId>/status', methods=['PUT'])
@jwt_required
def change_status(parcel_id):
    pass