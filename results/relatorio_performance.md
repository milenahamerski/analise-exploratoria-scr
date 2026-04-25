# Relatório de Performance dos Modelos

Este documento apresenta uma análise comparativa do desempenho dos modelos preditivos, avaliando o impacto das otimizações e a evolução dos resultados desde as rodadas iniciais até o estado atual.

---

## 📊 Visão Geral dos Resultados

A métrica principal de comparação utilizada foi o **ROC AUC**, que avalia a capacidade do modelo de distinguir entre as classes (inadimplente vs. adimplente).

### 1. Comparativo Baseline vs. Tuning (Melhores Resultados)

| Modelo | Baseline (ROC AUC) | Tuning / GridSearchCV (ROC AUC) | Diferença |
| :--- | :---: | :---: | :---: |
| **XGBoost** | ~0.930 | **0.930** | - |
| **Random Forest** | ~0.930 | **0.932** | +0.002 |
| **Decision Tree** | ~0.897 | **0.910** | +0.013 |
| **SVM (Linear)** | ~0.897 | **0.864** | -0.033* |
| **KNN** | ~0.811 | **0.829** | +0.018 |
| **Logistic Regression** | ~0.770 | **0.865** | +0.095 |

> [!NOTE]
> \* O decréscimo no SVM ocorreu devido à mudança para o `LinearSVC`. Embora o `rbf` (não-linear) apresentasse melhor performance no baseline, ele era computacionalmente inviável para o GridSearch no volume de dados atual. O `LinearSVC` permitiu concluir os experimentos em minutos em vez de dias.

---

## 🔍 Impacto do SMOTE

O Grid Search revelou que o impacto do **SMOTE** varia significativamente entre os modelos:

- **Modelos Lineares (LogReg, SVM)**: Apresentaram ganhos de performance com o balanceamento de classes. No caso da Regressão Logística, o SMOTE elevou o ROC AUC de ~0.77 para **0.86**.
- **Modelos de Árvore (XGBoost, RF)**: O ganho foi marginal ou inexistente, sugerindo que esses algoritmos já lidam bem com o desbalanceamento através de pesos ou estrutura inerente.

---

## 🛠️ Evolução Técnica e Correções

Durante o desenvolvimento, foram realizadas as seguintes melhorias críticas:

1. **Eliminação de Data Leakage**: O SMOTE foi movido para dentro do pipeline de validação cruzada. Antes, ele era aplicado em toda a base de treino de uma vez, o que gerava resultados artificialmente otimistas.
2. **Eficiência no SVM**: A substituição do `SVC(kernel='linear')` pelo `LinearSVC` reduziu o tempo de execução do GridSearch de **7843+ minutos** para aproximadamente **15 minutos**.
3. **Engine de Pré-processamento**: Transição para **Polars**, garantindo que a preparação de 310k registros ocorra em poucos segundos.

---

## 📂 Próximos Passos Sugeridos

1. **Ensemble Modeling**: Combinar os melhores modelos (XGBoost e RandomForest) via VotingClassifier para tentar superar a barreira dos 0.93.
2. **Calibração do LinearSVC**: Como o modelo agora é linear e rápido, podemos adicionar um `CalibratedClassifierCV` se houver necessidade de probabilidades reais (0 a 1) para fins de negócio.
3. **Análise de Features**: Investigar quais variáveis derivadas da "submodalidade" mais contribuíram para o ganho de performance.
