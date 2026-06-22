# Análise de Base SCR com Machine Learning (TCC)

Este trabalho apresenta uma abordagem voltada à análise e à predição de inadimplência no período pós-concessão de crédito, utilizando técnicas de aprendizado de máquina aplicadas a dados públicos do Sistema de Informações de Crédito (SCR). O objetivo consiste em investigar a capacidade de modelos preditivos de identificar padrões associados ao risco de inadimplência, contribuindo para o acompanhamento de operações de crédito após sua concessão. Para a realização do estudo, a base de dados foi submetida a etapas de pré-processamento, incluindo tratamento de valores ausentes, redução de alta cardinalidade categórica, balanceamento de classes e transformação de variáveis. Na etapa de modelagem, foram treinados e avaliados diferentes algoritmos de classificação, entre eles Regressão Logística, Árvore de Decisão, KNN, Random Forest, SVM e XGBoost, utilizando métricas como Acurácia, F1-Score e ROC AUC. Os resultados demonstraram que os modelos foram capazes de identificar padrões relacionados à inadimplência, apresentando desempenho satisfatório para a tarefa de classificação e evidenciando o potencial das técnicas de aprendizado de máquina na análise de risco de crédito. Como complemento ao estudo, foi desenvolvida uma interface web simplificada para ilustrar uma possível aplicação prática dos modelos gerados. Conclui-se que a abordagem proposta pode contribuir para atividades de monitoramento e análise de risco no contexto pós-concessão de crédito, fornecendo subsídios para a identificação antecipada de operações com maior probabilidade de inadimplência.

##  Estrutura do Projeto

```text
.
├── [exploratory_analysis/](exploratory_analysis/README.md)    # Notebooks de análise exploratória inicial
├── [predictive_models/](predictive_models/README.md)       # Notebooks individuais para cada algoritmo de ML
│   ├── logistic_regression.ipynb
│   ├── decision_tree.ipynb
│   ├── knn.ipynb
│   ├── random_forest.ipynb
│   ├── svm.ipynb
│   └── xgboost.ipynb
├── [preprocessing/](preprocessing/preprocessing.md)           # Lógica de tratamento e engenharia de atributos
├── [results/](results/README.md)                 # Logs e Análise de Desempenho
│   ├── results.ipynb          # Resultados históricos (até 19/04)
│   └── results_2.ipynb        # Resultados recentes (desde 19/04)
├── [system/](system/README.md)                  # MVP: Sistema Web de Monitoramento de Risco
├── [tests/](tests/noise_analysis.md)                   # Análises de ruído e testes de consistência
└── [utils/](utils/README.md)                   # Utilitários (logger, plotters, etc.)
```

##  Como Iniciar

### 1. Download das bases de dados
1. Acesse o link do [Google Drive](https://drive.google.com/drive/folders/1RKWM44RwyKJUUb-aR2h2N5Qfx_S6PMfV?usp=sharing) com as bases do SCR.
2. Faça o download de um arquivo CSV para a pasta raiz do projeto.

### 2. Configuração do Ambiente

Recomenda-se fortemente o uso de um ambiente virtual (`.venv`) para isolar as dependências do projeto e evitar conflitos.

**Passo a passo para criar o ambiente virtual:**

1. **Abra o terminal** na pasta principal do projeto.
2. **Crie o ambiente virtual** executando:
   ```bash
   python -m venv .venv
   ```
3. **Ative o ambiente virtual:**
   - No **Linux / macOS**:
     ```bash
     source .venv/bin/activate
     ```
   - No **Windows** (PowerShell):
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - No **Windows** (Prompt de Comando):
     ```cmd
     .venv\Scripts\activate.bat
     ```

**Instalação das dependências:**

Com o ambiente ativado (você verá um `(.venv)` no início da linha do terminal), instale os pacotes necessários utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Alternativamente, como o projeto possui um arquivo `pyproject.toml`, você também pode instalar em modo editável:

```bash
pip install -e .
```

##  Modelagem e Experimentos

O projeto utiliza uma abordagem de pipeline robusta (`imblearn.pipeline`) que integra:
- **Pré-processamento**: Tratamento de nulos e engenharia de atributos.
- **SMOTE**: Balanceamento de classes aplicado apenas dentro das dobras da validação cruzada.
- **GridSearchCV**: Otimização de hiperparâmetros para todos os modelos.

### Modelos Implementados
- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- Random Forest
- Support Vector Machine (SVM)
- XGBoost

##  Registro de Resultados

Todos os experimentos salvam automaticamente as métricas em `results/model_results.csv`. 
A nova lógica de log captura os melhores parâmetros para os cenários **com SMOTE** e **sem SMOTE** simultaneamente, permitindo uma comparação justa.

Para ver a análise consolidada:
- [Relatório de Performance](results/relatorio_performance.md) 
- [Resultados Históricos (até 19/04)](results/results.ipynb)
- [Resultados Recentes (desde 19/04)](results/results_2.ipynb)
- [Documentação de Pré-processamento](preprocessing/preprocessing.md)
- [Análise de Ruído (Submodalidade)](tests/noise_analysis.md)

##  Fluxo de Execução Recomendado

Para reproduzir os resultados ou testar novos modelos:
1. **Limpeza e Pré-processamento**: Rode o script em `preprocessing/main_preprocessing.py` para gerar a base tratada.
2. **Treinamento Baseline**: Execute os notebooks em `predictive_models/` para ter uma visão inicial.
3. **Otimização (GridSearch)**: Utilize a seção de GridSearch nos mesmos notebooks para encontrar os melhores hiperparâmetros.
4. **Análise Final**: Confira o `results/results.ipynb` ou o `relatorio_performance.md` para comparar os modelos.


##  Sistema Web (MVP) para a Banca Avaliadora

Para validar de forma prática a aplicação do melhor modelo treinado neste estudo (*Random Forest*), foi desenvolvido um Produto Mínimo Viável (MVP) contendo um formulário interativo de predição e um painel de saúde (*Dashboard*) gerencial para uma carteira fictícia de crédito.

Para ver todos os detalhes técnicos e a arquitetura do sistema, acesse a documentação completa do MVP em: [**`system/README.md`**](system/README.md).

###  Passo a Passo para Testar o Sistema

Abaixo encontra-se o guia simplificado para que a banca examinadora consiga testar a plataforma rodando-a localmente:

1. **Abra um terminal** e navegue até a pasta principal do projeto (`analise_ds`).
2. **Ative o ambiente virtual** (necessário para carregar as dependências de Machine Learning e do servidor Web):
   ```bash
   source .venv/bin/activate
   ```
3. **Navegue até o diretório do sistema**:
   ```bash
   cd system
   ```
4. **(Opcional) Gere uma base de dados simulada** para preencher o *Dashboard* com 100 associados ilustrativos:
   ```bash
   python generate_mock_db.py
   ```
5. **Inicie o servidor local FastAPI**:
   ```bash
   python -m uvicorn app:app --host 0.0.0.0 --port 5000
   ```
6. **Acesse o Sistema:** Abra o navegador de sua preferência (Google Chrome, Firefox, Safari, etc.) e acesse a URL local:
    **http://localhost:5000** ou **http://127.0.0.1:5000**

Na interface, será possível simular os dados de um novo cliente na aba **"Nova Análise"** ou visualizar os resultados agrupados de clientes ativos através do menu superior **"Painel de Saúde"**.
