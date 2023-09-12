from flask import Blueprint
import controller.admin_controller as admin_controller


admin = Blueprint('admin', __name__)


admin.add_url_rule('/',view_func=admin_controller.index)
admin.add_url_rule('/dashboard',view_func= admin_controller.admin_dashboard)
admin.add_url_rule('/dashboard/add-clinic',view_func=admin_controller.add_clinics, methods=["GET","POST"])
admin.add_url_rule('/dashboard/clinics', view_func=admin_controller.admin_clinic, methods =["GET","POST"])
admin.add_url_rule('/dashboard/users', view_func=admin_controller.admin_users)
admin.add_url_rule('/dashboard/appointments', view_func=admin_controller.admin_appointments)