from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    turma = db.Column(db.String)


class Livro(db.Model):
    __tablename__ = "livros"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)


class ConfigTurma(db.Model):
    __tablename__ = "config_turmas"

    turma = db.Column(db.String, primary_key=True)
    semana_atual = db.Column(db.Integer, default=1)


class Emprestimo(db.Model):
    __tablename__ = "emprestimos"

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey("alunos.id"))
    livro_id = db.Column(db.Integer, db.ForeignKey("livros.id"))
    data_emprestimo = db.Column(db.Date, default=func.current_date())
    data_devolucao_prevista = db.Column(db.Date)
    data_devolucao = db.Column(db.Date)
