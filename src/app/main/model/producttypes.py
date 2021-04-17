from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .. import db, flask_bcrypt
from dataclasses import dataclass
import json

@dataclass
class ProductType(db.Model):
    """ Product Type Model for storing type related details """
    id:int
    name:str
    code:str

    __tablename__ = "product_types"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=False)
    code = db.Column(db.String(255), unique=True, nullable=False)

def __repr__(self):
    return "<ProductType '{}'>".format(self.username)


def toJson(self):
    return json.dumps(self, default=lambda o: o.__dict__)
