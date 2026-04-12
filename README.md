# Análise de Base SCR com Polars

Este projeto tem como objetivo realizar a análise de dados a partir de bases do [**SCR**](bcb.gov.br/estabilidadefinanceira/scrdata), utilizando **Python** e a biblioteca **Polars**.

## Download das bases de dados

1. Acesse o link do [Google Drive](https://drive.google.com/drive/folders/1RKWM44RwyKJUUb-aR2h2N5Qfx_S6PMfV?usp=sharing) com as bases do SCR. No Drive, também é possível encontrar um PDF com a descrição de todos os parâmetros disponíveis na base de dados, além das análises referentes aos meses 02/25, 05/25 e 09/25.
2. Escolha qualquer arquivo CSV disponível.
3. Faça o download do arquivo para a mesma pasta onde está o código Python (ou ajuste o caminho no código, se necessário).

## Como usar uma base específica no código

Após baixar o arquivo desejado, basta alterar o nome do CSV na linha abaixo do código:

```python
df = pl.read_csv("scrdata_.csv", separator=";")
```

## Pré-processamento dos dados

Para entender todas as etapas de tratamento e preparação dos dados, acesse:

[Preprocessing](preprocessing/preprocessing.md)

## Análise da Variável Submodalidade

Foi realizada uma análise exploratória da variável **submodalidade** para identificar problemas de alta cardinalidade e categorias raras.

A variável apresentou comportamento de **long tail**, com muitas categorias pouco representativas, o que poderia impactar negativamente os modelos.

Para resolver isso, foi aplicada uma estratégia de **redução de cardinalidade baseada em frequência**, agrupando categorias raras em "Outros".

Veja a análise completa:  
[Documentação de Noise Analysis](tests/noise_analysis.md)

## Resultados

Os resultados obtidos a partir dos experimentos com os modelos de Machine Learning estão documentados em formato de notebook interativo.

Nele estão incluídos:

- Comparação entre diferentes modelos (XGBoost, KNN, Random Forest, SVM, etc.)
- Avaliação de desempenho utilizando métricas como ROC-AUC, F1-score e Accuracy
- Análise comparativa entre cenários com e sem SMOTE
- Impacto da engenharia de variáveis na performance dos modelos
- Resultados de GridSearchCV (tuning de hiperparâmetros)
- Visualizações gráficas (heatmaps e rankings)

Acesse os resultados completos aqui:  
[Notebook de Resultados](results/results.ipynb)
