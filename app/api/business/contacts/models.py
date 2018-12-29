from flask_restplus import fields
from app.api.restplus import api

contact = api.model('Contact', {

    'id': fields.String(readOnly=True, description='The unique identifier of a contact'),
    'suffix': fields.String(required=True, description='Suffix of a contact'),   
    'title': fields.String(required=True, description='Title of a contact'),  
    'last-name': fields.String(required=True, description='The last name of the contact'),
    'middle-names': fields.String(required=True, description='The middle name(s) of the contact'),
    'first-name': fields.String(required=True, description='The first name of the contact object'),
    'full-name': fields.String(required=True, description='The full name of the contact object'), 
    'description': fields.String(readOnly=True, description='Description of a contact'),
    'city': fields.String(readOnly=True, description='City of contact address'),
    'country': fields.String(readOnly=True, description='Country of contact address'),
    'region': fields.String(readOnly=True, description='Region of contact address(e.g. State, Province, Territory, Region, District)'), #Please read: https://en.wikipedia.org/wiki/ISO_3166-2
    'street': fields.String(readOnly=True, description='Street of contact address'),
    'postal-code': fields.String(readOnly=True, description='Postal Code of contact address'),
    'alternate-address': fields.String(readOnly=True, description='Alternate address details of a contact, compound form'),

})