from flask import request,jsonify
from models.clinic_model import Clinic, ClinicIn, ClinicOut
from models import db 


def create_clinic(clinic_name):

    clinic = Clinic(clinic_name=clinic_name)
    errors = ClinicIn().validate({"clinic_name":clinic.clinic_name})
    if errors:
        return  jsonify(errors), 400
    
    else:
        try:
            db.session.add(clinic)
            db.session.commit()
            serialized_clinics = ClinicOut().dump(clinic)
            return jsonify(serialized_clinics),201
    
        except:

            return "Error",400  


def get_clinics():

    clinics = Clinic.query.all()
    serialized_clinics = ClinicOut().dump(clinics, many=True)

    return jsonify(serialized_clinics)
