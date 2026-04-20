from models import db, ConfigTurmas

def get_turmas():
    turmas = ConfigTurmas.query.all()
    return turmas