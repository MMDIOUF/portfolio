# 💻 Exemples de Code Réutilisables

Collection de snippets prêts à l'emploi pour votre portfolio.

---

## 📊 Cartes et Métriques

### Carte Métrique Simple

```python
from components.cards import create_metric_card

st.markdown(create_metric_card(
    "1,234",           # Valeur
    "Utilisateurs",    # Label
    "👥",              # Icône
    "success"          # Gradient: default, success, warning, danger
), unsafe_allow_html=True)
```

### Carte d'Information

```python
from components.cards import create_info_card
from components.badges import create_badge

st.markdown(create_i