import os
import urllib

from flask import Blueprint
from flask import request, jsonify, redirect

from app.models import Movie, Review, db

main = Blueprint('main', __name__)

# movie = Blueprint('movie', __name__)


@main.route('/')
def index():
    return redirect('review.html')


@main.route('reviews', methods=['GET'])
def get_all_review():
        return jsonify([i.serialize() for i in Review.query.all()])


@main.route('reviews/has', methods=['GET'])
def get_all_has_review():
    data = []
    for e in Review.query.distinct(Review.MovieId).all():
        something = Movie.query.filter_by(Id=e.MovieId).first()
        if something is not None:
            data.append(e.serialize())
    # TODO: calculate average score
    return jsonify(data)


@main.route('movies/has', methods=['GET'])
def get_all_has_movies():
    j_data = request.get_json(True, True, False)
    data = []
    for e in Review.query.filter_by(Id=j_data.id).all():
        data.append(e.serialize())
    return jsonify(data)


@main.route('movies', methods=['GET'])
def get_all_movies():
    return jsonify([i.serialize() for i in Movie.query.all()])


@main.route('movies/<movie_name>', methods=['GET'])
def get_movie_by_name(movie_name):
    p = Movie.Name.startswith(movie_name)
    return jsonify([i.serialize() for i in Movie.query.filter(p).all()])


@main.route('movies/<movie_id>', methods=['GET'])
def get_all_movie_reviews(movie_id):
    return jsonify([i.serialize() for i in Movie.query.filter_by(Id=movie_id).all()])


@main.route('reviews', methods=['POST'])
def post_form_data():
    j_data = request.get_json(True, True, False)
    print(j_data)
    name = 'None'

    title = j_data['title']
    description = j_data['descr']
    score = j_data['score']
    user = j_data['user']

    if Movie.query.filter_by(Name=name).count() > 0:
        data = Movie.query.filter_by(Name=name).first()
        result = Review(title, description, data.id, user, 0, score)
    else:
        result = Review(title, description, 0, user, 0, score)

    db.session.add(result)
    db.session.commit()
    # TODO: get movie id

    return jsonify(j_data)


@main.route('movies', methods=['POST'])
def create_movie():
    j_data = request.get_json(True, True, False)
    local_poster_name = j_data['id'] + '.jpg'

    something = Movie.query.filter_by(Id=j_data['id']).first()
    if something is not None:
        try:
            file = open('posters/' + something.Poster, 'r')
            file.close()
        except:
            url_poster = j_data["poster"]
            url_local = os.path.join("posters", local_poster_name)
            urllib.urlretrieve(url_poster, url_local)
        finally:
            setattr(something, 'Poster', local_poster_name)
            db.session.commit()
            print('old entry')
    else:
        url_poster = j_data["poster"]
        url_local = os.path.join("posters", local_poster_name)
        urllib.urlretrieve(url_poster, url_local)

        result = Movie(j_data['id'], j_data['name'], j_data['descr'], local_poster_name)
        db.session.add(result)
        db.session.commit()
        print('new entry')

    return jsonify(j_data)
