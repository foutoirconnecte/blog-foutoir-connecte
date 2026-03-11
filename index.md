---
layout: layout.njk
title: Accueil - Le Foutoir Connecté
---

## Bienvenue dans le Foutoir

Ce blog va vous aider à ranger votre domotique en la rendant fiable et invisible. Fini les interrupteurs hors ligne.

### Les articles récents :

<ul>
{% for post in collections.article | reverse %}
  <li>
    <a href="{{ post.url }}">{{ post.data.title }}</a>
  </li>
{% endfor %}
</ul>
