#encoding UTF-8
# pylint: disable=too-few-public-methods

"""
Entity Json Schemas
===================

Represents the entity and entity type json schemas to use for api endpoints.
"""

from flask_restplus import fields
from app.extensions.api.restplus import api


entity_type = api.model('Entity_Type', {
    'name': fields.String(required=True, description='Entity Type Name.', attribute='id'),
    'schema': fields.Raw(required=True, description='Entity Type Json Schema.'),
})
