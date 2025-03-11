from collections import defaultdict
from ..models import Movie

def get_producer_award_years(movies):
    producers = defaultdict(list)
    
    for movie in movies:
        for producer in map(str.strip, movie.producers.replace('and', ',').split(',')):
            producers[producer].append(movie.year)
    
    return producers

def calculate_award_intervals():
    movies = Movie.query.filter_by(winner=True).order_by(Movie.year).all()
    producers = get_producer_award_years(movies)
    
    intervals = [
        {
            'producer': producer,
            'interval': years[i] - years[i - 1],
            'previousWin': years[i - 1],
            'followingWin': years[i],
        }
        for producer, years in producers.items() if len(years) > 1
        for i in range(1, len(years))
    ]
    
    return intervals
