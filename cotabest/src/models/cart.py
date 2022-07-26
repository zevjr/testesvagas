from datetime import datetime

from ..db import db, ma


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    product = db.relationship("Product", backref=db.backref("product", uselist=False))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self


class CartSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "product_id", "amount", "price", "total_price")

    total_price = ma.Method("get_total_price")
    price = ma.Method("get_price")

    def get_price(self, obj):
        return obj.product.price

    def get_total_price(self, obj):
        return obj.product.price * obj.amount


cart_schema = CartSchema()
carts_schema = CartSchema(many=True)
