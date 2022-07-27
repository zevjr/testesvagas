from flask import Blueprint, jsonify, make_response, request

from ..services.product import create_product, search_product

bp = Blueprint("product", __name__, url_prefix="/api/v1/products")


@bp.route("/", methods=["POST"])
def post_product():
    """
    Endpoint created only to register the initial products in the base
    ---
    tags:
        - Product
    """
    create_product(request)

    return jsonify({"message": "Product created"}), 201


@bp.route("/", methods=["GET"])
def get_search_products():
    """
    Search products for names
    ---
    tags:
        - Product
    parameters:
      - name: name
        in: query
        description: Name or part name that will search for the product
        required: true
    responses:
      200:
        description: Products found
      404:
        description: Products not found
    """
    name = request.args.get("name")
    products = search_product(name)
    return jsonify({"message": products}), 200
