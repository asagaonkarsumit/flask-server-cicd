from flask_restplus import Namespace, fields


class api_ssl_dto:
    api = Namespace("api_ssl", description="Create ssl")

    res_api_ssl= api.model("ssl request", {
        "status": fields.Boolean(description='brand fqdn create  True')
    })

    req_api_ssl = api.model('response of all sources', {
        "fqdn": fields.String(description='ssl qfqdn ')
    })

