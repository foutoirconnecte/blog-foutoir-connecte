---
date: '2026-02-25'
image: /images/capteurs-presence-ia.webp
layout: article.njk
summary: Découvrez comment les capteurs de présence IA résolvent définitivement le
  problème des lumières qui s'éteignent inopinément lorsque vous êtes immobile.
tags:
- débutant-en-domotique
- home-assistant
- ia-domotique
- éclairage-connecté
title: 'Capteurs de présence IA : fini les lumières qui s''éteignent quand vous lisez'
---



Le scénario est familier. Vous êtes confortablement installé dans votre fauteuil, absorbé par un livre. Soudain, l'obscurité se fait. Vous agitez un bras, comme pour saluer un fantôme, afin de signaler au capteur de mouvement que vous êtes bien là. La lumière se rallume. Cinq minutes plus tard, le cycle recommence. Cette frustration est le symptôme d'une technologie dépassée. Les capteurs de mouvement traditionnels ne détectent pas la présence, ils détectent le mouvement. La solution existe et devient enfin accessible : les capteurs de présence basés sur un radar à ondes millimétriques, souvent estampillés "ia".

Ce guide va au-delà des promesses marketing. Nous allons décortiquer le fonctionnement de cette technologie, comprendre pourquoi elle surpasse ses prédécesseurs, et voir comment l'intégrer efficacement dans un système domotique comme Home Assistant. L'objectif est simple : obtenir un éclairage qui s'adapte à votre présence réelle, et non à vos gesticulations.

### Le problème fondamental des capteurs de mouvement classiques

Pour comprendre la solution, il faut d'abord cerner la limite de l'outil que nous utilisons depuis des années. La quasi-totalité des détecteurs de mouvement grand public reposent sur la technologie PIR (Passive Infrared, ou infrarouge passif).

Un capteur PIR ne voit pas la pièce. Il est équipé d'une lentille de Fresnel qui divise son champ de vision en plusieurs zones. Il mesure en permanence la température infrarouge de ces zones. Quand un corps chaud, comme un être humain ou un animal, se déplace d'une zone à une autre, il crée une variation thermique rapide. C'est cette variation que le capteur détecte et interprète comme un "mouvement".

Le mot clé ici est "variation". Si vous êtes assis et immobile, votre signature thermique est stable. Vous occupez une zone, mais vous ne passez pas d'une zone à l'autre. Pour le capteur PIR, vous devenez rapidement un élément du décor, aussi inerte qu'un meuble. Le minuteur interne du capteur s'écoule, et l'ordre d'éteindre la lumière est envoyé.

Cette limitation rend les PIR inadaptés à de nombreuses situations :
- La lecture dans un salon.
- Le travail à un bureau.
- Regarder un film.
- Prendre un bain.

Augmenter la temporisation du capteur à 15 ou 30 minutes n'est qu'un pansement. Cela signifie que la lumière restera allumée inutilement pendant une demi-heure après votre départ. C'est inefficace et contraire à l'esprit même de la domotique, qui vise l'optimisation et l'intelligence. La technologie PIR a été une étape utile, mais elle ne répond plus aux exigences d'une maison véritablement intelligente.

### La technologie radar à ondes millimétriques (mmWave)

La nouvelle génération de capteurs de présence utilise une approche radicalement différente : le radar. Plus précisément, un radar à ondes millimétriques (mmWave). Le principe est actif, et non passif.

Imaginez un sonar de sous-marin. Il émet une impulsion sonore et écoute l'écho qui revient pour cartographier son environnement. Un capteur mmWave fait la même chose, mais avec des ondes radio de très haute fréquence.

1.  **Émission :** Le capteur émet en continu un signal radio de faible puissance (totalement inoffensif) dans la pièce.
2.  **Réflexion :** Ces ondes rebondissent sur tous les objets : murs, meubles, et bien sûr, les personnes présentes.
3.  **Réception et Analyse :** Une antenne capte les ondes réfléchies. Le microprocesseur du capteur analyse ensuite ces échos en se basant sur un principe physique fondamental : l'effet Doppler.

