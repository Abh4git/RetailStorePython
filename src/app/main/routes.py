#All Routes are defined here
from app.main.controller.products import ProductController
#Test route without any connections
def test():
    return "{testroutesuccess:'Test Route Success!'}"


#route returning Products list
def getProductsList():
    product = ProductController()
    return product.getAllProducts()

#route for products list filtered by product types
def getProductsListByType(typeid):
    product = ProductController()
    return product.getAllProductsByType(typeid)

