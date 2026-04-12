from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import pandas as pd

def split_data(df, use_smote=True):

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

    if use_smote:
        smote = SMOTE(random_state=42)
        X_train, y_train = smote.fit_resample(X_train, y_train)

    return X_train, X_test, y_train, y_test