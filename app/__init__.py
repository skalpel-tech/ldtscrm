# encoding: utf-8
"""
LDTS RESTful API Server.
"""
import logging.config
import os
import sys
from flask import Flask, Blueprint

from app.extensions.api.restplus import api

CONFIG_NAME_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'testing': 'config.TestingConfig',
    'production': 'config.ProductionConfig',
    'local': 'local_config.LocalConfig',
}

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

def create_app(flask_config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application
    """
    app = Flask(__name__, **kwargs)
    initialize_app(app)

    configure_app(app, flask_config_name)

    initialize_core(app)

    from . import extensions
    extensions.init_app(app)

    log.info('>>>>> Starting development server at http://%s/api/ <<<<<', app.config['SERVER_NAME'])
    return app

def configure_app(app, flask_config_name=None):
    env_flask_config_name = os.getenv('FLASK_CONFIG')
    if not env_flask_config_name and flask_config_name is None:
        flask_config_name = 'local'
    elif flask_config_name is None:
        flask_config_name = env_flask_config_name
    else:
        if env_flask_config_name and env_flask_config_name != flask_config_name:
            raise ValueError(
                "FLASK_CONFIG environment variable (\"%s\") and flask_config_name argument "
                "(\"%s\") are both set and are not the same." % (
                    env_flask_config_name,
                    flask_config_name
                )
            )

    try:
        app.config.from_object(CONFIG_NAME_MAPPER[flask_config_name])
    except ImportError:
        if flask_config_name == 'local':
            app.logger.error(
                "You have to have `local_config.py` or `local_config/__init__.py` in order to use "
                "the default 'local' Flask Config. Alternatively, you may set `FLASK_CONFIG` "
                "environment variable to one of the following options: development, production, "
                "testing."
            )
            sys.exit(1)
        raise

def initialize_core(app):
    """`
    Initializes core application modules

    Parameters
    ----------
    app (Flask): The flask application.

    """
    from . import core
    core.init_app(app)
    log.info("core initialized")

def initialize_app(app):
    configure_app(app)
    log.info('initialize app')
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    app.register_blueprint(blueprint)
