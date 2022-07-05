from flask_restplus import Api
from flask import Blueprint

from app.main.controllers.api_content_controller import api as con_api
from app.main.controllers.ssl_cert_controller import api as ssl_api


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='CuriousReads',
          version='1.0',
          description=''
          )


api.add_namespace(con_api, path='/')
api.add_namespace(ssl_api, path='/')
