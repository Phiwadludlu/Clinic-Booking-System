from flask import Blueprint
from controller.core import index
from controller.api import show,find,delete,create

api_blueprint = Blueprint('api',__name__)

api_blueprint.route('/', methods=['GET'])(index)
api_blueprint.post('/users/create')(create)
api_blueprint.get('/users')(show)
api_blueprint.get('/users/<int:user_id>')(find)
api_blueprint.delete('/users/<int:user_id>')(delete)