from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api/v2')

from app.main.service import products, auth, users, errors