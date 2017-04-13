from flask import Flask

from app.config import Config
from app.models import db
from app.review.controllers import main
from prefixmid import PrefixMiddleware

app = Flask(__name__)

app.config.from_object(Config)
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/arnulfo')
db.init_app(app)
db.create_all(app=app)

app.register_blueprint(main, url_prefix='/')
