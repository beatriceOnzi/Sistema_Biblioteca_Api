from flask import session

from models.config_turmas import ConfigTurmas
nova_turma = ConfigTurmas(id=1, turma="1º Ano", semana_atual=1)

session.add(nova_turma)

session.commit()
session.close()