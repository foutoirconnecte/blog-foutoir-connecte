---
layout: article.njk
title: "SONOFF Zigbee : Le guide complet pour maîtriser vos interrupteurs et capteurs connectés"
date: 2026-03-15
tags:
  - article
  - sonoff
  - zigbee-and-matter
  - home assistant
image: "/images/sonoff-zigbee-smart-switches.webp"
summary: "Découvrez comment la gamme SONOFF Zigbee (ZBMINI, ZBMINIL2, SNZB-01 à 04) peut transformer votre installation domotique. Plongeons techniques dans l'absence de neutre, le maillage réseau, et des cas d'usage avancés sur Home Assistant."
---

L'époque où l'on connectait frénétiquement le moindre interrupteur au réseau Wi-Fi de la maison est révolue. L'engorgement des routeurs, les latences insupportables et la dépendance au cloud des fabricants ont poussé les passionnés de domotique vers des solutions plus résilientes, locales et spécialisées. C'est là que le protocole Zigbee entre en scène, avec un acteur devenu incontournable : SONOFF.

Cette marque, jadis connue pour ses modules Wi-Fi bon marché qu'il fallait flasher avec Tasmota pour s'affranchir du cloud, a opéré un virage à 180 degrés ces dernières années. Leur gamme Zigbee est aujourd'hui l'une des plus populaires, des plus abordables et des plus fiables pour quiconque souhaite bâtir une maison connectée sérieuse autour de Home Assistant. 

Mais attention, intégrer des micromodules et des capteurs sans fil ne s'improvise pas. Entre les contraintes électriques des vieilles installations, la gestion d'un réseau maillé et les subtilités d'intégration avec des plateformes locales, il y a de nombreux pièges à éviter. J'ai moi-même passé des heures à chercher le neutre derrière des interrupteurs récalcitrants ou à comprendre pourquoi mon réseau Zigbee s'effondrait. Dans ce guide approfondi, nous allons décortiquer la gamme SONOFF Zigbee (ZBMINI, ZBMINIL2, et les capteurs SNZB) et voir comment l'exploiter à son plein potentiel.

## Le problème épineux du fil de neutre : Rant, Fix, Verdict

Si vous vous êtes déjà intéressé à la domotisation de l'éclairage, vous avez inévitablement rencontré ce mur technique : l'absence de neutre. 

**Rant :** Les installations électriques résidentielles, surtout celles qui datent d'avant les années 2010, ont été pensées pour de simples interrupteurs mécaniques. Un interrupteur classique ne fait que couper ou fermer la phase (le fil qui apporte le courant vers l'ampoule). Il n'a pas besoin de courant pour fonctionner, il ne fait qu'établir un contact physique. 
Mais un interrupteur connecté ou un micromodule est avant tout un petit ordinateur (avec une puce radio, un processeur, de la mémoire). Pour que cette puce puisse rester éveillée, écouter les ordres de votre box domotique et actionner son relais interne, elle a besoin d'être alimentée électriquement en permanence, même lorsque la lumière est éteinte ! Et pour faire un circuit électrique complet capable d'alimenter cette électronique, il faut une phase ET un neutre. 
Découvrir qu'il n'y a que des fils de phase derrière ses interrupteurs muraux est une immense frustration. Tirer un neutre depuis la boîte de dérivation ou le tableau électrique est souvent complexe, coûteux, et hors de portée de ceux qui ne sont pas électriciens. Le résultat ? Beaucoup abandonnent et se tournent vers des ampoules connectées (comme les Philips Hue), perdant au passage l'usage de leurs interrupteurs muraux traditionnels (un cauchemar ergonomique pour le reste de la famille, communément appelé le "WAF" ou *Wife/Husband Acceptance Factor*).

**Fix :** C'est là que SONOFF a frappé un grand coup avec son module **ZBMINIL2 Extreme**. Ce minuscule pavé (environ 40% plus petit que la génération précédente) est conçu spécifiquement pour fonctionner **sans neutre**. 
Comment est-ce possible ? Le ZBMINIL2 utilise une technique de "vol d'énergie" (parasitic power). Il laisse passer un infime filet de courant à travers le circuit, même lorsque la lumière est éteinte. Ce courant est si faible (quelques milliampères) qu'il ne suffit pas à allumer l'ampoule, mais il est suffisant pour maintenir la puce Zigbee en veille.
C'est une prouesse d'ingénierie, surtout que SONOFF a réussi à éliminer le besoin d'installer un condensateur ("bypass") en parallèle de l'ampoule (une contrainte insupportable sur les anciens modules sans neutre pour éviter que les ampoules LED ne clignotent). 

