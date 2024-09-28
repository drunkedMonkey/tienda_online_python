import os
# Importamos el módulo 'os' para interactuar con el sistema operativo, 
# lo cual nos permite manejar rutas de archivos y variables de entorno.

from datetime import timedelta
# Importamos 'timedelta' desde el módulo 'datetime'. Esto se utiliza para manejar duraciones
# de tiempo, como la expiración de tokens.

basedir = os.path.abspath(os.path.dirname(__file__))
# Definimos 'basedir' como el directorio base absoluto donde se encuentra el archivo actual. 
# Usamos 'os.path.abspath' para obtener la ruta absoluta y 'os.path.dirname(__file__)' 
# para obtener el directorio del archivo. Esto es útil para establecer rutas relativas dentro del proyecto.

class Config:
    # Definimos una clase 'Config' que contendrá configuraciones globales de la aplicación Flask.

    SECRET_KEY = os.environ.get('SECRET_KEY') or '1234'
    # 'SECRET_KEY' es una clave importante para la seguridad en Flask, utilizada para firmar cookies y manejar sesiones.
    # Aquí intentamos obtener la clave desde las variables de entorno del sistema operativo ('os.environ.get'), 
    # pero si no está definida, usamos un valor por defecto ('1234').

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    # Definimos la URI de la base de datos para SQLAlchemy. Utilizamos SQLite como base de datos.
    # 'sqlite:///' especifica la base de datos SQLite, y combinamos 'basedir' con 'app.db' 
    # para que el archivo de la base de datos se cree en el directorio base de la aplicación.

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Desactivamos el rastreo de modificaciones en los objetos de la base de datos para 
    # ahorrar recursos. Esto es parte de las configuraciones de SQLAlchemy.

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'clave_secreta_jwt'
    # Definimos una clave secreta específica para los tokens JWT, usada para firmar los tokens.
    # Si no se encuentra en las variables de entorno, se usará 'clave_secreta_jwt' como valor por defecto.
    # Este es un parámetro crucial para la seguridad en la autenticación JWT.

# Configuración para Flask-JWT-Extended
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
# Definimos la duración del token de acceso (JWT Access Token) utilizando 'timedelta'. 
# En este caso, el token expira una hora después de ser generado.

JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
# Definimos la duración del token de refresco (JWT Refresh Token), el cual expira después de 30 días.
# Este token permite al usuario obtener un nuevo token de acceso sin necesidad de volver a iniciar sesión.
