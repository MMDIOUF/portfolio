import streamlit as st
import pandas as pd
import plotly.express as px
from components.design_system import inject_custom_css
from components.cards import create_metric_card
from components.tables import create_styled_table

st.set_page_config(page_title="Dashboard Analytique", layout="wide")
inject_custom_css()

st.title("📊 Dashboard Analytique")

# Section KPI
st.subheader("Indicateurs Clés")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(create_metric_card("1,234", "Utilisateurs", "👥", "success"), unsafe_allow_html=True)

with col2:
    st.markdown(create_metric_card("€45K", "Revenus", "💰", "default"), unsafe_allow_html=True)

with col3:
    st.markdown(create_metric_card("87%", "Satisfaction", "⭐", "warning"), unsafe_allow_html=True)

with col4:
    st.markdown(create_metric_card("23", "Alertes", "🚨", "danger"), unsafe_allow_html=True)

# Section Graphiques
st.subheader("Analyses")
col1, col2 = st.columns(2)

with col1:
    df = pd.DataFrame({
        'Mois': ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin'],
        'Ventes': [100, 150, 120, 180, 200, 170]
    })
    fig = px.line(df, x='Mois', y='Ventes', title="Évolution des Ventes")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.pie(values=[30, 40, 30], names=['Produit A', 'Produit B', 'Produit C'], 
                 title="Répartition des Ventes")
    st.plotly_chart(fig, use_container_width=True)

# Section Tableau
st.subheader("Données Détaillées")
df_table = pd.DataFrame({
    'Produit': ['Produit A', 'Produit B', 'Produit C', 'Produit D'],
    'Ventes': [1200, 980, 750, 1100],
    'Revenus': ['€24K', '€19.6K', '€15K', '€22K'],
    'Croissance': ['+12%', '+8%', '-3%', '+15%']
})
st.markdown(create_styled_table(df_table), unsafe_allow_html=True)
