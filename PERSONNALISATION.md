# 🎨 Guide de Personnalisation

Ce guide vous aide à personnaliser facilement votre portfolio selon vos besoins.

---

## 🎯 Modifications Rapides

### 1. Informations Personnelles

**Fichier :** `app.py`

```python
# Ligne 13-14 : Nom et titre
st.title("📊 VOTRE NOM COMPLET")
st.subheader("Votre Titre Professionnel")

# Ligne 18 : Contact
st.markdown("📞 **Votre Numéro**")
st.markdown("💻 **Stack:** Vos Technologies")

# Ligne 21 : Statut
st.markdown(create_badge("Votre Statut", "success"), unsafe_allow_html=True)
```

### 2. Modifier les KPIs

**Fichier :** `app.py` (lignes 27-40)

```python
with col1:
    st.markdown(create_metric_card(
        "VALEUR",           # Votre chiffre
        "LABEL",            # Votre description
        "ICONE",            # Emoji de votre choix
        "COULEUR"           # success, default, warning, danger
    ), unsafe_allow_html=True)
```

**Exemples d'icônes :**
- 📊 📈 📉 💹 (Graphiques)
- 👥 👤 🧑‍💼 (Personnes)
- 💰 💵 💳 (Finance)
- ⏱️ ⏰ 🕐 (Temps)
- 🚀 🎯 ⭐ (Objectifs)
- 💻 🖥️ ⌨️ (Tech)

### 3. Section "À Propos"

**Fichier :** `app.py` (lignes 48-60)

```python
st.markdown("""
Votre description professionnelle ici.

Points clés :
- Point 1
- Point 2
- Point 3
""")
```

---

## 💼 Expériences Professionnelles

### Ajouter une Expérience

**Fichier :** `app.py`

```python
with st.expander("🏢 Titre Poste – ENTREPRISE (Dates)", expanded=False):
    st.markdown("**Contexte :** Description du contexte")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📊 Domaine 1**
        - Réalisation 1
        - Réalisation 2
        """)
    
    with col2:
        st.markdown("""
        **🔄 Domaine 2**
        - Réalisation 3
        - Réalisation 4
        
        **🛠️ Technologies**
        - Tech 1, Tech 2
        """)
```

### Modifier une Expérience Existante

Cherchez le bloc `with st.expander("🏢 ...")` et modifiez le contenu.

---

## 🚀 Projets

### Ajouter un Projet Simple

**Fichier :** `app.py` (section Projets)

```python
with col1:  # ou col2, col3
    st.markdown(create_info_card(
        "Nom du Projet",
        {
            "Description": "Description courte",
            "Technologies": "Tech 1, Tech 2",
            "Statut": create_badge("Terminé", "success")
        },
        "📊",  # Icône
        "primary"  # Couleur
    ), unsafe_allow_html=True)
```

### Ajouter un Projet Détaillé

**Fichier :** `pages/4_🚀_Projets_Détaillés.py`

```python
with st.expander("🆕 Titre de Votre Projet"):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Description
        Description détaillée de votre projet.
        
        ### Problématique
        Le problème à résoudre.
        
        ### Solution Développée
        Votre solution.
        
        ### Impact Mesurable
        - ⏱️ **Métrique 1**
        - 📈 **Métrique 2**
        """)
    
    with col2:
        st.markdown(create_info_card(
            "Informations Projet",
            {
                "Client": "Nom client",
                "Durée": "X mois",
                "Statut": create_badge("Terminé", "success")
            },
            "📊",
            "primary"
        ), unsafe_allow_html=True)
```

---

## 🛠️ Compétences

### Modifier les Jauges

**Fichier :** `pages/5_💻_Compétences.py` (lignes 13-25)

```python
with col1:
    fig = create_gauge(
        85,                    # Valeur (0-100)
        "Nom Compétence",      # Titre
        unit="%"               # Unité
    )
    st.plotly_chart(fig, use_container_width=True)
```

### Ajouter une Compétence

**Fichier :** `pages/5_💻_Compétences.py`

Dans l'onglet approprié :

```python
st.markdown(create_info_card(
    "Catégorie",
    {
        "Compétence 1": "⭐⭐⭐⭐⭐ (Expert)",
        "Compétence 2": "⭐⭐⭐⭐ (Avancé)",
        "Compétence 3": "⭐⭐⭐ (Intermédiaire)"
    },
    "💻",
    "primary"
), unsafe_allow_html=True)
```

**Niveaux suggérés :**
- ⭐⭐⭐⭐⭐ (Expert)
- ⭐⭐⭐⭐ (Avancé)
- ⭐⭐⭐ (Intermédiaire)
- ⭐⭐ (Débutant)

---

## 🎨 Personnalisation du Design

### Changer les Couleurs Principales

**Fichier :** `components/design_system.py`

```python
# Ligne 50-56 : Couleurs des cartes
.box-primary { border-left-color: #VOTRE_COULEUR; }
.box-success { border-left-color: #VOTRE_COULEUR; }
.box-warning { border-left-color: #VOTRE_COULEUR; }
.box-danger { border-left-color: #VOTRE_COULEUR; }
.box-info { border-left-color: #VOTRE_COULEUR; }
```

### Modifier les Gradients des Métriques

**Fichier :** `components/cards.py` (lignes 38-43)

```python
gradients = {
    "default": "linear-gradient(135deg, #COULEUR1 0%, #COULEUR2 100%)",
    "success": "linear-gradient(135deg, #COULEUR1 0%, #COULEUR2 100%)",
    "warning": "linear-gradient(135deg, #COULEUR1 0%, #COULEUR2 100%)",
    "danger": "linear-gradient(135deg, #COULEUR1 0%, #COULEUR2 100%)"
}
```

