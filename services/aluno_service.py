from models import db, Aluno

def get_alunos():
    alunos = Aluno.query.order_by(Aluno.turma).all()
    return alunos

def novoAluno(nome_aluno, turma):
    novo_aluno = Aluno(nome=nome_aluno, turma=turma)
    db.session.add(novo_aluno)