from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), index=True, unique=True)
    Description = db.Column(db.String(150))
    Poster = db.Column(db.String(64))
    reviews = db.relationship('Review', backref='movie', lazy='dynamic')

    def __init__(self, id, name, description, poster):
        self.id = id
        self.name = name
        self.description = description
        self.poster = poster

    def __repr__(self):
        return '<Movie %r>' % (self.name)

    def serie(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'poster': self.poster
        }


class Review(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(64), index=True, unique=True)
    Description = db.Column(db.String(150))
    Rating = db.Column(db.Integer)
    User = db.Column(db.String(64))
    DeviceId = db.Column(db.Integer)
    MovieId = db.Column(db.Integer, db.ForeignKey('movie.Id'))

    def __init__(self, title, desc, movieid, user, deviceid=0, rating=0):
        self.Title = title
        self.Description = desc
        self.Rating = rating
        self.User = user
        self.DeviceId = deviceid
        self.MovieId = movieid

    def __repr__(self):
        return '<Review %r>' & (Review.Title)

    def serialize(self):
        return {
            'id': self.Id,
            'title': self.Title,
            'description': self.Description,
            'rating': self.Rating,
            'user': self.User,
            'deviceid': self.DeviceId
        }
