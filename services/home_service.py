from models import db, Turmas

def get_turmas():
    turmas = Turmas.query.all()
    return turmas