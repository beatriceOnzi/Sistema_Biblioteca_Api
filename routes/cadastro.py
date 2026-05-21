from flask import Blueprint, jsonify, render_template, request
from services.aluno_service import *
from services.livro_service import *

bp = Blueprint("cadastro", __name__, url_prefix="/cadastro")

'''
1 -> turmas 
2 -> cadastro
3 -> histórico 
4 -> Manual de instruções
5 -> Passagem de ano
'''

# Alunos
@bp.route('/alunos/', methods=['GET'])
def carregar_cadastro_alunos():
    alunos = get_alunos()
    return render_template('cadastro.html', current_page = 2, grupo = "alunos", alunos = alunos)


# @bp.route('/alunos/novo', methods=['GET'])
# def cadastrar_novo_aluno():
    #alunos = get_alunos()
    #return render_template('cadastro.html', current_page = 2, grupo = "alunos", alunos = alunos)

# Livros
@bp.route('/livros/', methods=['GET'])
def carregar_cadastro_livros():
    livros = get_livros()
    return render_template('cadastro.html', current_page = 2, grupo = "livros", livros = livros)
