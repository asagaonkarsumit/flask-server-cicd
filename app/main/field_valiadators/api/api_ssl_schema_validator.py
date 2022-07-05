from marshmallow import Schema, fields
from marshmallow.validate import Length, OneOf
from pycountry import countries


class apiSslValidator(Schema):
    fqdn = fields.String(required=True)
    
