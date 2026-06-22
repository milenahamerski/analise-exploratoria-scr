import os
import json
import joblib
import pandas as pd
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="RiskAnalyzer API")

# Configura o diretório atual como base para arquivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best_model.joblib")
COLUMNS_PATH = os.path.join(BASE_DIR, "model_columns.joblib")

model = None
model_columns = None

def carregar_modelo():
    global model, model_columns
    if os.path.exists(MODEL_PATH) and os.path.exists(COLUMNS_PATH):
        model = joblib.load(MODEL_PATH)
        model_columns = joblib.load(COLUMNS_PATH)
        print("Modelo e colunas carregados com sucesso.")
    else:
        print("Aviso: Modelo ou arquivo de colunas não encontrados.")

carregar_modelo()

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

class PredictionRequest(BaseModel):
    uf: str = "SP"
    cnae_ocupacao: str = "Outros"
    porte: str = "Indisponível"
    modalidade: str = "Empréstimos"
    submodalidade: str = "Outros"
    numero_de_operacoes: float = 1.0
    a_vencer_ate_90_dias: float = 0.0
    a_vencer_de_91_ate_360_dias: float = 0.0
    a_vencer_de_361_ate_1080_dias: float = 0.0
    a_vencer_de_1081_ate_1800_dias: float = 0.0
    a_vencer_de_1801_ate_5400_dias: float = 0.0
    a_vencer_acima_de_5400_dias: float = 0.0
    carteira_a_vencer: float = 0.0

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    mock_db_path = os.path.join(BASE_DIR, "mock_members.json")
    if os.path.exists(mock_db_path):
        with open(mock_db_path, "r", encoding="utf-8") as f:
            members = json.load(f)
    else:
        members = []
        
    total = len(members)
    altos = sum(1 for m in members if m.get("risk_status") == "Alto")
    medios = sum(1 for m in members if m.get("risk_status") == "Médio")
    baixos = sum(1 for m in members if m.get("risk_status") == "Baixo")
    risco_medio = sum(m.get("risk_percent", 0) for m in members) / total if total > 0 else 0
    
    return templates.TemplateResponse(
        request=request, 
        name="dashboard.html", 
        context={
            "request": request, 
            "members": members,
            "total": total,
            "altos": altos,
            "medios": medios,
            "baixos": baixos,
            "risco_medio": round(risco_medio, 2)
        }
    )

@app.post("/predict")
async def predict(data: PredictionRequest):
    if model is None or model_columns is None:
        raise HTTPException(status_code=500, detail="Modelo não está carregado. Treine o modelo primeiro.")
        
    # Monta o DataFrame de uma linha
    input_dict = data.model_dump()
    
    df = pd.DataFrame([input_dict])
    
    # Adicionando features derivadas caso a limpeza fizesse isso
    df["operacoes_missing"] = 0
    if df.loc[0, "numero_de_operacoes"] < 0:
        df.loc[0, "operacoes_missing"] = 1
        df.loc[0, "numero_de_operacoes"] = 1  # valor padrao se negativo

    df["carteira_a_vencer"] = df["carteira_a_vencer"].replace(0, 1)
    
    # Aplica o get_dummies
    df_dummies = pd.get_dummies(df)
    
    # Garante que as colunas sejam exatamente as mesmas usadas no treinamento
    df_final = pd.DataFrame(columns=model_columns)
    for col in model_columns:
        if col in df_dummies.columns:
            df_final[col] = df_dummies[col]
        else:
            df_final[col] = 0
            
    # Garantir que não haja NaN e todos sejam numéricos
    df_final = df_final.fillna(0).apply(pd.to_numeric)
    
    # Faz a predição da probabilidade (inadimplência = classe 1)
    prob = model.predict_proba(df_final)[0]
    
    class_1_index = list(model.classes_).index(1) if 1 in model.classes_ else 1
    prob_inadimplencia = prob[class_1_index]
    
    return {"inadimplencia_percent": round(prob_inadimplencia * 100, 2)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
