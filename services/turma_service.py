from models import db, Aluno, ConfigTurmas

def get_alunos_turma(id):
    alunos_turma = Aluno.query.filter_by(turma=id)
    return alunos_turma
