import logging

from flask_restplus import Api
from src.app.config import settings

log = logging.getLogger(__name__)

api = Api(version='0.1', title='LTDS CRM API',
          description='full open source crm api')