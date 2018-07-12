from flask import request
from flask_restful import Resource
from app.models import db, Customer, CustomerSchema

customers_schema = CustomerSchema(many=True)
customer_schema = CustomerSchema()

class CustomersResource(Resource):
    def get(self):
        customers = Customer.query.all()

        customers = customers_schema.dump(customers).data
        return {'status': 'success', 'data': customers}, 200