from app import create_app
from flask_migrate import Migrate
from app.models import db

app = create_app()  # Crea la aplicación Flask
migrate = Migrate(app, db)  # Inicializa Flask-Migrate

if __name__ == "__main__":
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración
