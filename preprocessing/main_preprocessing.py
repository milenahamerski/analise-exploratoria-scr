from preprocessing._load_data import load_data
from preprocessing._cleaning import clean_data
from preprocessing._feature_engineering import create_features
from preprocessing._scenarios import apply_scenario
from preprocessing._split import split_data

def load_and_preprocess(path, scenario, use_smote=True):

    df = load_data(path)
    df = clean_data(df)
    df = create_features(df)
    df = apply_scenario(df, scenario)

    return split_data(df, use_smote)