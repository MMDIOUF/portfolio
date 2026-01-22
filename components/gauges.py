import plotly.graph_objects as go

def create_gauge(value, title, min_val=0, max_val=100, thresholds=None, unit="%"):
    """
    Crée une jauge interactive
    
    Args:
        value: Valeur actuelle
        title: Titre de la jauge
        min_val: Valeur minimale
        max_val: Valeur maximale
        thresholds: Liste de tuples [(seuil, couleur), ...]
        unit: Unité d'affichage
    """
    if thresholds is None:
        thresholds = [
            (max_val * 0.4, "lightgreen"),
            (max_val * 0.75, "orange"),
            (max_val, "red")
        ]
    
    # Déterminer la couleur de la barre
    bar_color = "green"
    for threshold, color in thresholds:
        if value > threshold:
            bar_color = color
    
    # Créer les steps
    steps = []
    prev_threshold = min_val
    for threshold, color in thresholds:
        steps.append({
            'range': [prev_threshold, threshold],
            'color': color
        })
        prev_threshold = threshold
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': f"{title}: {value}{unit}", 'font': {'size': 20}},
        gauge={
            'axis': {'range': [min_val, max_val]},
            'bar': {'color': bar_color},
            'steps': steps,
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': max_val * 0.8
            }
        }
    ))
    
    fig.update_layout(height=300)
    return fig
