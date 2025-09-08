import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "mysql+pymysql://root:1324@localhost:3306/bd_sd"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    