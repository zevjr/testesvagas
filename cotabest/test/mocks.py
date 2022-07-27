from src.models.product import Product
from src.models.cart import Cart
from src.models.user import User


class MockSales:
    create_sales = {"username": "test"}


class MockCart:
    create_cart = {"username": "test", "cart_id": 1, "product_id": 4, "amount": 24}
    create_cart_error = {"username": "test", "cart_id": 1, "product_id": 4, "amount": 4}
    cart_user = User(username="test")
    cart_product = Product(
        id=4,
        name="Product 4",
        price=4.0,
        amount_per_package=12,
        max_availability=12000,
        minimun=24
    )
    cart_items = [Cart(id=1, user_id=1, product_id=4, amount=24, product=cart_product)]
    cart_items_error_minimun = [Cart(id=1, user_id=1, product_id=4, amount=4, product=cart_product)]
    cart_items_error_max_availability = [Cart(id=1, user_id=1, product_id=4, amount=12001, product=cart_product)]
    cart_item = Cart(id=1, user_id=1, product_id=4, amount=24, product=cart_product)
    cart_item_response = [
        {
            "amount": 24,
            "id": 1,
            "price": 4.0,
            "product_id": 4,
            "total_price": 96.0,
            "user_id": 1,
        }
    ]
    cart_update = {"username": "test", "cart_id": 1, "amount": 24}
    cart_delete = {"cart_id": 1}


class MockProduct:
    list_product = [
        Product(
            id=4,
            amount_per_package=12,
            max_availability=12000,
            name="Feijão preto",
            price=4.0,
        ),
        Product(
            id=5,
            amount_per_package=12,
            max_availability=12000,
            name="Feijão carioca",
            price=6.0,
        ),
    ]
    create_product = [
        {
            "name": "Feijão preto",
            "price": 4.0,
            "minimun": 12,
            "amount-per-package": 12,
            "max-availability": 12000,
        }
    ]
