import services.user_service
import services.user_service as user_service
from flask import jsonify,request
from models.user_model import UserSchemaIn, UserSchemaOut
from models.clinic_model import ClinicIn, Clinic
from models import db 

user_schema_in = UserSchemaIn()
user_schema_out = UserSchemaOut()
clinic_schema_in = ClinicIn()
def show():
    users=user_service.get_users()
    user_list = []
    for user in users:
        serialized_user = user_schema_out.dump(user)
        user_list.append(serialized_user)

    return jsonify(user_list)

def find(user_id):
    user = user_service.get_user_by_id(user_id)

    if user != None:
        serialized_user = user_schema_out.dump(user)
    
        return jsonify(serialized_user)
    return "Resource not found", 404

def delete(user_id):
    users = user_service.delete_user_by_id(user_id)
    if users:
     return users ,200
    return "Not Found",404

def create():
    username = request.json['username']
    email = request.json['email']

    service_response = services.user_service.create_user(username,email)
    if service_response=='done':
        return 'Success',200
    else:
        return "An error has occured",400

def create_clinic():
    clinic_name = request.json['clinic_name']
    clinic = Clinic(clinic_name=clinic_name)
    errors = clinic_schema_in.dump(clinic)
    if errors:
        return "Error", 401
    
    try:
        db.session.add(clinic)
        db.session.commit()

        return "Done",201
    
    except:

        return "Error",401
