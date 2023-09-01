from flask import Blueprint
from controller.core import index,about_page,service_page,contact_us_page,dashboard, appointment
from flask_security import auth_required

blueprint = Blueprint('blueprint', __name__)

blueprint.get('/') (index)
blueprint.get('/about') (about_page)
blueprint.get('/services')(service_page)
blueprint.get('/contact-us') (contact_us_page)


blueprint.route('/appointment', methods=["GET","POST"]) (appointment)
blueprint.get('/dashboard') (dashboard)