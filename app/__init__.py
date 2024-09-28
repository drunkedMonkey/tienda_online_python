from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager  # Importa JWTManager
from .models import db  # Asegúrate de importar correctamente el objeto db

# Inicializa Migrate y JWTManager
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)  # Inicializa SQLAlchemy con la app
    migrate.init_app(app, db)  # Inicializa Flask-Migrate
    jwt.init_app(app)  # Inicializa JWTManager

    from app.routes import bp as routes_bp  # Importar el blueprint de rutas
    app.register_blueprint(routes_bp)  # Registrar el blueprint de rutas

    return app
