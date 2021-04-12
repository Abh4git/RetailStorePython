from flask import jsonify, request, url_for, g, abort
from app.main import db
from app.main.model.products  import Product
from app.main.service import bp
from app.main.service.auth import token_auth
from app.main.service.errors import bad_request


@bp.route('/products/', methods=['GET'])
#@token_auth.login_required
def get_products():
    return "{ testproducts:['book1','Food1']}"
