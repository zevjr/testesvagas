import uuid
from flask import abort
from ..models import carts_schema
from .cart import get_cart_by_user
from ..utils import get_all_or_404


def create_sales_order(username):
    total = 0
    cart = get_all_or_404(
        get_cart_by_user(username), f"Cart not found for user: {username}"
    )
    for item in cart:
        total += item.amount * item.product.price
        validate_sales_order(item)

    sales_order = {
        "id": str(uuid.uuid4()),
        "total-price": total,
        "items": carts_schema.dump(cart),
    }
    for item in cart:
        item.delete()

    return sales_order


def validate_sales_order(sales_order):
    if sales_order.amount < sales_order.product.minimun:
        raise abort(
            406,
            f"This product: {sales_order.product.name} is bellow the minimun amount, the minimun amount is: {sales_order.product.minimun}"
        )
    if sales_order.amount > sales_order.product.max_availability:
        raise abort(
            406,
            f"This product: {sales_order.product.name} is above the max availability",
        )
