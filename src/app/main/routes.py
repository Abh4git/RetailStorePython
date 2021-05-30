#All Routes are defined here
from flask_cors import CORS, cross_origin
from app.main.controller.products import ProductController
from app.main.controller.user import UserController
import app
from app.main.controller.auth import AuthenticationController
from flask import request
from flask_jwt_extended import jwt_required

#Test route without any connections
def test():
    return "{testroutesuccess:'Test Route Success!'}"

api_v2_cors_config = {
  "origins": [
    'http://localhost:3000'  # React
  # React
  ],
  "methods": ["OPTIONS", "GET", "POST"],
  "allow_headers": ["Authorization", "Content-Type"]
}

#route returning Products list
@cross_origin(**api_v2_cors_config)
def getProductsList():
    productC = ProductController()
    return productC.getAllProducts()

#route for products list filtered by product types
@cross_origin(**api_v2_cors_config)
def getProductsListByType(typeid):
    productC = ProductController()
    return productC.getAllProductsByType(typeid)

@cross_origin(**api_v2_cors_config)
def getProductTypesList():
    productC = ProductController()
    return productC.getProductTypes()
    userController = UserController()
    userController.addUser(username=request.json.username,password=request.json.password,email=request.json.email)
    return userController.getProductTypes()

@cross_origin()
def login():
    auth = AuthenticationController()
    #print(request.is_json)
    userinfo = request.get_json()
    print(userinfo)
    authResult=auth.verify_password (userinfo['username'], userinfo['password'])
    accesstoken = auth.create_token(userinfo['username'])
    response= {"AuthResult": authResult,"accessToken":accesstoken,"user":userinfo['username']}
    return response


@cross_origin(**api_v2_cors_config)
@jwt_required()
def addUser():
    userController = UserController()
    print(request.is_json)
    userinfo =request.get_json()
    print(userinfo)
    userController.addUser(username=userinfo['username'], password=userinfo['password'], email=userinfo['email'])
    return {"Success":"1"}

@cross_origin(**api_v2_cors_config)
def addProduct():
    productController = ProductController()
    print(request.is_json)
    productinfo =request.get_json()
    print(productinfo)
    response=productController.addProduct(id=productinfo['id'], name=productinfo['name'], description=productinfo['description']
                                          , producttype_id=productinfo['producttype_id'], imagename=productinfo['imagename'])
    return response
