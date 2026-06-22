def _agrupar_submodalidade(df, threshold=1000):
    freq = df["submodalidade"].value_counts()
    validas = freq[freq > threshold].index

    df["submodalidade"] = df["submodalidade"].apply(
        lambda x: x if x in validas else "Outros"
    )
    return df

def _group_submodalidade_engineered(df):
    def get_group(sub):
        s = str(sub).lower().strip()
        
        # 1. Cartão de Crédito
        if "cartão de crédito" in s or "cartao de credito" in s or "fatura de cartão" in s or "fatura de cartao" in s:
            return "Cartão de Crédito"
        
        # 2. Crédito Pessoal
        elif "crédito pessoal" in s or "credito pessoal" in s:
            return "Crédito Pessoal"
            
        # 3. Financiamento Habitacional / Imobiliário
        elif "habitacional" in s or "imobiliário" in s or "imobiliario" in s or "home equity" in s:
            return "Financiamento Habitacional"
            
        # 4. Financiamento de Veículos / Arrendamento
        elif "veículos automotores" in s or "veiculos automotores" in s or "veículos autom." in s or "veiculos autom." in s or "arrendamento" in s:
            return "Financiamento de Veículos"
            
        # 5. Crédito Rural / Agroindustrial
        elif "custeio" in s or "comercialização" in s or "comercializacao" in s or "agroindustriais" in s:
            return "Crédito Rural"
            
        # 6. Capital de Giro
        elif "capital de giro" in s or "conta garantida" in s:
            return "Capital de Giro"
            
        # 7. Microcrédito
        elif "microcrédito" in s or "microcredito" in s:
            return "Microcrédito"
            
        # 8. Cheque Especial
        elif "cheque especial" in s:
            return "Cheque Especial"
            
        # 9. Aquisição de Bens
        elif "aquisição de bens" in s or "aquisicao de bens" in s:
            return "Aquisição de Bens"
            
        # 10. Outros / Não classificados
        else:
            return "Outros"
            
    df["submodalidade_grupo"] = df["submodalidade"].apply(get_group)
    return df

def apply_scenario(df, scenario):

    if scenario == "sem_submodalidade":
        return df.drop("submodalidade", axis=1)

    elif scenario == "submodalidade_agrupada":
        return _agrupar_submodalidade(df)

    elif scenario == "submodalidade_engineered":
        df = _group_submodalidade_engineered(df)
        return df.drop("submodalidade", axis=1)

    else:
        raise ValueError("Cenário inválido")