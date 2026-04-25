# Análise de Base SCR com Polars e Machine Learning

Este projeto tem como objetivo realizar a análise de dados a partir de bases do [**SCR**](bcb.gov.br/estabilidadefinanceira/scrdata), utilizando **Python**, **Polars** e bibliotecas de **Machine Learning** para predição de inadimplência.

## 📂 Estrutura do Projeto

```text
.
├── exploratory_analysis/    # Notebooks de análise exploratória inicial
├── predictive_models/       # Notebooks individuais para cada algoritmo de ML
│   ├── logistic_regression.ipynb
│   ├── decision_tree.ipynb
│   ├── knn.ipynb
│   ├── random_forest.ipynb
│   ├── svm.ipynb
│   └── xgboost.ipynb
├── preprocessing/           # Lógica de tratamento e engenharia de atributos
├── results/                 # Logs e Análise de Desempenho
│   ├── results.ipynb          # Resultados históricos (até 19/04)
│   └── results_2.ipynb        # Resultados recentes (desde 19/04)
├── tests/                   # Análises de ruído e testes de consistência
└── utils/                   # Utilitários (logger, plotters, etc.)
```

## 🚀 Como Iniciar

### 1. Download das bases de dados
1. Acesse o link do [Google Drive](https://drive.google.com/drive/folders/1RKWM44RwyKJUUb-aR2h2N5Qfx_S6PMfV?usp=sharing) com as bases do SCR.
2. Faça o download de um arquivo CSV para a pasta raiz do projeto.

### 2. Configuração do Ambiente
Certifique-se de ter as dependências instaladas (recomenda-se o uso de um virtual environment):
```bash
pip install pandas polars scikit-learn imbalanced-learn xgboost matplotlib seaborn
```

## 🧠 Modelagem e Experimentos

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

## 📊 Registro de Resultados

Todos os experimentos salvam automaticamente as métricas em `results/model_results.csv`. 
A nova lógica de log captura os melhores parâmetros para os cenários **com SMOTE** e **sem SMOTE** simultaneamente, permitindo uma comparação justa.

Para ver a análise consolidada:
- [Relatório de Performance](results/relatorio_performance.md) 🚀
- [Resultados Históricos (até 19/04)](results/results.ipynb)
- [Resultados Recentes (desde 19/04)](results/results_2.ipynb)
- [Documentação de Pré-processamento](preprocessing/preprocessing.md)
- [Análise de Ruído (Submodalidade)](tests/noise_analysis.md)

## 🔄 Fluxo de Execução Recomendado

Para reproduzir os resultados ou testar novos modelos:
1. **Limpeza e Pré-processamento**: Rode o script em `preprocessing/main_preprocessing.py` para gerar a base tratada.
2. **Treinamento Baseline**: Execute os notebooks em `predictive_models/` para ter uma visão inicial.
3. **Otimização (GridSearch)**: Utilize a seção de GridSearch nos mesmos notebooks para encontrar os melhores hiperparâmetros.
4. **Análise Final**: Confira o `results/results.ipynb` ou o `relatorio_performance.md` para comparar os modelos.

