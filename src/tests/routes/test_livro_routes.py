def test_cadastro_livro_status_code(client):
    response = client.get("/cadastro/livros")
    assert response.status_code == 308


def test_criar_livro_por_status_code(client):

    response = client.post(
        '/cadastro/livros/novo', 
        data={
            "titulo": "Título Teste"
        },
        follow_redirects = False
    )

    assert response.status_code == 302