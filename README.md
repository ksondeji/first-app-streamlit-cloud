# Prédicteur de churn — Streamlit

<div align="center">
  
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://first-app-cloud-vhjtmtp83vfptgbkssvy8i.streamlit.app/)

</div>

## Présentation

Petite application web qui estime le **risque de churn** d’un client à partir de deux indicateurs : l’**ancienneté** (en mois) et la **facture mensuelle** (€). L’interface permet de régler ces paramètres dans la barre latérale et d’obtenir une probabilité de départ, avec un message visuel selon le niveau de risque.

## Problématique

Le churn (départ des clients) a un impact direct sur le chiffre d’affaires et les coûts d’acquisition. Anticiper ce risque permet de cibler les actions de rétention. Ici, le besoin est volontairement **simple** : montrer un flux complet *données → modèle → interface*, sans base de données déploiement rapide sur le cloud.

## Résultats

- Sortie : **probabilité de churn** (classe positive), entre 0 % et 100 %.
- **Seuil d’alerte** : au-delà de **50 %**, le risque est affiché comme élevé ; en dessous, comme faible.
Pour un usage métier, il faudrait entraîner sur de vraies données et valider les performances (métriques, seuil, biais).

---
 ## [Démo live sur streamlit cloud](https://first-app-cloud-vhjtmtp83vfptgbkssvy8i.streamlit.app/)

 ---
 
## Installation rapide

```bash
git clone <url-du-repo>
cd first-app-streamlit-cloud
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
python train_churn_model.py     # génère churn_model.pkl si besoin
streamlit run app.py
```

Ouvrir le navigateur à l’adresse indiquée par Streamlit (souvent `http://localhost:8501`).

## Stack

| Élément | Technologie |
|--------|-------------|
| Interface | [Streamlit](https://streamlit.io/) |
| Données / entrées | [pandas](https://pandas.pydata.org/) |
| Modèle ML | [scikit-learn](https://scikit-learn.org/) (forêt aléatoire, entraînement dans `train_churn_model.py`) |
| Sérialisation | [joblib](https://joblib.readthedocs.io/) (`.pkl`) |
| Hébergement (démo) | [Streamlit Community Cloud](https://streamlit.io/cloud) |

---

