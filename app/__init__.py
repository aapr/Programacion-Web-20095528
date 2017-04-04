from flask import Flask

from app.config import Config
from app.models import db
from app.review.controllers import main

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
db.create_all(app=app)

app.register_blueprint(main, url_prefix='/')
