# encoding: utf-8
"""
Modules
=======

LDTS CRM Features are organized in modules.
Each module is independent and can be activated/deactivated using configuration.

Configuration
-------------

Modules can be activated/deactivated in config.py

.. code-block:: python
    # ENABLED MODULES
    MODULES = (
        'entity'
    )

"""
def init_app(app, **kwargs):
    """
    Bootsraps modules.

    Called at initialization of flask application to register modules.

    Parameters
    ----------
    app (Flask): The flask application.
    **kwargs: Arbitrary keyword arguments.

    """
    from importlib import import_module

    for module_name in app.config['MODULES']:
        import_module('.%s' % module_name, package=__name__).init_app(app, **kwargs)
