

from flask_security import (
        RegisterForm,
        LoginForm,
        Security,
        lookup_identity,
        uia_username_mapper,
        unique_identity_attribute,
    )

from werkzeug.local import LocalProxy
from wtforms import StringField, ValidationError, validators, IntegerField

def username_validator(form, field):
        # Side-effect - field.data is updated to normalized value.
        # Use proxy to we can declare this prior to initializing Security.
        from app import app
        _security = LocalProxy(lambda: app.extensions["security"])
        msg, field.data = _security._username_util.validate(field.data)
        if msg:
            raise ValidationError(msg)

class MyRegisterForm(RegisterForm):
        # Note that unique_identity_attribute uses the defined field 'mapper' to
        # normalize. We validate before that to give better error messages and
        # to set the normalized value into the form for saving.
        username = StringField(
            "Username",
            validators=[
                validators.data_required(),
                username_validator,
                unique_identity_attribute,
            ],

        )

        student_number = StringField(
               "Student Number",validators=[
               validators.data_required(),
               validators.length(min = 8, max=8,message="Student number is incorrect" )
               ]

        )