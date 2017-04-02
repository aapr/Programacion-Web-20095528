import os
import urllib.request

from flask import Blueprint
from flask import request, jsonify, render_template

from app.models import Movie, Review, db

main = Blueprint('main', __name__)


# movie = Blueprint('movie', __name__)


@main.route('/')
def index():
    return render_template('review.html')


# @review.route('/reviews', methods=['GET'])
def get_all_review():
    if request.method == 'GET':
        data = []
        for i in Review.query.all():
            data.append(i.serialize())
        result = jsonify(data)
        return result


@main.route('movies', methods=['GET'])
def get_all_movies():
    if request.method == 'GET':
        data = []
        for i in Review.query.all():
            data.append(i.serialize())
        result = jsonify(data)
        return result


@main.route('movies/<movie_name>', methods=['GET'])
def get_movie_by_name():
    if request.method == 'GET':
        name = request.form['name']

        if Movie.query.filter_by(Name=name).startswith() > 0:
            data = Movie.query.filter_by(Name=name).startswith()
            result = jsonify(data.serialize())
            return result
        else:
            return render_template('review.html')
    return render_template('movie.html')


# @review.route('/reviews', methods=['POST'])
def post_form_data():
    if request.method == 'POST':
        name = request.form['name']

        if Movie.query.filter_by(Name=name).count() > 0:
            data = Movie.query.filter_by(Name=name).first()

            title = request.form['reviewTitle']
            description = request.form['Description']
            score = request.form['movieScore']
            user = request.form['user']

            result = Review(title, description, data.id, data.id, user, None, score);

            db.session.add(result)
            db.session.commit()

    return render_template('review.html')


@main.route('movies', methods=['POST'])
def create_movie():
    j_data = request.get_json(True, True, False)
    local_poster_name = j_data['id'] + '.jpg'

    something = Movie.query.filter_by(Id=j_data['id']).first()
    if something is not None:
        try:
            file = open('app/static/posters/' + something.Poster, 'r')
            file.close()
        except:
            url_poster = j_data["poster"]
            url_local = os.path.join("app\static\posters", local_poster_name)
            urllib.request.urlretrieve(url_poster, url_local)
        finally:
            setattr(something, 'Poster', local_poster_name)
            db.session.commit()
            print('old entry')
    else:
        url_poster = j_data["poster"]
        url_local = os.path.join("app\static\posters", local_poster_name)
        urllib.request.urlretrieve(url_poster, url_local)

        result = Movie(j_data['id'], j_data['name'], j_data['descr'], local_poster_name)
        db.session.add(result)
        db.session.commit()
        print('new entry')

    return jsonify(j_data)
