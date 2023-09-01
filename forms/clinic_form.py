from wtforms import Form,StringField, SelectField, TimeField, validators
from flask_wtf import FlaskForm

class ClinicForm(FlaskForm):

    clinic_name =  StringField("Clinic Name", validators=[validators.DataRequired()])
