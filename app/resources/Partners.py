from flask import request
from flask_restful import Resource
from app.models import db, Partners, PartnersSchema

partners_schema = PartnersSchema(many=True)
partner_schema = PartnersSchema()

class PartnersResource(Resource):
    def get(self):
        key = request.args.get('key')

        if key:
            partners = Partners.query.filter(Partners.type==key).all()
        else:
            partners = Partners.query.all()

        partners = partners_schema.dump(partners).data
        return {'status': 'success', 'message': partners[0]['values']}, 200