from flask import Blueprint, jsonify, make_response, request
from ..services.sales import create_sales_order

bp = Blueprint("sales_order", __name__, url_prefix="/api/v1/sales")


@bp.route("/", methods=["POST"])
def create_sales():
    data = request.json
    sales_order = create_sales_order(data["username"])
    return make_response(jsonify({"message": sales_order}), 201)
