# encoding: utf-8
"""
Entity module
============

Entities are used to model and manage business data
Entities defines business data using entityType.
Entities Data Model is dynamic and defined using jsonSchema.
Business Data is stored in the content field of the entity.

"""
from .models import *

def init_app(app):#pylint: disable=W0613
    """
    Loads the entity modules.

    pylint disable as registration does not perform action yet.

    Parameters
    ----------
    app (Flask): The flask application.
    """
    pass
