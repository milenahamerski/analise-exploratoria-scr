## Pré-processamento e Estratégias de Modelagem

Nesta etapa, foi realizado o pré-processamento da base de dados do SCR com o objetivo de preparar os dados para modelagem preditiva de inadimplência.

O processo envolveu limpeza, transformação de variáveis e criação de novas features, além da definição de diferentes cenários experimentais para avaliar o impacto dessas decisões no desempenho dos modelos.

---

## 🔹 Tratamento dos Dados

Inicialmente, foram realizadas as seguintes etapas:

- Leitura da base utilizando **Pandas**
- Tratamento de valores ausentes
- Conversão de tipos de dados quando necessário
- Remoção de variáveis consideradas irrelevantes ou redundantes

---

## 🔹 Engenharia de Atributos (Feature Engineering)

Foram criadas novas variáveis com o objetivo de enriquecer a representação dos dados e capturar padrões relevantes para a predição:

- **Indicadores binários de texto** na variável _submodalidade_, como:
  - presença de termos como "crédito", "cartão", entre outros
- **Frequência da submodalidade**, representando o número de ocorrências de cada categoria
- Outras transformações derivadas com base no conhecimento do domínio

Essas variáveis permitem transformar informações categóricas e textuais em sinais numéricos mais úteis para os modelos de machine learning.

---

## 🔹 Criação de Diferentes Cenários de Dataset

Para avaliar o impacto da variável _submodalidade_ e das estratégias de engenharia de atributos, foram construídos três conjuntos de dados distintos:

- **sem_submodalidade**  
  A variável _submodalidade_ foi completamente removida

- **submodalidade_agrupada**  
  As categorias da variável foram agrupadas com base em frequência (threshold), reduzindo cardinalidade

- **submodalidade_engineered**  
  A variável original foi mantida e enriquecida com novas features derivadas

---

## 🔹 Por que criar múltiplos datasets?

A criação desses cenários permite analisar como diferentes formas de representar a mesma informação impactam o desempenho do modelo.

Especificamente, foi possível avaliar:

- Se a variável _submodalidade_ realmente agrega valor preditivo
- Se o agrupamento reduz ruído ou perda de informação
- Se a engenharia de atributos melhora a capacidade de generalização

Essa abordagem experimental torna a análise mais robusta e fundamentada.

---

## 🔹 Estratégias adicionais

Além dos cenários acima, também foram avaliadas variações com:

- Aplicação de **SMOTE**, para balanceamento das classes
- Diferentes combinações de features

---

## 🔹 Divisão dos Dados

Para todos os cenários, os dados foram divididos em:

- **Treino**: utilizado para ajuste dos modelos
- **Teste**: utilizado para avaliação final de desempenho

A divisão foi mantida consistente entre os cenários para garantir comparabilidade justa entre os resultados.

---

## 🔹 Avaliação Inicial (Baseline)

Antes da otimização, foi realizado um treinamento inicial (baseline) utilizando em todos os modelos, em cada um dos três cenários.

O objetivo dessa etapa foi:

- Comparar rapidamente o desempenho entre os datasets
- Identificar qual estratégia de pré-processamento apresenta melhores resultados
- Evitar custo computacional desnecessário com otimização em cenários inferiores

As métricas utilizadas foram:

- ROC AUC
- F1-score
- Accuracy

---

## 🔹 Análise dos Resultados

Os resultados indicaram que:

- O desempenho do modelo se manteve **consistente entre os cenários**
- A engenharia de atributos conseguiu capturar a maior parte da informação da variável _submodalidade_
- A aplicação de **SMOTE não trouxe ganhos significativos**, podendo inclusive reduzir levemente o desempenho

Dessa forma, optou-se por utilizar o cenário:

**sem_submodalidade (sem SMOTE)**

Essa escolha foi baseada em:

- menor complexidade do modelo
- menor risco de overfitting
- desempenho equivalente aos demais cenários

---

## 🔹 Otimização de Hiperparâmetros (Grid Search)

Após a definição do melhor cenário, foi realizada a otimização dos hiperparâmetros do modelo **XGBoost** utilizando Grid Search.

O objetivo dessa etapa foi refinar o desempenho do modelo por meio do ajuste de parâmetros como:

- número de estimadores (`n_estimators`)
- profundidade das árvores (`max_depth`)
- taxa de aprendizado (`learning_rate`)
- entre outros

Essa otimização foi aplicada apenas no melhor cenário identificado na etapa anterior, garantindo eficiência computacional e foco na melhor configuração de dados.

---
