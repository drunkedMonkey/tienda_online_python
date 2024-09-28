from flask_sqlalchemy import SQLAlchemy
# Importamos 'SQLAlchemy', el ORM (Object-Relational Mapping) que se encarga de gestionar la interacción
# con la base de datos de manera más sencilla, utilizando objetos de Python en lugar de consultas SQL directas.

from flask_bcrypt import Bcrypt
# Importamos 'Bcrypt' de Flask, una herramienta utilizada para encriptar contraseñas, lo que añade seguridad 
# a la gestión de usuarios.

db = SQLAlchemy()
# Creamos una instancia de 'SQLAlchemy' que manejará la base de datos de la aplicación.

bcrypt = Bcrypt()
# Creamos una instancia de 'Bcrypt' que se utilizará para encriptar y verificar contraseñas de los usuarios.

class Usuario(db.Model):
    # Definimos el modelo 'Usuario', que representa la tabla 'Usuario' en la base de datos.
    # Heredamos de 'db.Model', lo que indica que este es un modelo gestionado por SQLAlchemy.

    id = db.Column(db.Integer, primary_key=True)
    # Definimos la columna 'id' como un entero (db.Integer), que será la clave primaria (primary_key) 
    # de la tabla 'Usuario'.

    nombre = db.Column(db.String(100), nullable=False)
    # Definimos la columna 'nombre' como una cadena de texto de longitud máxima 100, y no puede ser nulo (nullable=False).

    email = db.Column(db.String(100), unique=True, nullable=False)
    # Definimos la columna 'email' como una cadena de texto de longitud máxima 100. 
    # Debe ser único (unique=True) para evitar registros duplicados y no puede ser nulo.

    password_hash = db.Column(db.String(128), nullable=False)
    # Definimos la columna 'password_hash' como una cadena de texto de longitud máxima 128.
    # Almacenará el hash de la contraseña, no la contraseña en texto plano, y es obligatorio (nullable=False).

    def set_password(self, password):
        # Método para establecer la contraseña de un usuario.
        # Este método recibe la contraseña en texto plano y la encripta usando Bcrypt.

        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        # Usamos 'generate_password_hash' de Bcrypt para generar el hash de la contraseña.
        # El método 'decode' convierte el hash de bytes a una cadena UTF-8 para almacenarlo en la base de datos.

    def check_password(self, password):
        # Método para verificar si la contraseña ingresada coincide con el hash almacenado.

        return bcrypt.check_password_hash(self.password_hash, password)
        # 'check_password_hash' compara la contraseña ingresada (en texto plano) con el hash almacenado en la base de datos.
        # Si coinciden, devuelve 'True', de lo contrario, devuelve 'False'.

class Producto(db.Model):
    # Definimos el modelo 'Producto', que representa la tabla 'Producto' en la base de datos.
    
    id = db.Column(db.Integer, primary_key=True)
    # Definimos la columna 'id' como un entero, que será la clave primaria (primary_key) de la tabla 'Producto'.

    nombre = db.Column(db.String(100), nullable=False)
    # Definimos la columna 'nombre' como una cadena de texto de longitud máxima 100, y es obligatoria.

    precio = db.Column(db.Float, nullable=False)
    # Definimos la columna 'precio' como un número de coma flotante (db.Float) y es obligatorio.

    descripcion = db.Column(db.String(500), nullable=True)
    # Definimos la columna 'descripcion' como una cadena de texto de longitud máxima 500. Este campo es opcional (nullable=True).

    def __repr__(self):
        # Método especial que define cómo se representa el objeto 'Producto' como cadena de texto.
        
        return f'<Producto {self.nombre}>'
        # Cuando imprimimos o inspeccionamos un objeto 'Producto', este método devolverá una cadena que incluye 
        # el nombre del producto, facilitando la depuración o la representación en registros.
