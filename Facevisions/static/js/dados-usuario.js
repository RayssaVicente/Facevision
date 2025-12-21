function calcularAnoLetivo(dataIngresso) {
    const anoIngresso = new Date(dataIngresso).getFullYear();
    const anoAtual = new Date().getFullYear();
    
    // Calcula a diferença (Ex: 2025 - 2023 = 2)
    // Somamos 1 pois quem entrou em 2025 está no 1º ano
    const diferenca = (anoAtual - anoIngresso) + 1;

    if (diferenca === 1) return "1º ano Ensino Médio";
    if (diferenca === 2) return "2º ano Ensino Médio";
    if (diferenca === 3) return "3º ano Ensino Médio";
    
    return "Concluído ou Período Inválido";
}

function toggleEdit() {
    const view = document.getElementById('view-section');
    const edit = document.getElementById('edit-section');
    if (edit.style.display === "none") {
        edit.style.display = "block";
        view.style.display = "none";
    } else {
        edit.style.display = "none";
        view.style.display = "block";
    }
}