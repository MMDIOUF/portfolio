def create_badge(text, badge_type="info"):
    """
    Crée un badge coloré
    
    Args:
        text: Texte du badge
        badge_type: success, warning, danger, info
    """
    return f'<span class="badge badge-{badge_type}">{text}</span>'
