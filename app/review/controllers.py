import urllib.request

from flask import Blueprint
from flask import request, jsonify, render_template

from app.models import Movie, Review, db

main = Blueprint('main', __name__)
movie = Blueprint('movie', __name__)


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


@movie.route('/', methods=['GET'])
def get_all_movies():
    if request.method == 'GET':
        data = []
        for i in Review.query.all():
            data.append(i.serialize())
        result = jsonify(data)
        return result


@movie.route('/<movie_name>', methods=['GET'])
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


# @movie.route('/', methods=['POST'])
def create_movie():
    if request.method == 'POST':
        name = request.form['name']

        if Movie.query.filter_by(Name=name).count() == 0:
            poster = request.form['poster']

            try:
                f = open('app/static/posters/' + name + '.jpg', 'wb')
                with urllib.request.urlopen(poster) as url:
                    s = url.read()
                    f.write(s)
                    f.close()
                    local_poster = '_' + name + '.jpg'
            except:
                local_poster = ''

            description = request.form['Description']

            result = Movie(name, description, local_poster);

            db.session.add(result)
            db.session.commit()
    return render_template('movie.html')
