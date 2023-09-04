from flask import Blueprint
import controller.admin_controller as admin_controller
from flask_security import auth_required

admin = Blueprint('admin', __name__)

admin.get('/') (admin_controller.index)
admin.get('/dashboard') (admin_controller.admin_dashboard)
admin.route('/dashboard/add-clinic', methods=["GET","POST"])(admin_controller.add_clinics)
admin.add_url_rule('/dashboard/clinics', view_func=admin_controller.admin_clinic)
admin.add_url_rule('/dashboard/users', view_func=admin_controller.admin_users)
admin.add_url_rule('/dashboard/appointments', view_func=admin_controller.admin_appointments)