import logging

from flask_restplus import Api
from config import settings

log = logging.getLogger(__name__)

api = Api(version='0.1', title='Skpcrm API',
          description='SKP Crm api')