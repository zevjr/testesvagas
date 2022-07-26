from sqlalchemy.dialects.postgresql import UUID
from ..db import db, ma
from datetime import datetime
import uuid


class Sales(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)

    product = db.relationship("Product", backref=db.backref("product", uselist=False))
    user = db.relationship("User", backref=db.backref("user", uselist=False))
