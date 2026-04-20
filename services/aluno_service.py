from models import db, Aluno, Livro

def get_alunos():
    alunos = Aluno.query.all()
    return alunos