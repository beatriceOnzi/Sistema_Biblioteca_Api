from models import db, Livro

def get_livros():
    livro = Livro.query.order_by(Livro.nome).all()
    return livro

def novoLivro(titulo):
    novo_livro = Livro(nome=titulo)
    db.session.add(novo_livro)
    db.session.commit()