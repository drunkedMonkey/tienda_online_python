# **TIENDA ONLINE**
Esto es un proyecto para aprendizaje sin ningún tipo de ánimo de lucro iniciado el 15/09/2024
para probar diferentes tecnologías

## TECNOLOGIAS UTILIZADAS

* Flask
* SQLAlchemy
* SQLITE
* Flask-Migrate

## ESTRUCTURA DEL PROYECTO

    app                     # Carpeta principal del proyecto
        __init__.py          # Inicializa la app de Flask y las extensiones
        models.py            # Modelos de base de datos
        routes.py            # Rutas (endpoints)
        config.py            # Configuración de la base de datos

    migrations              # Carpeta para las migraciones

    venv                    # Entorno virtual

    app.db                   # Base de datos SQLite
    README.md                # Fichero de explicación de la app
    run.py                   # Script principal para correr la app
    requirements.txt         # Lista de dependencias del proyecto

## INICIAR EL PROYECTO

**python run.py**

## ACTIVAR EL ENTORNO VIRTUAL
*En Windows*

        venv\Scripts\activate
        
*En macOS/Linux*

        source venv/bin/activate

## INSTALAR DEPENDENCIAS
    pip install -r requirements.txt

El comando pip install -r requirements.txt se utiliza para instalar las dependencias del proyecto, pero solo necesitas ejecutarlo una vez, o cuando:
* Instalas el proyecto por primera vez en un nuevo entorno o máquina.
* Añades nuevas dependencias al archivo requirements.txt y necesitas instalarlas.
* Actualizas el archivo requirements.txt y necesitas instalar las nuevas versiones de las dependencias.

## INICIALIZAR MIGRACIONES

    flask db init

Este comando solo necesitas ejecutarlo una vez, cuando configuras las migraciones por primera vez en tu proyecto. Se utiliza para crear la carpeta migrations/, que almacena la información sobre las migraciones.

    flask db migrate -m "Initial migration"

Este comando crea una nueva migración basada en los cambios detectados en los modelos de tu aplicación. Solo debes ejecutarlo cuando haces cambios en los modelos de tu base de datos (por ejemplo, cuando añades, modificas o eliminas columnas en tus tablas).

    flask db upgrade

Este comando aplica las migraciones a la base de datos, es decir, actualiza la estructura de la base de datos según los cambios realizados en los modelos.
Solo debes ejecutarlo cuando hayas generado una nueva migración (con flask db migrate). Si no hay migraciones pendientes, no necesitas ejecutarlo cada vez que inicias el proyecto.

## HACER UN CRUD DESDE POSTMAN

### GET TODOS LOS PRODUCTOS
    GET http://127.0.0.1:5000/productos
### GET UN PRODUCTO
    GET http://127.0.0.1:5000/productos/1
### POST UN PRODUCTO
    POST http://127.0.0.1:5000/productos
    body-> {
                "nombre": "Chaqueta",
                "descripcion": "Chaqueta 100% algodón",
                "precio": 69.99
            }
### PUT UN PRODUCTO
    PUT http://127.0.0.1:5000/productos/1
    body-> {
        "nombre": "Camiseta Actualizada",
        "descripcion": "Nueva descripción",
        "precio": 24.99
    }
### DELETE UN PRODUCTO
    DELETE http://127.0.0.1:5000/productos/1


    







