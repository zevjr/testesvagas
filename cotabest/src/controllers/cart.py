from flask import Blueprint, jsonify, make_response, request
from ..services.cart import get_all_cart, create_cart, update_cart, delete_cart

bp = Blueprint("cart", __name__, url_prefix="/api/v1/cart")


@bp.route("/", methods=["POST"])
def post_cart():
    """Create a cart"""
    cart = request.json
    create_cart(cart)
    return make_response(jsonify({"message": "Cart created"}), 201)


@bp.route("/", methods=["GET"])
def get_cart():
    """Get all carts"""
    carts = get_all_cart()
    return make_response(jsonify(carts), 200)


@bp.route("/", methods=["PUT"])
def put_cart():
    """Update a cart"""
    data = request.json
    update_cart(data)
    return make_response(jsonify({"message": "Cart updated"}), 200)


@bp.route("/", methods=["DELETE"])
def del_cart():
    """Delete a cart"""
    data = request.json
    delete_cart(data)
    return make_response(jsonify({"message": "Cart deleted"}), 200)
