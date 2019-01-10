# encoding: utf-8
"""
Test Entity init
================

Test suite to validate entity registration

"""

def test_entity_module_registration():

    from flask import Flask
    app = Flask("test")

    from app.core import entity
    entity.init_app(app)
