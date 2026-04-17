from models.livro import Livro

def get_livros():
    livro = Livro.query.all()
    return livro