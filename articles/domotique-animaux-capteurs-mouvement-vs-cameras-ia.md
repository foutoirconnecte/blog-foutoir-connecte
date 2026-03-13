---
layout: article.njk
title: "Domotique et animaux : capteurs de mouvement vs caméras IA pour les chats"
date: 2026-03-13
tags: ["capteurs", "caméras", "animaux"]
image: "/images/domotique-animaux-chats.webp"
summary: "Faut-il choisir des capteurs de mouvement traditionnels ou des caméras IA pour la détection des animaux ? Analyse technique approfondie pour un système domotique fiable et sans fausses alertes."
---

La gestion de la présence de nos animaux de compagnie est un défi classique, presque un rite de passage, en domotique. L'objectif initial semble pourtant simple : créer des automatisations qui améliorent notre confort et notre sécurité, sans que le passage du chat ne déclenche l'alarme à trois heures du matin ou n'allume toutes les lumières du salon en pleine journée. La question n'est plus "si" on peut le faire, mais "comment" le faire de la manière la plus fiable, robuste et évolutive possible. Deux technologies s'affrontent principalement sur ce terrain : les capteurs de mouvement traditionnels, principalement les PIR, et les caméras de surveillance dopées à l'intelligence artificielle pour la reconnaissance d'objets.

Le problème de fond est que les solutions basiques, souvent les premières que l'on adopte pour leur coût et leur simplicité, montrent très vite leurs limites. Un capteur de mouvement infrarouge passif (PIR) est une merveille d'ingénierie pour ce qu'il est : un détecteur de signatures thermiques en mouvement. Pour lui, un chat de cinq kilos qui traverse son champ de vision est une source de chaleur qui bouge, au même titre qu'un humain, ou même qu'un courant d'air chaud provenant d'un radiateur mal placé. Les fabricants ont bien tenté d'intégrer des réglages de sensibilité ou des logiques marketing de "pet immunity", mais ces systèmes restent fondamentalement imparfaits. Ils se basent sur des estimations de masse ou de taille qui ne fonctionnent que dans des conditions de laboratoire. Dans le monde réel, un animal qui saute sur un meuble, passe très près du capteur, ou deux chats qui se poursuivent, peuvent facilement être interprétés comme une présence humaine légitime.

Cette imprécision fondamentale a des conséquences directes et dévastatrices sur la fiabilité et l'acceptation du système domotique par la famille (le fameux "WAF", Wife Acceptance Factor). Au mieux, elle génère des nuisances quotidiennes : des lumières qui s'allument inutilement, gaspillant de l'énergie, un chauffage qui se met en route alors que la pièce est vide d'humains. Au pire, elle compromet la sécurité. Une alarme qui se déclenche sans raison à cause du chat perd toute sa crédibilité. Après deux ou trois fausses alertes nocturnes, l'utilisateur finit par la désactiver complètement, rendant un investissement de plusieurs centaines d'euros totalement inutile et contre-productif. C'est précisément ici que l'intelligence artificielle embarquée dans les caméras modernes, surtout lorsqu'elle est traitée localement, change radicalement la donne. Elle ne se contente pas de voir "un mouvement", elle est capable de comprendre "ce qui" bouge, apportant le contexte qui manquait cruellement.

## Le capteur de mouvement PIR : une physique simple, des limites complexes

Pour bien comprendre les enjeux, il faut revenir au fonctionnement même du capteur PIR. Cet acronyme signifie "Passive InfraRed". "Passif" car il n'émet aucun rayonnement ; il se contente d'analyser le rayonnement thermique (la chaleur) naturellement émis par tous les corps dans son environnement. Tout objet ayant une température supérieure au zéro absolu émet un rayonnement dit "de corps noir". Le corps humain, à environ 37°C, émet fortement dans la bande infrarouge autour de 9-10 micromètres. Le cœur du système PIR est un capteur pyroélectrique, un cristal qui génère une tension électrique en réponse à une variation de l'énergie infrarouge qu'il reçoit.

Ce capteur est placé derrière une lentille de Fresnel, cette pièce de plastique striée qui n'est pas là pour l'esthétique, mais qui joue un rôle crucial de "collecteur" et de "diviseur". Elle divise le champ de vision en de multiples faisceaux de détection. Lorsqu'un corps chaud, comme un humain ou un animal, se déplace et traverse successivement ces faisceaux, il provoque des variations rapides et alternées du signal infrarouge capté, ce qui déclenche l'alerte. Le circuit interne est conçu pour réagir à ce changement rapide, et non à une augmentation lente de la température (comme le soleil qui chauffe un mur). C'est un mécanisme simple, robuste, et surtout, extrêmement économe en énergie, ce qui explique pourquoi ces capteurs peuvent fonctionner sur une simple pile bouton pendant plusieurs années.

