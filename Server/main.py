from flask import Flask, jsonify, request
from flask_cors import CORS
from db import db
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    "DATABASE_URL", "mysql+pymysql://root:Sagas123@localhost:3307/odonto"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



if __name__ == "__main__":
    app.run(debug=True, port=5000)
