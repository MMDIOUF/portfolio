def create_alert(message, alert_type="info", icon=None):
    """
    Crée un message d'alerte stylisé
    
    Args:
        message: Texte du message
        alert_type: success, warning, danger, info
        icon: Emoji optionnel
    """
    icons = {
        "success": "✅",
        "warning": "⚠️",
        "danger": "🚨",
        "info": "ℹ️"
    }
    
    display_icon = icon or icons.get(alert_type, "")
    
    html = f"""
    <div class="alert alert-{alert_type}">
        <strong>{display_icon} {message}</strong>
    </div>
    """
    return html
