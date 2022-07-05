from app.main.utils.api_ssl_dto import api_ssl_dto
from flask_restplus import Resource
from app.main.field_valiadators.api.api_ssl_schema_validator import apiSslValidator
from flask import request
from app.main.controllers import error_m
from werkzeug.exceptions import abort
from http import HTTPStatus
from app.main.services.api_ssl_services import save_content
api = api_ssl_dto.api
_req_api_ssl = api_ssl_dto.req_api_ssl
_res_api_ssl = api_ssl_dto.res_api_ssl
_post_validator = apiSslValidator()


@api.route("api/v.1/test/ci")
class Content(Resource):
    # @api.marshal_with(_res_api_ssl)
    # @api.expect(_req_api_ssl)
    def get(self):
        data = request.json
        return save_content(data)
