from flask import abort
from ..models import Cart, User, cart_schema, carts_schema,Product
from ..utils import search_or_create


def create_cart(cart):
    user = search_or_create(cart["username"], User)
    product = Product.query.get_or_404(cart["product_id"])
    if  cart["amount"] < product.amount_per_package:
        raise abort(
            406,
            f"This product: {product.name} is above the amount per package",
        )
    data = Cart(
        user_id=user.id,
        product_id=product.id,
        amount=cart["amount"],
    )
    data.create()


def get_all_cart():
    carts = Cart.query.all()
    return carts_schema.dump(carts)


def get_cart_by_user(username):
    user = User.query.filter_by(username=username).first_or_404(
        f"User not found: {username}"
    )
    return Cart.query.filter_by(user_id=user.id).all()


def update_cart(cart):
    data = Cart.query.get(cart["cart_id"])
    data.amount = cart["amount"]
    data.update()


def delete_cart(cart):
    data = Cart.query.get(cart["cart_id"])
    data.delete()
