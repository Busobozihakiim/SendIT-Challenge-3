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

        if key != 'name' and key != 'pick_up' and key != 'drop_off' and key != 'description':
            return jsonify({"message":"You've messed up the input",
                            "status":"failure",
                            "Error":"{}".format(key)})


    user_id = get_jwt_identity()
    new_order.create_parcel(order['name'], order['pick_up'],
                            order['drop_off'], order['description'], user_id[0])
    return jsonify({"message":"Delivery order created", "status":"success"}), 201

@apiv2.route('/parcels', methods=['GET'])
@jwt_required
def see_all_orders():
    pass

@apiv2.route('/parcels/<int:parcel_id>', methods=['GET'])
@jwt_required
def get_order_by_id(parcel_id):
    """Return a single delivery order based on its id"""
    current_user = get_jwt_identity()
    parcel = DatabaseOps()
    parcel.connect_to_db()
    parcel = parcel.get_delivery_from_db(parcel_id, current_user[0])
    if parcel:
        return jsonify({"message":"Here is delivery order {}".format(parcel_id),
                        "status":"success", "Data":parcel})
    return jsonify({"message":"Delivery order {} not available".format(parcel_id),
                    "status":"failure"})


@apiv2.route('/users/<int:userid>/parcels', methods=['GET'])
@jwt_required
def get_all_orders_by_userid(userid):
    """Used to view all the parce; delivery orders by a user id"""
    current_user = get_jwt_identity()
    if userid != current_user[0]:
        return jsonify({"Error":"This is not your userid = {}".format(userid), "status":"failure",
                        "message":"Access denied, trying to access another users delivery orders"})
    parcels = DatabaseOps()
    parcels.connect_to_db()
    parcels = parcels.get_from_db(current_user[0])
    print(parcels)
    if not parcels:
        return jsonify({"message":"You have not made any delivery orders"})
    return jsonify({"message":"here is the delivery order of {}".format(userid),
                    "data":parcels}), 200


@apiv2.route('/parcels/<int:parcel_id>/cancel', methods=['PUT'])
@jwt_required
def cancel_delivery_order(parcel_id):
    pass
