from .database import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    studios = db.Column(db.String(200), nullable=False)
    producers = db.Column(db.String(200), nullable=False)
    winner = db.Column(db.Boolean, default=False)
