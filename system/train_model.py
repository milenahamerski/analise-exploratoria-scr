import os
import sys
import joblib
from sklearn.ensemble import RandomForestClassifier

# Adiciona o diretório raiz ao path para importar pacotes locais
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from preprocessing.main_preprocessing import load_and_preprocess

def main():
    print("Iniciando carregamento e preprocessamento dos dados...")
    
    # Caminho do dataset
    dataset_path = "../predictive_models/scrdata_202505.csv"
    
    # Parâmetros escolhidos (conforme análise)
    scenario = "submodalidade_agrupada"
    use_smote = False
    
    # Carregando dados já formatados (o script de split interno aplica pd.get_dummies)
    X_train, X_test, y_train, y_test = load_and_preprocess(
        path=dataset_path,
        scenario=scenario,
        use_smote=use_smote
    )
    
    # Salvando as colunas exatas usadas no treinamento para alinhar na predição
    model_columns = list(X_train.columns)
    
    print(f"Colunas de treinamento geradas ({len(model_columns)} features).")
    
    print("Treinando o modelo RandomForestClassifier...")
    # Instanciando o modelo com os melhores hiperparâmetros
    rf = RandomForestClassifier(
        n_estimators=200,
        min_samples_split=5,
        min_samples_leaf=1,
        random_state=42,
        class_weight="balanced"  # Estava no baseline
    )
    
    rf.fit(X_train, y_train)
    print("Treinamento finalizado.")
    
    # Exportando modelo e colunas
    os.makedirs(os.path.dirname(__file__), exist_ok=True)
    joblib.dump(rf, os.path.join(os.path.dirname(__file__), "best_model.joblib"))
    joblib.dump(model_columns, os.path.join(os.path.dirname(__file__), "model_columns.joblib"))
    
    print("Modelo e colunas exportados com sucesso para a pasta system/.")

if __name__ == "__main__":
    main()
