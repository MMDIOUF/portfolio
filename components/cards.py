def create_info_card(title, data_dict, icon="📊", color="primary"):
    """
    Crée une carte d'information stylisée
    
    Args:
        title: Titre de la carte
        data_dict: Dictionnaire {label: value}
        icon: Emoji ou icône
        color: primary, success, warning, danger, info
    """
    items_html = ""
    for label, value in data_dict.items():
        items_html += f"<p><strong>{label}:</strong> {value}</p>\n"
    
    html = f"""
    <div class="box box-{color}">
        <h3>{icon} {title}</h3>
        {items_html}
    """
    return html


def create_metric_card(value, label, icon="📈", gradient="default"):
    """
    Crée une carte métrique avec gradient
    
    Args:
        value: Valeur principale (nombre ou texte)
        label: Label descriptif
        icon: Emoji ou icône
        gradient: default, success, warning, danger
    """
    gradients = {
        "default": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "success": "linear-gradient(135deg, #11998e 0%, #38ef7d 100%)",
        "warning": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
        "danger": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)"
    }
    
    html = f"""
    <div style="text-align: center; padding: 30px; border-radius: 12px; 
                background: {gradients[gradient]}; color: white; 
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);">
        <div style="font-size: 1.2em; opacity: 0.9;">{icon} {label}
        <div style="font-size: 3em; font-weight: bold; margin: 10px 0;">{value}
    """
    return html
