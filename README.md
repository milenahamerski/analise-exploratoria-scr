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
├── results/                 # Arquivos de log (.csv) e notebook de comparação final
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
- [Notebook de Resultados](results/results.ipynb)
- [Documentação de Pré-processamento](preprocessing/preprocessing.md)
- [Análise de Ruído (Submodalidade)](tests/noise_analysis.md)
