from .alunos import bp as alunos_bp

def registrar_routes(app):
    app.register_blueprint(alunos_bp)