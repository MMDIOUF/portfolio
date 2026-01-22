import streamlit as st
from components.design_system import inject_custom_css
from components.cards import create_info_card

st.set_page_config(page_title="Portfolio - Projets Data", layout="wide")
inject_custom_css()

# === 1. HERO — SILENCE VISUEL ===
st.markdown("""
<div style="text-align: center; padding: 5rem 2rem 4rem;">
    <h1 style="font-size: 3.2rem; font-weight: 800; color: #1f2937; margin-bottom: 1.5rem;">
        Portfolio Data
    </h1>
    <p style="font-size: 1.4rem; color: #6b7280; max-width: 820px; margin: 0 auto; line-height: 1.6;">
        De la donnée brute<br/>
        <strong>à la décision stratégique.</strong>
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# === 2. ACTE I — LA BASE : PIPELINES & ARCHITECTURE ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        ☁️ La fondation
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Sans pipeline fiable, aucune analyse n'est crédible.
    </p>
""", unsafe_allow_html=True)

# CARDS RÉSUMÉ
col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Pipeline Multi-Cloud Immobilier",
        {
            "Objectif": "Automatisation data",
            "Cloud": "AWS • GCP",
            "Valeur": "Analyse fiable & scalable"
        },
        "☁️",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Big Data & Automatisation",
        {
            "Objectif": "Traitement massif",
            "Mode": "Batch & Temps réel",
            "Valeur": "Zéro intervention humaine"
        },
        "🔄",
        "success"
    ), unsafe_allow_html=True)

# EXPANDERS (DÉTAIL SUR DEMANDE)
with st.expander("🔍 Voir les détails — Pipeline Multi-Cloud"):
    st.markdown("""
    **Problème**  
    Données immobilières dispersées, non exploitables.
    
    **Solution**  
    Pipeline automatisé entre AWS et GCP pour collecter, stocker, sécuriser et analyser.
    
    **Impact**
    - Fiabilité des données garantie
    - Analyse quasi temps réel
    - Architecture scalable et sécurisée
    - Réduction 80% des interventions manuelles
    
    **Technologies**  
    `AWS S3` • `Lambda` • `IAM` • `GCP BigQuery` • `Cloud Storage` • `Python` • `SQL`
    """)

with st.expander("🔍 Voir les détails — Big Data & Automatisation"):
    st.markdown("""
    **Problème**  
    Volumes massifs de données nécessitant traitement batch et temps réel.
    
    **Solution**  
    Pipelines Big Data avec ingestion automatisée, monitoring et alerting.
    
    **Impact**
    - Automatisation complète ETL
    - Monitoring temps réel des flux
    - Alerting automatique sur anomalies
    - Traçabilité complète des données
    
    **Technologies**  
    `Hadoop` • `Hive` • `Apache NiFi` • `Talend` • `Python` • `SQL`
    """)

st.markdown("---")

# === 3. ACTE II — PRÉDIRE AU LIEU DE CONSTATER ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        🤖 Anticiper
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        La data prend de la valeur quand elle prédit.
    </p>
