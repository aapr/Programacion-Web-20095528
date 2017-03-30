from flask import Flask
from app.models import db
from app.review.controllers import main,movie
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
db.create_all(app=app)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(movie, url_prefix='/movies')
