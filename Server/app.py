from flask import Flask
from flask_cors import CORS
from config import Config
from db import db
from routes.estado_routes import estado_bp
from routes.rol_routes import rol_bp
from routes.usuario_routes import usuario_bp
from models.estado import Estado
from models.rol import Rol
from models.usuario import Usuario

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    db.init_app(app)
    
    app.register_blueprint(estado_bp)
    app.register_blueprint(rol_bp)
    app.register_blueprint(usuario_bp)
   

    return app

if __name__ == "__main__":
    app = create_app()
    
    with app.app_context():
        db.create_all() 
    
    app.run(debug=True, port=5000)

    