Cependant, il est crucial de comprendre la contrepartie technique de cette magie. Un module sans neutre dispose de très peu d'énergie. Par conséquent, le ZBMINIL2 est un **End Device** (appareil terminal) dans le jargon Zigbee, et non un **Routeur**. Il ne participera pas au maillage (mesh) de votre réseau pour étendre la portée du signal. Il se contente d'écouter et de parler au routeur le plus proche. De plus, il ne propose pas de mesure de consommation d'énergie (power monitoring), car la puce nécessaire consommerait trop de courant.

Si vous avez la chance d'avoir le neutre derrière vos interrupteurs (ou directement au plafonnier), utilisez le modèle standard : le **ZBMINI**. Ce module, alimenté par phase et neutre, agit comme un routeur Zigbee actif. Il renforcera considérablement la stabilité et la portée globale de votre réseau. 

**Verdict :** Le ZBMINIL2 est le sauveur des installations anciennes. Il permet de conserver ses interrupteurs mécaniques (boutons poussoirs ou à bascule) tout en domotisant l'éclairage de manière invisible, sans tirer le moindre câble. Si vous avez le neutre, foncez sur le ZBMINI classique pour solidifier votre maillage réseau.

## La famille SNZB : Capteurs et interactions sans fil

L'éclairage est une chose, mais une maison connectée n'est intelligente que si elle possède des sens (les capteurs) et des moyens d'interagir librement (les boutons sans fil). La gamme SONOFF SNZB répond à ces deux besoins avec une efficacité redoutable.

### Le SNZB-01 / SNZB-01P : L'interrupteur libéré de toute contrainte

Le SNZB-01 est un petit bouton sans fil fonctionnant sur pile (CR2450 pour la version "P" récente, qui offre une meilleure autonomie). Il permet trois types d'actions de base : un clic simple, un double clic, et un appui long.
La force de ce bouton est qu'il n'est relié à rien physiquement. Vous pouvez le coller sur la table de chevet, le fixer au mur à côté de l'entrée, ou le laisser sur la table basse du salon. 

D'un point de vue technique, ce bouton est un "End Device" endormi (Sleepy End Device). Pour économiser sa pile, il éteint complètement sa radio Zigbee 99% du temps. Ce n'est que lorsque vous appuyez physiquement sur le bouton qu'il se réveille, envoie la trame Zigbee contenant l'information ("clic simple" par exemple) à votre coordinateur, puis se rendort immédiatement. C'est ce qui lui permet de tenir un à deux ans avec une simple pile bouton.

### Les capteurs environnementaux et de sécurité (SNZB-02, SNZB-03, SNZB-04)

SONOFF propose les trois piliers de la détection domotique :

1.  **SNZB-02 (Température et Humidité) :** Ce petit capteur est essentiel pour gérer le chauffage, la climatisation ou la VMC. Plutôt que d'envoyer la température en continu (ce qui viderait la batterie en quelques jours), il fonctionne sur un principe de seuil de rapport (reporting configuration). Il n'envoie une donnée au réseau Zigbee que si la température change d'une certaine valeur (par exemple 0.5°C) ou si un temps maximum s'est écoulé (par exemple toutes les heures). 
2.  **SNZB-03 (Détecteur de mouvement PIR) :** Il utilise l'infrarouge passif pour détecter la chaleur corporelle en mouvement. Parfait pour allumer les lumières d'un couloir la nuit ou déclencher une alarme. Attention au délai de "blind time" (temps de repos) d'environ 60 secondes entre deux détections, conçu pour économiser la pile, ce qui le rend impropre à des automatisations exigeant une réactivité constante dans des pièces de vie.
3.  **SNZB-04 (Contacteur de porte/fenêtre) :** Basé sur un contact magnétique (interrupteur Reed), il envoie un signal instantané lorsque les deux parties s'éloignent ou se rapprochent. Sa conception très basse consommation permet une autonomie exceptionnelle.

## Comprendre et optimiser le maillage Zigbee (Mesh Network)

Contrairement au Wi-Fi où tous les appareils se connectent à un point central (votre routeur internet), le protocole Zigbee (tout comme Matter over Thread, voir notre [comparatif Zigbee vs Matter en 2026](/articles/zigbee-vs-matter-2026)) fonctionne en réseau maillé. C'est la clé de sa résilience et de sa portée. 

Pour que votre écosystème SONOFF soit parfaitement stable, il faut comprendre les trois rôles d'un réseau Zigbee :

