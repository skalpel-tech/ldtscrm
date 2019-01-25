# encoding: utf-8
"""
Flask-RESTplus API registration module
======================================
"""
import logging

from flask_restplus import Api

log = logging.getLogger(__name__)

api = Api(version='0.1', title='LTDS CRM API',
          description='full open source crm api')
