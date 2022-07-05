from marshmallow import Schema, fields
from marshmallow.validate import Length


class apiBrandArticleValidator(Schema):
    title = fields.String(required=True, validate=Length(min=10, max=1000))
    description = fields.String(required=True, validate=Length(min=10, max=1000))
    canonical_link = fields.URL(required=True, validate=Length(max=1000))
    image_link = fields.String(required=True, validate=Length(max=1000))
    content_type = fields.String(required=True, validate=Length(min=1, max=40))
    site_name = fields.String(required=False, validate=Length(max=200))
    tags = fields.List(required=False, cls_or_instance=fields.String(validate=Length(min=1, max=50)))
    favicon_icon_link = fields.String(required=False, validate=Length(max=1000))