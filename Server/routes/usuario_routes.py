from flask import Blueprint, request, jsonify
from controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    """Este obtiene todos los usuarios"""
    resultado = UsuarioController.obtener_todos()
    status_code = 200 if resultado['success'] else 500
    return jsonify(resultado), status_code

@usuario_bp.route('/api/usuarios/<int:idusuario>', methods=['GET'])
def obtener_usuario(idusuario):
    """Obtiene un usuario por ID"""
    #CHECAR SI ES CORRECTO PASARLO POR PAARAMETROS
    resultado = UsuarioController.obtener_por_id(idusuario)
    status_code = 200 if resultado['success'] else 404
    return jsonify(resultado), status_code

@usuario_bp.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    """Crea nuevo usuario"""
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'mensaje': 'No se enviaron datos'}), 400
    
    resultado = UsuarioController.crear_usuario(data)
    status_code = 201 if resultado['success'] else 400
    return jsonify(resultado), status_code

@usuario_bp.route('/api/usuarios/<int:idusuario>', methods=['PUT'])
def actualizar_usuario(idusuario):
    """Actualiza usuario"""
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'mensaje': 'No se enviaron datos'}), 400
    
    resultado = UsuarioController.actualizar_usuario(idusuario, data)
    status_code = 200 if resultado['success'] else 400
    return jsonify(resultado), status_code

@usuario_bp.route('/api/usuarios/<int:idusuario>', methods=['DELETE'])
def eliminar_usuario(idusuario):
    """Elimina usuario"""
    resultado = UsuarioController.eliminar_usuario(idusuario)
    status_code = 200 if resultado['success'] else 404
    return jsonify(resultado), status_code

@usuario_bp.route('/api/usuarios/login', methods=['POST'])
def login():
    """Login de usuario"""
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'mensaje': 'No se enviaron datos'}), 400
    
    email = data.get('email') or data.get('Usuario')  
    password = data.get('password') or data.get('Password') 
    
    if not email or not password:
        return jsonify({'success': False, 'mensaje': 'Email y contraseña son requeridos'}), 400
    
    resultado = UsuarioController.login(email, password)
    status_code = 200 if resultado['success'] else 401
    return jsonify(resultado), status_code