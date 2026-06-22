import os
import json
import joblib
import random
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best_model.joblib")
COLUMNS_PATH = os.path.join(BASE_DIR, "model_columns.joblib")

def generate_mock_data():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(COLUMNS_PATH):
        print("Model or columns not found. Aborting mock data generation.")
        return

    model = joblib.load(MODEL_PATH)
    model_columns = joblib.load(COLUMNS_PATH)

    # Names for random generation
    first_names = ["Ana", "Carlos", "Milena", "Lucas", "Fernanda", "Pedro", "Juliana", "Marcos", "Camila", "João", "Rafael", "Letícia", "Bruno", "Amanda", "Rodrigo"]
    last_names = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho", "Almeida"]
    
    estados = ["SP", "RJ", "MG", "PR", "SC", "RS", "AC", "Outros"]
    portes = ["Até 1 salário mínimo", "Mais de 1 a 2 salários mínimos", "Mais de 2 a 3 salários mínimos", "Mais de 3 a 5 salários mínimos", "Mais de 5 a 10 salários mínimos", "Mais de 10 a 20 salários mínimos", "Sem rendimento", "Indisponível"]
    cnaes = ["Autônomo", "Empregado de empresa privada", "Servidor ou empregado público", "Empresário", "MEI", "Outros"]
    modalidades = ["Empréstimos", "Financiamentos", "Financiamentos imobiliários", "Operações de arrendamento", "Outros créditos"]
    submodalidades = ["Crédito pessoal - com consignação em folha de pagam.", "Crédito pessoal - sem consignação em folha de pagam.", "Cartão de crédito - compra, fatura parcelada ou saque financiado pela instituição financeira emitente do cartão", "Cheque especial", "Financiamento habitacional - SFH", "Aquisição de bens - veículos automotores", "Outros"]

    records = []
    
    # Generate 100 records
    for i in range(100):
        nome = f"{random.choice(first_names)} {random.choice(last_names)}"
        carteira_a_vencer = round(random.uniform(100, 50000), 2)
        
        # Distribute the carteira into different ranges randomly
        rem = carteira_a_vencer
        a_vencer_ate_90_dias = round(random.uniform(0, rem), 2)
        rem -= a_vencer_ate_90_dias
        a_vencer_de_91_ate_360_dias = round(random.uniform(0, rem), 2)
        rem -= a_vencer_de_91_ate_360_dias
        a_vencer_de_361_ate_1080_dias = round(rem, 2)
        
        record = {
            "id": i + 1,
            "nome": nome,
            "uf": random.choice(estados),
            "cnae_ocupacao": random.choice(cnaes),
            "porte": random.choice(portes),
            "modalidade": random.choice(modalidades),
            "submodalidade": random.choice(submodalidades),
            "numero_de_operacoes": float(random.randint(1, 20)),
            "carteira_a_vencer": carteira_a_vencer,
            "a_vencer_ate_90_dias": a_vencer_ate_90_dias,
            "a_vencer_de_91_ate_360_dias": a_vencer_de_91_ate_360_dias,
            "a_vencer_de_361_ate_1080_dias": a_vencer_de_361_ate_1080_dias,
            "a_vencer_de_1081_ate_1800_dias": 0.0,
            "a_vencer_de_1801_ate_5400_dias": 0.0,
            "a_vencer_acima_de_5400_dias": 0.0
        }
        records.append(record)

    df = pd.DataFrame(records)
    
    # Keep original records for JSON
    original_records = df.to_dict(orient="records")

    # Clean and predict
    df["operacoes_missing"] = 0
    df.loc[df["numero_de_operacoes"] < 0, "operacoes_missing"] = 1
    df.loc[df["numero_de_operacoes"] < 0, "numero_de_operacoes"] = 1

    df["carteira_a_vencer"] = df["carteira_a_vencer"].replace(0, 1)
    
    # We must not pass 'id' and 'nome' to get_dummies or prediction
    df_pred = df.drop(columns=["id", "nome"])
    
    df_dummies = pd.get_dummies(df_pred)
    
    df_final = pd.DataFrame(columns=model_columns)
    for col in model_columns:
        if col in df_dummies.columns:
            df_final[col] = df_dummies[col]
        else:
            df_final[col] = 0
            
    df_final = df_final.fillna(0).apply(pd.to_numeric)
    
    probs = model.predict_proba(df_final)
    class_1_index = list(model.classes_).index(1) if 1 in model.classes_ else 1
    
    for i in range(len(original_records)):
        prob_inadimplencia = probs[i][class_1_index]
        risk_percent = round(prob_inadimplencia * 100, 2)
        
        # Risk thresholds: Green < 30%, Yellow 30-70%, Red > 70%
        if risk_percent < 30:
            status = "Baixo"
        elif risk_percent <= 70:
            status = "Médio"
        else:
            status = "Alto"
            
        original_records[i]["risk_percent"] = risk_percent
        original_records[i]["risk_status"] = status

    # Save to JSON
    output_path = os.path.join(BASE_DIR, "mock_members.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(original_records, f, ensure_ascii=False, indent=4)
        
    print(f"Gerado {len(original_records)} associados no arquivo mock_members.json.")

if __name__ == "__main__":
    generate_mock_data()
