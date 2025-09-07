from flask import Flask
from flask_cors import CORS
from config import Config
from models.usuario import db
from routes.usuario_routes import usuario_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    db.init_app(app)
    
    app.register_blueprint(usuario_bp)

if __name__ == "__main__":
    app = create_app()
    
    with app.app_context():
        db.create_all() 
    
    app.run(debug=True, port=5000)