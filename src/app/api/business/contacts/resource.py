import logging
import uuid

from flask import request
from flask_restplus import Resource
from src.app.api.restplus import api
from src.app.api.business.contacts.models import contact

log = logging.getLogger(__name__)

ns = api.namespace('contacts', description='Operations related to contacts')

contacts = {}

@ns.route('/')
class ContactCollection(Resource):

    @api.response(201, 'Contact successfully created.')
    @api.response(400, 'Bad Data.')
    @api.expect(contact)
    @ns.marshal_with(contact, code=201)
    def post(self):
        """
        Creates a new contact.
        """
        data = api.payload
        id = str(uuid.uuid4())
        data['id'] = id
        contacts[id] = data
        return contacts[id], 201    


@ns.route('/<string:id>')
@api.response(200, 'Success.')
@api.response(404, 'Contact not found.')
class ContactItem(Resource):

    @api.marshal_with(contact)
    def get(self, id):
        """
        Returns a single contact by id.
        """
        return contacts[id], 200