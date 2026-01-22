import streamlit as st
from components.design_system import inject_custom_css
from components.cards import create_info_card
from components.alerts import create_alert
from components.badges import create_badge
from components.gauges import create_gauge

st.set_page_config(page_title="Dashboard CRM", layout="wide")
inject_custom_css()

st.title("👥 Dashboard CRM")

# Recherche Client
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    search_type = st.radio("Rechercher par:", ["ID Client", "Nom", "Email"], horizontal=True)
    search_value = st.text_input(f"Entrez {search_type}")

if search_value:
    # Informations Client
    st.subheader("Profil Client")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(create_info_card(
            "Informations Personnelles",
            {
                "Nom": "Jean Dupont",
                "Email": "jean@example.com",
                "Téléphone": "+33 6 12 34 56 78",
                "Statut": create_badge("Premium", "success")
            },
            "👤",
            "primary"
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_info_card(
            "Activité",
            {
                "Dernière connexion": "Il y a 2 heures",
                "Commandes": "47",
                "Valeur totale": "€12,450",
                "Satisfaction": "⭐⭐⭐⭐⭐"
            },
            "📊",
            "info"
        ), unsafe_allow_html=True)
    
    # Score Client
    st.subheader("Score de Fidélité")
    fig = create_gauge(85, "Score Client", thresholds=[
        (50, "lightgreen"),
        (75, "orange"),
        (100, "red")
    ])
    st.plotly_chart(fig, use_container_width=True)
    
    # Recommandations
    st.subheader("Actions Recommandées")
    st.markdown(create_alert("Client à forte valeur - Proposer une offre premium", "success", "💎"), 
                unsafe_allow_html=True)
