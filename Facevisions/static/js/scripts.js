function botaoMenu() {
    let menu = document.getElementById("menu");

    if (menu.style.display === "block" || menu.style.display === "") {
        menu.style.display = "none"; // Esconde o menu
    } else {
        menu.style.display = "block"; // Mostra o menu
    }
}


document.getElementById("trigger-icon").addEventListener("click", function() {
    var options = document.getElementById("options");
    if (options.style.display === "none" || options.style.display === "") {
        options.style.display = "block";
    } else {
        options.style.display = "none";
    }
});


document.getElementById("opcoes").addEventListener("change", function() {
    let tabelas = {
        "1": "tabelaLinguagem",
        "2": "tabelaHumanas",
        "3": "tabelaExatas",
        "4": "tabelaTecnica"
    };

    // Esconder todas as tabelas primeiro
    Object.values(tabelas).forEach(id => {
        document.getElementById(id).style.display = "none";
    });

    // Pegar o valor selecionado
    let valorSelecionado = this.value;

    // Exibir a tabela correspondente
    if (tabelas[valorSelecionado]) {
        document.getElementById(tabelas[valorSelecionado]).style.display = "block";
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const erro = "{{ erro|escapejs }}";
    if (erro) {
        const modal = new bootstrap.Modal(document.getElementById('erroModal'));
        modal.show();
    }
});
