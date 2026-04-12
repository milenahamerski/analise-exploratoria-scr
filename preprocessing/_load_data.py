import pandas as pd

def load_data(path):
    df = pd.read_csv(path, sep=";")

    df = df[[
        "uf", "cliente", "cnae_ocupacao",
        "porte", "modalidade", "submodalidade",
        "carteira_vencida",
        "numero_de_operacoes",
        "a_vencer_ate_90_dias",
        "a_vencer_de_91_ate_360_dias",
        "a_vencer_de_361_ate_1080_dias",
        "a_vencer_de_1081_ate_1800_dias",
        "a_vencer_de_1801_ate_5400_dias",
        "a_vencer_acima_de_5400_dias",
        "carteira_a_vencer"
    ]]

    return df