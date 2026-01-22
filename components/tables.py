def create_styled_table(df, max_rows=10):
    """
    Crée un tableau HTML stylisé à partir d'un DataFrame
    
    Args:
        df: DataFrame pandas
        max_rows: Nombre maximum de lignes à afficher
    """
    df_display = df.head(max_rows)
    
    # Créer l'en-tête
    headers = "".join([f"<th>{col}</th>" for col in df_display.columns])
    
    # Créer les lignes
    rows = ""
    for _, row in df_display.iterrows():
        cells = "".join([f"<td>{val}</td>" for val in row])
        rows += f"<tr>{cells}</tr>\n"
    
    html = f"""
    <table class="styled-table">
        <thead>
            <tr>{headers}</tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
    """
    return html
