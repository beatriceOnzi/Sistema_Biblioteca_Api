// Assim que a página carrega, ele chama a função para buscar as tarefas
document.addEventListener('DOMContentLoaded', carregarTarefas), () => {
    
    var table = new Tabulator("#tabela", {
        layout: "fitColumns",
        columns: [
            {title: "ID", field: "id"},
            {title: "Nome", field: "nome"},
            {title: "Turma", field: "turma"}
        ]
    });

    fetch("/api/alunos")
    .then(res => res.json())
    .then(data => table.setData(data))
}


// function carregarTarefas() {
//     // Comunicação: JS pede as informações para a rota GET do Flask
//     fetch('/api/tarefas')
//         .then(resposta => resposta.json()) // Transforma a resposta do Flask em JSON
//         .then(tarefas => {
//             const lista = document.getElementById('lista-tarefas');
//             lista.innerHTML = ''; // Limpa a lista na tela
            
//             // Para cada tarefa que veio do banco, cria um item <li> no HTML
//             tarefas.forEach(tarefa => {
//                 const li = document.createElement('li');
//                 li.textContent = tarefa.texto;
//                 lista.appendChild(li);
//             });
//         });
// }

// function adicionarTarefa() {
//     const input = document.getElementById('nova-tarefa');
//     const texto = input.value;
    
//     if (texto.trim() === '') return; // Não faz nada se estiver vazio

//     // Comunicação: JS envia um JSON para a rota POST do Flask
//     fetch('/api/tarefas', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ texto: texto }) // Dados sendo enviados para o Python
//     })
//     .then(resposta => resposta.json())
//     .then(dados => {
//         console.log(dados.mensagem); // Mensagem de sucesso do Flask
//         input.value = '';            // Limpa o campo de texto
//         carregarTarefas();           // Busca do banco novamente para atualizar a tela
//     });
// }