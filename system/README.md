# MVP: Sistema de Monitoramento e Análise de Risco (RiskAnalyzer)

Este diretório contém o **Produto Mínimo Viável (MVP)** do seu TCC. Ele é uma aplicação web construída com **FastAPI** (Python) e **HTML/CSS/JS** (Frontend) que tem como principal objetivo demonstrar a aplicabilidade prática do modelo de *Machine Learning* construído durante a pesquisa, especificamente o algoritmo **Random Forest** (cenário agrupado), que teve a melhor performance.

---

## Estrutura de Arquivos e o que fazem

Abaixo está a explicação dos principais arquivos que compõem o sistema:

### Scripts e Backend
- **`app.py`**: É o "cérebro" e coração da aplicação (Servidor Web). Ele cria a API usando o FastAPI, carrega o modelo treinado, intercepta os dados preenchidos no formulário, converte para *dummies* e retorna a porcentagem de risco. Também é responsável por renderizar e servir a página do Dashboard.
- **`train_model.py`**: Script avulso que treina o melhor modelo *Random Forest* (com os parâmetros hiper-ajustados) na base completa e o exporta na extensão `.joblib`. Serve para caso você decida retreinar o modelo no futuro.
- **`generate_mock_db.py`**: Script auxiliar que gera uma base de dados fictícia com 100 perfis de associados (com nomes realistas). Ele passa cada associado pelo seu modelo de ML para pré-calcular a chance de Inadimplência e exporta tudo em formato JSON.

### Modelos Salvos
- **`best_model.joblib`**: É o modelo matemático de *Machine Learning* exportado. O `app.py` não treina nada, ele simplesmente carrega esse arquivo para fazer as predições de forma super rápida.
- **`model_columns.joblib`**: Salva a lista exata das colunas (após o tratamento de categóricas do treino) que o modelo espera receber. Evita que o site "quebre" se você inserir categorias não conhecidas.
- **`mock_members.json`**: Funciona como o nosso banco de dados. Guarda os 100 registros gerados pelo script mock e alimenta o *Dashboard* de Saúde Financeira.

### Interface Gráfica (Frontend)
- **`templates/index.html`**: A tela principal da aplicação com o formulário onde o usuário pode inserir os dados de um cliente manualmente para avaliar o risco na hora.
- **`templates/dashboard.html`**: A tela de Monitoramento (Painel de Saúde), que exibe um panorama gerencial e a tabela completa dos 100 associados com seus respectivos limiares de risco coloridos.
- **`static/style.css`**: O arquivo que dita as cores, tamanhos e formato visual do sistema inteiro (layout, tabelas, selos, botões).
- **`static/script.js`**: (se houver) Cuida das animações e dos gatilhos no formulário (ex: carregar os botões, atualizar o percentual na tela sem recarregar a página).

---

## Passo a Passo: Como Testar a Aplicação

Para rodar este sistema no seu computador, siga os passos abaixo. Eles presumem que você já tem os pacotes instalados (como `fastapi`, `uvicorn`, `scikit-learn`, `pandas`, etc.) no seu ambiente virtual.

### 1. Ativar o Ambiente Virtual
Sempre rode o sistema por dentro do ambiente virtual (`.venv`) para que ele consiga acessar as bibliotecas corretas:
```bash
# Navegue até a pasta do TCC
cd /caminho/para/analise_ds

# Ative o ambiente
source .venv/bin/activate
```

### 2. (Opcional) Gerar / Atualizar os dados
Se quiser garantir que o modelo e o banco de dados estejam fresquinhos:
```bash
# Entre na pasta do sistema
cd system

# Para retreinar o modelo de Machine Learning (Pode demorar um pouco)
python train_model.py

# Para gerar uma nova base de dados fictícia de associados
python generate_mock_db.py
```

### 3. Iniciar o Servidor Web
Com tudo configurado, execute o comando abaixo para colocar o site "no ar" localmente:
```bash
# Opção A:
python app.py

# Opção B (Usando Uvicorn diretamente, melhor para evitar erros de versão):
python -m uvicorn app:app --host 0.0.0.0 --port 5000 --reload
```

### 4. Acessar o Sistema no Navegador
Abra o seu navegador (Chrome, Firefox, Safari) e digite o endereço local:

 **http://localhost:5000** ou **http://127.0.0.1:5000**

A partir daí, você poderá brincar preenchendo o formulário de Nova Análise de Crédito ou navegar no topo da página para ver o **Painel de Saúde**!
