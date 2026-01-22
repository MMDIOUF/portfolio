# 🚀 Guide de Démarrage Rapide

## Installation et Lancement

### 1. Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### 2. Installation des dépendances

```bash
pip install -r requirements.txt
```

### 3. Lancement de l'application

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse : `http://localhost:8501`

## 📱 Navigation

### Pages Disponibles

1. **🏠 Accueil** (`app.py`)
   - Vue d'ensemble du profil
   - Expériences professionnelles
   - Formation et projets académiques
   - Compétences résumées

2. **📊 Dashboard Analytique**
   - Exemple de dashboard BI
   - KPIs et métriques
   - Graphiques interactifs
   - Tableaux de données

3. **🔍 Monitoring**
   - Dashboard de monitoring système
   - Statut des services
   - Alertes temps réel
   - Jauges de performance

4. **👥 CRM**
   - Interface de gestion client
   - Recherche et profils
   - Score de fidélité
   - Recommandations

5. **🚀 Projets Détaillés**
   - Portfolio complet de projets
   - Descriptions approfondies
   - Technologies utilisées
   - Résultats et impacts

6. **💻 Compétences**
   - Compétences techniques détaillées
   - Jauges de niveau
   - Certifications
   - Langues

## 🎨 Personnalisation

### Modifier les Informations Personnelles

Éditez le fichier `app.py` et modifiez les sections :

```python
# En-tête
st.title("📊 VOTRE NOM")
st.subheader("Votre Titre")

# Contact
st.markdown("📞 **Votre Téléphone**")
```

### Ajouter un Nouveau Projet

Dans `pages/4_🚀_Projets_Détaillés.py`, ajoutez un nouveau `expander` :

```python
with st.expander("🆕 Titre de votre projet"):
    st.markdown("""
    ### Description
    Votre description ici...
    
    ### Technologies
    - Tech 1
    - Tech 2
    """)
```

### Modifier les Couleurs

Éditez `components/design_system.py` et modifiez les couleurs dans le CSS :

```python
.box-primary { border-left-color: #VOTRE_COULEUR; }
```

### Ajouter une Nouvelle Page

1. Créez un fichier dans `pages/` avec le format : `6_🎯_Nom_Page.py`
2. Copiez la structure de base :

```python
import streamlit as st
from components.design_system import inject_custom_css

st.set_page_config(page_title="Titre", layout="wide")
inject_custom_css()

st.title("🎯 Titre de la Page")
# Votre contenu ici
```

## 🛠️ Utilisation des Composants

### Carte d'Information

```python
from components.cards import create_info_card

st.markdown(create_info_card(
    "Titre",
    {
        "Label 1": "Valeur 1",
        "Label 2": "Valeur 2"
    },
    "📊",  # Icône
    "primary"  # Couleur
), unsafe_allow_html=True)
```

### Métrique KPI

```python
from components.cards import create_metric_card

st.markdown(create_metric_card(
    "1,234",      # Valeur
    "Utilisateurs",  # Label
    "👥",         # Icône
    "success"     # Gradient
), unsafe_allow_html=True)
```

### Alerte

```python
from components.alerts import create_alert

st.markdown(create_alert(
    "Message d'alerte",
    "success",  # Type: success, warning, danger, info
    "✅"        # Icône optionnelle
), unsafe_allow_html=True)
```

### Badge

```python
from components.badges import create_badge

badge = create_badge("Actif", "success")
st.markdown(f"Statut: {badge}", unsafe_allow_html=True)
```

### Jauge

```python
from components.gauges import create_gauge

fig = create_gauge(
    75,           # Valeur
    "Performance", # Titre
    unit="%"      # Unité
)
st.plotly_chart(fig, use_container_width=True)
```

### Tableau Stylisé

```python
from components.tables import create_styled_table
import pandas as pd

df = pd.DataFrame({
    'Colonne 1': ['A', 'B', 'C'],
    'Colonne 2': [1, 2, 3]
})

st.markdown(create_styled_table(df), unsafe_allow_html=True)
```

## 📊 Déploiement

### Streamlit Cloud (Gratuit)

1. Créez un compte sur [streamlit.io](https://streamlit.io)
2. Connectez votre repository GitHub
3. Sélectionnez `app.py` comme fichier principal
4. Déployez !

### Heroku

1. Créez un fichier `Procfile` :
```
web: streamlit run app.py --server.port=$PORT
```

2. Créez un fichier `setup.sh` :
```bash
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

3. Déployez sur Heroku

## 🐛 Dépannage

### L'application ne démarre pas
- Vérifiez que Python 3.8+ est installé : `python --version`
- Réinstallez les dépendances : `pip install -r requirements.txt --upgrade`

### Les graphiques ne s'affichent pas
- Vérifiez que Plotly est installé : `pip install plotly`
- Rechargez la page (Ctrl+R)

### Erreur d'import des composants
- Vérifiez que vous êtes dans le bon répertoire
- Vérifiez que le dossier `components/` contient `__init__.py`

## 💡 Conseils

1. **Performance** : Utilisez `@st.cache_data` pour les données volumineuses
2. **Responsive** : Testez sur mobile avec les DevTools du navigateur
3. **SEO** : Configurez `page_title` et `page_icon` pour chaque page
4. **Accessibilité** : Utilisez des contrastes de couleurs suffisants

## 📚 Ressources

- [Documentation Streamlit](https://docs.streamlit.io)
- [Documentation Plotly](https://plotly.com/python/)
- [Documentation Pandas](https://pandas.pydata.org/docs/)

## 🆘 Support

Pour toute question ou problème :
- Consultez la documentation Streamlit
- Vérifiez les issues GitHub du projet
- Contactez le développeur

---

**Bon développement ! 🚀**
