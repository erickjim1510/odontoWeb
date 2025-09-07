from models.usuario import Usuario, db
from utils.auth import generar_token
from flask import jsonify

class UsuarioController:
    
    @staticmethod
    def obtener_todos():
        try:
            usuarios = Usuario.query.all()
            return {
                'success': True,
                'data': [usuario.to_dict() for usuario in usuarios],
                'mensaje': 'Usuarios obtenidos exitosamente'
            }
        except Exception as e:
            return {
                'success': False,
                'mensaje': f'Error al obtener usuarios: {str(e)}'
            }
    
    @staticmethod
    def obtener_por_id(idusuario):
        try:
            usuario = Usuario.query.get(idusuario)
            if not usuario:
                return {
                    'success': False,
                    'mensaje': 'Usuario no encontrado'
                }
            
            return {
                'success': True,
                'data': usuario.to_dict(),
                'mensaje': 'Usuario encontrado'
            }
        except Exception as e:
            return {
                'success': False,
                'mensaje': f'Error al obtener usuario: {str(e)}'
            }
    
    @staticmethod
    def crear_usuario(data):
        try:
            campos_requeridos = ['nombre', 'apellido', 'email', 'password']
            for campo in campos_requeridos:
                if not data.get(campo):
                    return {
                        'success': False,
                        'mensaje': f'El campo {campo} es requerido'
                    }
            
            usuario_existente = Usuario.query.filter_by(email=data['email']).first()
            if usuario_existente:
                return {
                    'success': False,
                    'mensaje': 'El email ya está registrado'
                }
            
            nuevo_usuario = Usuario(
                nombre=data['nombre'],
                apellido=data['apellido'],
                email=data['email'],
                password=data['password'],
                idestatus=data.get('idestatus', 0)
            )
            
            db.session.add(nuevo_usuario)
            db.session.commit()
            
            return {
                'success': True,
                'data': nuevo_usuario.to_dict(),
                'mensaje': 'Usuario creado exitosamente'
            }
            
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'mensaje': f'Error al crear usuario: {str(e)}'
            }
    
    @staticmethod
    def actualizar_usuario(idusuario, data):
        try:
            usuario = Usuario.query.get(idusuario)
            if not usuario:
                return {
                    'success': False,
                    'mensaje': 'Usuario no encontrado'
                }
            
            if 'nombre' in data:
                usuario.nombre = data['nombre']
            if 'apellido' in data:
                usuario.apellido = data['apellido']
            if 'email' in data:
                usuario_existente = Usuario.query.filter(
                    Usuario.email == data['email'],
                    Usuario.idusuario != idusuario
                ).first()
                if usuario_existente:
                    return {
                        'success': False,
                        'mensaje': 'El email ya está en uso por otro usuario'
                    }
                usuario.email = data['email']
            if 'password' in data:
                usuario.password = data['password']
            if 'idestatus' in data:
                usuario.idestatus = data['idestatus']
            
            db.session.commit()
            
            return {
                'success': True,
                'data': usuario.to_dict(),
                'mensaje': 'Usuario actualizado exitosamente'
            }
            
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'mensaje': f'Error al actualizar usuario: {str(e)}'
            }
    
    @staticmethod
    def eliminar_usuario(idusuario):
        try:
            usuario = Usuario.query.get(idusuario)
            if not usuario:
                return {
                    'success': False,
                    'mensaje': 'Usuario no encontrado'
                }
            
            db.session.delete(usuario)
            db.session.commit()
            
            return {
                'success': True,
                'mensaje': 'Usuario eliminado exitosamente'
            }
            
        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'mensaje': f'Error al eliminar usuario: {str(e)}'
            }
    
    @staticmethod
    def login(email, password):
        try:
            usuario = Usuario.query.filter_by(email=email).first()
            
            if not usuario:
                return {
                    'success': False,
                    'mensaje': 'Usuario no encontrado'
                }
            
            if not usuario.verificar_password(password):
                return {
                    'success': False,
                    'mensaje': 'Contraseña incorrecta'
                }
            
            token = generar_token()
            
            return {
                'success': True,
                'data': {
                    **usuario.to_dict(),
                    'token': token
                },
                'mensaje': 'Login exitoso'
            }
            
        except Exception as e:
            return {
                'success': False,
                'mensaje': f'Error en login: {str(e)}'
            }