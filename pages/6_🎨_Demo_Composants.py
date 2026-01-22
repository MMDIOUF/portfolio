import streamlit as st
import pandas as pd
from components.design_system import inject_custom_css
from components.cards import create_info_card, create_metric_card
from components.alerts import create_alert
from components.badges import create_badge
from components.tables import create_styled_table
from components.gauges import create_gauge

st.set_page_config(page_title="Démo Composants", layout="wide")
inject_custom_css()

st.title("🎨 Démonstration des Composants")
st.markdown("Testez tous les composants du design system")

st.markdown("---")

# Métriques KPI
st.subheader("📊 Cartes Métriques KPI")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(create_metric_card("1,234", "Utilisateurs", "👥", "success"), unsafe_allow_html=True)

with col2:
    st.markdown(create_metric_card("€45K", "Revenus", "💰", "default"), unsafe_allow_html=True)

with col3:
    st.markdown(create_metric_card("87%", "Satisfaction", "⭐", "warning"), unsafe_allow_html=True)

with col4:
    st.markdown(create_metric_card("23", "Alertes", "🚨", "danger"), unsafe_allow_html=True)

st.markdown("---")

# Cartes d'information
st.subheader("📋 Cartes d'Information")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(create_info_card(
        "Carte Primary",
        {
            "Info 1": "Valeur 1",
            "Info 2": "Valeur 2",
            "Info 3": "Valeur 3"
        },
        "📊",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Carte Success",
        {
            "Statut": create_badge("Actif", "success"),
            "Performance": "95%",
            "Uptime": "99.9%"
        },
        "✅",
        "success"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(create_info_card(
        "Carte Warning",
        {
            "Attention": "Vérification requise",
            "Niveau": create_badge("Moyen", "warning"),
            "Action": "À traiter"
        },
        "⚠️",
        "warning"
    ), unsafe_allow_html=True)

st.markdown("---")

# Alertes
st.subheader("🔔 Messages d'Alerte")
st.markdown(create_alert("Opération réussie avec succès!", "success"), unsafe_allow_html=True)
st.markdown(create_alert("Attention: Vérifiez les données avant de continuer", "warning"), unsafe_allow_html=True)
st.markdown(create_alert("Erreur critique détectée dans le système", "danger"), unsafe_allow_html=True)
st.markdown(create_alert("Information: Nouvelle mise à jour disponible", "info"), unsafe_allow_html=True)

st.markdown("---")

# Badges
st.subheader("🏷️ Badges de Statut")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"**Success:** {create_badge('Actif', 'success')}", unsafe_allow_html=True)
    st.markdown(f"**Success:** {create_badge('Validé', 'success')}", unsafe_allow_html=True)

with col2:
    st.markdown(f"**Warning:** {create_badge('En attente', 'warning')}", unsafe_allow_html=True)
    st.markdown(f"**Warning:** {create_badge('À vérifier', 'warning')}", unsafe_allow_html=True)

with col3:
    st.markdown(f"**Danger:** {create_badge('Erreur', 'danger')}", unsafe_allow_html=True)
    st.markdown(f"**Danger:** {create_badge('Critique', 'danger')}", unsafe_allow_html=True)

with col4:
    st.markdown(f"**Info:** {create_badge('Information', 'info')}", unsafe_allow_html=True)
    st.markdown(f"**Info:** {create_badge('Nouveau', 'info')}", unsafe_allow_html=True)

st.markdown("---")

# Jauges
st.subheader("📊 Jauges Interactives")
col1, col2, col3 = st.columns(3)

with col1:
    fig = create_gauge(35, "Performance Faible", unit="%")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = create_gauge(65, "Performance Moyenne", unit="%")
    st.plotly_chart(fig, use_container_width=True)

with col3:
    fig = create_gauge(92, "Performance Élevée", unit="%")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Tableaux
st.subheader("📋 Tableaux Stylisés")

df = pd.DataFrame({
    'Nom': ['Alice Martin', 'Bob Dupont', 'Charlie Durand', 'Diana Lefebvre', 'Eric Moreau'],
    'Département': ['Data', 'BI', 'Dev', 'Data', 'BI'],
    'Score': [95, 87, 92, 88, 91],
    'Statut': [
        create_badge('Actif', 'success'),
        create_badge('Actif', 'success'),
        create_badge('En congé', 'warning'),
        create_badge('Actif', 'success'),
        create_badge('Inactif', 'danger')
    ]
})

st.markdown(create_styled_table(df), unsafe_allow_html=True)

st.markdown("---")

# Expanders
st.subheader("📂 Sections Extensibles")

with st.expander("🔍 Section 1 - Cliquez pour développer", expanded=True):
    st.markdown("""
    ### Contenu de la Section 1
    
    Ceci est un exemple de contenu dans une section extensible.
    
    - Point 1
    - Point 2
    - Point 3
    
    Vous pouvez y mettre n'importe quel contenu Streamlit !
    """)

with st.expander("📊 Section 2 - Avec graphique"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(create_info_card(
            "Informations",
            {
                "Métrique 1": "100",
                "Métrique 2": "200",
                "Total": "300"
            },
            "📈",
            "primary"
        ), unsafe_allow_html=True)
    
    with col2:
        fig = create_gauge(78, "Progression", unit="%")
        st.plotly_chart(fig, use_container_width=True)

with st.expander("⚙️ Section 3 - Avec tableau"):
    df_mini = pd.DataFrame({
        'Produit': ['A', 'B', 'C'],
        'Ventes': [100, 150, 120],
        'Statut': [
            create_badge('Stock OK', 'success'),
            create_badge('Stock bas', 'warning'),
            create_badge('Rupture', 'danger')
        ]
    })
    st.markdown(create_styled_table(df_mini), unsafe_allow_html=True)

st.markdown("---")

# Layout en colonnes
st.subheader("📐 Layouts en Colonnes")

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.markdown("""
    ### Colonne Large (2/4)
    Cette colonne prend 2 parts sur 4 au total.
    Idéal pour du contenu principal.
    """)
    st.markdown(create_alert("Contenu principal ici", "info"), unsafe_allow_html=True)

with col2:
    st.markdown("""
    ### Col 2 (1/4)
    Colonne étroite
    """)
    st.markdown(create_metric_card("42", "Valeur", "📊", "success"), unsafe_allow_html=True)

with col3:
    st.markdown("""
    ### Col 3 (1/4)
    Colonne étroite
    """)
    st.markdown(create_metric_card("87%", "Taux", "📈", "warning"), unsafe_allow_html=True)

st.markdown("---")

# Code examples
st.subheader("💻 Exemples de Code")

with st.expander("📝 Code pour créer une carte métrique"):
    st.code("""
from components.cards import create_metric_card

st.markdown(create_metric_card(
    "1,234",      # Valeur
    "Utilisateurs",  # Label
    "👥",         # Icône
    "success"     # Gradient: default, success, warning, danger
), unsafe_allow_html=True)
    """, language="python")

with st.expander("📝 Code pour créer une alerte"):
    st.code("""
from components.alerts import create_alert

st.markdown(create_alert(
    "Message d'alerte",
    "success",  # Type: success, warning, danger, info
    "✅"        # Icône optionnelle
), unsafe_allow_html=True)
    """, language="python")

with st.expander("📝 Code pour créer une jauge"):
    st.code("""
from components.gauges import create_gauge

fig = create_gauge(
    75,           # Valeur
    "Performance", # Titre
    unit="%"      # Unité
)
st.plotly_chart(fig, use_container_width=True)
    """, language="python")

st.markdown("---")

st.success("✅ Tous les composants sont fonctionnels ! Utilisez-les dans vos pages.")
