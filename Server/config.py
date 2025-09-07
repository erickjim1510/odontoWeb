import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "mysql+pymysql://usuario:contraseña@localhost:puerto/nameDB"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False