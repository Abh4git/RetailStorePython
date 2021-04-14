from app.main.model.products import Product
from flask import  jsonify
import json
class ProductController:

    def __init__(self):
        pass

    def obj_dict(self,obj):
        return obj.to_json()

    def getAllProducts(self):
        products=Product.query.all()
        #return jsonify(products)
        result = []
        for product in products:
            result.append(product.to_json())
        #products.to_collection_dict()
        #result=json.dumps([dict(mpn=pn) for pn in products])
        return jsonify({"products":products})

    def getAllProductsByType(self,producttypeid):
        products=Product.query.filter_by(producttype_id =producttypeid)
        #return jsonify(products)
        result = []
        for product in products:
            result.append(product.to_json())
        return jsonify({"products":result})