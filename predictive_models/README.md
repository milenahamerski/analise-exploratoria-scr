# Modelos Preditivos (Predictive Models)

Esta pasta contém os notebooks Jupyter responsáveis pelo treinamento, sintonia de hiperparâmetros (*Tuning*) e validação dos modelos preditivos de Machine Learning.

A abordagem padrão adotada em cada notebook inclui:
- Construção de *Pipelines* robustos (utilizando `imblearn.pipeline.Pipeline`).
- Validação cruzada (usando `GridSearchCV`).
- Treinamento e avaliação considerando cenários iterativos (com e sem a aplicação do SMOTE para o tratamento do desbalanceamento de classes, de modo a evitar *data leakage*).

**Algoritmos Testados:**
- Decision Tree (`decision_tree.ipynb`)
- Random Forest (`random_forest.ipynb`)
- XGBoost (`xgboost.ipynb`)
- Regressão Logística (`logistic_regression.ipynb`)
- K-Nearest Neighbors - KNN (`knn.ipynb`)
- Máquinas de Vetores de Suporte - SVM (`svm.ipynb`)