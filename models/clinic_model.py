from models import db
from models.user_model import User
from marshmallow import Schema, fields
from datetime import datetime

#Flask SqlAlchemy Schemas
class Clinic(db.Model):

    __tablename__ = 'clinics'

    id = db.Column(db.Integer, primary_key=True)
    clinic_name = db.Column(db.String,nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)


class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key = True)
    clinic_id = db.Column(db.Integer, db.ForeignKey('clinics.id'), nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    #relationships
    user = db.relationship('User', backref='appointments')
    clinic = db.relationship('Clinic', backref='appointments')

#Marshmallow schemas
class ClinicIn(Schema):
    id = fields.Int()
    clinic_name = fields.Str()
    created_at = fields.DateTime()

class ClinicOut(Schema):
    id = fields.Int()
    clinic_name = fields.Str()
    created_at = fields.DateTime()

class AppointmentsIn(Schema):
    id = fields.Int()
    clinic_id = fields.Int()
    user_id = fields.Int()
    created_at = fields.DateTime()