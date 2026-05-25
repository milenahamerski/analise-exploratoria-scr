import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load and clean experiments.csv (Baselines)
def parse_metric(val):
    if pd.isna(val) or val == '': return 0.0
    if isinstance(val, (int, float)): return float(val)
    s = str(val).replace('.', '').strip()
    if len(s) > 1:
        # Normalized to 0.XXXX format
        try:
            res = float(s[0] + '.' + s[1:])
            if res > 1.0: res /= 10.0
            return res
        except:
            return 0.0
    try:
        return float(s)
    except:
        return 0.0

def load_baselines():
    data = []
    with open('/home/milena-hamerski/Documents/UTFPR/TCC/analise_ds/results/experiments.csv', 'r') as f:
        lines = f.readlines()
    
    for line in lines[1:]:
        line = line.strip()
        if not line: continue
        
        sep = ';' if ';' in line else ','
        parts = [p.strip() for p in line.split(sep)]
        
        if len(parts) < 6: continue
        
        # Check if it's a baseline row
        is_baseline = any(p.lower() == 'baseline' for p in parts)
        
        if is_baseline:
            try:
                data.append({
                    'model': parts[0],
                    'scenario': parts[1],
                    'smote': parts[2].lower() == 'true',
                    'roc_auc': parse_metric(parts[3]),
                    'type': 'baseline'
                })
            except: continue
    return pd.DataFrame(data)

# Function to load and clean model_results.csv (Tuning)
def load_tuning():
    df = pd.read_csv('/home/milena-hamerski/Documents/UTFPR/TCC/analise_ds/results/model_results.csv', sep=';')
    df['smote'] = df['smote'].astype(str).str.lower() == 'true'
    return df

df_baseline = load_baselines()
df_tuning = load_tuning()

summary = []
models = df_tuning['model'].unique()

for m in models:
    for s in [False, True]:
        t_cv = df_tuning[(df_tuning['model'] == m) & (df_tuning['smote'] == s) & (df_tuning['phase'] == 'tuning_cv')]
        t_test = df_tuning[(df_tuning['model'] == m) & (df_tuning['smote'] == s) & (df_tuning['phase'] == 'test')]
        
        b = df_baseline[(df_baseline['model'] == m) & (df_baseline['smote'] == s) & (df_baseline['scenario'] == 'sem_submodalidade')]
        
        if not t_cv.empty or not t_test.empty:
            summary.append({
                'Modelo': m,
                'SMOTE': 'Sim' if s else 'Não',
                'Baseline (Teste)': b['roc_auc'].iloc[-1] if not b.empty else np.nan,
                'Tuning (Treino CV)': t_cv['roc_auc'].iloc[0] if not t_cv.empty else np.nan,
                'Tuning (Teste)': t_test['roc_auc'].iloc[0] if not t_test.empty else np.nan
            })

df_summary = pd.DataFrame(summary).sort_values(['Modelo', 'SMOTE'])

# Create Heatmap
plt.figure(figsize=(12, 8))
plot_data = df_summary.set_index(['Modelo', 'SMOTE'])
plot_data = plot_data.dropna(how='all')

sns.heatmap(plot_data, annot=True, fmt=".4f", cmap="YlGnBu", cbar_kws={'label': 'ROC AUC'})
plt.title('Comparativo de Performance (ROC AUC): Baseline vs GridSearch', fontsize=15)
plt.ylabel('Modelo / SMOTE', fontsize=12)
plt.xlabel('Fase do Experimento', fontsize=12)
plt.tight_layout()
plt.savefig('/home/milena-hamerski/Documents/UTFPR/TCC/analise_ds/results/heatmap_resultados.png', dpi=300)

df_summary.to_csv('/home/milena-hamerski/Documents/UTFPR/TCC/analise_ds/results/summary_table.csv', index=False)
