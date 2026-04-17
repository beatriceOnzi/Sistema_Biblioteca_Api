from . import db

class ConfigTurmas(db.Model):
    __tablename__ = "config_turmas"

    id = db.Column(db.Integer, primary_key=True)
    turma = db.Column(db.String)
    semana_atual = db.Column(db.Integer, default=1)