from models import db, Aluno, Turmas

def get_alunos_turma(turma):
    alunos_turma = Aluno.query.filter_by(turma=turma)
    return alunos_turma
