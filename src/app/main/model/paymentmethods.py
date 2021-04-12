from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .. import db, flask_bcrypt

class PaymentMethods(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "payment_methods"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=False)
    code = db.Column(db.Integer, autoincrement=True)

def __repr__(self):
    return "<ProductType '{}'>".format(self.username)
