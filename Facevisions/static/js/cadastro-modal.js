document.addEventListener("DOMContentLoaded", function () {
    // Pegamos a mensagem e o tipo do HTML (usando data-attributes ou variáveis globais)
    // Uma forma simples é verificar se o elemento existe e tem conteúdo
    const mensagemElement = document.querySelector('#mensagemModal .modal-body p');
    const mensagemTexto = mensagemElement ? mensagemElement.innerText.trim() : "";
    
    // Pegamos o tipo de mensagem (sucesso ou erro) para decidir o redirecionamento
    const modalContent = document.querySelector('.modal-content');
    const ehSucesso = modalContent && modalContent.classList.contains('sucesso');

    if (mensagemTexto !== "") {
        const modalElement = document.getElementById('mensagemModal');
        const modal = new bootstrap.Modal(modalElement);
        modal.show();

        // Se for sucesso, redireciona após 2.5 segundos
        if (ehSucesso) {
            setTimeout(function() {
                window.location.href = "/"; // Altere para a URL da sua página de login
            }, 2500);
        }
    }
});