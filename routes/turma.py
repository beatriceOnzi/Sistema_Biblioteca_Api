from flask import Blueprint, jsonify, render_template, request
import services.turma_service as turma_service

bp = Blueprint("turma", __name__, url_prefix="/turma")

# dar um jeito de bloquear ser redirecionada || ir para links || clicar em coisas que pode dar pau
# quando está em certos lugares: ex -> quando entrou dentro de uma turma ( para sair vai ter um botão de voltar e um de salvar)
# ouuuuu se não der para fazer isso, vai ser redirecionada, mas não vai salvar. Acho que não dá pau não.

@bp.route('/<id>')
def load_turma(id):
    alunos_turma = turma_service.get_alunos_turma(id)
    return render_template('turma.html', current_page = 1, alunos_turma = alunos_turma, turma = id)