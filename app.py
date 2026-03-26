from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from model.database import Aluno, Livro, Emprestimo, ConfigTurma, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/api/alunos', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    print(alunos)
    return jsonify([{'nome': t.nome, 'turma': t.turma} for t in alunos])

'''Rotas:
- @app.route('/home', methods=['GET']) -> Turmas botões
- @app.route('/historico', methods=['GET']) -> Tabela do historico
- @app.route('/historico/situacao/:id', methods=['GET']) -> Alterar a situação de devolvido 

- @app.route('/cadastro/aluno', methods=['GET']) -> Renderizar página
- @app.route('/cadastro/aluno/novo', methods=['POST']) -> Cadastrar novo aluno

- @app.route('/cadastro/livro', methods=['GET']) -> Renderizar página
- @app.route('/cadastro/livro/novo', methods=['POST']) -> Cadastrar novo livro

- @app.route('/manual', methods=['GET']) -> Página do manual (static no js)

- @app.route('/passagem_ano', methods=['POST']) -> Passagem de ano

TURMAS:
- @app.route('/turma/:ano', methods=['GET']) -> Mostrar a tabela e deixar colocar novos emprestimos
- @app.route('/turma/:ano/salvar_dados', methods=['POST']) -> salva os dados no banco 
'''


if __name__ == '__main__':
    app.run(debug=True)