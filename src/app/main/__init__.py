from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .config import config_by_name
db = SQLAlchemy()
flask_bcrypt = Bcrypt()
#We will be using the application factory pattern for creating our
#Flask object.
from flask_cors import CORS, cross_origin

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    db.init_app(app)
    flask_bcrypt.init_app(app)
    return app