# encoding: utf-8
"""
Test Core Init
==============

Test suite to validate entity registration

"""

def test_entity_module_registration():

    from flask import Flask
    app = Flask("test")

    from app import core
    core.init_app(app)
