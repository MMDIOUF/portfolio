import streamlit as st

def inject_custom_css():
    """Injecte le CSS personnalisé pour le design system"""
    st.markdown("""
    <style>
    /* === SCROLLYTELLING - ANIMATIONS GLOBALES === */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
    
    /* Appliquer scrollytelling aux sections principales */
    .stMarkdown, .stMetric, .element-container {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* === SIDEBAR GLASS MORPHISM DESIGN === */
    section[data-testid="stSidebar"] {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(168, 85, 247, 0.1) 100%) !important;
        backdrop-filter: blur(10px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.2) !important;
        box-shadow: 4px 0 24px rgba(0, 0, 0, 0.1) !important;
    }
    
    /* Sidebar header styling */
    section[data-testid="stSidebar"] > div:first-child {
        background: transparent !important;
        padding-top: 2rem !important;
    }
    
    /* Navigation items */
    [data-testid="stSidebarNav"] {
        background: transparent !important;
        padding: 1rem 0.5rem !important;
    }
    
    [data-testid="stSidebarNav"] ul {
        padding: 0 !important;
        gap: 8px !important;
    }
    
    [data-testid="stSidebarNav"] li {
        margin-bottom: 8px !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        animation: slideInLeft 0.5s ease-out !important;
    }
    
    [data-testid="stSidebarNav"] li:nth-child(1) { animation-delay: 0.1s !important; }
    [data-testid="stSidebarNav"] li:nth-child(2) { animation-delay: 0.2s !important; }
    [data-testid="stSidebarNav"] li:nth-child(3) { animation-delay: 0.3s !important; }
    [data-testid="stSidebarNav"] li:nth-child(4) { animation-delay: 0.4s !important; }
    
    [data-testid="stSidebarNav"] a {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 14px !important;
        padding: 18px 20px !important;
        color: #1f2937 !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        letter-spacing: 0.3px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(5px) !important;
        display: flex !important;
        align-items: center !important;
        gap: 14px !important;
        min-height: 56px !important;
    }
    
    [data-testid="stSidebarNav"] a:hover {
        background: rgba(99, 102, 241, 0.15) !important;
        border-color: rgba(99, 102, 241, 0.3) !important;
        transform: translateX(8px) scale(1.02) !important;
        box-shadow: 0 8px 16px rgba(99, 102, 241, 0.2) !important;
    }
    
    /* Active page styling */
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
        color: white !important;
        border-color: transparent !important;
        box-shadow: 0 8px 20px rgba(99, 102, 241, 0.4) !important;
        font-weight: 600 !important;
    }
    
    /* Icon styling in sidebar */
    [data-testid="stSidebarNav"] a span {
        font-size: 1.5em !important;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1)) !important;
        min-width: 28px !important;
        display: inline-block !important;
    }
    
    /* Sidebar title/logo area */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #1f2937 !important;
        font-weight: 700 !important;
        text-align: center !important;
        padding: 1rem 0 !important;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    
    /* Masquer complètement tout le texte original des labels IMMÉDIATEMENT */
    span[label] {
        font-size: 0 !important;
        color: transparent !important;
        visibility: hidden !important;
    }
    
    /* Ajouter emoji et texte propre pour chaque page */
    span[label]::before {
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        color: #1f2937 !important;
        display: inline-flex !important;
        align-items: center !important;
        visibility: visible !important;
    }
    
    /* Labels personnalisés pour chaque page */
    span[label="app"]::before {
        content: "🏠 Accueil";
    }
    
    span[label="Portfolio"]::before {
        content: "🎯 Portfolio";
    }
    
    span[label="Expertise"]::before {
        content: "⚡ Expertise";
    }
    
    /* Masquer aussi le texte dans les liens de navigation pendant le chargement */
    [data-testid="stSidebarNav"] a {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 14px !important;
        padding: 18px 20px !important;
        color: transparent !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        letter-spacing: 0.3px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(5px) !important;
        display: flex !important;
        align-items: center !important;
        gap: 14px !important;
        min-height: 56px !important;
    }
    
    /* Rendre visible uniquement le contenu ::before */
    [data-testid="stSidebarNav"] a span[label]::before {
        color: #1f2937 !important;
    }
    
    /* Masquer les pages indésirables */
    a[href*="Demo_Composants"],
    a[href*="Dashboard_Analytique"],
    a[href*="CRM"],
    a[href*="Monitoring"] {
        display: none !important;
    }
    
    /* === CONTENEURS === */
    .container-row {
        display: flex;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 30px;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .container-full {
        margin-bottom: 40px;
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* === CARTES (BOXES) === */
    .box {
        padding: 20px;
        border-radius: 16px;
        flex: 1;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        border-left: 5px solid #007bff;
        background-color: #ffffff;
        animation: fadeInUp 0.6s ease-out;
    }
    
    .box:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        animation: pulse 2s infinite;
    }
    
    .box h3 {
        text-align: center;
        font-size: 1.6em;
        margin-bottom: 20px;
        color: #333;
    }
    
    /* === VARIANTES DE COULEURS === */
    .box-primary { border-left-color: #007bff; }
    .box-success { border-left-color: #28a745; }
    .box-warning { border-left-color: #ffc107; }
    .box-danger { border-left-color: #dc3545; }
    .box-info { border-left-color: #17a2b8; }
    
    /* === MESSAGES D'ALERTE === */
    .alert {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        animation: fadeInUp 0.7s ease-out;
    }
    
    .alert-success {
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        color: #155724;
    }
    
    .alert-warning {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        color: #856404;
    }
    
    .alert-danger {
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
        color: #721c24;
    }
    
    .alert-info {
        background-color: #d1ecf1;
        border-left: 5px solid #17a2b8;
        color: #0c5460;
    }
    
    /* === MÉTRIQUES (KPI) === */
    .metric-card {
        text-align: center;
        padding: 30px;
        border-radius: 12px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        animation: fadeInUp 0.8s ease-out;
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
    }
    
    .metric-value {
        font-size: 3em;
        font-weight: bold;
        margin: 10px 0;
    }
    
    .metric-label {
        font-size: 1.2em;
        opacity: 0.9;
    }
    
    /* === TABLEAUX === */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 0.9em;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        animation: fadeInUp 0.9s ease-out;
    }
    
    .styled-table thead tr {
        background-color: #007bff;
        color: #ffffff;
        text-align: left;
    }
    
    .styled-table th,
    .styled-table td {
        padding: 12px 15px;
    }
    
    .styled-table tbody tr {
        border-bottom: 1px solid #dddddd;
        transition: background-color 0.3s ease;
    }
    
    .styled-table tbody tr:nth-of-type(even) {
        background-color: #f3f3f3;
    }
    
    .styled-table tbody tr:hover {
        background-color: #e9ecef;
        transform: scale(1.01);
    }
    
    /* === BADGES === */
    .badge {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 12px;
        font-size: 0.85em;
        font-weight: bold;
        animation: fadeInUp 0.5s ease-out;
    }
    
    .badge-success { background-color: #28a745; color: white; }
    .badge-warning { background-color: #ffc107; color: #333; }
    .badge-danger { background-color: #dc3545; color: white; }
    .badge-info { background-color: #17a2b8; color: white; }
    
    
    /* === SCROLLYTELLING - SMOOTH SCROLL === */
    html {
        scroll-behavior: smooth;
    }
    
    /* Fade in elements on scroll */
    .stMarkdown > div,
    .stMetric,
    .stExpander {
        opacity: 0;
        animation: fadeInUp 0.8s ease-out forwards;
    }
    
    /* Stagger animations */
    .stMarkdown > div:nth-child(1) { animation-delay: 0.1s; }
    .stMarkdown > div:nth-child(2) { animation-delay: 0.2s; }
    .stMarkdown > div:nth-child(3) { animation-delay: 0.3s; }
    .stMarkdown > div:nth-child(4) { animation-delay: 0.4s; }
    
    /* === RESPONSIVE === */
    @media (max-width: 768px) {
        .container-row {
            flex-direction: column;
        }
        
        .box h3 {
            font-size: 1.3em;
        }
        
        .metric-value {
            font-size: 2em;
        }
        
        section[data-testid="stSidebar"] {
            backdrop-filter: blur(20px) !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Palettes de couleurs prédéfinies
COLOR_SCHEMES = {
    "default": {
        "primary": "#007bff",
        "success": "#28a745",
        "warning": "#ffc107",
        "danger": "#dc3545",
        "info": "#17a2b8"
    },
    "dark": {
        "primary": "#375a7f",
        "success": "#00bc8c",
        "warning": "#f39c12",
        "danger": "#e74c3c",
        "info": "#3498db"
    },
    "pastel": {
        "primary": "#a8dadc",
        "success": "#06d6a0",
        "warning": "#ffd166",
        "danger": "#ef476f",
        "info": "#118ab2"
    }
}
