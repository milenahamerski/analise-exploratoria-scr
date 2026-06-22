# Resultados (Results)

Diretório destinado a armazenar as saídas geradas pelos experimentos de Machine Learning e permitir a análise comparativa entre as abordagens.

### Arquivos Principais:
- **`model_results.csv` e `model_results_limpo.csv`**: Tabelas de log que centralizam o registro de desempenho. Cada linha corresponde a um experimento, documentando o algoritmo, as métricas avaliadas (ROC AUC, F1-Score, Acurácia, etc.), os melhores hiperparâmetros selecionados e se a técnica SMOTE foi ativada.
- **`analise_resultados.ipynb`**: Notebook voltado para a tabulação e comparação de resultados. Ele lê os logs, plota gráficos comparativos entre os algoritmos e os 3 cenários diferentes de pré-processamento, estruturando as conclusões metodológicas da pesquisa do TCC.