from . import db

# Definir el modelo Producto que representa la tabla 'productos'
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    descripcion = db.Column(db.String(500))
    precio = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Producto {self.nombre}>'
