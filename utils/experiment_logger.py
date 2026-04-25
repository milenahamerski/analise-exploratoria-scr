import pandas as pd
import os
import matplotlib.pyplot as plt

def save_results(results, file_path="../results/experiments.csv"):
    df = pd.DataFrame(results)

    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False, sep=";")
    else:
        df.to_csv(file_path, mode="a", header=False, index=False, sep=";")

def plot_model_results(file_path, model_name):
    df = pd.read_csv(file_path, sep=";")

    df_model = df[df["model"] == model_name]

    df_grouped = df_model.groupby("scenario")[["roc_auc", "f1", "accuracy"]].mean()

    df_grouped.plot(kind="bar")

    plt.title(f"Scenario Comparison - {model_name}")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_model_comparison(file_path, metric="roc_auc"):
    df = pd.read_csv(file_path, sep=";")

    df_grouped = df.groupby("model")[metric].mean()

    df_grouped.plot(kind="bar")

    plt.title(f"Model Comparison ({metric})")
    plt.ylabel(metric)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()