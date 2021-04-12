from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .. import db, flask_bcrypt

class Product(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=False)
    producttype =  db.relationship('ProductType', backref='Product', lazy=True)


def __repr__(self):
    return "<Product '{}'>".format(self.username)
