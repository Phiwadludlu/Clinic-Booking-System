from flask import render_template, redirect, url_for,request
from flask_security import current_user
from forms.clinic_form import ClinicForm
from models.clinic_model import Clinic
from models import db
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('security.login', next=request.url))

    return redirect(url_for('admin.admin_dashboard'))

def admin_dashboard():
    return render_template("admin/dashboard.html")

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