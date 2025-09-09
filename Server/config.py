import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "mysql+pymysql://root:Sagas123@localhost:3307/odonto"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False