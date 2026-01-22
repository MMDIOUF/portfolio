import streamlit as st
from components.design_system import inject_custom_css
from components.cards import create_info_card
from components.badges import create_badge

st.set_page_config(page_title="Expertise Technique", layout="wide")
inject_custom_css()

# === HERO ===
st.markdown("""
<div style="text-align: center; padding: 5rem 2rem 4rem;">
    <h1 style="font-size: 3.2rem; font-weight: 800; color: #1f2937; margin-bottom: 1.5rem;">
        ⚡ Mon Expertise
    </h1>
    <p style="font-size: 1.4rem; color: #6b7280; max-width: 820px; margin: 0 auto; line-height: 1.6;">
        La maîtrise technique<br/>
        <strong>au service de l'impact business.</strong>
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# === DATA ANALYSIS & BI ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        📊 Data Analysis & Business Intelligence
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Transformer les données en décisions concrètes.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Visualisation & Dashboards",
        {
            "Streamlit": "Création de dashboards interactifs",
            "Plotly": "Visualisations interactives",
            "Seaborn": "Exploration graphique",
            "Excel": "Reporting et KPIs dynamiques"
        },
        "📊",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Analyse de Données",
        {
            "Python (Pandas)": "Préparation et analyse de données",
            "NumPy": "Calculs et statistiques",
            "SQL": "Extraction et transformation de données",
            "Statistiques": "Tests et analyses pour décisions métier"
        },
        "🔍",
        "info"
    ), unsafe_allow_html=True)

with st.expander("🔍 Détails — Data Analysis & BI"):
    st.markdown("""
    **Réalisations**
    - Dashboards interactifs pour suivi performance
    - Automatisation processus reporting
    - Analyse exploratoire et segmentation clients
    - KPIs dynamiques et visualisations parlantes
    """)

st.markdown("---")

# === DATA ENGINEERING ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        ⚙️ Data Engineering & Automatisation
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Construire des pipelines fiables et scalables.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "ETL & Pipelines",
        {
            "Python": "Automatisation ETL",
            "Apache NiFi": "Orchestration workflows",
            "Talend": "Intégration de données",
            "SQL": "Extraction et transformation"
        },
        "🔄",
        "success"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Big Data",
        {
            "Hadoop": "Traitement données massives",
            "Hive": "Analyse distribuée",
            "PySpark": "Data processing scalable",
            "Kafka": "Streaming et ingestion temps réel"
        },
        "📦",
        "warning"
    ), unsafe_allow_html=True)

with st.expander("🔍 Détails — Data Engineering"):
    st.markdown("""
    **Réalisations**
    - Pipelines multi-cloud (AWS + GCP)
    - Orchestration ETL et workflows complexes
    - Data quality management
    - Optimisation des performances
    """)

st.markdown("---")

# === MACHINE LEARNING ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        🤖 Machine Learning & IA
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Prédire pour mieux décider.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Frameworks ML",
        {
            "Scikit-Learn": "Modèles prédictifs",
            "TensorFlow/Keras": "Deep learning et vision",
            "XGBoost": "Classification et régression",
            "OpenCV": "Traitement d'images"
        },
        "🤖",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Techniques ML",
        {
            "Classification": "Prédire le comportement",
            "Régression": "Prévision quantitative",
            "Clustering": "Segmentation clients",
            "Deep Learning": "Détection d'anomalies"
        },
        "🎯",
        "info"
    ), unsafe_allow_html=True)

with st.expander("🔍 Détails — Machine Learning"):
    st.markdown("""
    **Projets réalisés**
    - Prédiction churn, souscription assurance, prévision salaires
    - Détection de faux billets
    - Segmentation clients et scoring
    """)

st.markdown("---")

# === WEB & DATABASES ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        🌐 Web Development & Databases
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Du front-end au back-end, de bout en bout.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Développement Web",
        {
            "Streamlit": "Applications data interactives",
            "PHP": "Back-end et APIs",
            "HTML/CSS": "Interfaces utilisateur",
            "JavaScript": "Interactivité front-end"
        },
        "🌐",
        "success"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Bases de Données",
        {
            "SQL Server": "Administration et optimisation",
            "Oracle": "Bases critiques",
            "MySQL": "Applications web",
            "BigQuery": "Data warehouse cloud"
        },
        "🗄️",
        "warning"
    ), unsafe_allow_html=True)

with st.expander("🔍 Détails — Web & Databases"):
    st.markdown("""
    **Réalisations**
    - Système réservation API Amadeus
    - Applications web data-driven
    - Dashboards interactifs Streamlit
    - Administration bases critiques
    """)

st.markdown("---")

# === CLOUD & DEVOPS ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        ☁️ Cloud & DevOps
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Infrastructure scalable et sécurisée.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Cloud Platforms",
        {
            "AWS": "S3, Lambda, IAM",
            "GCP": "BigQuery, Cloud Storage",
            "Azure": "Services cloud"
        },
        "☁️",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Outils & Pratiques",
        {
            "Git/GitHub": "Version control et collaboration",
            "Docker": "Conteneurisation",
            "CI/CD": "Automatisation déploiement",
            "Monitoring": "Suivi et alerting"
        },
        "🛠️",
        "info"
    ), unsafe_allow_html=True)

with st.expander("🔍 Détails — Cloud & DevOps"):
    st.markdown("""
    **Services utilisés**
    - AWS : S3, Lambda, IAM, Secrets Manager
    - GCP : BigQuery, Cloud Storage, Cloud Functions
    - Pratiques : Version control, code review, documentation
    """)

st.markdown("---")

# === SOFT SKILLS ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        🎯 Compétences Transversales
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        La technique ne suffit pas. L'humain fait la différence.
    </p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(create_info_card(
        "Communication",
        {
            "Présentation": "Vulgarisation résultats",
            "Documentation": "Clarté et précision",
            "Équipe": "Collaboration efficace"
        },
        "💬",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Gestion de Projet",
        {
            "Planification": "Organisation méthodique",
            "Priorisation": "Focus sur l'essentiel",
            "Autonomie": "Prise d'initiative"
        },
        "📋",
        "success"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(create_info_card(
        "Mindset",
        {
            "Résolution": "Approche pragmatique",
            "Apprentissage": "Curiosité continue",
            "Adaptabilité": "Flexibilité"
        },
        "🧠",
        "info"
    ), unsafe_allow_html=True)

st.markdown("---")

# === FORMATION ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        🎓 Formation & Certifications
    </h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🎓 Diplômes
    - **Master Data Science & IA** - ISI Dakar (2024-2026)
    - **Master Big Data** - ISM Dakar (2023-2024)
    - **Licence Génie Logiciel** - ISM Dakar (2020-2023)
    """)

with col2:
    st.markdown("""
    ### 📚 Formations Continues
    - Power BI Advanced Analytics
    - AWS Cloud Practitioner
    - Machine Learning Specialization
    - Big Data Engineering
    """)

st.markdown("---")



# === CTA ===
st.markdown("""
<div style="text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, rgba(99, 102, 241, 0.05) 0%, rgba(168, 85, 247, 0.05) 100%); border-radius: 20px;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 1rem;">
        À la recherche de nouvelles opportunités
    </h2>
    <p style="font-size: 1.3rem; color: #6b7280; margin-bottom: 2.5rem; max-width: 700px; margin-left: auto; margin-right: auto; line-height: 1.5;">
        Je souhaite mettre en pratique mes connaissances, apprendre de nouvelles compétences, relever de nouveaux défis et participer activement à des projets data stimulants au sein d’entreprises innovantes.
    </p>
    <a href="tel:+221771479009" style="display: inline-block; background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white; padding: 1rem 3rem; border-radius: 50px; font-size: 1.2rem; font-weight: 600; text-decoration: none; box-shadow: 0 8px 20px rgba(99, 102, 241, 0.4); transition: transform 0.3s ease;">
        📞 Me Contacter
    </a>
</div>
""", unsafe_allow_html=True)
