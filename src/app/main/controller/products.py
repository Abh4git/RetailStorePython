from app.main.model.products import Product
from app.main.model.producttypes import ProductType
from app.main import db
from flask import  jsonify
import json
class ProductController:

    def __init__(self):
        pass

    def obj_dict(self,obj):
        return obj.to_json()

    def getAllProducts(self):
        products=Product.query.all()
        return jsonify({"products":products})

    def getAllProductsByType(self,producttypeid):
        products=Product.query.filter_by(producttype_id =producttypeid)
        return jsonify({"products":products})

    def addProduct(self, id, name, description, producttype_id, imagename):
        product=Product()
        product.id=id
        product.name=name
        product.description=description
        product.producttype_id=producttype_id
        product.imagename=imagename
        db.session.add(product)
        db.session.commit()
        response = jsonify(product)
        response.status_code = 201
        return response

    def getProductTypes(self):
        producttypes=ProductType.query.all()
        return jsonify({"producttypes":producttypes})

