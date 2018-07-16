from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

class Contact(db.Model):
    __tablename__ = 'contact'
    
    id = db.Column(db.Integer, primary_key=True)
    contact_key = db.Column(db.String(60))
    contact_value = db.Column(db.String(255))

    def __init__(self, contact_value, contact_key):
        self.contact_value = contact_value
        self.contact_key = contact_key

class Customers(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer,primary_key=True)
    type = db.Column(db.String(100))
    values = db.Column(db.Text)

    def __init__(self, content, values):
        self.type = type
        self.values = values

class Partners(db.Model):
    __tablename__ = 'partners'

    id = db.Column(db.Integer,primary_key=True)
    type = db.Column(db.String(100))
    values = db.Column(db.Text)

    def __init__(self, content, values):
        self.type = type
        self.values = values

class ContactSchema(ma.Schema):
    id = fields.Integer()
    contact_key = fields.String()
    contact_value = fields.String()

class CustomersSchema(ma.Schema):
    id = fields.Integer()
    type = fields.String()
    values = fields.String()

class PartnersSchema(ma.Schema):
    id = fields.Integer()
    type = fields.String()
    values = fields.String()