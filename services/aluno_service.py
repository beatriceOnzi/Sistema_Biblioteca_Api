from models import db, Aluno, Livro

def get_alunos():
    alunos = Aluno.query.all()
    return alunos

# def add_alunos(nome, turma):
#     novo_aluno = Aluno(nome="Beatrice1ano", turma=1)
#     db.session.add(novo_aluno)

#     db.session.commit()