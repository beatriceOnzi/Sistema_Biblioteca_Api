from models import db, Aluno, Turmas

def get_alunos():
    alunos = Aluno.query.all()
    return alunos

def add_alunos():
    novo_aluno = Aluno(nome="Beatrice1ano", turma=1)
    db.session.add(novo_aluno)
    novo_aluno = Aluno(nome="Murilo1ano", turma=1)
    db.session.add(novo_aluno)
    novo_aluno = Aluno(nome="Beatrice2ano", turma=2)
    db.session.add(novo_aluno)
    novo_aluno = Aluno(nome="Beatrice4ano", turma=4)
    db.session.add(novo_aluno)
    novo_aluno = Aluno(nome="Beatrice4ano", turma=4)
    db.session.add(novo_aluno)
    novo_aluno = Aluno(nome="Beatrice9ano", turma=9)
    db.session.add(novo_aluno)
    novo_aluno = Aluno(nome="Murilo9ano", turma=9)
    db.session.add(novo_aluno)
    novo_aluno = Aluno(nome="Beatrice3ano", turma=3)
    db.session.add(novo_aluno)

    db.session.commit()

def add_turmas():
    nova_turma = Turmas(turma=1, turma_formatada = "1º Ano")
    db.session.add(nova_turma)
    nova_turma = Turmas(turma=2, turma_formatada = "2º Ano")
    db.session.add(nova_turma)
    nova_turma = Turmas(turma=3, turma_formatada = "3º Ano")
    db.session.add(nova_turma)
    nova_turma = Turmas(turma=4, turma_formatada = "4º Ano")
    db.session.add(nova_turma)
    nova_turma = Turmas(turma=5, turma_formatada = "5º Ano")
    db.session.add(nova_turma)
    nova_turma = Turmas(turma=6, turma_formatada = "6º Ano")
    db.session.add(nova_turma)
    nova_turma = Turmas(turma=7, turma_formatada = "7º Ano")
    db.session.add(nova_turma)
    nova_turma = Turmas(turma=8, turma_formatada = "8º Ano")
    db.session.add(nova_turma)
    nova_turma = Turmas(turma=9, turma_formatada = "9º Ano")
    db.session.add(nova_turma)

    db.session.commit()