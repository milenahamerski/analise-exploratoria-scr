def _agrupar_submodalidade(df, threshold=1000):
    freq = df["submodalidade"].value_counts()
    validas = freq[freq > threshold].index

    df["submodalidade"] = df["submodalidade"].apply(
        lambda x: x if x in validas else "Outros"
    )
    return df

def apply_scenario(df, scenario):

    if scenario == "sem_submodalidade":
        return df.drop("submodalidade", axis=1)

    elif scenario == "submodalidade_agrupada":
        return _agrupar_submodalidade(df)

    elif scenario == "submodalidade_engineered":

        df["origem"] = df["modalidade"].apply(
            lambda x: "Sem_dest" if "sem dest" in str(x).lower() else "Com_dest"
        )

        df["indexador"] = df["modalidade"].apply(
            lambda x: "Prefixado" if "prefix" in str(x).lower() else "Outros"
        )

        return df.drop("submodalidade", axis=1)

    else:
        raise ValueError("Cenário inválido")