from flask import Blueprint, jsonify, make_response, request
from ..services.sales import create_sales_order

bp = Blueprint("sales_order", __name__, url_prefix="/api/v1/sales")


@bp.route("/", methods=["POST"])
def create_sales():
    """
    Completes sale of the products in the cart
    ---
    tags:
        - Sales
    parameters:
      - name: body
        in: body
        schema:
          id: Sales
          required:
            - username
          properties:
            username:
              type: string
              description: Username is used as a reference to locate the cart more easily
    responses:
      201:
        description: Cart created
      404:
        description: Cart not found
      406:
        description: Product is different amount than expected
    """
    data = request.json
    sales_order = create_sales_order(data["username"])
    return make_response(jsonify({"message": sales_order}), 201)
