import numpy as np
import pandas as pd

def clean_data(df):
    df = df[df["cliente"] == "PF"].copy()

    df["carteira_vencida"] = (
        df["carteira_vencida"]
        .astype(str)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )
    df["carteira_vencida"] = (df["carteira_vencida"] > 0).astype(int)

    df["porte"] = df["porte"].fillna("Indisponível")
    df["submodalidade"] = df["submodalidade"].fillna("desconhecido")

    # Conversão de valores monetários de string (vírgula) para float
    cols_valores = [
        "a_vencer_ate_90_dias",
        "a_vencer_de_91_ate_360_dias",
        "a_vencer_de_361_ate_1080_dias",
        "a_vencer_de_1081_ate_1800_dias",
        "a_vencer_de_1801_ate_5400_dias",
        "a_vencer_acima_de_5400_dias",
        "carteira_a_vencer"
    ]

    for col in cols_valores:
        df[col] = (
            df[col].astype(str)
            .str.replace(",", ".", regex=False)
        )
        df[col] = df[col].astype(float)

    df["carteira_a_vencer"] = df["carteira_a_vencer"].replace(0, 1)

    # operações
    df["numero_de_operacoes"] = df["numero_de_operacoes"].replace("<= 15", 15)
    df["numero_de_operacoes"] = pd.to_numeric(df["numero_de_operacoes"], errors="coerce")

    df["operacoes_missing"] = (df["numero_de_operacoes"] < 0).astype(int)
    df.loc[df["numero_de_operacoes"] < 0, "numero_de_operacoes"] = np.nan

    df["numero_de_operacoes"] = df["numero_de_operacoes"].fillna(
        df["numero_de_operacoes"].median()
    )

    return df