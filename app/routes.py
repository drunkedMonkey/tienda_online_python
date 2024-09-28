from flask import Blueprint, jsonify, request
# Importamos 'Blueprint' para organizar las rutas, 'jsonify' para devolver respuestas en formato JSON,
# y 'request' para obtener datos de la solicitud.

from app.models import Producto
from app.models import Usuario
from app import db
# Importamos los modelos 'Producto' y 'Usuario', y la instancia de 'db' para interactuar con la base de datos.

# Crear un Blueprint para las rutas
bp = Blueprint('routes', __name__)
# Creamos un 'Blueprint' llamado 'routes', que agrupa todas las rutas bajo un único contexto.

# Ruta para crear un producto (POST)
@bp.route('/productos', methods=['POST'])
def crear_producto():
    # Obtenemos los datos enviados en formato JSON
    datos = request.get_json()
    
    # Creamos un nuevo objeto Producto con los datos recibidos
    nuevo_producto = Producto(
        nombre=datos['nombre'],
        descripcion=datos['descripcion'],
        precio=datos['precio']
    )
    
    # Añadimos el producto a la base de datos y confirmamos la transacción
    db.session.add(nuevo_producto)
    db.session.commit()
    
    # Devolvemos una respuesta indicando que el producto fue creado exitosamente
    return jsonify({"mensaje": "Producto creado exitosamente"}), 201

# Ruta para obtener todos los productos (GET)
@bp.route('/productos', methods=['GET'])
def obtener_productos():
    # Consultamos todos los productos en la base de datos
    productos = Producto.query.all()
    
    # Preparamos una lista vacía para almacenar los resultados
    resultado = []
    
    # Recorremos los productos y los añadimos a la lista de resultados
    for producto in productos:
        resultado.append({
            'id': producto.id,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio
        })
    
    # Devolvemos la lista de productos en formato JSON
    return jsonify(resultado)

# Ruta para obtener un producto por ID (GET)
@bp.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    # Buscamos el producto por ID
    producto = Producto.query.get(id)
    
    # Si no encontramos el producto, devolvemos un mensaje de error
    if not producto:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

    # Devolvemos el producto encontrado en formato JSON
    return jsonify({
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': producto.precio
    })

# Ruta para actualizar un producto (PUT)
@bp.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    # Buscamos el producto por ID
    producto = Producto.query.get(id)
    
    # Si no encontramos el producto, devolvemos un mensaje de error
    if not producto:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

    # Obtenemos los nuevos datos desde el cuerpo de la solicitud
    datos = request.get_json()
    
    # Actualizamos los atributos del producto solo si fueron proporcionados en la solicitud
    producto.nombre = datos.get('nombre', producto.nombre)
    producto.descripcion = datos.get('descripcion', producto.descripcion)
    producto.precio = datos.get('precio', producto.precio)

    # Confirmamos los cambios en la base de datos
    db.session.commit()

    # Devolvemos el producto actualizado en formato JSON
    return jsonify({
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': producto.precio
    })

# Ruta para eliminar un producto (DELETE)
@bp.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    # Buscamos el producto por ID
    producto = Producto.query.get(id)
    
    # Si no encontramos el producto, devolvemos un mensaje de error
    if not producto:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

    # Eliminamos el producto de la base de datos y confirmamos la operación
    db.session.delete(producto)
    db.session.commit()

    # Devolvemos un mensaje indicando que el producto fue eliminado exitosamente
    return jsonify({"mensaje": "Producto eliminado exitosamente"})

# Ruta para registrar usuarios (POST)
@bp.route('/registro', methods=['POST'])
def registro():
    # Obtenemos los datos enviados en formato JSON
    data = request.get_json()
    
    # Extraemos los valores de nombre, email y contraseña
    nombre = data.get('nombre')
    email = data.get('email')
    password = data.get('password')

    # Verificamos que todos los campos requeridos están presentes
    if not nombre or not email or not password:
        return jsonify({"mensaje": "Faltan datos"}), 400

    # Verificamos si el usuario ya existe en la base de datos
    if Usuario.query.filter_by(email=email).first():
        return jsonify({"mensaje": "Usuario ya existe"}), 400

    # Creamos un nuevo usuario y establecemos la contraseña
    nuevo_usuario = Usuario(nombre=nombre, email=email)
    nuevo_usuario.set_password(password)

    # Añadimos el usuario a la base de datos y confirmamos la transacción
    db.session.add(nuevo_usuario)
    db.session.commit()

    # Devolvemos un mensaje indicando que el usuario fue creado exitosamente
    return jsonify({"mensaje": "Usuario creado exitosamente"}), 201

# Ruta para iniciar sesión (POST)
@bp.route('/login', methods=['POST'])
def login():
    # Obtenemos los datos enviados en formato JSON
    data = request.get_json()
    
    # Extraemos el email y la contraseña
    email = data.get('email')
    password = data.get('password')

    # Buscamos el usuario por email
    usuario = Usuario.query.filter_by(email=email).first()

    # Verificamos si el usuario existe y si la contraseña es correcta
    if usuario is None or not usuario.check_password(password):
        return jsonify({"mensaje": "Credenciales inválidas"}), 401

    # Creamos un token JWT para el usuario
    access_token = create_access_token(identity=usuario.id)
    
    # Devolvemos el token de acceso en formato JSON
    return jsonify(access_token=access_token), 200
