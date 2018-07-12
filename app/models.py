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

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text)

    def __init__(self, content):
        self.content = content

class ContactSchema(ma.Schema):
    id = fields.Integer()
    contact_key = fields.String()
    contact_value = fields.String()

class CustomerSchema(ma.Schema):
    id = fields.Integer()
    content = fields.String()