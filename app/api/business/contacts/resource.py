# encoding: utf-8
# pylint: disable=too-few-public-methods,invalid-name,bad-continuation
"""
RESTful API Contacts resources
==============================
"""
import logging

from flask import request
from flask_restplus import Resource
from app.api.restplus import api
from .schemas import contactSchema
from .services import create_contact, get_contact_by_id

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
    @api.expect(contactSchema)
    @ns.marshal_with(contactSchema, code=201)
    def post(self):
        """
        Creates a new contact.
        """
        new_contact = create_contact(request.json)
        return new_contact, 201

@ns.route('/<string:contact_id>')
@api.response(200, 'Success.')
@api.response(404, 'Contact not found.')
class ContactItem(Resource):
    """
    Manipulations with a specific contact.
    """
    @api.marshal_with(contactSchema)
    def get(self, contact_id):
        """
        Returns a single contact by id.
        """
        return get_contact_by_id(contact_id), 200
