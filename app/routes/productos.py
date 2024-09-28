from flask import Blueprint, request, jsonify
# Importamos 'Blueprint' para modularizar las rutas, 'request' para manejar peticiones HTTP 
# y 'jsonify' para devolver las respuestas en formato JSON.

from app.models import Producto, db
# Importamos el modelo 'Producto' y la instancia de la base de datos 'db' desde 'app.models'. 
# 'Producto' representa la tabla donde se almacenan los productos, y 'db' se usa para interactuar con la base de datos.

productos_bp = Blueprint('productos', __name__)
# Creamos el blueprint 'productos_bp' para definir las rutas relacionadas con la gestión de productos.
# El nombre del blueprint es 'productos', y '__name__' asocia este blueprint con el módulo actual.

# Crear producto (POST)
@productos_bp.route('/crear-producto', methods=['POST'])
# Definimos una ruta '/productos' que acepta peticiones POST para crear un nuevo producto.

def crear_producto():
    data = request.get_json()
    # Obtenemos los datos enviados en formato JSON desde la petición.

    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    precio = data.get('precio')
    # Extraemos los campos 'nombre', 'descripcion' y 'precio' del JSON recibido.

    if not nombre or not descripcion or not precio:
        return jsonify({"mensaje": "Faltan datos"}), 400
        # Si alguno de los campos es nulo o vacío, devolvemos un mensaje de error con un código 400 (solicitud incorrecta).

    nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio)
    # Creamos una instancia de 'Producto' con los datos proporcionados (nombre, descripción y precio).

    db.session.add(nuevo_producto)
    # Añadimos el nuevo producto a la sesión de la base de datos.

    db.session.commit()
    # Guardamos (hacemos commit) los cambios en la base de datos.

    return jsonify({"mensaje": "Producto creado exitosamente"}), 201
    # Devolvemos una respuesta de éxito con un código 201 (creado) y un mensaje en formato JSON.

# Obtener productos (GET)
@productos_bp.route('/listar', methods=['GET'])
# Definimos una ruta '/productos' que acepta peticiones GET para obtener la lista de productos.

def obtener_productos():
    productos = Producto.query.all()
    # Consultamos todos los productos en la base de datos.

    productos_lista = [{"id": p.id, "nombre": p.nombre, "descripcion": p.descripcion, "precio": p.precio} for p in productos]
    # Creamos una lista de diccionarios con los atributos de cada producto (id, nombre, descripción, precio).

    return jsonify(productos_lista)
    # Devolvemos la lista de productos en formato JSON.

# Obtener un solo producto (GET)
@productos_bp.route('/obtener-producto/<int:id>', methods=['GET'])
# Definimos una ruta '/productos/<int:id>' que acepta peticiones GET para obtener un solo producto por su ID.

def obtener_producto(id):
    producto = Producto.query.get_or_404(id)
    # Buscamos el producto por su ID. Si no se encuentra, devuelve automáticamente un error 404 (no encontrado).

    return jsonify({"id": producto.id, "nombre": producto.nombre, "descripcion": producto.descripcion, "precio": producto.precio})
    # Devolvemos el producto en formato JSON con sus atributos.

# Actualizar producto (PUT)
@productos_bp.route('/update-producto/<int:id>', methods=['PUT'])
# Definimos una ruta '/productos/<int:id>' que acepta peticiones PUT para actualizar un producto existente.

def actualizar_producto(id):
    producto = Producto.query.get_or_404(id)
    # Buscamos el producto por su ID. Si no se encuentra, devuelve automáticamente un error 404.

    data = request.get_json()
    # Obtenemos los datos enviados en formato JSON desde la petición.

    producto.nombre = data.get('nombre', producto.nombre)
    # Actualizamos el nombre del producto si se proporciona en los datos, de lo contrario, mantenemos el actual.

    producto.descripcion = data.get('descripcion', producto.descripcion)
    # Actualizamos la descripción del producto si se proporciona.

    producto.precio = data.get('precio', producto.precio)
    # Actualizamos el precio del producto si se proporciona.

    db.session.commit()
    # Guardamos los cambios en la base de datos.

    return jsonify({"mensaje": "Producto actualizado exitosamente"})
    # Devolvemos un mensaje indicando que el producto ha sido actualizado exitosamente.

# Eliminar producto (DELETE)
@productos_bp.route('/delete-producto/<int:id>', methods=['DELETE'])
# Definimos una ruta '/productos/<int:id>' que acepta peticiones DELETE para eliminar un producto por su ID.

def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    # Buscamos el producto por su ID. Si no se encuentra, devuelve automáticamente un error 404.

    db.session.delete(producto)
    # Eliminamos el producto de la sesión de la base de datos.

    db.session.commit()
    # Guardamos los cambios en la base de datos para confirmar la eliminación.

    return jsonify({"mensaje": "Producto eliminado exitosamente"})
    # Devolvemos un mensaje indicando que el producto ha sido eliminado exitosamente.
