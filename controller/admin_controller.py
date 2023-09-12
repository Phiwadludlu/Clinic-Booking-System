from flask import render_template, redirect, url_for,request, flash
from flask_security import current_user, auth_required
from forms.clinic_form import ClinicForm
from models.clinic_model import Clinic, Appointment
from models import db
from models.user_model import User

@auth_required()
def index():

    return redirect(url_for('admin.admin_dashboard'))

@auth_required()
def admin_dashboard():
    return render_template("admin/dashboard.html")

@auth_required()
def admin_clinic():

    clinics = Clinic.query.all()
    form = ClinicForm()
   
    
    if request.method == "POST":
        
        if form.validate_on_submit():
            clinic_name = form.clinic_name.data
            clinic = Clinic(clinic_name=clinic_name)

            #Save data to database

            db.session.add(clinic)
            db.session.commit()
            flash(message = "Clinic added successfully", category='success')

            return redirect(url_for("admin.admin_clinic"))
    
    return render_template("admin/clinic.html",clinics=clinics, form=form)

@auth_required()
def admin_users():

    users = User.query.all()

    return render_template("admin/users.html", users=users)

@auth_required()
def admin_appointments():
    appointments = Appointment.query.all()

    return render_template("admin/admin_appointments.html", appointments=appointments)

@auth_required()
def add_clinics():

    form = ClinicForm()

    if request.method=="POST":

        #check if form is valid
        if form.validate_on_submit():
            clinic_name = form.clinic_name.data
            clinic = Clinic(clinic_name=clinic_name)
            db.session.add(clinic)
            db.session.commit()
            
            return redirect(url_for("blueprint.index"))
        return render_template("forms/clinic_form.html")
            
  

    return render_template("forms/clinic_form.html", form=form)