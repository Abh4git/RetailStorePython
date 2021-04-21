from app.main.model.user import User
from app.main import db
from datetime import date
from flask import request
from flask import  jsonify
import json
class UserController:
    def __init__(self):
        pass

    def addUser(self,username,password,email):
        user = User()
        user.username=username
        user.password =password
        user.email=email
        user.registered_on=date.today()
        user.admin = False
        user.public_id = username
        db.session.add(user)
        db.session.commit()
        response = jsonify(user)
        response.status_code = 201
        return response

