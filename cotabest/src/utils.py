from flask import abort


def search_or_create(username, model):
    user = model.query.filter_by(username=username).first()
    if user:
        return user
    else:
        user = model(username=username)
        user.create()
        return user


def get_all_or_404(query, message=None):
    empty = []
    if query == empty:
        raise abort(404, message)
    return query
