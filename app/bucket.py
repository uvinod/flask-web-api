from flask import Blueprint
from flask_restful import Api
from app.resources.Hello import Hello
from app.resources.Contact import ContactResource
from app.resources.Customers import CustomersResource
from app.resources.Partners import PartnersResource

bucket = Blueprint('bucket', __name__)
api = Api(bucket)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(ContactResource, '/Contact')
api.add_resource(CustomersResource, '/Customers')
api.add_resource(PartnersResource, '/Partners')