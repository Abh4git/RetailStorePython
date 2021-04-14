#All Routes are defined here
from flask_cors import CORS, cross_origin
from app.main.controller.products import ProductController
#Test route without any connections
def test():
    return "{testroutesuccess:'Test Route Success!'}"

api_v2_cors_config = {
  "origins": ["http://localhost:3000"],
  "methods": ["OPTIONS", "GET", "POST"],
  "allow_headers": ["Authorization", "Content-Type"]
}

#route returning Products list
@cross_origin(**api_v2_cors_config)
def getProductsList():
    product = ProductController()
    return product.getAllProducts()

#route for products list filtered by product types
def getProductsListByType(typeid):
    product = ProductController()
    return product.getAllProductsByType(typeid)

