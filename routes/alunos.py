from flask import Blueprint, jsonify, render_template
from models.aluno import Aluno

bp = Blueprint("alunos", __name__, url_prefix="/") # depois separar as rotas entre Home e Turma?

@bp.route('/')
def index():
    return render_template('home.html')

@bp.route('/api/alunos/', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    print(alunos)
    return jsonify([{'nome': t.nome, 'turma': t.turma} for t in alunos])