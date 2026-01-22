# 🚀 Guide de Déploiement

## Déploiement sur Streamlit Cloud (Recommandé - Gratuit)

### Prérequis
- Compte GitHub
- Compte Streamlit Cloud (gratuit)

### Étapes

#### 1. Préparer le Repository GitHub

```bash
# Initialiser Git (si pas déjà fait)
git init

# Ajouter tous les fichiers
git add .

# Commit initial
git commit -m "Portfolio Data Analyst - Version initiale"

# Créer un repository sur GitHub
# Puis lier et pousser
git remote add origin https://github.com/VOTRE_USERNAME/portfolio-data-analyst.git
git branch -M main
git push -u origin main
```

#### 2. Déployer sur Streamlit Cloud

1. Allez sur [share.streamlit.io](https://share.streamlit.io)
2. Connectez-vous avec GitHub
3. Cliquez sur "New app"
4. Sélectionnez :
   - **Repository** : votre-username/portfolio-data-analyst
   - **Branch** : main
   - **Main file path** : app.py
5. Cliquez sur "Deploy!"

⏱️ Le déploiement prend 2-3 minutes.

#### 3. Votre Portfolio est en Ligne ! 🎉

Vous obtiendrez une URL du type :
```
https://votre-username-portfolio-data-analyst.streamlit.app
```

### Configuration Avancée

Si besoin, créez un fichier `.streamlit/secrets.toml` pour les secrets :
```toml
# Ne pas commiter ce fichier !
api_key = "votre_clé_api"
```

---

## Déploiement sur Heroku

### Prérequis
- Compte Heroku
- Heroku CLI installé

### Fichiers Nécessaires

#### 1. Créer `Procfile`
```
web: sh setup.sh && streamlit run app.py
```

#### 2. Créer `setup.sh`
```bash
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"votre.email@example.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

#### 3. Créer `runtime.txt`
```
python-3.11.0
```

### Commandes de Déploiement

```bash
# Login Heroku
heroku login

# Créer l'application
heroku create portfolio-makhtar-diouf

# Déployer
git push heroku main

# Ouvrir l'application
heroku open
```

---

## Déploiement sur Vercel

### Prérequis
- Compte Vercel
- Vercel CLI (optionnel)

### Configuration

#### 1. Créer `vercel.json`
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

#### 2. Déployer

Via l'interface web :
1. Allez sur [vercel.com](https://vercel.com)
2. Importez votre repository GitHub
3. Configurez le projet
4. Déployez !

Via CLI :
```bash
npm i -g vercel
vercel
```

---

## Déploiement Local (Développement)

### Lancement Simple
```bash
streamlit run app.py
```

### Avec Configuration Personnalisée
```bash
streamlit run app.py --server.port 8080 --server.address localhost
```

### Mode Debug
```bash
streamlit run app.py --logger.level=debug
```

---

## Configuration DNS Personnalisé

### Streamlit Cloud

1. Allez dans les paramètres de votre app
2. Section "Custom domain"
3. Ajoutez votre domaine (ex: portfolio.votredomaine.com)
4. Configurez les DNS chez votre registrar :
   ```
   Type: CNAME
   Name: portfolio
   Value: votre-app.streamlit.app
   ```

### Heroku

```bash
heroku domains:add portfolio.votredomaine.com
```

Puis configurez le DNS :
```
Type: CNAME
Name: portfolio
Value: votre-app.herokuapp.com
```

---

## Optimisations pour la Production

### 1. Cache des Données
```python
@st.cache_data(ttl=3600)
def load_data():
    # Votre code
    return data
```

### 2. Compression des Images
Utilisez des images optimisées (WebP, compression)

### 3. Lazy Loading
Chargez les données lourdes uniquement quand nécessaire

### 4. Monitoring
Activez les analytics Streamlit Cloud pour suivre l'utilisation

---

## Sécurité

### Variables d'Environnement

**Streamlit Cloud :**
Dans les paramètres de l'app > Secrets

**Heroku :**
```bash
heroku config:set API_KEY=votre_clé
```

**Local :**
Créez `.streamlit/secrets.toml` (ne pas commiter)

### Bonnes Pratiques
- ✅ Ne jamais commiter de secrets
- ✅ Utiliser `.gitignore`
- ✅ Valider les entrées utilisateur
- ✅ Limiter les requêtes API

---

## Maintenance

### Mise à Jour

```bash
# Modifier votre code
git add .
git commit -m "Mise à jour: description"
git push origin main
```

Streamlit Cloud redéploie automatiquement !

### Rollback

Sur Streamlit Cloud :
1. Allez dans "Manage app"
2. Section "App history"
3. Sélectionnez une version précédente

### Logs

**Streamlit Cloud :**
Bouton "Manage app" > "Logs"

**Heroku :**
```bash
heroku logs --tail
```

---

## Monitoring & Analytics

### Streamlit Cloud
- Métriques d'utilisation intégrées
- Nombre de visiteurs
- Temps de chargement

### Google Analytics (Optionnel)

Ajoutez dans `app.py` :
```python
# Google Analytics
st.markdown("""
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
""", unsafe_allow_html=True)
```

---

## Troubleshooting

### Erreur de Dépendances
```bash
# Mettre à jour requirements.txt
pip freeze > requirements.txt
```

### Erreur de Mémoire
- Réduire la taille des datasets
- Utiliser le cache Streamlit
- Optimiser les graphiques

### Erreur de Port
Vérifiez que le port est bien configuré dans `config.toml`

### App Lente
- Activez le cache (`@st.cache_data`)
- Optimisez les requêtes
- Réduisez les données chargées

---

## Checklist de Déploiement

- [ ] Code testé localement
- [ ] `requirements.txt` à jour
- [ ] Secrets configurés (si nécessaire)
- [ ] `.gitignore` configuré
- [ ] README.md complet
- [ ] Repository GitHub créé
- [ ] App déployée sur Streamlit Cloud
- [ ] URL testée et fonctionnelle
- [ ] DNS personnalisé configuré (optionnel)
- [ ] Analytics activés (optionnel)

---

## Support

### Documentation Officielle
- [Streamlit Docs](https://docs.streamlit.io)
- [Streamlit Cloud](https://docs.streamlit.io/streamlit-community-cloud)
- [Heroku Docs](https://devcenter.heroku.com)

### Communauté
- [Forum Streamlit](https://discuss.streamlit.io)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)

---

## 🎉 Félicitations !

Votre portfolio est maintenant en ligne et accessible au monde entier !

**URL à partager :**
- LinkedIn
- CV
- Email de candidature
- Carte de visite

**Prochaines étapes :**
1. Partagez votre portfolio
2. Collectez les retours
3. Améliorez continuellement
4. Ajoutez de nouveaux projets

**Bonne chance dans votre recherche ! 🚀**
