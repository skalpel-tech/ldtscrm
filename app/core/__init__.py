# encoding: utf-8
"""
Core
=======

LDTS CRM Core Features are organized in modules.

Modules
-------

* Entity => Core model for graph nodes
* Relationship => Core model for graph edges

"""
def init_app(app):
    """
    Bootsraps core modules.

    Called at initialization of flask application to register core modules.

    Parameters
    ----------
    app (Flask): The flask application.

    """
    from . import entity

    for module in (
            entity,
        ):
        module.init_app(app)