Leur principal avantage, qui a assuré leur domination sur le marché pendant des décennies, réside dans leur coût dérisoire et leur simplicité d'intégration. Cependant, leur incapacité fondamentale à distinguer la nature de la source de chaleur est leur talon d'Achille. Les tentatives pour améliorer la situation, comme les fameux modes "pet friendly", ne sont que des rustines logicielles et matérielles. Ces capteurs utilisent souvent un capteur pyroélectrique à double élément. Pour déclencher une alerte, il faut qu'un signal "chaud" quitte le premier élément et arrive sur le second dans un temps donné, ce qui correspond à un mouvement latéral. La logique "pet friendly" va alors jouer sur des seuils : elle peut ignorer les signaux en dessous d'une certaine amplitude (ce qui est censé correspondre à un petit animal) ou exiger un nombre de "pulses" (traversées de faisceaux) plus élevé pour valider une détection.

Le problème est que tous ces réglages sont des paris statistiques. Ils parient sur le fait qu'un animal est plus petit qu'un humain et reste au sol. Mais si votre chat de 6 kg saute sur le dossier du canapé, il se présente comme une masse thermique conséquente, en hauteur, et traverse plusieurs faisceaux, cochant toutes les cases d'une détection humaine. Pour être tout à fait honnête, j'ai moi-même perdu des semaines à essayer de trouver le bon réglage avant de capituler. Le résultat a toujours été le même : un compromis inacceptable. Soit le capteur était réglé pour être assez sensible pour détecter un humain marchant lentement, et le chat finissait toujours par le déclencher. Soit il était réglé pour ignorer le chat, et il devenait alors possible pour une personne de ramper ou de se déplacer très lentement sans être détectée. Pour une analyse plus technique des alternatives, l'article sur [les capteurs de présence mmWave vs PIR](/articles/capteur-presence-mmwave-vs-mouvement-pir) explore des technologies plus modernes mais qui ne résolvent pas non plus le problème des animaux.

## La caméra IA : la révolution contextuelle du traitement local

L'approche des caméras à intelligence artificielle est fondamentalement différente. Elle opère un saut conceptuel. Au lieu de mesurer une simple grandeur physique, elle interprète un flux d'informations riches. L'algorithme de reconnaissance d'objet, qui tourne soit dans le cloud du fabricant soit sur un serveur local, a été entraîné sur d'immenses bases de données d'images pour apprendre à identifier des formes spécifiques. On parle de modèles de détection, comme COCO (Common Objects in Context) ou YOLO (You Only Look Once), qui peuvent reconnaître des dizaines, voire des centaines d'objets différents : une personne, une voiture, un colis, un chat, un chien, un oiseau...

Cette capacité de classification change absolument tout. Le système domotique ne reçoit plus une information binaire (mouvement : oui/non), mais une information contextuelle : "détection d'une 'personne' dans le salon" ou "détection d'un 'chat' près de la porte". Les possibilités d'automatisation deviennent exponentiellement plus fines et pertinentes. On peut enfin créer une règle de sécurité qui dit : "Si une 'personne' est détectée dans la maison entre 23h et 6h alors que le mode 'nuit' est activé, déclencher la sirène", tout en ignorant royalement les allées et venues nocturnes du chat.

La mise en œuvre de cette technologie peut se faire de deux manières principales, avec des implications très différentes.

**1. Le traitement Cloud : la simplicité au détriment de la vie privée**
Des marques grand public comme Reolink, Eufy, ou Netatmo proposent des caméras qui intègrent cette fonction "clé en main". La caméra détecte un mouvement, envoie le clip vidéo sur les serveurs du fabricant, où des algorithmes l'analysent et renvoient une notification enrichie ("Animal détecté"). L'avantage est la simplicité. L'inconvénient est triple : la dépendance à une connexion internet, la latence (plusieurs secondes entre l'événement et la notification), et surtout, la confidentialité. Envoyer un flux vidéo de son intérieur vers des serveurs externes est un choix qui doit être mûrement réfléchi. Ces services sont souvent liés à des [abonnements cloud payants](/articles/cameras-securite-abonnement-cloud) qui peuvent représenter un coût récurrent non négligeable.

