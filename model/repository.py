from model.database import db, Aluno, Livro, ConfigTurma, Emprestimo

Aluno = db.Aluno
Livro = db.Livro
Config_turma = db.Config_turma
Emprestimo = db.Emprestimo
session = db.session


class Repository:

    @staticmethod
    def criar_aluno(nome, turma):
        aluno = Aluno(nome, turma)
        session.add(aluno)
        session.commit()
        return aluno # depois vai retorna uma mensagem de confirmção


    @staticmethod
    def listar():
        return session.query(Aluno).all()


    @staticmethod
    def buscar_aluno_por_id(id):
        return session.query(Aluno).filter(Aluno.id == id).first()


    @staticmethod
    def deletar_aluno(id):
        aluno = session.query(Aluno).filter(Aluno.id == id).first()
        if aluno:
            session.delete(aluno)
            session.commit()