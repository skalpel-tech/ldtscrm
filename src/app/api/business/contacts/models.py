from flask_restplus import fields
from api.restplus import api

contact = api.model('Contact', {
    'id': fields.String(readOnly=True, description='The unique identifier of a contact'),
    'last-name': fields.String(required=True, description='The last name of the contact'),
    'middle-names': fields.String(required=True, description='The middle name(s) of the contact'),
    'first-name': fields.String(required=True, description='The firstname of the contact object'),
})