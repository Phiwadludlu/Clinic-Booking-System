import os
import dotenv

dotenv.load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

#SQL ALCHAMEY CONFIG
SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'
SQLALCHEMY_ENGINE_OPTIONS =  {
    "pool_pre_ping": True,
}
SQLALCHEMY_TRACK_MODIFICATION = False

#Flask-Secuirty Config
SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT")
REMEMBER_COOKIE_SAMESITE = "strict"
SESSION_COOKIE_SAMESITE = "strict"
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_EMAIL_VALIDATOR_ARGS = {"check_deliverability": False}