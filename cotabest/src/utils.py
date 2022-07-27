from flask import abort, Blueprint

bp = Blueprint("utils", __name__)

def search_or_create(username, model):
    user = model.query.filter_by(username=username).first()
    if user:
        return user
    else:
        user = model(username=username)
        user.create()
        return user


def get_all_or_404(query, message=None):
    empty = []
    if query == empty:
        raise abort(404, message)
    return query


@bp.cli.command("populate")
def populate():
    from .models import Product
    from .db import db
    import os
    import json

    path = os.path.abspath("input.json")
    input_json = open(path, "r")
    products = json.load(input_json)
    db.create_all()

    for product in products:
        data = Product(
            name=product["name"],
            price=product["price"],
            minimun=product["minimun"],
            amount_per_package=product["amount-per-package"],
            max_availability=product["max-availability"],
        )
        data.create()
    input_json.close()
