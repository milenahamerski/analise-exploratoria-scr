# import pandas as pd
# from sklearn.model_selection import train_test_split

# def load_and_preprocess(path):
#     # 1. carregar
#     df = pd.read_csv(path, sep=";")

#     # 2. selecionar colunas
#     df = df[[
#         "uf", "cliente", "cnae_ocupacao",
#         "porte", "modalidade", "submodalidade",
#         "carteira_vencida"
#     ]]

#     # 3. filtrar PF
#     df = df[df["cliente"] == "PF"].copy()

#     # 4. target binário
#     df["carteira_vencida"] = (
#         df["carteira_vencida"]
#         .str.replace(",", ".")
#         .astype(float)
#     )
#     df["carteira_vencida"] = (df["carteira_vencida"] > 0).astype(int)

#     # 5. separar X e y
#     X = df.drop(["carteira_vencida", "cliente"], axis=1)
#     y = df["carteira_vencida"]

#     # 6. one-hot encoding direto
#     X = pd.get_dummies(X, drop_first=True).astype(int)
#     print(X.head())
#     print(y.head())

#     # 7. split
#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y,
#         test_size=0.3,
#         random_state=42,
#         stratify=y
#     )

#     return X_train, X_test, y_train, y_test

import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def load_and_preprocess(path):
    # =========================
    # 1. CARREGAR
    # =========================
    df = pd.read_csv(path, sep=";")

    # =========================
    # 2. SELEÇÃO DE COLUNAS
    # =========================
    df = df[[
        "uf", "cliente", "cnae_ocupacao",
        "porte", "modalidade", "submodalidade",
        "carteira_vencida"
    ]]

    # =========================
    # 3. FILTRAR PF
    # =========================
    df = df[df["cliente"] == "PF"].copy()

    # =========================
    # 4. TARGET BINÁRIO
    # =========================
    df["carteira_vencida"] = (
        df["carteira_vencida"]
        .str.replace(",", ".")
        .astype(float)
    )
    df["carteira_vencida"] = (df["carteira_vencida"] > 0).astype(int)

    # =========================
    # 5. X e y
    # =========================
    X = df.drop(["carteira_vencida", "cliente"], axis=1)
    y = df["carteira_vencida"]

    # =========================
    # 6. ONE-HOT (CORRIGIDO 🔥)
    # =========================
    X = pd.get_dummies(X, drop_first=True).astype(int)
    print(X.head())
    print(y.head())

    # =========================
    # 7. SPLIT
    # =========================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.3,
        random_state=42,
        stratify=y
    )
    
    
    # =========================
    # 8. SMOTE (SÓ TREINO 🔥)
    # =========================
    smote = SMOTE(random_state=42)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    # =========================
    # 9. DEBUG OPCIONAL
    # =========================
    print("Distribuição original:")
    print(y.value_counts(normalize=True))

    print("\nDistribuição após SMOTE:")
    print(pd.Series(y_train).value_counts(normalize=True))

    print("\nTipos de dados:")
    print(X_train.dtypes.value_counts())

    return X_train, X_test, y_train, y_test



# X_train, X_test, y_train, y_test = load_and_preprocess(
#     "predictive_models/scrdata_202505.csv"
# )