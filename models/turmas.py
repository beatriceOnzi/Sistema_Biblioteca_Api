from . import db

class Turmas(db.Model):
    __tablename__ = "turmas"

    turma = db.Column(db.Integer, primary_key=True)
    turma_formatada = db.Column(db.String)
    semana_atual = db.Column(db.Integer, default=1)