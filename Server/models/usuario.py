from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    idusuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    idestatus = db.Column(db.Integer, nullable=False, default=0)
    fechacreacion = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'idusuario': self.idusuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'password': self.password,
            'idestatus': self.idestatus,
            'fechacreacion': self.fechacreacion.isoformat() if self.fechacreacion else None
        }
    
    def verificar_password(self, password):
        return self.password == password