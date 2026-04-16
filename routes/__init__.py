# executa quando a pasta é importada 
from .cadastro import bp as cadastro_bp
from .turmas import bp as turmas_bp

def registrar_routes(app):
    app.register_blueprint(cadastro_bp)
    app.register_blueprint(turmas_bp)