# services: 
# - turma (pegar tudo? /registrar emprestimo / setupautocomplete etc)
# - historico ( pegar tudo? / mudar situação / pesquisar)
# - 
# - outros: botoes-home / manual 

from models import db, Emprestimo
from datetime import date, timedelta


def criar_emprestimo(aluno_id, livro_id):

    data_devolucao = date.today() + timedelta(days=7)

    emprestimo = Emprestimo(
        aluno_id=aluno_id,
        livro_id=livro_id,
        data_devolucao_prevista=data_devolucao
    )

    db.session.add(emprestimo)
    db.session.commit()

    return emprestimo