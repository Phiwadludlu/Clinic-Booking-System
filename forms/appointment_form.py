from flask_wtf.form import _Auto
from wtforms import Form,StringField, SelectField, TimeField,DateField, validators
from models.clinic_model import Clinic
from models.user_model import User
from services import user_service 
from flask_security import current_user
from flask_wtf import FlaskForm
import datetime

def date_validator(form, field:datetime):
    date = field.data
    if date:
        if not date.weekday():
            raise validators.ValidationError(message="Ivalid date provide weekday date")


def time_slot_validator(form,field):
    time_slot = field.data
    open_time =  datetime.datetime.strptime("09:00:00", "%H:%M:%S")
    closing_time = datetime.datetime.strptime("17:00:00", "%H:%M:%S")
    time_slot = datetime.datetime.combine(datetime.date.today(), time_slot)

    
    if time_slot.time()< open_time.time() and time_slot.time()>closing_time.time():
        raise validators.ValidationError(message="Please choose time between 8:30 and 17:30")


class AppointmentForm(FlaskForm):
    
    

    clinic = SelectField("Clinic")
    user = SelectField("User")
    time_slot = TimeField("Time", validators=[validators.DataRequired(), time_slot_validator])
    date = DateField("Date", validators=[ date_validator])


    def populate_clinic_choices(self):
        clinic_choices = [(choice.id, choice.clinic_name) for choice in Clinic.query.all()]
        self.clinic.choices = clinic_choices

    
    def populate_user_choices(self):
        user = User.query.get(current_user.id)
        user_choice = [(user.id,user.username),]
        self.user.choices = user_choice

