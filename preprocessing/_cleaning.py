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

    # operações
    df["numero_de_operacoes"] = df["numero_de_operacoes"].replace("<= 15", 15)
    df["numero_de_operacoes"] = pd.to_numeric(df["numero_de_operacoes"], errors="coerce")

    df["operacoes_missing"] = (df["numero_de_operacoes"] < 0).astype(int)
    df.loc[df["numero_de_operacoes"] < 0, "numero_de_operacoes"] = np.nan

    df["numero_de_operacoes"] = df["numero_de_operacoes"].fillna(
        df["numero_de_operacoes"].median()
    )

    return df