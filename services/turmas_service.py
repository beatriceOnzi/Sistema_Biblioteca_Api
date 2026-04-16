from models import db, Aluno, Livro

def pegar_aluno(nome, turma):
    aluno = Aluno(nome=nome, turma=turma)

    db.session.add(aluno)
    db.session.commit()

    return aluno