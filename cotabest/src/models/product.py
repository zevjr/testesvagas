from ..db import db, ma
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    minimun = db.Column(db.Integer, nullable=False)
    amount_per_package = db.Column(db.Integer, nullable=False)
    max_availability = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class ProductSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
            "price",
            "minimum",
            "amount_per_package",
            "max_availability",
        )


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