**2. Le traitement local : la voie de la performance et de la souveraineté**
La seconde option, le traitement local, est la voie royale pour qui cherche performance, confidentialité et personnalisation. Des logiciels open-source comme Frigate, intégrés à des plateformes comme Home Assistant, transforment n'importe quelle caméra IP standard en un puissant système de détection NVR (Network Video Recorder) intelligent. Frigate utilise un accélérateur matériel, comme une clé USB Google Coral (un co-processeur TPU, Tensor Processing Unit), pour analyser les flux vidéo en temps réel sur le réseau domestique. L'intégralité du traitement se fait à la maison, aucune image ne quitte votre réseau. La configuration est certes plus complexe et demande un investissement matériel initial, mais le résultat est sans commune mesure. La fiabilité est absolue, la latence est de quelques millisecondes, les possibilités de personnalisation sont infinies (on peut même entraîner ses propres modèles) et la confidentialité est totale. Pour le matériel, il faut prévoir un mini-PC (un NUC Intel, un Beelink, ou même un ancien PC portable) capable de faire tourner Docker. Un Raspberry Pi 5 peut faire l'affaire pour 1 ou 2 flux en basse résolution, mais il montrera vite ses limites. L'idéal est un petit serveur avec un processeur Intel moderne (pour Quick Sync) et la fameuse clé Coral, qui décharge quasi entièrement le CPU de l'analyse IA. Côté réseau, il est fortement recommandé d'isoler les caméras sur leur propre VLAN pour des raisons de sécurité.

## Comparatif technique détaillé : PIR vs Caméra IA Locale