L'effet Doppler décrit le changement de fréquence d'une onde lorsque la source ou l'observateur est en mouvement. C'est ce qui fait que le son d'une sirène d'ambulance semble plus aigu quand elle s'approche et plus grave quand elle s'éloigne.

Dans notre cas, si tout est statique dans la pièce, les ondes retournent au capteur avec la même fréquence que celle émise. Mais si un objet bouge, même de façon infime, la fréquence de l'onde réfléchie par cet objet sera légèrement modifiée. Le capteur est capable de détecter ces variations de fréquence infinitésimales.

C'est là que réside toute la puissance de cette technologie. Elle ne cherche pas une large variation thermique, mais le plus petit des mouvements. Le battement de votre cœur qui soulève votre poitrine, le mouvement de vos doigts sur un clavier, le simple fait de respirer. Ces micro-mouvements sont largement suffisants pour que le radar confirme une présence humaine. Vous pouvez rester parfaitement immobile pendant une heure, le capteur saura que vous êtes là tant que vous respirez.

### "ia" : simple marketing ou vraie intelligence ?

Le terme "ia" est souvent utilisé à des fins marketing. Dans le contexte des capteurs de présence, il ne s'agit pas d'une conscience artificielle logée dans votre détecteur. L'intelligence réside dans les algorithmes de traitement du signal.

Un capteur mmWave brut est si sensible qu'il pourrait déclencher une alerte à cause d'un rideau qui ondule sous l'effet d'une ventilation, d'un ventilateur en rotation ou des feuilles d'une plante d'intérieur. C'est là que "l'IA" entre en jeu.

Les fabricants développent des algorithmes complexes, entraînés à reconnaître les schémas de micro-mouvements typiques d'un être humain au repos. Le processeur du capteur analyse en temps réel la signature Doppler des objets détectés et la compare à ces modèles.

-   **Mouvement rythmique et lent ?** Probablement une respiration humaine. -> Présence confirmée.
-   **Mouvement rapide et régulier à un endroit fixe ?** Probablement un ventilateur. -> Ignorer.
-   **Mouvement erratique et léger ?** Peut-être un rideau. -> Ignorer.

Cette capacité de filtrage est ce qui transforme un simple détecteur de micro-mouvements en un véritable capteur de présence fiable. L'intelligence est donc la capacité de distinguer un humain immobile des fausses alertes. Certains modèles plus avancés poussent cette logique plus loin, en étant capables de compter le nombre de personnes ou de détecter des chutes, en analysant des signatures de mouvement encore plus complexes.

### Guide pratique : choisir et placer son capteur de présence

Le choix et le positionnement d'un capteur mmWave sont plus déterminants qu'avec un simple PIR. Une mauvaise installation peut anéantir tous les bénéfices de la technologie.

#### Critères de sélection d'un capteur

-   **Protocole de communication :** Le Zigbee est souvent un excellent choix pour sa réactivité et son intégration aisée dans les écosystèmes existants. Il s'intègre parfaitement aux coordinateurs comme ceux utilisés dans **[mon guide sur Zigbee2MQTT](/articles/zigbee2mqtt-guide)**. Le Wi-Fi est une autre option, mais peut encombrer votre réseau et dépend parfois du cloud du fabricant.
-   **Alimentation :** La grande majorité des capteurs mmWave nécessitent une alimentation filaire, généralement via un port USB-C. Leur consommation est trop élevée pour fonctionner sur pile pendant une durée raisonnable. Pensez à l'emplacement d'une prise ou à la possibilité de tirer un câble discret.
-   **Fonctionnalités avancées :** Certains modèles, comme l'Aqara FP2, offrent la détection de zones. Vous pouvez virtuellement diviser une pièce en plusieurs secteurs (zone canapé, zone bureau, zone passage) et créer des automatisations spécifiques pour chacun. C'est un atout considérable pour la fiabilité.
-   **Angle de détection et portée :** Vérifiez les spécifications. Un capteur monté au plafond aura typiquement un angle conique. Un capteur mural aura un angle de détection plus horizontal. Assurez-vous que la portée est suffisante pour votre pièce.

