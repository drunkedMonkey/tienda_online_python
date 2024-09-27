from flask import Blueprint, jsonify, request
from app.models import Producto
from app import db

# Crear un Blueprint para las rutas
bp = Blueprint('routes', __name__)

# Ruta para crear un producto (POST)
@bp.route('/productos', methods=['POST'])
def crear_producto():
    datos = request.get_json()
    nuevo_producto = Producto(
        nombre=datos['nombre'],
        descripcion=datos['descripcion'],
        precio=datos['precio']
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify({"mensaje": "Producto creado exitosamente"}), 201

# Ruta para obtener todos los productos (GET)
@bp.route('/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.query.all()
    resultado = []
    for producto in productos:
        resultado.append({
            'id': producto.id,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio
        })
    return jsonify(resultado)

# Ruta para actualizar un producto (PUT)
@bp.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

    datos = request.get_json()
    producto.nombre = datos.get('nombre', producto.nombre)
    producto.descripcion = datos.get('descripcion', producto.descripcion)
    producto.precio = datos.get('precio', producto.precio)

    db.session.commit()

    return jsonify({
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': producto.precio
    })

# Ruta para eliminar un producto (DELETE)
@bp.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

    db.session.delete(producto)
    db.session.commit()

    return jsonify({"mensaje": "Producto eliminado exitosamente"})
