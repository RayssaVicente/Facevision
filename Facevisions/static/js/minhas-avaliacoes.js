document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.filter-card');
    const labelCategoria = document.getElementById('labelCategoria');
    const tabelaCorpo = document.getElementById('tabelaAvaliacoes');

    // Dados fictícios para demonstração
    const dadosPorCategoria = {
        "Linguagens": [
            { disc: "Português", data: "12/05", desc: "Avaliação Mensal", status: "Publicada", statusClass: "success" },
            { disc: "Inglês", data: "15/04", desc: "Atividade Avaliativa", status: "Pendente", statusClass: "warning" }
        ],
        "Exatas": [
            { disc: "Matemática", data: "20/05", desc: "Prova de Álgebra", status: "Publicada", statusClass: "success" },
            { disc: "Física", data: "22/05", desc: "Laboratório", status: "Agendada", statusClass: "info" }
        ],
        "Humanas": [
            { disc: "História", data: "10/06", desc: "Trabalho Bimestral", status: "Pendente", statusClass: "warning" }
        ],
        "Biológicas": [
            { disc: "Biologia", data: "05/06", desc: "Prova Prática", status: "Publicada", statusClass: "success" }
        ]
    };

    cards.forEach(card => {
        card.addEventListener('click', function() {
            // 1. Remover 'active' de todos e adicionar ao clicado
            cards.forEach(c => c.classList.remove('active'));
            this.classList.add('active');

            // 2. Pegar o nome da categoria do atributo data
            const categoria = this.getAttribute('data-categoria');
            labelCategoria.innerText = categoria;

            // 3. Limpar e preencher a tabela com efeito de fade simples
            tabelaCorpo.style.opacity = '0';
            
            setTimeout(() => {
                let html = "";
                const itens = dadosPorCategoria[categoria] || [];

                itens.forEach(item => {
                    html += `
                        <tr>
                            <td class="time-col">${item.disc}</td>
                            <td>${item.data}</td>
                            <td><span class="subject">${item.desc}</span></td>
                            <td><span class="badge rounded-pill bg-${item.statusClass} bg-opacity-25 text-${item.statusClass}">${item.status}</span></td>
                        </tr>
                    `;
                });

                tabelaCorpo.innerHTML = html || '<tr><td colspan="4" class="text-center opacity-50">Nenhuma avaliação encontrada.</td></tr>';
                tabelaCorpo.style.opacity = '1';
            }, 200);
        });
    });
});