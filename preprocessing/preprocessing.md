## Pré-processamento e Estratégias de Modelagem

Nesta etapa, foi realizado o pré-processamento da base de dados do SCR com o objetivo de preparar os dados para modelagem preditiva de inadimplência.

O processo envolveu limpeza, transformação de variáveis e criação de novas features, além da definição de diferentes cenários experimentais para avaliar o impacto dessas decisões no desempenho dos modelos.

---

## 🔹 Tratamento dos Dados

A preparação inicial dos dados foi realizada utilizando a biblioteca **Polars** para garantir alta performance no processamento de grandes volumes:

- Tratamento de valores ausentes.
- Conversão de tipos de dados.
- Filtragem de variáveis irrelevantes ou redundantes.
- Engenharia de atributos inicial.

---

## 🔹 Engenharia de Atributos (Feature Engineering)

Foram criadas novas variáveis com o objetivo de enriquecer a representação dos dados:

- **Indicadores binários de texto** na variável _submodalidade_ (ex: presença de termos específicos).
- **Frequência da submodalidade**, transformando a variável categórica em um sinal numérico de popularidade.
- **Redução de Cardinalidade**: Agrupamento de categorias raras em "Outros" com base em um threshold de 1000 ocorrências (veja [Noise Analysis](../tests/noise_analysis.md)).

---

## 🔹 Cenários de Modelagem

Para avaliar o impacto das features, os modelos são testados em três cenários:

1. **sem_submodalidade**: Variável removida.
2. **submodalidade_agrupada**: Categorias raras agrupadas.
3. **submodalidade_engineered**: Variável original + features derivadas.

---

## 🔹 Pipeline de Machine Learning

O projeto adota uma abordagem de **Pipeline Robusta** utilizando `imblearn.pipeline.Pipeline`, garantindo que:
- O **Scaling** (`StandardScaler`) seja calculado apenas no treino.
- O **SMOTE** (oversampling) seja aplicado estritamente dentro das dobras de validação cruzada para evitar vazamento de dados (*data leakage*).

---

## 🔹 Otimização e Registro de Resultados

Para cada modelo (XGBoost, KNN, RandomForest, SVM, LogisticRegression, DecisionTree), realizamos:

- **Grid Search CV**: Busca exaustiva pelos melhores hiperparâmetros.
- **Avaliação de SMOTE como Hiperparâmetro**: O grid search testa tanto a presença quanto a ausência do SMOTE.
- **Log Duplo**: O sistema registra automaticamente os melhores resultados para o cenário **Com SMOTE** e **Sem SMOTE**, permitindo identificar qual técnica de balanceamento foi mais eficaz para cada algoritmo.

As métricas registradas em `results/model_results.csv` são:
- **ROC AUC** (Principal métrica de comparação)
- **F1-score**
- **Accuracy**

---

## 🔹 Conclusões Preliminares

Até o momento, observou-se que a engenharia de atributos e a redução de cardinalidade conseguem preservar a maior parte da informação relevante sem a necessidade de manter centenas de colunas esparsas. A escolha do cenário final depende do equilíbrio entre interpretabilidade e performance de cada modelo.

---
