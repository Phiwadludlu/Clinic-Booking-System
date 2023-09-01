from flask import Flask
from routes.routes import  blueprint
from routes.api import api_blueprint
from routes.admin_routes import admin
from models import db,user_model
from forms import authentication_forms
from flask_migrate import Migrate
from flask_security.models import fsqla_v3 as fsqla
from flask_security import Security, current_user, auth_required, hash_password, \
     SQLAlchemySessionUserDatastore, permissions_accepted
from flask_mailman import Mail

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    return app

app = create_app()
db.init_app(app)
migrate = Migrate(app, db)

#Flask Security Config
user_datastore = SQLAlchemySessionUserDatastore(session=db.session, user_model=user_model.User, role_model=user_model.Role)
security = Security(app=app,datastore=user_datastore,register_form=authentication_forms.MyRegisterForm)
security.init_app(app=app, register_blueprint=False)

app.register_blueprint(blueprint,url_prefix ='/')
app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)
