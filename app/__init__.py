from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()

# Inicializar Flask y cargar la configuración
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar la base de datos y las migraciones
    db.init_app(app)
    Migrate(app, db)

    # Registrar rutas o blueprints
    with app.app_context():
        from .models import Producto  # Importar modelos

    return app
