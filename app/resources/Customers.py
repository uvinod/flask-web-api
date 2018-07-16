from flask import request
from flask_restful import Resource
from app.models import db, Customers, CustomersSchema

customers_schema = CustomersSchema(many=True)
customer_schema = CustomersSchema()

class CustomersResource(Resource):
    def get(self):
        key = request.args.get('key')

        if key:
            customers = Customers.query.filter(Customers.type==key).all()
        else:
            customers = Customers.query.all()

        customers = customers_schema.dump(customers).data
        return {'status': 'success', 'message': customers[0]['values']}, 200