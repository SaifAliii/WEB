from .resources import ProductAPI, ProductAPIbyParam

def initialize_route(api):
    api.add_resource(ProductAPI, '/api/product')
    api.add_resource(ProductAPIbyParam, '/api/product/<id>')