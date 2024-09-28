from flask import Blueprint
# Importamos la clase 'Blueprint' del módulo 'flask', que se utiliza para organizar 
# las rutas y funcionalidades en módulos separados dentro de la aplicación Flask.

bp = Blueprint('routes', __name__)
# Creamos un objeto 'Blueprint' llamado 'bp'. Este blueprint se denomina 'routes' 
# y se asocia al nombre del módulo actual ('__name__'). 
# Sirve para agrupar varias rutas de la aplicación y manejarlas como un módulo separado.

from app.routes.auth import auth_bp
# Importamos el blueprint 'auth_bp' desde el módulo 'auth' dentro de 'app.routes'. 
# 'auth_bp' agrupa todas las rutas relacionadas con la autenticación.

from app.routes.productos import productos_bp
# Importamos el blueprint 'productos_bp' desde el módulo 'productos' dentro de 'app.routes'. 
# 'productos_bp' agrupa todas las rutas relacionadas con la gestión de productos.

bp.register_blueprint(auth_bp, url_prefix='/auth')  
# Registramos el blueprint 'auth_bp' en 'bp'. Esto indica que todas las rutas definidas 
# dentro de 'auth_bp' estarán accesibles a través del prefijo de URL '/auth'. 
# Por ejemplo, si 'auth_bp' define una ruta '/login', se accederá como '/auth/login'.

bp.register_blueprint(productos_bp, url_prefix='/productos')  
# Registramos el blueprint 'productos_bp' en 'bp'. 
# Esto hace que todas las rutas de 'productos_bp' estén accesibles con el prefijo '/productos'. 
# Si 'productos_bp' tiene una ruta '/listar', se accederá como '/productos/listar'.
