# Análise de Ruído: Variável Submodalidade

Este documento descreve a análise exploratória realizada sobre a variável **submodalidade**, com foco na identificação de **ruído**, **alta cardinalidade** e **categorias raras** que poderiam impactar negativamente os modelos de Machine Learning.

---

## Objetivo

O principal objetivo desta análise foi:

- Entender a distribuição da variável `submodalidade`
- Identificar a presença de categorias pouco representativas
- Definir uma estratégia de **redução de cardinalidade**
- Melhorar a qualidade dos dados para modelagem preditiva

---

## Análise Inicial

A variável `submodalidade` foi analisada considerando:

- Quantidade total de categorias distintas
- Frequência das categorias mais comuns
- Frequência das categorias mais raras

Foi observado que a variável possui uma distribuição do tipo **long tail (cauda longa)**.

---

## Problema Identificado

A distribuição apresentou as seguintes características:

- Poucas categorias concentram grande parte dos registros
- Muitas categorias possuem baixa frequência (algumas com menos de 10 ocorrências)

Esse comportamento pode gerar diversos problemas:

- **Overfitting**: o modelo aprende padrões específicos de categorias raras
- **Ruído**: categorias pouco frequentes não contribuem significativamente
- **Alta dimensionalidade**: aumento do número de colunas após codificação (ex: One-Hot Encoding)

---

## Teste de Thresholds

Para tratar o problema, foi realizada uma análise baseada em diferentes valores de corte (**thresholds**).

Para cada threshold, foram avaliados:

- Número de categorias mantidas
- Percentual de dados preservados (cobertura)

Os thresholds testados foram:

- 50
- 100
- 200
- 500
- 1000

---

## Escolha do Threshold

O valor escolhido foi:

**Threshold = 1000**

### Justificativa:

- Redução significativa da cardinalidade (aproximadamente de 50 para 30 categorias)
- Preservação de cerca de **97% dos dados**
- Eliminação de categorias com baixa relevância estatística
- Melhor equilíbrio entre simplicidade e retenção de informação

---

## Estratégia Aplicada

Com base no threshold definido, foi adotada a seguinte abordagem:

- Categorias com frequência **menor que 1000** foram agrupadas em uma nova categoria: `"Outros"`
- Categorias com frequência **maior ou igual a 1000** foram mantidas

Essa técnica é conhecida como:

**Agrupamento de categorias raras (rare category grouping)**

---

## Impacto da Estratégia

A aplicação dessa técnica resultou em:

- Redução da dimensionalidade dos dados
- Diminuição do risco de overfitting
- Melhoria na capacidade de generalização do modelo
- Simplificação do espaço de features

---

## Relação com o Pré-processamento

Essa análise foi fundamental para a definição dos cenários de pré-processamento utilizados no projeto:

- `sem_submodalidade`
- `submodalidade_agrupada`
- `submodalidade_engineered`

A estratégia de agrupamento foi aplicada especificamente no cenário **submodalidade_agrupada**.

---

## Conclusão

A variável `submodalidade`, embora rica em informação, apresentava alto nível de ruído devido à sua alta cardinalidade.

A aplicação de uma estratégia baseada em frequência permitiu:

- Preservar a informação relevante
- Reduzir a complexidade dos dados
- Tornar os modelos mais robustos

Essa etapa foi essencial para garantir a qualidade do pipeline de modelagem.
