from flask import Blueprint, jsonify, render_template, request
import services.aluno_service as aluno_service
import services.livro_service as livro_service

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
def carregar_pagina_alunos():
    alunos = aluno_service.get_alunos()
    return render_template('cadastro.html', current_page = 2, grupo = "alunos", alunos = alunos)


# Livros
@bp.route('/livros/', methods=['GET'])
def carregar_pagina_livros():
    livros = livro_service.get_livros()
    return render_template('cadastro.html', current_page = 2, grupo = "livros", livros = livros)