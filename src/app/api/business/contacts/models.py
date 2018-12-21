from flask_restplus import fields
from api.restplus import api

givenName = api.model('GivenNames', {
    'firstname': fields.String(required=True, description='The surname of the contact'),
    'middlename': fields.String(required=True, description='The surname of the contact')
})

contact = api.model('Contact', {
    'id': fields.String(readOnly=True, description='The unique identifier of a contact'),
    'surname': fields.String(required=True, description='The surname of the contact'),
    'givenNames': fields.Nested(givenName)
})

