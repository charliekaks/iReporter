from marshmallow import ValidationError, Schema, fields, ValidationError

def validation_of_strings(s):
    if not s.strip():
        raise ValidationError('Empty string invalid')


class IncidentSchema(Schema):
    id = fields.Int()
    createdOn = fields.DateTime()
    createdBy = fields.Int(required=True)
    incident_type = fields.Str(required=True)
    location = fields.Str(required=True)
    comment = fields.Str(required=True)
    status = fields.Str()
    image = fields.List(fields.Str())
    video = fields.List(fields.Str())


class UserSchema(Schema):
    id = fields.Int()
    firstname = fields.Str(required=True, validate=validation_of_strings)
    lastname = fields.Str(required=True, validate=validation_of_strings)
    othernames = fields.Str(validate=validation_of_strings)
    phoneNumber = fields.Str(required=True, validate=validation_of_strings)
    username = fields.Str(required=True, validate=validation_of_strings)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validation_of_strings)
    isAdmin = fields.Bool()
    registeredOn = fields.DateTime()


class IncidentEditSchema(Schema):
    """Incident schema for edit comment/location as well as delete"""
    id = fields.Int(required=True)
    comment = fields.Str(required=True)
    location = fields.Str(required=True)