#### Les règles d'or du placement

Le placement est la clé du succès. Les ondes millimétriques traversent les matériaux de faible densité (placo, plastique, verre fin) mais sont bloquées par le métal, le béton et l'eau (y compris le corps humain).

**Règle n°1 : Pensez en 3D.**
Imaginez que le capteur émet un cône de lumière invisible. Votre objectif est que ce cône couvre les zones d'occupation sans être obstrué.
-   **Montage au plafond :** C'est souvent l'idéal pour une couverture globale d'une pièce carrée comme une chambre ou un bureau. Placé au centre, il "voit" tout l'espace de haut en bas.
-   **Montage mural :** Très efficace pour une zone spécifique. Dans un salon, le monter sur un mur face au canapé garantit une détection parfaite lorsque vous êtes assis. Dans un bureau, le placer au-dessus de l'écran, pointé vers votre chaise, est une excellente stratégie. La hauteur recommandée est souvent entre 1.80m et 2.50m.

**Règle n°2 : Identifiez et neutralisez les sources de fausses détections.**
Avant de fixer le capteur, analysez la pièce.
-   **Ventilateurs (plafond ou sur pied) :** Ce sont les ennemis jurés des capteurs mmWave. Leurs pales en mouvement créent une perturbation constante. Ne pointez jamais un capteur directement sur un ventilateur. Utilisez la détection de zone pour exclure cette partie de la pièce si nécessaire.
-   **VMC et bouches de climatisation :** Le flux d'air peut faire bouger des objets légers. Évitez de placer le capteur juste à côté.
-   **Rideaux et plantes :** Un courant d'air peut les faire bouger. Si possible, orientez le capteur de manière à ce qu'ils soient en bordure de son champ de détection, ou utilisez des zones.
-   **Animaux domestiques :** Un gros chien dormant sur le canapé sera détecté comme une présence. Un chat qui passe sera détecté. Les algorithmes sont de plus en plus performants pour les ignorer, mais la sensibilité joue un grand rôle. J’ai personnellement réglé la sensibilité de mon capteur de salon sur un niveau moyen pour éviter que mes chats ne déclenchent l'éclairage en pleine nuit.

**Règle n°3 : Testez avant de fixer définitivement.**
Utilisez du ruban adhésif double-face pour positionner temporairement le capteur. Vivez avec pendant un jour ou deux. Observez son comportement dans votre tableau de bord domotique. Est-ce qu'il se déclenche sans raison ? Est-ce qu'il vous "perd" à certains moments ? Ajustez l'angle et l'emplacement jusqu'à obtenir une fiabilité de 100%. Cette phase de test est indispensable.

### Intégration et configuration dans Home Assistant

Une fois le capteur physiquement installé, il faut l'intégrer logiquement dans votre système domotique. Home Assistant, via ses intégrations ZHA (Zigbee Home Automation) ou Zigbee2MQTT, est parfaitement adapté pour cela.

#### Appairage et entités disponibles

L'appairage d'un capteur Zigbee est standard. Une fois connecté, il expose plusieurs "entités" dans Home Assistant. Vous trouverez typiquement :
-   `binary_sensor.presence`: L'entité principale. Elle passe à l'état `on` (détecté) ou `off` (libre).
-   `sensor.distance`: Certains modèles indiquent la distance de la cible détectée. Utile pour des scénarios avancés.
-   Des contrôles de configuration (`select.sensitivity`, `number.detection_delay`, etc.).

La richesse des entités dépend du modèle et de la qualité de son intégration. La communauté autour des solutions comme Zigbee2MQTT améliore constamment la prise en charge des nouveaux appareils, ce qui renforce l'intérêt d'un **[réseau maillé Zigbee](/articles/reseau-maille-zigbee)** bien construit.