1.  **Le Coordinateur :** C'est le chef d'orchestre. Il n'y en a qu'un seul par réseau. C'est généralement une clé USB branchée sur votre Raspberry Pi ou votre mini-PC exécutant Home Assistant. Les clés SONOFF Dongle Plus (version ZBDongle-E ou ZBDongle-P) font figure de référence sur le marché grâce à leur antenne externe offrant un gain massif de portée.
2.  **Les Routeurs :** Ils répètent et amplifient le signal. Ils permettent aux capteurs éloignés de communiquer avec le coordinateur en passant de routeur en routeur. **Règle d'or : tout appareil Zigbee branché en permanence sur le secteur agit comme un routeur.** C'est le cas des micromodules SONOFF ZBMINI (avec neutre) ou des prises connectées (SONOFF S26R2ZB). Plus vous avez de routeurs bien répartis dans la maison, plus le maillage est dense et robuste.
3.  **Les End Devices (Appareils terminaux) :** Ils fonctionnent sur pile (comme les SNZB-01, 02, 03, 04) ou en "vol d'énergie" sans neutre (ZBMINIL2). Ils se contentent de dormir et de se réveiller pour envoyer une info. Ils ne répètent jamais le signal des autres. 

**L'erreur classique du débutant** est d'acheter un coordinateur et 15 capteurs sur pile (SNZB) et de les disperser dans une grande maison. Les capteurs les plus éloignés n'arriveront jamais à atteindre le coordinateur et se déconnecteront sans cesse (les fameux "Lost devices" ou périphériques injoignables). 

La solution technique ? Construisez l'ossature de votre réseau d'abord. Installez vos ZBMINI (ou des prises Zigbee) dans différentes pièces pour créer un maillage fort. Ensuite seulement, appairez vos capteurs sur pile, en les appairant physiquement à leur emplacement définitif afin qu'ils accrochent naturellement le routeur le plus proche et le plus puissant, plutôt que d'essayer de s'accrocher vainement au coordinateur situé à l'autre bout de la maison.

## Intégration sous Home Assistant : ZHA vs Zigbee2MQTT

Une fois le matériel en main, il faut l'interfacer avec le cerveau de la maison. Home Assistant propose deux approches majeures pour gérer les appareils Zigbee.

**ZHA (Zigbee Home Automation) :** C'est l'intégration native de Home Assistant. Elle est intégrée au cœur du système, très facile à configurer en quelques clics depuis l'interface utilisateur. Tous les appareils SONOFF récents y sont parfaitement reconnus. Si vous cherchez la simplicité absolue pour vos ZBMINI et capteurs SNZB, c'est un excellent choix. Cependant, la personnalisation fine des appareils (mise à jour du firmware OTA, configuration complexe du seuil de rapport des capteurs) est parfois plus ardue.

**Zigbee2MQTT (Z2M) :** C'est l'alternative prisée par les power-users. C'est un service indépendant qui traduit les trames Zigbee en messages MQTT, que Home Assistant interprète ensuite. Z2M nécessite un peu plus de configuration (installation d'un broker MQTT Mosquitto), mais il offre des avantages monumentaux :
*   **Prise en charge colossale :** Z2M est souvent le premier à supporter les tout nouveaux produits du marché.
*   **Contrôle fin :** L'interface de Z2M permet de visualiser la topologie de votre réseau maillé de manière très précise, d'obliger un capteur à se lier à un routeur spécifique, ou de configurer les délais précis avant le passage en veille d'un détecteur de mouvement SNZB-03.
*   **Mises à jour OTA (Over-The-Air) :** Z2M gère très bien la récupération et le déploiement des nouveaux firmwares officiels SONOFF sur vos appareils, assurant sécurité et corrections de bugs sans avoir besoin de la passerelle propriétaire de la marque.

*Mon verdict technique :* Si vous démarrez, ZHA fait le travail. Mais si vous équipez toute une maison avec des dizaines de micromodules et de capteurs SONOFF, prenez le temps d'installer Zigbee2MQTT. C'est un investissement en temps minime qui vous offrira un contrôle absolu sur votre réseau radio. Vous n'aurez d'ailleurs aucun problème de cohabitation si vous utilisez des équipements Apple HomeKit en parallèle, comme détaillé dans notre [analyse HA vs Apple Home](/articles/ha_vs_apple_home_2026).

## Cas d'usages avancés et actions concrètes

La théorie est maîtrisée. Passons à la pratique. Voici comment la combinaison de la gamme SONOFF et de Home Assistant permet de résoudre des problèmes quotidiens de manière élégante et invisible.

### 1. Le "Va-et-Vient" virtuel sans tirer de câbles

**Le scénario :** Vous avez une longue pièce avec un seul interrupteur à l'entrée. Vous voulez pouvoir éteindre la lumière depuis votre canapé à l'autre bout de la pièce, mais faire des saignées dans le mur pour passer un câble de navette est inenvisageable.

