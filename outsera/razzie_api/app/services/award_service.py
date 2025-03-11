from ..models import Movie

def calculate_award_intervals():
    movies = Movie.query.filter_by(winner=True).order_by(Movie.year).all()
    producers = {}

    for movie in movies:
        for producer in movie.producers.replace('and',',').split(','):
            producer = producer.strip()
            if producer not in producers:
                producers[producer] = []
            producers[producer].append(movie.year)

    intervals = []
    for producer, years in producers.items():
        if len(years) > 1:
            for i in range(1, len(years)):
                interval = years[i] - years[i - 1]
                intervals.append(
                    {
                        'producer': producer,
                        'interval': interval,
                        'previousWin': years[i - 1],
                        'followingWin': years[i],
                    }
                )
    return intervals