""", unsafe_allow_html=True)

# CARTES ML (SYNTHÈSE)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(create_info_card(
        "Prédiction Churn Client",
        {
            "Usage": "Rétention",
            "Résultat": "Recall 85%",
            "Décision": "Ciblage proactif"
        },
        "📉",
        "warning"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Souscription Assurance",
        {
            "Usage": "Marketing",
            "Résultat": "Accuracy 89%",
            "Décision": "ROI +45%"
        },
        "🏦",
        "info"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(create_info_card(
        "Prévision de Salaire",
        {
            "Usage": "RH",
            "Résultat": "R² 0.87",
            "Décision": "Équité & pilotage"
        },
        "💰",
        "success"
    ), unsafe_allow_html=True)

# EXPANDERS (ULTRA STRATÉGIQUES)
with st.expander("🔍 Détails — Prédiction Churn Client"):
    st.markdown("""
    **Objectif**  
    Identifier les clients à risque avant la rupture.
    
    **Méthode**  
    - Feature engineering avancé (RFM, comportement, historique)
    - Modèles de classification (Random Forest, XGBoost)
    - Validation croisée et optimisation hyperparamètres
    
    **Valeur business**  
    - Réduction des pertes clients de 30%
    - Campagnes de rétention ciblées
    - ROI positif dès le 2ème mois
    
    **Stack**  
    `Python` • `Scikit-Learn` • `Pandas` • `Streamlit`
    """)

with st.expander("🔍 Détails — Prédiction Souscription Assurance"):
    st.markdown("""
    **Objectif**  
    Cibler les profils à fort potentiel de souscription.
    
    **Méthode**  
    - Réseau de neurones (Deep Learning)
    - Analyse historique campagnes + données clients
    - Scoring prédictif en temps réel
    
    **Valeur business**  
    - Réduction coûts marketing de 45%
    - Taux de conversion +35%
    - Ciblage précis des prospects
    
    **Stack**  
    `TensorFlow` • `Keras` • `Scikit-Learn` • `Pandas`
    """)

with st.expander("🔍 Détails — Prévision de Salaire"):
    st.markdown("""
    **Objectif**  
    Aider les décisions RH par des modèles objectifs et équitables.
    
    **Méthode**  
    - Régression multiple avec feature engineering
    - Analyse des facteurs explicatifs (expérience, compétences, secteur)
    - Rapports automatisés pour RH
    
    **Valeur business**  
    - Équité salariale garantie
    - Pilotage masse salariale optimisé
    - Transparence des décisions
    
    **Stack**  
    `Python` • `Scikit-Learn` • `Seaborn` • `Pandas`
    """)

st.markdown("---")

# === 4. ACTE III — VOIR POUR DÉCIDER ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
         Voir pour décider
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Un bon dashboard élimine le bruit.
    </p>
</div>
""", unsafe_allow_html=True)

# CARTES VISUALISATION
col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Dashboards BI — IPSOS",
        {
            "Usage": "Suivi performance agents",
            "Impact": "Automatisation processus",
            "Valeur": "Réduction coûts humains"
        },
        "📊",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Dashboard Ventes USA",
        {
            "Usage": "Analyse commerciale",
            "Fonctions": "KPIs & Cartes",
            "Valeur": "Lecture immédiate"
        },
        "📈",
        "info"
    ), unsafe_allow_html=True)

# EXPANDERS
with st.expander("🔍 Détails — Dashboards BI IPSOS"):
    st.markdown("""
    **Contexte**  
    Cabinet d'études avec équipes terrain et téléphoniques. Besoin de suivi de performance et automatisation du reporting.
    
    **Solution**  
    - Dashboards décisionnels pour visualisation KPIs agents
    - Automatisation des processus de reporting manuels
    - Suivi performance en temps réel par agent et campagne
    - Visualisation dynamique des indicateurs métier
    
    **Impact**  
    - Réduction drastique du temps de reporting manuel
    - Diminution des coûts humains liés au suivi
    - KPIs parlants et accessibles instantanément
    - Suivi performance agents optimisé
    
    **Stack**  
    `Python` • `Streamlit` • `Pandas` • `Plotly` • `Seaborn` • `Excel`
    """)

with st.expander("🔍 Détails — Dashboard Ventes USA"):
    st.markdown("""
    **Objectif**  
    Analyse interactive des ventes par région, état et client.
    
    **Fonctionnalités**  
    - KPIs temps réel (CA, volume, marge)
    - Top 10 clients dynamique
    - Cartes géographiques interactives
    - Filtres multi-critères (période, région, produit)
    
    **Valeur**  
    - Lecture immédiate des tendances
    - Identification rapide des opportunités
    - Pilotage commercial data-driven
    
    **Stack**  
    `Streamlit` • `Plotly` • `Pandas` • `Matplotlib`
    """)

st.markdown("---")

