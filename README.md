# Portfolio MOUHAMADOU MAKHTAR DIOUF
## Data Analyst | BI | Process Automation

Portfolio professionnel interactif construit avec Streamlit et un design system moderne.

## 🚀 Installation

```bash
pip install -r requirements.txt
```

## 📦 Lancement

```bash
streamlit run app.py
```

L'application sera accessible sur `http://localhost:8501`

## 📁 Structure du projet

```
.
├── app.py                              # Page d'accueil du portfolio
├── components/                         # Composants réutilisables
│   ├── __init__.py
│   ├── design_system.py               # CSS global et palettes
│   ├── cards.py                       # Cartes info et métriques KPI
│   ├── alerts.py                      # Messages d'alerte stylisés
│   ├── badges.py                      # Badges de statut
│   ├── tables.py                      # Tableaux HTML stylisés
│   └── gauges.py                      # Jauges interactives Plotly
├── pages/                             # Pages du portfolio
│   ├── 1_📊_Dashboard_Analytique.py   # Exemple dashboard BI
│   ├── 2_🔍_Monitoring.py             # Exemple monitoring
│   ├── 3_👥_CRM.py                    # Exemple dashboard CRM
│   ├── 4_🚀_Projets_Détaillés.py      # Portfolio projets complet
│   └── 5_💻_Compétences.py            # Compétences techniques
├── requirements.txt
└── README.md
```

## 📊 Contenu du Portfolio

### Page d'Accueil
- Présentation professionnelle
- KPIs et métriques clés
- Expériences professionnelles détaillées (IPSOS, SNSOFTWARE, BHS)
- Formation académique (Masters Data Science & Big Data)
- Compétences techniques par domaine
- Projets portfolio

### Pages Additionnelles
1. **Dashboard Analytique** - Exemple de dashboard BI avec KPIs et graphiques
2. **Monitoring** - Dashboard de suivi système temps réel
3. **CRM** - Interface de gestion relation client
4. **Projets Détaillés** - Portfolio complet avec descriptions approfondies
5. **Compétences** - Vue détaillée des compétences techniques et soft skills

## 🎨 Design System

Le portfolio utilise un design system complet avec :

### Composants Disponibles
- **Cards extensibles** : Cartes d'information avec effet hover
- **Métriques KPI** : Cartes avec gradients colorés
- **Alerts** : Messages stylisés (success, warning, danger, info)
- **Badges** : Indicateurs de statut colorés
- **Tables** : Tableaux HTML avec style moderne
- **Gauges** : Jauges interactives Plotly

### Palettes de Couleurs
- **Primary** : #007bff (Bleu)
- **Success** : #28a745 (Vert)
- **Warning** : #ffc107 (Jaune)
- **Danger** : #dc3545 (Rouge)
- **Info** : #17a2b8 (Cyan)

## 🛠️ Technologies Utilisées

- **Frontend** : Streamlit, HTML/CSS
- **Visualisation** : Plotly, Matplotlib
- **Data** : Pandas, NumPy
- **Python** : 3.8+

## 📝 Personnalisation

Pour adapter le portfolio à vos besoins :

1. **Modifier les informations personnelles** : Éditez `app.py`
2. **Ajouter des projets** : Complétez `pages/4_🚀_Projets_Détaillés.py`
3. **Personnaliser le design** : Modifiez `components/design_system.py`
4. **Ajouter des pages** : Créez de nouveaux fichiers dans `pages/`

## 📧 Contact

**MOUHAMADOU MAKHTAR DIOUF**
- 📞 +221 77 147 90 09
- 📍 Dakar, Sénégal
- 💼 Data Analyst | BI | Process Automation

## 📄 Licence

Ce portfolio est un projet personnel. Libre d'utilisation pour inspiration.
