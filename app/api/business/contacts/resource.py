# encoding: utf-8
# pylint: disable=too-few-public-methods,invalid-name,bad-continuation
"""
RESTful API Contacts resources
==============================
"""
import logging
import uuid

from flask_restplus import Resource
from app.api.restplus import api
from app.api.business.contacts.models import contact

log = logging.getLogger(__name__)

ns = api.namespace('contacts', description='Operations related to contacts')

contacts = {}

@ns.route('/')
class ContactCollection(Resource):
    """
    Manipulations with contacts.
    """
    @api.response(201, 'Contact successfully created.')
    @api.response(400, 'Bad Data.')
    @api.expect(contact)
    @ns.marshal_with(contact, code=201)
    def post(self):
        """
        Creates a new contact.
        """
        data = api.payload
        contactId = str(uuid.uuid4())
        data['id'] = contactId
        contacts[id] = data
        return contacts[id], 201

@ns.route('/<string:id>')
@api.response(200, 'Success.')
@api.response(404, 'Contact not found.')
class ContactItem(Resource):
    """
    Manipulations with a specific contact.
    """
    @api.marshal_with(contact)
    def get(self, contactId):
        """
        Returns a single contact by id.
        """
        return contacts[contactId], 200