**L'implémentation SONOFF :**
1. Derrière l'interrupteur mécanique existant à l'entrée, installez un **ZBMINIL2** (si pas de neutre) ou un **ZBMINI**. Ce module contrôlera physiquement l'ampoule.
2. Fixez un bouton sans fil **SNZB-01** au mur, près de votre canapé (avec du simple scotch double-face).
3. Dans Home Assistant (via une automatisation native ou Node-RED), créez une règle simple : `SI l'état du SNZB-01 passe à "clic simple", ALORS "basculer" (toggle) l'état du relais du ZBMINI`.

Vous venez de créer un va-et-vient parfait, invisible et réversible, en quelques minutes. Mieux encore, si vous utilisez Zigbee2MQTT, vous pouvez utiliser la fonction de **Binding** (liaison directe). Le Binding permet de lier logiciellement le bouton SNZB-01 directement au micromodule ZBMINI, sans que l'ordre n'ait à transiter par Home Assistant. Résultat : même en cas de plantage de votre serveur ou de mise à jour de votre box domotique, votre interrupteur sans fil continuera d'allumer et d'éteindre la lumière de manière instantanée. C'est le summum de la résilience, un concept critique comme abordé lors de nos tests sur les [pannes de courant en domotique](/articles/panne-courant-domotique).

### 2. L'aération intelligente de la salle de bain (SNZB-02 + ZBMINI)

**Le scénario :** La VMC ou l'extracteur d'air de votre salle de bain tourne en permanence ou est contrôlé par un interrupteur manuel qu'on oublie toujours d'éteindre, générant du bruit et une déperdition thermique en hiver.

**L'implémentation SONOFF :**
1. Installez un micromodule **ZBMINI** (avec neutre obligatoire pour les moteurs d'extracteurs) derrière l'interrupteur de la VMC.
2. Placez un capteur de température et d'humidité **SNZB-02** discrètement sur une étagère de la salle de bain, loin des projections d'eau directes mais proche de la douche.
3. Créez une automatisation Home Assistant basée sur une entité "Generic Thermostat" (détournée pour l'humidité) ou une automatisation classique : `SI l'humidité rapportée par le SNZB-02 dépasse 70% pendant plus de 2 minutes, ALORS allumer le ZBMINI (VMC)`.
4. Ajoutez une condition de retour à la normale : `SI l'humidité redescend en dessous de 55%, ALORS éteindre le ZBMINI`.

Votre ventilation devient intelligente. Elle ne s'active que lorsque l'air est effectivement saturé d'eau après une douche, et se coupe d'elle-même, protégeant vos murs des moisissures tout en économisant l'énergie électrique et thermique de votre maison.

### 3. La sécurité périphérique silencieuse (SNZB-04 + SNZB-03)

**Le scénario :** Vous voulez être alerté si quelqu'un pénètre dans votre abri de jardin ou ouvre la porte du garage, mais sans investir dans un système d'alarme hors de prix et complexe.

**L'implémentation SONOFF :**
1. Placez des contacteurs d'ouverture **SNZB-04** sur les portes et fenêtres stratégiques.
2. Positionnez un détecteur de mouvement **SNZB-03** dans la zone de passage obligatoire.
3. Sous Home Assistant, utilisez l'intégration "Manual Alarm Control Panel". Vous pouvez définir des états (Armé Absent, Armé Nuit, Désarmé).
4. Configurez l'automatisation : `SI l'alarme est "Armée Nuit" ET que le capteur SNZB-04 de la porte du garage passe à "Ouvert", ALORS envoyer une notification critique sur les smartphones de la famille ET faire clignoter les ampoules du salon en rouge`.

Le faible coût de ces capteurs permet de multiplier les points de contrôle. Puisqu'ils communiquent en local via Zigbee, il n'y a aucune latence inhérente au cloud, et vos données de sécurité (heures d'ouvertures de portes, détections de présence) ne quittent jamais votre domicile, garantissant le respect de votre vie privée.

## Conclusion : L'arme fatale de la domotique souveraine

La gamme SONOFF Zigbee illustre parfaitement la maturité qu'a atteinte la domotique locale. Fini le temps des bidouilles hasardeuses, des soudures sur des puces ESP8266 et des connexions Wi-Fi instables. Avec des modules conçus intelligemment comme le ZBMINIL2 pour contourner l'absence de neutre, et un écosystème de capteurs SNZB ultra-économes en énergie, bâtir un maillage radio dense, fiable et hyper-réactif est aujourd'hui à la portée de tous.

Couplés à un cerveau local puissant comme Home Assistant (via ZHA ou Zigbee2MQTT), ces minuscules modules disparaissent derrière les cloisons pour rendre l'intelligence omniprésente mais invisible. Ils redonnent tout son sens au mot "domotique" : un foyer qui s'adapte à ses habitants, de manière autonome, sécurisée et pérenne, sans jamais demander l'autorisation à un serveur distant.
