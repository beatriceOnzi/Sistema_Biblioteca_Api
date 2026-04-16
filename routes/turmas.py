from flask import Blueprint, jsonify, render_template, request
from models.aluno import Aluno
from models.livro import Livro
import services.turmas_service

bp = Blueprint("turmas", __name__, url_prefix="/")

'''
1 -> turmas 
2 -> cadastro
3 -> histórico 
4 -> Manual de instruções
5 -> Passagem de ano
'''

@bp.route('/')
def index():
    return render_template('turmas.html', current_page = 1)

@bp.route('/alunos/', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    return jsonify([{'nome': t.nome, 'turma': t.turma} for t in alunos])