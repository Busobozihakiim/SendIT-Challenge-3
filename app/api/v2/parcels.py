"""HANDLES OPERATIONS ON THE PARCELS"""
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request
from app.api import apiv2
from app.api.models import DatabaseOps

@apiv2.route('/parcels', methods=['POST'])
@jwt_required
def make_a_delivery_order():
    """Create a parcel delivery order"""
    order = request.get_json() or {}
    new_order = DatabaseOps()
    new_order.connect_to_db()

    if not order:
        return jsonify({"message":"You entered nothing", "status":"failure"})

    for key in order:
        if len(order) < 4:
            return jsonify({"message":"You are missing a required field", "status":"failure"})

    for key, value in order.items():
        if value == "":
            return jsonify({"message":"You are missing {} in your input".format(key),
                            "status":"failure"})

        if 'name' != key and 'pick_up' != key and 'drop_off' != key and 'description' != key:
            return jsonify({"message":"You've messed up the input",
                            "status":"failure",
                            "Error":"{}".format(key)})


    user_id = get_jwt_identity()
    new_order.create_parcel(user_id[0], order['pick_up'],
                            order['drop_off'], order['name'], order['description'], )
    return jsonify({"message":"Delivery order created", "status":"success"}), 201

@apiv2.route('/parcels', methods=['GET'])
@jwt_required
def see_all_orders():
    pass

@apiv2.route('/parcels/<int:parcel_id>', methods=['GET'])
@jwt_required
def get_order_by_id(parcel_id):
    pass

@apiv2.route('/users/<string:userid>/parcels', methods=['GET'])
@jwt_required
def get_all_orders_by_userid(userid):
    pass

@apiv2.route('/parcels/<int:parcel_id>/cancel', methods=['PUT'])
@jwt_required
def cancel_delivery_order(parcel_id):
    pass
