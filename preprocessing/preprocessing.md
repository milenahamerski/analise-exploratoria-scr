# Pré-processamento e Estratégias de Modelagem

Este documento descreve detalhadamente o fluxo de pré-processamento aplicado à base de dados do SCR (Sistema de Informações de Crédito), a criação de cenários de *features*, e as estratégias de validação e otimização de modelos.

O ponto de entrada do pipeline de dados é a função `load_and_preprocess` em `main_preprocessing.py`.

---

## Passo 1: Carregamento dos Dados (`_load_data.py`)
Os dados originais em formato CSV são importados utilizando a biblioteca **Pandas**. Como o delimitador do CSV é o ponto e vírgula (`;`), a função garante a leitura correta e seleciona as colunas de interesse para o projeto.

---

## Passo 2: Limpeza e Saneamento (`_cleaning.py`)
Nesta etapa, os dados são padronizados e os problemas mais comuns do dataset são corrigidos:

1. **Filtro de Clientes:** Filtra o dataset para manter apenas registros onde `cliente == "PF"` (Pessoa Física).
2. **Definição da Target (`carteira_vencida`):** 
   - Converte os valores da coluna de string para float.
   - Transforma a coluna em uma variável binária ($1$ para inadimplente se `carteira_vencida > 0`, $0$ para adimplente).
3. **Tratamento de Nulos:**
   - Preenche valores nulos da coluna `porte` com `"Indisponível"`.
   - Preenche valores nulos de `submodalidade` com `"desconhecido"`.
4. **Padronização Monetária:** As colunas financeiras são convertidas de string para float.
5. **Correção Matemática:** Substitui valores $0$ por $1$ na `carteira_a_vencer` para evitar problemas de divisão por zero na criação de features.
6. **Saneamento de `numero_de_operacoes`:**
   - Identifica valores negativos de operações como dados faltantes e cria uma flag indicativa (`operacoes_missing = 1`).
   - Imputa os valores ausentes com a mediana da distribuição.

---

## Passo 3: Engenharia de Atributos (Feature Engineering)
*(Realizado em módulos auxiliares como `_feature_engineering.py` quando aplicável)*

Cria novas variáveis com o objetivo de enriquecer a representação dos dados:
- **Razões de Vencimento:** Proporção do saldo a vencer em curto, médio e longo prazo em relação ao saldo total da carteira.
- **Transformações Logarítmicas:** Aplicadas a saldos e número de operações para suavizar a assimetria na distribuição de valores.
- **Indicadores Numéricos/Textuais:** Mapeamento de informações relevantes em variáveis binárias (flags) para os modelos.

---

## Passo 4: Criação dos 3 Cenários (Datasets) (`_scenarios.py`)
Para testar a relevância da coluna `submodalidade` (que apresenta alta cardinalidade), os dados são divididos em 3 cenários experimentais distintos:

### 1. Cenário: `sem_submodalidade`
A coluna `submodalidade` é completamente descartada. Serve como *baseline* básico para avaliar se apenas dados de saldo e demográficos são suficientes.

### 2. Cenário: `submodalidade_agrupada`
Para reduzir o ruído gerado por categorias com baixíssima ocorrência:
- Categorias com menos de **1000 ocorrências** são agrupadas sob o rótulo único de **"Outros"**.

### 3. Cenário: `submodalidade_engineered`
Aplica agrupamentos lógicos de negócio baseados em regras de texto para diminuir a cardinalidade para 10 grupos principais (ex: Cartão de Crédito, Crédito Pessoal, Financiamento Habitacional, etc.). Após este mapeamento, a coluna original é descartada.

---

## Passo 5: Codificação e Divisão dos Dados (`_split.py`)

1. **One-Hot Encoding:** Converte todas as variáveis categóricas em binárias (*dummies*) numéricas (`drop_first=True`).
2. **Divisão de Treino/Teste:** Divide os dados em **70% para treinamento** e **30% para teste**, estratificados com base na variável target (`carteira_vencida`).

---

## Pipeline de Machine Learning e Balanceamento (SMOTE)

O projeto adota uma abordagem de **Pipeline Robusta** utilizando `imblearn.pipeline.Pipeline`, garantindo que:
- O **Scaling** (`StandardScaler`) seja calculado apenas no treino.
- **Nota Importante sobre SMOTE:** Para evitar o vazamento de dados (*data leakage*), o balanceamento de classes com **SMOTE não é aplicado no pré-processamento global**, sendo realizado estritamente dentro das dobras de validação cruzada.

---

## Otimização e Registro de Resultados

Para cada algoritmo (XGBoost, KNN, RandomForest, SVM, LogisticRegression, DecisionTree), realiza-se:

- **Grid Search CV**: Busca exaustiva pelos melhores hiperparâmetros.
- **SMOTE como Hiperparâmetro**: O grid search testa o pipeline *com* e *sem* SMOTE.
- **Log de Resultados**: O sistema registra os melhores desempenhos no arquivo `results/model_results.csv`, englobando as métricas de **ROC AUC** (principal), **F1-score** e **Accuracy**.