#### Paramétrage fin pour une fiabilité maximale

C'est ici que l'on passe d'un gadget à un outil de précision. Ne négligez pas ces réglages, accessibles depuis l'interface de ZHA ou Zigbee2MQTT.

-   **Sensibilité (Sensitivity) :** C'est le réglage le plus important. Une sensibilité élevée détectera la plus infime respiration mais augmentera le risque de fausses détections (le fameux rideau). Une sensibilité faible sera plus robuste mais pourrait rater une personne particulièrement calme. Commencez avec une valeur moyenne et ajustez en fonction de vos observations. Pour une chambre, une sensibilité élevée est souvent possible. Pour un salon avec un ventilateur, une sensibilité plus faible sera nécessaire.

-   **Délai de départ (Departure Delay / Cooldown Time) :** Ce n'est pas la même chose que le délai d'un PIR. Ce paramètre définit combien de secondes *après la dernière détection de micro-mouvement* le capteur doit attendre avant de passer à l'état "libre". Une valeur entre 5 et 15 secondes est généralement un bon compromis. Elle permet d'éviter que le capteur ne "clignote" si vous retenez votre souffle une seconde.

-   **Distance de détection :** Si votre capteur est dans un bureau qui donne sur un couloir, vous pouvez limiter sa portée maximale à 3 mètres, par exemple. Cela empêchera la détection d'une personne qui ne fait que passer devant la porte.

-   **Zonage (si disponible) :** Pour les modèles compatibles, l'interface vous permettra de dessiner des zones sur une carte de la pièce. Vous pouvez alors créer des `binary_sensor` pour chaque zone. L'automatisation peut alors devenir très granulaire : "Si une présence est détectée dans la `zone_canape` ET que le soleil est couché, allumer la liseuse".

#### Exemple d'automatisation de base dans Home Assistant

L'automatisation la plus simple devient d'une fiabilité redoutable. Voici à quoi ressemble une automatisation de base en YAML pour contrôler une lumière de bureau :

```yaml
alias: Lumière Bureau Présence
description: "Allume et éteint la lumière du bureau en fonction de la présence réelle"
trigger:
  - platform: state
    entity_id: binary_sensor.capteur_presence_bureau
    to: "on"
    id: "presence_detectee"
  - platform: state
    entity_id: binary_sensor.capteur_presence_bureau
    to: "off"
    id: "presence_partie"
condition: []
action:
  - choose:
      - conditions:
          - condition: trigger
            id: "presence_detectee"
        sequence:
          - service: light.turn_on
            target:
              entity_id: light.lampe_de_bureau
      - conditions:
          - condition: trigger
            id: "presence_partie"
        sequence:
          - service: light.turn_off
            target:
              entity_id: light.lampe_de_bureau
mode: single
```

Cette automatisation est simple, mais elle est maintenant basée sur une information de présence fiable à 99.9%. Fini les bras agités dans le vide.

### Un pas de plus vers la maison invisible

Les capteurs de présence à ondes millimétriques ne sont pas une simple évolution. Ils représentent un changement de paradigme. Ils permettent de passer d'une domotique réactive ("quand un mouvement est détecté") à une domotique proactive et contextuelle ("parce que quelqu'un est dans la pièce").

L'investissement initial, en temps et en argent, est légèrement supérieur à celui d'un capteur PIR. Il faut réfléchir au placement, prévoir une alimentation et passer quelques minutes à ajuster les paramètres. Mais le gain en confort et en fiabilité est immense. La technologie devient invisible. Les lumières s'allument quand vous entrez, restent allumées tant que vous êtes là, et s'éteignent peu après votre départ. C'est tout. C'est simple, logique, et ça fonctionne enfin comme on l'a toujours imaginé.

Personnellement, je considère l'installation de ces capteurs dans les pièces de vie comme l'une des améliorations les plus significatives de mon installation domotique depuis des années. C'est le genre de technologie qui, une fois adoptée, rend tout retour en arrière impensable. L'ère de la "danse de la lumière" est révolue.
```