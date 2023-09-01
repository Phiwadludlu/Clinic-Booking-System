from models.database import user_db
from models.user_model import User, UserSchemaIn, UserSchemaOut
from models import db



user_schema_in = UserSchemaIn()
user_schema_out = UserSchemaOut()

def get_users():
    users = User.query.all()

    return users


def create_user(username,email):

    user = User(username=username,email=email )
    errors = user_schema_in.validate(user)

    if errors:
        try:
            db.session.add(user)
            db.session.commit()
            return 'done'
        except:
            return 'error'
    return 'invalid'



def get_user_by_id(id):
       

    user = User.query.get(id)
    serialized_user = user_schema_out.dump(user)
    return user


def delete_user_by_id(id):
    user = get_user_by_id(id)
    if user:
        user_db.remove(user)
        return get_users()
    return None
