# Contexte Technique : Le Foutoir Connecté
*(Fichier de mémoire et d'instruction pour l'agent)*

## 🛠 Stack Technique & Déploiement
- **Générateur** : Eleventy (11ty) via Node.js (`npm run build`).
- **Déploiement** : GitHub Pages via GitHub Actions (déclenchement au push sur `main`).
- **Moteur de Recherche** : Pagefind (indexation post-build `npx pagefind --site _site`).

## 📁 Structure du Projet
- `site/articles/` : Fichiers `.md` des articles (utilisent `layout: article.njk`).
- `site/pages/` : Fichiers `.md` des pages statiques type contact, recherche, mentions (utilisent `layout: layout.njk`).
- `site/tags/` : Géré par `index.njk` qui boucle sur `collections.tagList` pour générer les archives.
- `site/_includes/` : Contient les gabarits (templates) Nunjucks (`.njk`).
- `site/_site/` : Dossier de build (à ne pas modifier manuellement).

## ⚙️ Gabarits (Templates Nunjucks)
- `site/_includes/layout.njk` : Gabarit parent. Gère le HTML global, `<head>` (SEO, balises Open Graph, Twitter Cards).
  - **Exclusion Pagefind** : Les pages non-articles sont masquées du moteur de recherche via un attribut dynamique sur le `<body>` : `{% if layout != "article.njk" %}data-pagefind-ignore="all"{% endif %}`.
- `site/articles/article.njk` : Hérite de `layout.njk`. Gère le corps de l'article, le temps de lecture et les recommandations.

## 📝 Front Matter (Métadonnées)
Chaque `.md` contient un en-tête YAML décisif pour la génération et le SEO :
- `layout` (définit le rendu visuel)
- `title`, `description` (injectés directement dans Open Graph et `<title>`)
- `image` (chemin de la miniature, crucial pour le rendu social)
- `tags` (liste) et `date` (YYYY-MM-DD)

## ⚙️ Configuration & Assets
- **Configuration Eleventy** : Le fichier maître est `.eleventy.js` situé à la racine du dossier `site/`. Il gère la copie des fichiers statiques (`images`, `CNAME`), la génération dynamique de la liste des tags, et intègre des filtres métiers complexes (`getRelatedPosts`, `readableDate`, `readingTime`, `slugify`).
- **Gestion des Assets** : Les images sont stockées dans le dossier `images/` (copié tel quel au build). Il n'y a pas de dossier `/assets/css/` indépendant : le CSS global est actuellement intégré directement (inline) dans la balise `<style>` du gabarit `_includes/layout.njk`.
- **La Donnée de Site (Variables Globales)** : Le projet utilise désormais un dossier `site/_data/` pour centraliser les variables globales. Le fichier principal est `metadata.js`, contenant l'URL de base du site, le titre et une description par défaut. Ces variables sont maintenant utilisées dans `site/_includes/layout.njk` pour construire les balises Open Graph et SEO, remplaçant l'URL précédemment codée en dur.
