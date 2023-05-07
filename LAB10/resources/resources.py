from flask import request, Response, jsonify
from flask_restful import Resource
from database.models import Product

class ProductAPI(Resource):
    def get(self):
        products = Product.all().to_json()
        return Response(products, mimetype="application/json", status=200)

    def post(self):
        data = request.get_json()
        pro = Product(**data)
        pro.save()
        id = pro.id
        return {"id": str(id)},200

class ProductAPIbyParam(Resource):
    def get(self, id):
        products = Product.objects.get(id=id).to_json()
        return Response(products, mimetype="application/json", status=200)
    def put(self, id):
        body = request.get_json()
        Product.objects.get(id=id).update(**body)
        return {'id': str(id)}, 200

    def delete(self, id):
        Product.objects.get(id=id).delete()

