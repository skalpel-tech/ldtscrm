# encoding: utf-8
"""
LDTS RESTful API Server.
"""
import logging.config
import os
from flask import Flask, Blueprint

from app.config import settings
from app.api.restplus import api

from app.api.business.contacts.resource import ns as contact_namespace


logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def create_app(**kwargs):
  """
  Entry point to the Flask RESTful Server application
  """
  app = Flask(__name__, **kwargs)
  initialize_app(app)
  log.info('>>>>> Starting development server at http://%s/api/ <<<<<', app.config['SERVER_NAME'])
  return app

def configure_app(flask_app):
  flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
  flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
  flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
  flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
  flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
  configure_app(flask_app)
  log.info('initialize app')
  blueprint = Blueprint('api', __name__, url_prefix='/api')
  api.init_app(blueprint)
  api.add_namespace(contact_namespace)
  flask_app.register_blueprint(blueprint)
