from app import create_app

# Crear una instancia de la app
app = create_app()

# Definir una ruta para la página principal
@app.route('/')
def index():
    return "Bienvenido a la tienda online"

if __name__ == "__main__":
    app.run(debug=True)
