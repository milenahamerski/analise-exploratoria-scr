from sklearn.model_selection import train_test_split
import pandas as pd

def split_data(df, use_smote=False):

    X = df.drop(["carteira_vencida", "cliente"], axis=1)
    y = df["carteira_vencida"]

    X = pd.get_dummies(X, drop_first=True)
    X = X.apply(pd.to_numeric)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.3,
        random_state=42,
        stratify=y
    )

    # Nota: O SMOTE foi removido daqui para evitar vazamento de dados (data leakage)
    # durante a validação cruzada. Agora o SMOTE deve ser aplicado via Pipeline
    # nos notebooks de modelagem.

    return X_train, X_test, y_train, y_test