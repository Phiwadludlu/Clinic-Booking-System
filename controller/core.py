import json
from flask import render_template, redirect, url_for,request, flash
from flask_security import current_user, auth_required
from forms.appointment_form import AppointmentForm
from models.clinic_model import Appointment
from models import db

def index():
    return render_template("index/index.html")

def about_page():
    return render_template("index/about.html")


def service_page():
    return render_template("index/service.html")

def contact_us_page():
    return render_template("index/contact_us.html")

def dashboard():
    return render_template("admin/dashboard.html")

@auth_required()
def appointment():
    form = AppointmentForm()
    
    if not current_user.is_authenticated:
        return redirect(url_for('security.login', next=request.url))
    
    form.populate_clinic_choices()
    form.populate_user_choices()
    
    if request.method == "POST":
        if form.validate_on_submit():
            clinic = form.clinic.data
            user = form.user.data
            time_slots = form.time_slot.data
            appointment = Appointment(clinic_id=clinic,user_id = user,appointment_time=time_slots )

            #save data to database
            db.session.add(appointment)
            db.session.commit()
            flash(message="Form was submitted succesfully", category="success")
            return redirect(url_for("blueprint.index"))
        else:

            flash("Choose a time between 0900h and 1700h")
            return render_template("admin/appointments.html", form=form )
        
    return render_template("admin/appointments.html", form=form )

