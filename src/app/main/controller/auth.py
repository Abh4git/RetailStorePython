from app.main.model.user import User

from flask import  jsonify
import json
import jwt
import datetime
import app
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity

from flask_jwt_extended import JWTManager

class AuthenticationController:
    def __init__(self):
        pass

    def verify_password(self,username, password):
        user = User.query.filter_by(username=username).first()
        if user is None:
            return False
        return user.check_password(password)

    def create_token(self,username):
        return create_access_token(username)
    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.main.config.get('SECRET_KEY'),
                algorithm='HS256'
            ).decode('UTF-8')
        except Exception as e:
            return e