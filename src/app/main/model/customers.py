from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .. import db, flask_bcrypt

class Customer(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(255), unique=True, nullable=False)
    lastname = db.Column(db.String(255), unique=True, nullable=False)
    profile = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(255), unique=True, nullable=False)
    address_line1 = db.Column(db.String(255), unique=True, nullable=False)
    address_line2 = db.Column(db.String(255), unique=True, nullable=False)
    city = db.Column(db.Integer,  nullable=False)
    country = db.Column(db.Integer,  nullable=False)
    paymenttype =  db.relationship('PaymentType', backref='Customer', lazy=True)


def __repr__(self):
    return "<Product '{}'>".format(self.username)
