from ..models import Product, products_schema
from ..utils import get_all_or_404


def create_product(request):
    products = request.json
    for product in products:
        data = Product(
            name=product["name"],
            price=product["price"],
            minimun=product["minimun"],
            amount_per_package=product["amount-per-package"],
            max_availability=product["max-availability"],
        )
        data.create()


def get_all_products():
    products = get_all_or_404(Product.query.all(), "Products not found")
    return products_schema.dump(products)


def search_product(name):
    product = get_all_or_404(
        Product.query.filter(Product.name.ilike(f"%{name}%")).all()
    )
    return products_schema.dump(product)
