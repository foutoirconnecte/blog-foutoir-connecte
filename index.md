---
layout: layout.njk
title: Accueil - Le Foutoir Connecté
---

## Votre maison est devenue un enfer numérique ? Rassurez-vous, c'est normal.

Tout commence généralement par une simple ampoule colorée ou une prise Wi-Fi en promotion. C'est amusant, facile à installer, et on a l'impression de vivre dans le futur. Puis, sans vraiment s'en rendre compte, on ajoute un thermostat, des caméras, des détecteurs d'ouverture sur les fenêtres... 

Quelques mois plus tard, la réalité technique vous rattrape : vous avez six applications différentes sur votre smartphone, votre routeur Wi-Fi est à l'agonie, et votre famille s'énerve parce que la lumière du couloir refuse de s'allumer quand la box internet décide de faire une mise à jour. 

Félicitations, vous êtes l'heureux propriétaire d'un **foutoir connecté**.

### Reprenez le contrôle de votre installation

J'ai passé ces dernières années à faire exactement les mêmes erreurs d'architecture. J'ai acheté du matériel incompatible, j'ai saturé mon réseau avec des gadgets dépendants du Cloud, et j'ai subi les foudres de mon entourage quand la domotique compliquait notre quotidien au lieu de le simplifier.

**Le Foutoir Connecté** est né d'une volonté très simple : vous aider à construire des fondations fiables. 

Ici, pas de jargon d'ingénieur incompréhensible ni de tests de gadgets gadgets sponsorisés. L'objectif est de vous fournir des **guides de référence et des solutions de dépannage concrètes** pour construire une vraie maison intelligente. 

Une installation domotique réussie doit respecter trois règles d'or :
1. **Elle doit être invisible** (le bouton mural physique doit toujours fonctionner).
2. **Elle doit être locale** (elle ne doit pas dépendre de serveurs en Chine ou aux États-Unis).
3. **Elle doit résoudre de vrais problèmes** (et non en créer de nouveaux).

Que vous soyez un débutant cherchant à comprendre pourquoi votre ampoule clignote, ou un utilisateur régulier voulant migrer vers Home Assistant, vous trouverez ici de quoi ranger votre installation.

---

### Nos derniers dossiers de fond :

<ul class="article-list">
{% for post in collections.article | reverse %}
  <li>
    <a href="{{ post.url }}">{{ post.data.title }}</a>
  </li>
{% endfor %}
</ul>