| Caractéristique | Capteur de Mouvement PIR | Caméra avec IA (Traitement Local via Frigate) |
|---|---|---|
| **Principe de détection** | Variation de chaleur (infrarouge) | Analyse d'image en temps réel et reconnaissance d'objet |
| **Précision de la détection** | Faible à moyenne. Ne distingue pas la source. | Très élevée. Distinction précise entre ~80 types d'objets. |
| **Fiabilité (Fausses alertes)** | Élevée (sujet aux animaux, courants d'air, soleil). | Quasi nulle. Proche de 100% avec une configuration correcte. |
| **Confidentialité des données** | Parfaite. Aucune donnée personnelle n'est traitée. | Parfaite. Le traitement est 100% local. |
| **Coût initial** | Très faible (5€ - 20€ par capteur). | Élevé (caméra IP ~50€ + serveur ~100€ + accélérateur IA ~60€). |
| **Coût récurrent** | Nul (sauf pile tous les 2-3 ans). | Nul (consommation électrique du serveur). |
| **Consommation électrique** | Extrêmement faible (µW). | Significative (10-30W pour le serveur et la caméra). |
| **Complexité d'installation** | Très simple (quelques minutes). | Complexe (installation Docker, configuration YAML, réseau). |
| **Latence de détection** | Très faible (< 500 ms). | Très faible (< 200 ms avec un accélérateur Coral). |
| **Information fournie** | Binaire (mouvement / pas de mouvement). | Riche (objet détecté, zone, score de confiance, image). |
| **Cas d'usage optimal** | Détection simple non critique (éclairage de couloir). | Sécurité, CVC, automatisations complexes, surveillance. |

## Approches Hybrides : le meilleur des deux mondes ?

Il n'est pas toujours nécessaire d'opposer les deux technologies. Dans certains cas, les combiner peut aboutir à des solutions encore plus efficaces. Un des reproches faits à l'analyse vidéo permanente est sa consommation de ressources CPU. Même avec un accélérateur Coral, analyser 4 ou 5 flux 24/7 sollicite le matériel. Une approche hybride consiste à utiliser des capteurs PIR comme déclencheurs de bas niveau. Le PIR, avec sa consommation quasi nulle, est en veille permanente. Lorsqu'il détecte un mouvement (n'importe lequel), il ne déclenche pas l'alarme, mais envoie un signal à Frigate pour "réveiller" l'analyse IA sur la caméra correspondante pour une durée de 30 secondes. Si l'IA confirme qu'il s'agit d'une personne, alors seulement l'automatisation principale (l'alarme, par exemple) est déclenchée. Cette méthode réduit considérablement la charge du serveur, tout en garantissant la précision de l'IA pour la décision finale. C'est une optimisation élégante qui tire parti de la faible consommation du PIR et de l'intelligence de la caméra.

## Mise en pratique : intégration avancée dans Home Assistant

La détection est une chose, l'automatisation en est une autre. Voici comment transformer l'information fournie by Frigate en actions intelligentes dans Home Assistant.

Frigate expose pour chaque caméra une multitude d'entités : un capteur pour le nombre d'objets de chaque type détecté (`sensor.salon_person`), un interrupteur pour activer/désactiver la détection (`switch.salon_detect`), et surtout, une entité `binary_sensor` pour chaque objet suivi dans une zone définie (`binary_sensor.salon_person_in_zone_canape`). C'est cette dernière qui est la plus utile.

**Exemple 1 : Alarme intelligente**
L'automatisation de l'alarme devient triviale et robuste.

{% raw %}
```yaml
trigger:
  - platform: state
    entity_id: binary_sensor.salon_person
    to: 'on'
condition:
  - condition: state
    entity_id: alarm_control_panel.maison
    state: armed_away
action:
  - service: siren.turn_on
    target:
      entity_id: siren.exterieure
  - service: notify.mobile_app_fx
    data:
      message: "Intrusion détectée dans le salon !"
      data:
        image: '/api/frigate/notifications/{{trigger.entity_id.split(".")[1]}}/thumbnail.jpg'
```
{% endraw %}
Ici, l'alarme ne se déclenchera QUE si une personne est détectée. Le passage du chat (`binary_sensor.salon_cat`) est complètement ignoré.

**Exemple 2 : Gestion fine de la présence pour le chauffage**
On peut créer un `binary_sensor` global qui agrège la présence humaine dans toute la maison.

{% raw %}
```yaml
- platform: template
  sensors:
    presence_humaine_maison:
      friendly_name: "Présence Humaine à la Maison"
      device_class: presence
      value_template: >-
        {{ is_state('binary_sensor.salon_person', 'on') or
           is_state('binary_sensor.cuisine_person', 'on') or
           is_state('binary_sensor.bureau_person', 'on') }}
```
{% endraw %}
Ce capteur passera à `on` dès qu'une personne est vue par n'importe laquelle des caméras, mais restera à `off` si seuls les animaux sont présents. On peut alors piloter le thermostat sur cette base, réalisant des économies d'énergie significatives.

**Exemple 3 : Automatisation de la chatière**
Si vous avez une chatière électronique, vous pouvez l'automatiser pour qu'elle ne s'ouvre que lorsque votre chat est détecté près de la porte, et non un autre animal du quartier.

{% raw %}
```yaml
trigger:
  - platform: state
    entity_id: binary_sensor.jardin_cat_in_zone_porte
    to: 'on'
action:
  - service: lock.unlock
    target:
      entity_id: lock.chatiere
  - delay: '00:01:00'
  - service: lock.lock
    target:
      entity_id: lock.chatiere
```
{% endraw %}

## Verdict : Faut-il jeter ses capteurs PIR ?

En conclusion, la cohabitation entre domotique et animaux de compagnie n'est plus un casse-tête. Les capteurs PIR, bien que technologiquement simples, conservent une place pour des usages très spécifiques et non critiques, comme l'allumage d'un éclairage de passage. Cependant, dès que la fiabilité devient un enjeu, et particulièrement pour la sécurité, ils constituent une impasse technologique. Tenter de construire un système d'alarme fiable avec des capteurs PIR en présence d'animaux est une cause perdue d'avance, qui mènera inévitablement à des frustrations et à l'abandon du système.

L'avènement des caméras dotées d'intelligence artificielle, et plus particulièrement des systèmes de traitement local comme Frigate, offre une solution quasi parfaite et définitive au problème. En étant capable de comprendre ce qu'elle voit, la caméra ne subit plus les mouvements des animaux, mais les intègre comme une information contextuelle riche. L'effort de configuration initial, bien que plus important, est largement récompensé par la tranquillité d'esprit et la puissance d'un système qui ne se trompe jamais. Pour ma part, je considère que c'est le seul investissement qui garantit une paix durable avec le système d'alarme. C'est ce niveau d'intelligence contextuelle qui transforme une maison connectée en une maison véritablement au service de ses habitants, humains comme félins. L'investissement est conséquent, mais il s'agit de la fondation d'un système de perception qui pourra évoluer et s'adapter à de nouveaux besoins bien au-delà de la simple détection de présence.
