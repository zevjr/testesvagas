from flask import Blueprint, jsonify, make_response, request
from ..services.cart import get_all_cart, create_cart, update_cart, delete_cart, get_cart_by_user
from ..models.cart import carts_schema

bp = Blueprint("cart", __name__, url_prefix="/api/v1/cart")


@bp.route("/", methods=["POST"])
def post_cart():
    """
    Add items to cart
    ---
    tags:
        - Cart
    parameters:
      - name: body
        in: body
        schema:
          id: AddCart
          required:
            - username
            - product_id
            - amount
          properties:
            username:
              type: string
              description: Username is used as a reference to locate the cart more easily
            product_id:
              type: integer
              description: Product id that will be added to the cart
            amount:
              type: integer
              description: Amount of desired product
    responses:
      201:
        description: Cart created
      404:
        description: Cart not found
      406:
        description: Product is above the amount per package
    """
    cart = request.json
    create_cart(cart)
    return make_response(jsonify({"message": "Cart created"}), 201)


@bp.route("/", methods=["GET"])
def get_cart():
    """
    Get data from cart for user
    ---
    tags:
        - Cart
    parameters:
      - name: username
        in: query
        description: Username is used as a reference to locate the cart more easily
        required: true
    responses:
      200:
        description: Cart found
      404:
        description: Cart not found
    """
    username = request.args.get("username")
    carts = get_cart_by_user(username)
    return make_response(jsonify(carts_schema.dump(carts)), 200)


@bp.route("/", methods=["PUT"])
def put_cart():
    """
    Update items to cart
    ---
    tags:
        - Cart
    parameters:
      - name: body
        in: body
        schema:
          id: UpdateCart
          required:
            - cart_id
            - amount
          properties:
            cart_id:
              type: integer
              description: Cart id that will be updated to the cart
            amount:
              type: integer
              description: Amount of desired product
    responses:
      200:
        description: Cart updated
      404:
        description: Cart not found
    """
    data = request.json
    update_cart(data)
    return make_response(jsonify({"message": "Cart updated"}), 200)


@bp.route("/", methods=["DELETE"])
def del_cart():
    """
    Delete items to cart
    ---
    tags:
        - Cart
    parameters:
      - name: body
        in: body
        schema:
          id: DeleteCart
          required:
            - cart_id
          properties:
            cart_id:
              type: integer
              description: Cart id that will be updated to the cart
    responses:
      200:
        description: Cart deleted
      404:
        description: Cart not found
    """
    data = request.json
    delete_cart(data)
    return make_response(jsonify({"message": "Cart deleted"}), 200)
