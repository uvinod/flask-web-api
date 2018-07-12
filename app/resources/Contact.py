from flask import request
from flask_restful import Resource
from app.models import db, Contact, ContactSchema

contacts_schema = ContactSchema(many=True)
contact_schema = ContactSchema()

class ContactResource(Resource):
    def get(self):
        key = request.args.get('key')

        if key:
            contacts = Contact.query.filter(Contact.contact_key==key).all()
        else:
            contacts = Contact.query.all()

        contacts = contacts_schema.dump(contacts).data
        return {'status': 'success', 'message': '<a href="#">test</a>'}, 200