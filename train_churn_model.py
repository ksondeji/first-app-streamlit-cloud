"""
Entraîne un modèle simple de churn et enregistre le model churn_model.pkl.
À exécuter une fois en local : python train_churn_model.py
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Données synthétiques cohérentes : churn souvent lié à faible ancienneté / charges élevées
rng = np.random.default_rng(42)
n = 500
tenure = rng.integers(1, 73, size=n)
monthly_charges = rng.uniform(20, 120, size=n)
# Score latent : plus de risque si tenure bas et charges hautes
risk = -0.04 * tenure + 0.015 * monthly_charges + rng.normal(0, 0.5, size=n)
churn = (risk > 0).astype(int)

X = pd.DataFrame({"tenure": tenure, "MonthlyCharges": monthly_charges})
y = churn

model = RandomForestClassifier(n_estimators=50, max_depth=6, random_state=42)
model.fit(X, y)

joblib.dump(model, "churn_model.pkl")
print("Modèle enregistré : churn_model.pkl")
