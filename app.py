import streamlit as st
from components.design_system import inject_custom_css
from components.cards import create_info_card, create_metric_card
from components.alerts import create_alert
from components.badges import create_badge

# Configuration de la page
st.set_page_config(
    page_title="MOUHAMADOU MAKHTAR DIOUF - Data Analyst",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🏠"
)

# Injection du CSS personnalisé
inject_custom_css()

# === ACTE I — LE PROBLÈME (HOOK IMMÉDIAT) ===
st.markdown("""
<div style="min-height: 60vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 4rem 2rem;">
    <h1 style="font-size: 3.5rem; font-weight: 800; color: #1f2937; margin-bottom: 2rem; line-height: 1.2;">
        Les organisations collectent des données.<br/>
        <span style="background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Peu savent réellement les exploiter.
        </span>
    </h1>
    <p style="font-size: 1.4rem; color: #6b7280; max-width: 800px; line-height: 1.8;">
        Entre fichiers dispersés, traitements manuels et décisions tardives, 
        <strong>la donnée devient un frein au lieu d'un levier.</strong>
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# === ACTE II — LA PROMESSE (POSITIONNEMENT) ===
st.markdown("""
<div style="text-align: center; padding: 3rem 2rem; background: linear-gradient(135deg, rgba(99, 102, 241, 0.05) 0%, rgba(168, 85, 247, 0.05) 100%); border-radius: 20px; margin: 2rem 0;">
    <h2 style="font-size: 2.5rem; font-weight: 700; color: #1f2937; margin-bottom: 2rem;">
        La Solution
    </h2>
    <p style="font-size: 1.3rem; color: #374151; max-width: 900px; margin: 0 auto; line-height: 1.8;">
        Je conçois des <strong>systèmes data</strong> qui transforment des <strong>données complexes en outils simples</strong>, 
        des <strong>indicateurs flous en décisions claires</strong>, et des <strong>processus manuels en chaînes automatisées</strong>.
    </p>
    <div style="margin-top: 2rem;">
        <h3 style="font-size: 1.8rem; font-weight: 600; background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            MOUHAMADOU MAKHTAR DIOUF
        </h3>
        <p style="font-size: 1.2rem; color: #6b7280; margin-top: 0.5rem;">
            Data Analyst | Business Intelligence | Process Automation
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <p style="font-size: 1.1rem; color: #6b7280;">
            📞 +221 77 147 90 09 | 📍 Dakar, Sénégal
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# === ACTE III — L'HOMME DERRIÈRE LA MÉTHODE ===
st.markdown("""
<div style="padding: 3rem 2rem; max-width: 1000px; margin: 0 auto;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 2rem; text-align: center;">
        👤 L'Homme Derrière la Méthode
    </h2>
    <p style="font-size: 1.2rem; color: #374151; line-height: 1.9; text-align: center; max-width: 800px; margin: 0 auto;">
        <strong>Data Analyst orienté impact opérationnel.</strong> Mon approche est pragmatique : 
        <span style="color: #6366f1; font-weight: 600;">une donnée n'a de valeur que si elle est comprise, fiable et utilisée.</span>
    </p>
    <p style="font-size: 1.2rem; color: #374151; line-height: 1.9; text-align: center; margin-top: 1.5rem;">
        J'interviens sur toute la chaîne data : 
        <strong>Nettoyage → structuration → analyse → visualisation → automatisation</strong>
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# === ACTE IV — LA PREUVE PAR L'IMPACT (IPSOS) ===
st.markdown("""
<div style="padding: 3rem 2rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 1rem; text-align: center;">
        📊 Le Réel Avant la Théorie
    </h2>
    <p style="font-size: 1.1rem; color: #6b7280; text-align: center; margin-bottom: 3rem;">
        La preuve par l'impact
    </p>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 3rem; border-radius: 20px; color: white; margin-bottom: 2rem;">
        <h3 style="font-size: 2rem; font-weight: 700; margin-bottom: 1rem;">
            🏢 IPSOS Sénégal — Business Intelligence & Automatisation
        </h3>
        <p style="font-size: 1.2rem; opacity: 0.95; margin-bottom: 2rem;">
            Dans un environnement d'études terrain et téléphoniques, les décisions doivent être <strong>rapides, fiables et traçables.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 16px; border-left: 5px solid #6366f1; box-shadow: 0 4px 12px rgba(0,0,0,0.1); height: 100%;">
            <h4 style="color: #6366f1; font-size: 1.5rem; margin-bottom: 1.5rem;">⚙️ Ce que j'ai fait</h4>
            <ul style="font-size: 1.1rem; color: #374151; line-height: 2;">
                <li>Conçu des <strong>dashboards décisionnels</strong> </li>
                <li>Automatisé la <strong>codification</strong> des données</li>
                <li>Fiabilisé les <strong>KPIs</strong> métier</li>
                <li>Réduit drastiquement les <strong>traitements manuels</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: white; padding: 2rem; border-radius: 16px; border-left: 5px solid #10b981; box-shadow: 0 4px 12px rgba(0,0,0,0.1); height: 100%;">
            <h4 style="color: #10b981; font-size: 1.5rem; margin-bottom: 1.5rem;">✅ Résultat</h4>
            <p style="font-size: 1.3rem; color: #374151; line-height: 1.8; font-weight: 600;">
                Les managers décident avec des <span style="color: #10b981;">chiffres fiables</span>.
            </p>
            <div style="margin-top: 2rem; padding: 1rem; background: #d1fae5; border-radius: 10px;">
                <p style="color: #065f46; font-weight: 600; margin: 0;">
                    💡 Impact : Décisions plus rapides, erreurs réduites.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# === ACTE V — IMPACT MESURABLE ===
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 3rem;">
        📈 Impact Mesurable
    </h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(create_metric_card("1+", "Années d'expérience", "⏱️", "success"), unsafe_allow_html=True)

with col2:
    st.markdown(create_metric_card("10+", "Projets Data", "🚀", "default"), unsafe_allow_html=True)

with col3:
    st.markdown(create_metric_card("70%", "Réduction erreurs", "✅", "success"), unsafe_allow_html=True)


st.markdown("---")

# === ACTE X — LA CONCLUSION (CONVERSION) ===
st.markdown("""
<div style="background: linear-gradient(135deg, #1f2937 0%, #111827 100%); padding: 4rem 2rem; border-radius: 20px; text-align: center; color: white; margin: 3rem 0;">
    <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 1.5rem;">
        Je ne construis pas des analyses.<br/>
        <span style="background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Je construis des outils de décision.
        </span>
    </h2>
    <p style="font-size: 1.3rem; opacity: 0.9; margin-bottom: 2rem;">
        Disponible immediatement <strong>Data Analysis, BI et Automatisation</strong>
    </p>
    <div style="margin-top: 2rem;">
        <a href="tel:+221771479009" style="display: inline-block; background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white; padding: 1rem 3rem; border-radius: 50px; font-size: 1.2rem; font-weight: 600; text-decoration: none; margin: 0.5rem; box-shadow: 0 8px 20px rgba(99, 102, 241, 0.4); transition: transform 0.3s ease;">
            📞 Me Contacter
        </a>
    </div>
    <p style="font-size: 1rem; opacity: 0.7; margin-top: 2rem;">
        📞 +221 77 147 90 09 | Dakar, Sénégal
    </p>
</div>
""", unsafe_allow_html=True)
