import csv
from ..models import Movie
from ..database import db

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
