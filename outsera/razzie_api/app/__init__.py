import csv
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'data', 'movielist.csv')

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


db = SQLAlchemy()


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    studios = db.Column(db.String(200), nullable=False)
    producers = db.Column(db.String(200), nullable=False)
    winner = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


def load_movies_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            movie = Movie(
                year=int(row['year']),
                title=row['title'],
                studios=row['studios'],
                producers=row['producers'],
                winner=row['winner'].lower() == 'yes'
            )
            db.session.add(movie)
        db.session.commit()


with app.app_context():
    db.create_all()
    load_movies_from_csv(caminho_arquivo)



def calculate_award_intervals():
    movies = Movie.query.filter_by(winner=True).order_by(Movie.year).all()
    producers = {}

    for movie in movies:
        for producer in movie.producers.split(', '):
            if producer not in producers:
                producers[producer] = []
            producers[producer].append(movie.year)

    intervals = []
    for producer, years in producers.items():
        if len(years) > 1:
            for i in range(1, len(years)):
                interval = years[i] - years[i - 1]
                intervals.append({
                    'producer': producer,
                    'interval': interval,
                    'previousWin': years[i - 1],
                    'followingWin': years[i]
                })

    return intervals

@app.route('/intervals', methods=['GET'])
def get_award_intervals():
    intervals = calculate_award_intervals()
    if not intervals:
        return jsonify({'min': [], 'max': []})

    min_interval = min(intervals, key=lambda x: x['interval'])
    max_interval = max(intervals, key=lambda x: x['interval'])

    min_intervals = [x for x in intervals if x['interval'] == min_interval['interval']]
    max_intervals = [x for x in intervals if x['interval'] == max_interval['interval']]

    return jsonify({
        'min': min_intervals,
        'max': max_intervals
    })
