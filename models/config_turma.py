from . import db
class ConfigTurma(db.Model):
    __tablename__ = "config_turmas"

    turma = db.Column(db.String, primary_key=True)
    semana_atual = db.Column(db.Integer, default=1)