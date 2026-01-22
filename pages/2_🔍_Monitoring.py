import streamlit as st
from datetime import datetime
from components.design_system import inject_custom_css
from components.cards import create_info_card
from components.alerts import create_alert
from components.badges import create_badge
from components.gauges import create_gauge

st.set_page_config(page_title="Dashboard Monitoring", layout="wide")
inject_custom_css()

st.title("🔍 Dashboard de Monitoring")

# Statut Système
st.subheader("Statut des Services")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(create_info_card(
        "Service API",
        {
            "Statut": create_badge("En ligne", "success"),
            "Uptime": "99.9%",
            "Dernière vérification": datetime.now().strftime("%H:%M:%S")
        },
        "🌐",
        "success"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Base de données",
        {
            "Statut": create_badge("En ligne", "success"),
            "Connexions": "45/100",
            "Latence": "12ms"
        },
        "💾",
        "success"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(create_info_card(
        "Cache Redis",
        {
            "Statut": create_badge("Dégradé", "warning"),
            "Mémoire": "78%",
            "Hit Rate": "85%"
        },
        "⚡",
        "warning"
    ), unsafe_allow_html=True)

# Alertes
st.subheader("Alertes Récentes")
st.markdown(create_alert("Utilisation CPU élevée sur serveur-01", "warning"), unsafe_allow_html=True)
st.markdown(create_alert("Sauvegarde complétée avec succès", "success"), unsafe_allow_html=True)

# Métriques Temps Réel
st.subheader("Métriques en Temps Réel")
col1, col2 = st.columns(2)

with col1:
    fig = create_gauge(67, "CPU Usage", unit="%")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = create_gauge(45, "Memory Usage", unit="%")
    st.plotly_chart(fig, use_container_width=True)
