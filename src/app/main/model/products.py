from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from .. import db, flask_bcrypt
import json

@dataclass
class Product(db.Model):
    """ Product Model for storing Product related details """
    id:int
    name:str
    description:str
    imagename:str

    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=False)
    producttype_id = db.Column(db.Integer, db.ForeignKey('product_types.id'))
    producttype =  db.relationship('ProductType', backref='Product', lazy=True)
    imagename = db.Column(db.String(255), unique=True, nullable=True)

    def __repr__(self):
        return "<Product '{}'>".format(self.name)

    def to_json(self):
        return "{ id:" + str(self.id) + ", name:" + self.name +",description:" + self.description + "}"

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