# === 5. ACTE IV — FIABILITÉ & DONNÉES SENSIBLES ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        🛡️ Fiabilité & sécurité
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Certaines données ne tolèrent aucune erreur.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Détection Faux Billets",
        {
            "Usage": "Contrôle automatique",
            "Résultat": "Accuracy 94%",
            "Valeur": "Sécurité renforcée"
        },
        "💵",
        "danger"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Administration Oracle",
        {
            "Usage": "Bases critiques",
            "Impact": "Optimisation -40%",
            "Valeur": "Performance & stabilité"
        },
        "🗄️",
        "success"
    ), unsafe_allow_html=True)

with st.expander("🔍 Détails — Détection Faux Billets"):
    st.markdown("""
    **Objectif**  
    Automatiser le contrôle de billets par vision artificielle.
    
    **Méthode**  
    - Traitement d'images et extraction de features
    - Classification automatique (authentique/contrefait)
    - Temps de traitement < 2 secondes
    
    **Impact**  
    - Accuracy 94%
    - Automatisation complète du contrôle
    - Réduction risques financiers
    
    **Stack**  
    `Python` • `OpenCV` • `TensorFlow` • `Keras`
    """)

with st.expander("🔍 Détails — Administration Oracle"):
    st.markdown("""
    **Contexte**  
    Bases de données critiques nécessitant performance et sécurité maximales.
    
    **Réalisations**  
    - Upgrade Oracle Express 18.1
    - Optimisation requêtes complexes (-40% temps)
    - Sécurisation des accès et audit
    - Développement fonctionnalités métier
    
    **Impact**  
    - Performance améliorée
    - Stabilité garantie
    - Sécurité renforcée
    
    **Stack**  
    `Oracle Express` • `SQL` • `PL/SQL`
    """)

st.markdown("---")

# === 6. ACTE V — LA DATA DANS LE PRODUIT FINAL ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        💻 Le produit final
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        La data ne vit pas seule. Elle alimente des applications réelles.
    </p>
""", unsafe_allow_html=True)

st.markdown(create_info_card(
    "Système de Réservation — API Amadeus",
    {
        "Type": "Application full-stack",
        "Intégration": "API externe temps réel",
        "Valeur": "Produit complet livré"
    },
    "✈️",
    "primary"
), unsafe_allow_html=True)

with st.expander("🔍 Détails — Système de Réservation"):
    st.markdown("""
    **Objectif**  
    Développer un système de réservation complet connecté à l'API Amadeus.
    
    **Réalisations**  
    - **Back-end** : Gestion réservations, traitement API, logique métier
    - **Front-end** : Interface utilisateur intuitive et responsive
    - **Sécurité** : Flux sécurisés, gestion sessions, protection données
    - **Reporting** : Génération automatique rapports de suivi
    
    **Valeur**  
    - Produit livré de bout en bout
    - Intégration API externe maîtrisée
    - Automatisation complète du workflow
    
    **Stack**  
    `PHP` • `HTML/CSS` • `JavaScript` • `API Amadeus` • `MySQL`
    """)

st.markdown("---")

# === 7. CTA — CONVERSION ===
st.markdown("""
<div style="text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, rgba(99, 102, 241, 0.05) 0%, rgba(168, 85, 247, 0.05) 100%); border-radius: 20px;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 1rem;">
        Prêt à passer à l'action ?
    </h2>
    <p style="font-size: 1.3rem; color: #6b7280; margin-bottom: 2.5rem; max-width: 700px; margin-left: auto; margin-right: auto;">
        Je construis des systèmes data qui aident à décider.
    </p>
    <a href="tel:+221771479009" style="display: inline-block; background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white; padding: 1rem 3rem; border-radius: 50px; font-size: 1.2rem; font-weight: 600; text-decoration: none; box-shadow: 0 8px 20px rgba(99, 102, 241, 0.4); transition: transform 0.3s ease;">
        📞 Discutons de votre projet
    </a>
""", unsafe_allow_html=True)
