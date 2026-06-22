document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const form = e.target;
    const btn = form.querySelector('button');
    const spinner = document.getElementById('btn-spinner');
    const btnText = btn.querySelector('span');
    const resultCard = document.getElementById('result-card');
    const circle = document.getElementById('percentage-circle');
    const valueSpan = document.getElementById('percentage-value');
    const messageP = document.getElementById('result-message');

    // UI Loading state
    btn.disabled = true;
    spinner.style.display = 'block';
    btnText.textContent = 'Processando...';
    resultCard.classList.add('hidden');

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            const percent = result.inadimplencia_percent;
            valueSpan.textContent = `${percent}%`;
            
            // Determine color based on risk
            let color = 'var(--success)';
            let msg = 'Risco Baixo de Inadimplência';
            
            if (percent > 40 && percent <= 70) {
                color = 'var(--warning)';
                msg = 'Risco Moderado de Inadimplência';
            } else if (percent > 70) {
                color = 'var(--danger)';
                msg = 'Risco Alto de Inadimplência';
            }

            circle.style.background = `conic-gradient(${color} ${percent}%, var(--bg-color) ${percent}%)`;
            circle.style.boxShadow = `0 0 30px ${color}40`;
            messageP.textContent = msg;
            messageP.style.color = color;
            
            resultCard.classList.remove('hidden');
        } else {
            alert('Erro: ' + (result.error || 'Falha ao analisar risco'));
        }
    } catch (error) {
        console.error(error);
        alert('Erro ao se conectar com o servidor.');
    } finally {
        btn.disabled = false;
        spinner.style.display = 'none';
        btnText.textContent = 'Analisar Risco';
    }
});
