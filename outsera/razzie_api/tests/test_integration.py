from app.database import db
from app.models import Movie


def test_get_award_intervals(client, app):
    movie1 = Movie(year=2000, title='Movie 1', studios='Studio 1', producers='Producer A', winner=True)
    movie2 = Movie(year=2005, title='Movie 2', studios='Studio 2', producers='Producer A', winner=True)
    movie3 = Movie(year=2010, title='Movie 3', studios='Studio 3', producers='Producer B', winner=True)
    movie4 = Movie(year=2015, title='Movie 4', studios='Studio 4', producers='Producer B', winner=True)

    with app.app_context():
        db.session.add(movie1)
        db.session.add(movie2)
        db.session.add(movie3)
        db.session.add(movie4)
        db.session.commit()

    response = client.get('/award/intervals')
    data = response.get_json()

    assert response.status_code == 200
    assert 'min' in data
    assert 'max' in data
    assert len(data['min']) > 0
    assert len(data['max']) > 0


def test_get_award_intervals_no_winners(client, app):
    response = client.get('/award/intervals')
    data = response.get_json()

    assert response.status_code == 200
    assert 'min' in data
    assert 'max' in data
    assert len(data['min']) == 0  # A lista de intervalos mínimos deve estar vazia
    assert len(data['max']) == 0  # A lista de intervalos máximos deve estar vazia
