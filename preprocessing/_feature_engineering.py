import numpy as np

def create_features(df):

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

    # proporções
    df["perc_curto"] = df["a_vencer_ate_90_dias"] / df["carteira_a_vencer"]

    df["perc_medio"] = (
        df["a_vencer_de_91_ate_360_dias"] +
        df["a_vencer_de_361_ate_1080_dias"]
    ) / df["carteira_a_vencer"]

    df["perc_longo"] = (
        df["a_vencer_de_1081_ate_1800_dias"] +
        df["a_vencer_de_1801_ate_5400_dias"] +
        df["a_vencer_acima_de_5400_dias"]
    ) / df["carteira_a_vencer"]

    df["log_carteira"] = np.log1p(df["carteira_a_vencer"])
    df["operacoes_log"] = np.log1p(df["numero_de_operacoes"])

    return df