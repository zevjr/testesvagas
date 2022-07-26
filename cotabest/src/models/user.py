from datetime import datetime

from ..db import db, ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f"<User {self.username}>"


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
