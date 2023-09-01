from flask import Blueprint
import controller.admin_controller as admin_controller
from flask_security import auth_required

admin = Blueprint('admin', __name__)

admin.get('/') (admin_controller.index)
admin.get('/dashboard') (admin_controller.admin_dashboard)
admin.route('/dashboard/add-clinic', methods=["GET","POST"])(admin_controller.add_clinics)