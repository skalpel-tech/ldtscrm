# encoding: utf-8
"""
Entity module
============

Entities are used to model and manage business data
Entities defines business data using entityType.
Entities Data Model is dynamic and defined using jsonSchema.
Business Data is stored in the content field of the entity.

"""
from .models import Entity, EntityType, EntityAudit
from .resources import init_routes


def init_app(app):
    """
    Loads the entity modules.

    pylint disable as registration does not perform action yet.

    Parameters
    ----------
    app (Flask): The flask application.
    """
    init_routes(app)