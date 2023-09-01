from models import db
from datetime import datetime
from marshmallow import Schema, fields
from enum import Enum as pyEnum
from flask_security.models import fsqla_v3 as fsqla
from sqlalchemy.orm import relationship, backref

#creating choices for sex
class SexEnum(pyEnum):
    MALE = 'Male'
    FEMALE = 'Female'
    LGBTQ = 'LGBTQ'



#Normal Database Models
class User(db.Model,fsqla.FsUserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    student_number = db.Column(db.String(8), unique=True, nullable=False )
    is_active=db.Column(db.Boolean, default=False)
    password = db.Column(db.String,nullable=False)
    confirmed_at = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    roles = relationship('Role', secondary='roles_users', backref=backref("users",lazy="dynamic"))

    def add_time(self):

         self.created_at = datetime.utcnow

class UserProfile(db.Model):

    __tablename__ = 'user_profles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    middle_name = db.Column(db.String,nullable=True)
    last_name = db.Column(db.String, nullable=False)
    sex =db.Column(db.Enum(SexEnum),  nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(9), unique=True, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    #relationship
    user = db.relationship('User', backref='user_profile')
    

class Role(db.Model, fsqla.FsRoleMixin):

    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    

class RolesUsers(db.Model):
    
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'))

class UserSchemaIn(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
    created_at = fields.DateTime()
    is_active = fields.Bool()
    
class UserSchemaOut(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()
    is_active = fields.Bool()


class UserProfileIn(Schema):
    id = fields.Int()
    sex = fields.Enum(SexEnum, by_value=True)
    user_id = fields.Int()
    date_of_birth = fields.Date()
    created_at = fields.DateTime()


class UserProfileOut(Schema):
    id = fields.Int()
    sex = fields.Enum(SexEnum, by_value=True)
    user_id = fields.Int()
    date_of_birth = fields.Date()
    created_at = fields.DateTime(format='%Y-%m-%dT%H:%M:%S+03:00')



