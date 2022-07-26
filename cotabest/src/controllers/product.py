from flask import Blueprint, jsonify, make_response, request

from ..services.product import create_product, search_product

bp = Blueprint("product", __name__, url_prefix="/api/v1/products")


@bp.route("/", methods=["POST"])
def post_product():
    """
    Create a new user
    ---
    responses:
      201:
        description: User created
    """
    create_product(request)

    return jsonify({"message": "User created"}), 201


@bp.route("/", methods=["GET"])
def get_search_products():
    """
    Get search products for names
    ---
    responses:
      200:
        description: Products found
    """
    name = request.args.get("name")
    products = search_product(name)
    return jsonify({"message": products}), 200