**Générateurs de gradients :**
- [cssgradient.io](https://cssgradient.io/)
- [uigradients.com](https://uigradients.com/)

### Changer la Police

**Fichier :** `.streamlit/config.toml`

```toml
[theme]
font = "sans serif"  # Options: "sans serif", "serif", "monospace"
```

### Modifier les Couleurs du Thème

**Fichier :** `.streamlit/config.toml`

```toml
[theme]
primaryColor = "#007bff"           # Couleur principale
backgroundColor = "#ffffff"         # Fond
secondaryBackgroundColor = "#f0f2f6"  # Fond secondaire
textColor = "#262730"              # Texte
```

---

## 📄 Ajouter une Nouvelle Page

### 1. Créer le Fichier

**Nom :** `pages/7_🎯_Nom_Page.py`

Le numéro (7) détermine l'ordre dans le menu.

### 2. Structure de Base

```python
import streamlit as st
from components.design_system import inject_custom_css
from components.cards import create_info_card, create_metric_card
from components.alerts import create_alert
from components.badges import create_badge

st.set_page_config(page_title="Titre de la Page", layout="wide")
inject_custom_css()

st.title("🎯 Titre de la Page")
st.markdown("Description de la page")

st.markdown("---")

# Votre contenu ici
st.subheader("Section 1")
# ...

st.markdown("---")

st.subheader("Section 2")
# ...
```

---

## 🖼️ Ajouter des Images

### Image Simple

```python
st.image("chemin/vers/image.png", caption="Légende", use_column_width=True)
```

### Image dans une Carte

```python
col1, col2 = st.columns([1, 2])

with col1:
    st.image("photo.jpg", use_column_width=True)

with col2:
    st.markdown(create_info_card(
        "Informations",
        {"Info": "Valeur"},
        "📊",
        "primary"
    ), unsafe_allow_html=True)
```

---

## 📊 Ajouter des Graphiques

### Graphique Plotly

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 15, 13, 17]
})

fig = px.line(df, x='x', y='y', title="Mon Graphique")
st.plotly_chart(fig, use_container_width=True)
```

### Graphique Matplotlib

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 15, 13, 17])
ax.set_title("Mon Graphique")
st.pyplot(fig)
```

---

## 🔗 Ajouter des Liens

### Lien Simple

```python
st.markdown("[Texte du lien](https://url.com)")
```

### Bouton Lien

```python
if st.button("Voir le Projet"):
    st.markdown("[Lien vers le projet](https://github.com/...)")
```

### Liens Sociaux

```python
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://linkedin.com/in/...)")

with col2:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-black)](https://github.com/...)")

with col3:
    st.markdown("[![Email](https://img.shields.io/badge/Email-red)](mailto:...)")
```

---

## 📱 Responsive Design

### Layout Adaptatif

```python
# Desktop : 4 colonnes, Tablet : 2 colonnes, Mobile : 1 colonne
col1, col2, col3, col4 = st.columns(4)

# Ou avec proportions personnalisées
col1, col2 = st.columns([2, 1])  # col1 = 2/3, col2 = 1/3
```

### Tester le Responsive

1. Lancez l'app : `streamlit run app.py`
2. Ouvrez les DevTools (F12)
3. Activez le mode responsive
4. Testez différentes tailles d'écran

---

## 🎯 Astuces Avancées

### Cache pour Performance

```python
@st.cache_data(ttl=3600)  # Cache 1 heure
def load_data():
    # Chargement de données lourdes
    return data
```

### Sidebar Personnalisée

```python
with st.sidebar:
    st.image("logo.png")
    st.markdown("---")
    st.markdown("### Navigation")
    st.markdown("- [Accueil](#)")
    st.markdown("- [Projets](#)")
```

### Téléchargement de Fichiers

```python
import pandas as pd

df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
csv = df.to_csv(index=False)

st.download_button(
    label="Télécharger CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv"
)
```

---

## 🐛 Debugging

### Afficher des Variables

```python
st.write("Debug:", variable)
st.json({"key": "value"})
```

### Mode Debug

```bash
streamlit run app.py --logger.level=debug
```

---

## ✅ Checklist de Personnalisation

- [ ] Nom et titre modifiés
- [ ] Contact mis à jour
- [ ] KPIs personnalisés
- [ ] Expériences ajoutées/modifiées
- [ ] Projets ajoutés
- [ ] Compétences mises à jour
- [ ] Couleurs personnalisées (optionnel)
- [ ] Images ajoutées (optionnel)
- [ ] Liens sociaux ajoutés (optionnel)
- [ ] Testé localement
- [ ] Responsive vérifié

---

## 📚 Ressources

### Documentation
- [Streamlit Docs](https://docs.streamlit.io)
- [Plotly Python](https://plotly.com/python/)
- [Pandas Docs](https://pandas.pydata.org/docs/)

### Inspiration Design
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Dribbble](https://dribbble.com/tags/portfolio)
- [Behance](https://www.behance.net/search/projects?search=portfolio)

### Outils
- [Coolors](https://coolors.co/) - Palettes de couleurs
- [Flaticon](https://www.flaticon.com/) - Icônes
- [Unsplash](https://unsplash.com/) - Images gratuites

---

## 💡 Besoin d'Aide ?

1. Consultez le `GUIDE_DEMARRAGE.md`
2. Regardez la page `6_🎨_Demo_Composants.py`
3. Testez les exemples fournis
4. Consultez la documentation Streamlit

**Bon développement ! 🚀**
