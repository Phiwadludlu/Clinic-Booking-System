from flask_wtf.form import _Auto
from wtforms import Form,StringField, SelectField, TimeField, validators
from models.clinic_model import Clinic
from models.user_model import User
from services import user_service 
from flask_security import current_user
from flask_wtf import FlaskForm

def get_user_choice():
    user = user_service.get_users()
    



class AppointmentForm(FlaskForm):
    
    

    clinic = SelectField("Clinic")
    user = SelectField("User")
    time_slot = TimeField("Time", validators=[validators.DataRequired()])

 

    def populate_clinic_choices(self):
        clinic_choices = [(choice.id, choice.clinic_name) for choice in Clinic.query.all()]
        self.clinic.choices = clinic_choices

    
    def populate_user_choices(self):
        user = User.query.get(current_user.id)
        user_choice = [(user.id,user.username),]
        self.user.choices = user_choice

