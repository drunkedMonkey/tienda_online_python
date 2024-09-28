from flask import Blueprint, request, jsonify
# Importamos 'Blueprint' para modularizar rutas, 'request' para manejar las peticiones HTTP
# y 'jsonify' para devolver las respuestas en formato JSON.

from app.models import Usuario, db
# Importamos el modelo 'Usuario' y la instancia de la base de datos 'db' desde 'app.models'. 
# 'Usuario' es la tabla donde se gestionan los datos de los usuarios, y 'db' se usa para interactuar con la base de datos.

from flask_jwt_extended import create_access_token
# Importamos 'create_access_token' de 'flask_jwt_extended' para crear tokens JWT, que se usan para autenticar a los usuarios.

auth_bp = Blueprint('auth', __name__)
# Creamos el blueprint 'auth_bp' para definir las rutas relacionadas con la autenticación. 
# El nombre del blueprint es 'auth', y el argumento '__name__' vincula el blueprint al módulo actual.

# Registro de usuarios
@auth_bp.route('/registro', methods=['POST'])
# Definimos una ruta '/registro' que acepta peticiones POST para registrar nuevos usuarios.

def registro():
    data = request.get_json()
    # Obtenemos los datos enviados en formato JSON desde la petición.

    nombre = data.get('nombre')
    email = data.get('email')
    password = data.get('password')
    # Extraemos los campos 'nombre', 'email' y 'password' del JSON recibido.

    if not nombre or not email or not password:
        return jsonify({"mensaje": "Faltan datos"}), 400
        # Si alguno de los campos es nulo o vacío, devolvemos un mensaje de error con un código 400 (solicitud incorrecta).

    if Usuario.query.filter_by(email=email).first():
        return jsonify({"mensaje": "Usuario ya existe"}), 400
        # Verificamos si el email ya existe en la base de datos. Si es así, devolvemos un error 400.

    nuevo_usuario = Usuario(nombre=nombre, email=email)
    # Creamos una instancia del modelo 'Usuario' con el nombre y email recibidos.

    nuevo_usuario.set_password(password)
    # Usamos un método del modelo 'Usuario' (probablemente definido en el modelo) para 
    # establecer y encriptar la contraseña.

    db.session.add(nuevo_usuario)
    # Añadimos el nuevo usuario a la sesión de la base de datos.

    db.session.commit()
    # Guardamos (hacemos commit) los cambios en la base de datos.

    return jsonify({"mensaje": "Usuario creado exitosamente"}), 201
    # Devolvemos una respuesta de éxito (código 201, creado) junto con un mensaje en formato JSON.

# Inicio de sesión
@auth_bp.route('/login', methods=['POST'])
# Definimos la ruta '/login' que acepta peticiones POST para que los usuarios inicien sesión.

def login():
    data = request.get_json()
    # Obtenemos los datos enviados en formato JSON desde la petición.

    email = data.get('email')
    password = data.get('password')
    # Extraemos los campos 'email' y 'password' del JSON recibido.

    usuario = Usuario.query.filter_by(email=email).first()
    # Buscamos al usuario en la base de datos mediante su email.

    if usuario is None or not usuario.check_password(password):
        return jsonify({"mensaje": "Credenciales inválidas"}), 401
        # Si el usuario no existe o la contraseña es incorrecta, devolvemos un mensaje de error 
        # con un código 401 (no autorizado).

    access_token = create_access_token(identity=usuario.id)  # Genera el token aquí
    # Generamos un token JWT utilizando el ID del usuario como identidad. Este token se usará
    # para autorizar peticiones futuras.

    return jsonify(access_token=access_token), 200
    # Devolvemos el token de acceso en formato JSON con un código 200 (éxito).
