---
layout: article.njk
title: "Test croisé : Thermostat Hub W200 et Caméra Hub G350, le combo ultime ?"
date: 2026-03-15
tags: ["article", "chauffage-intelligent", "sécurité-and-caméras"]
image: "/images/w200-g350-combo.webp"
summary: "Analyse technique et retour d'expérience sur l'intégration du thermostat W200 avec la caméra Hub G350. Un duo performant qui cache de vrais atouts techniques."
---

## Le Problème : Le dilemme de la gestion centralisée

Lorsqu'on équipe son domicile en domotique, la prolifération des ponts de connexion devient vite incontrôlable. Un hub pour les ampoules, un autre pour les capteurs d'ouverture, un troisième pour les caméras de sécurité, et encore un pour le chauffage. La promesse de la maison intelligente se transforme souvent en un cauchemar de câblage Ethernet, de prises électriques monopolisées et d'interférences radio, spécialement sur la bande des 2.4 GHz où cohabitent le Wi-Fi, le Bluetooth et le Zigbee. L'utilisateur se retrouve à devoir gérer la topologie d'un réseau complexe au lieu de profiter d'une installation fluide. 

Le chauffage, pilier du confort et du budget, est généralement géré par un dispositif dédié. La sécurité, elle, dépend de caméras autonomes. Les tentatives de croisement entre ces deux mondes reposent trop souvent sur le cloud : un capteur de mouvement lié à la caméra déclenche le thermostat via des requêtes API externes, induisant une latence perceptible et une dépendance inacceptable à la connexion internet. Si la box internet plante, le scénario échoue. Le chauffage tourne à vide pendant que vous êtes au travail, ou la caméra enregistre des séquences inutiles alors que vous êtes dans la pièce.

L'objectif de mon installation actuelle est d'éliminer cette dépendance au cloud et de réduire le nombre de coordinateurs domotiques. La solution réside dans la convergence des fonctions matérielles. L'apparition d'appareils hybrides, capables d'assurer leur fonction première tout en servant de routeur ou de coordinateur pour d'autres protocoles (notamment Matter over Thread et Zigbee 3.0), change la donne. 

## La Solution : Le couplage W200 et G350

C'est ici qu'intervient le duo formé par le Thermostat Hub W200 et la Caméra Hub G350. Loin d'être de simples gadgets de surface, ces deux équipements intègrent nativement des fonctions de coordination Zigbee et de relais Matter. L'idée est de les utiliser non pas comme deux systèmes distincts, mais comme une colonne vertébrale unifiée pour la gestion climatique et la sécurité, le tout en local.

### Analyse technique du Thermostat Hub W200

Le thermostat W200 se distingue par sa conception interne. Contrairement aux modèles traditionnels qui se contentent d'un simple relais sec et d'une puce Wi-Fi basique (souvent un ESP8266 vieillissant ou un ESP32 sous-exploité), le W200 intègre un microcontrôleur ARM Cortex-M4 couplé à une puce radio multiprotocole. 

#### La question du neutre électrique

L'installation matérielle soulève le problème récurrent du fil neutre. La majorité des thermostats filaires remplacent un simple contacteur bimétallique et ne disposent que de la phase et du retour lampe/chaudière. Le W200, pour maintenir ses fonctions de hub Zigbee actives en permanence (un coordinateur ne peut pas se mettre en veille sous peine de faire tomber tout le réseau maillé), exige une alimentation continue. Il existe des versions "No Neutral" qui contournent le problème en laissant fuiter un courant résiduel infime, mais cela pose des problèmes de scintillement sur les éclairages LED couplés ou d'usure prématurée des relais de la chaudière. Je vous recommande fortement de tirer un vrai fil neutre jusqu'à la boîte d'encastrement de votre thermostat. Cela garantit une stabilité électrique irréprochable et permet au W200 d'exploiter pleinement la puissance d'émission de son antenne Zigbee (jusqu'à +20 dBm en Europe). 

#### Capacités de routage et maillage Zigbee

En tant que coordinateur, le W200 gère jusqu'à 128 appareils enfants directs. Sa gestion de la topologie réseau est exemplaire. Dans une maison de 120 mètres carrés, avec des murs porteurs en brique, j'ai constaté que le signal traverse les obstacles avec une atténuation bien inférieure à celle d'un dongle USB classique branché derrière un serveur métallique. Le positionnement mural du thermostat (généralement à 1,50 mètre du sol, au centre de l'habitation) est optimal pour la propagation des ondes radio, créant un réseau maillé dense et réactif pour tous les petits capteurs fonctionnant sur pile (température, humidité, ouverture de porte). Vous pouvez retrouver plus de détails sur l'importance du maillage dans [notre analyse sur le chauffage](/articles/thermostat-intelligent-fenetre-ouverte-multizone).

### Analyse technique de la Caméra Hub G350

La caméra G350 ne se contente pas d'enregistrer des flux vidéo. Elle est dotée d'un NPU (Neural Processing Unit) capable d'exécuter des modèles de vision par ordinateur en local, à la vitesse de 30 images par seconde. 

#### Traitement vidéo local et détection d'humains

La reconnaissance de formes, de visages ou de mouvements spécifiques (comme la chute d'une personne) s'effectue sur le matériel lui-même. Aucun flux vidéo n'est envoyé sur des serveurs distants pour analyse, ce qui élimine la latence habituelle de plusieurs secondes. Lors de mes tests, la détection d'une présence humaine prenait moins de 400 millisecondes pour générer un événement sur le réseau local. Cette rapidité est la clé de voûte de l'intégration avec le thermostat W200.

#### Connectivité et rôle d'extenseur de signal

La G350 est alimentée par USB-C (5V/2A), ce qui la qualifie de "routeur" dans la topologie Zigbee ou Thread, à défaut d'être le coordinateur principal (rôle laissé au W200). Elle capte le signal Wi-Fi 5 GHz pour transmettre les flux vidéo haute résolution (2K) sans saturer la bande des 2.4 GHz, tout en dialoguant avec les capteurs Zigbee sur cette dernière. Elle sert de pont répéteur idéal pour étendre la portée du réseau vers les zones périphériques de la maison, comme le garage ou le jardin.

### L'intégration logicielle et les automatisations locales

La véritable plus-value de ce duo réside dans la synergie locale de leurs capteurs. L'objectif est d'utiliser la détection de présence ultra-précise de la caméra G350 pour piloter la consigne de température du thermostat W200.

#### Détection de présence avancée vs Capteurs PIR

Les capteurs de mouvement traditionnels (PIR - Infrarouge Passif) présentent un défaut majeur : ils ne détectent que le mouvement. Si vous êtes immobile sur le canapé en train de lire, le capteur considère la pièce comme vide au bout de quelques minutes, et le thermostat abaisse la température. La caméra G350, grâce à son analyse d'image par réseau neuronal, maintient l'état "Présence détectée" tant que la forme humaine est visible, même statique. 

La configuration de l'automatisation s'effectue directement sur le réseau local, idéalement via un contrôleur centralisé comme décrit dans [mon article sur le comparatif Zigbee vs Matter](/articles/zigbee-vs-matter-2026). L'événement généré par la caméra est transmis sous forme de payload JSON via MQTT ou via une intégration locale directe. Le temps de réaction entre le franchissement de la porte du salon (vu par la G350) et l'activation du relais de chauffe du W200 est imperceptible, de l'ordre d'une demi-seconde.

#### Scénarios d'utilisation poussés

1.  **Anticipation du retour :** La G350 pointée vers l'allée de garage détecte l'arrivée d'un véhicule familier (grâce à la reconnaissance de forme locale). Avant même que vous n'ouvriez la porte, elle envoie l'information au W200 qui relance la chaudière, passant de la température "Éco" à la température de "Confort". 
2.  **Gestion thermique par zone :** Si la caméra ne détecte personne dans le salon après 22h, mais qu'un capteur de mouvement (routé via le W200) signale de l'activité dans les chambres, le système ajuste dynamiquement la demande de chaleur vers les vannes thermostatiques des pièces concernées, optimisant ainsi la consommation énergétique globale.
3.  **Alerte gel intelligente :** Si la température descend drastiquement mais qu'une fenêtre est détectée ouverte (par un capteur d'ouverture Zigbee relié au W200), la caméra peut envoyer un snapshot de la pièce sur votre téléphone, confirmant visuellement qu'il ne s'agit pas d'un faux positif avant d'envoyer l'ordre brutal de couper complètement le chauffage pour éviter le gaspillage.

### Problèmes de configuration et astuces de débogage

Tout n'est pas parfait dès la sortie de la boîte. Le firmware d'usine du W200 a tendance à prioriser sa propre connexion cloud par défaut. Il faut fouiller dans les paramètres avancés (accessibles via l'interface web locale de l'appareil, port 80) pour activer le mode "LAN Priority" ou désactiver purement et simplement le MQTT distant au profit du broker local. 

Concernant la G350, le flux RSTP n'est parfois pas activé par défaut. Sans cela, impossible de récupérer la vidéo dans un NVR (Network Video Recorder) tiers ou un système comme Frigate. Il faut activer le protocole ONVIF dans l'application de base, définir un mot de passe fort spécifique au flux vidéo, puis l'importer manuellement. De même, veillez à séparer les réseaux : le Wi-Fi des objets connectés (IoT) doit être isolé sur un VLAN dédié pour des raisons de sécurité évidentes, avec des règles de pare-feu strictes autorisant uniquement le trafic vers le contrôleur domotique.

Un autre point de friction concerne la saturation du canal Zigbee. Le W200 propose par défaut le canal 15 ou 20. Vérifiez l'encombrement spectral de votre Wi-Fi 2.4 GHz environnant. Si votre box internet ou celle de vos voisins émet fortement sur le canal 6, il est préférable de forcer le W200 sur le canal Zigbee 25 pour éviter les pertes de paquets et les latences erratiques. Le changement de canal oblige cependant à réappairer la majorité des périphériques à pile, une opération fastidieuse mais indispensable pour la stabilité à long terme.

## Le Verdict

Le couplage du Thermostat Hub W200 et de la Caméra Hub G350 offre une solution matérielle d'une redoutable efficacité pour consolider l'infrastructure réseau d'une installation domotique. En combinant la force d'un coordinateur centralisé toujours alimenté et les capacités de routage vidéo/radio d'une caméra IA, vous réduisez considérablement le nombre de hubs nécessaires, diminuez la latence globale et reprenez le contrôle total sur vos données environnementales en local.

Le W200 excelle par sa stabilité radio et sa finition matérielle, bien que l'exigence du fil neutre puisse refroidir certains installateurs amateurs. La G350, quant à elle, justifie son prix par un NPU performant qui relègue les anciens capteurs de mouvement PIR au rang d'antiquités. 

Cette installation demande un investissement en temps pour affiner les paramètres réseau (isolation VLAN, choix des canaux radio, configuration du broker local), mais le gain en réactivité et en fiabilité justifie pleinement cet effort. Ce n'est pas la solution la plus plug-and-play du marché, mais sur le plan technique, c'est l'une des architectures les plus saines pour bâtir une maison intelligente résiliente aux pannes internet.

Vous l'aurez compris, confier la coordination de son réseau radio à des éléments structurels (thermostat, caméra) plutôt qu'à une petite clé USB cachée dans une baie serveur change drastiquement la portée et la fiabilité des communications. C'est un pas de plus vers une domotique invisible et robuste.


### Analyse détaillée du firmware et des réglages avancés

Pour aller au fond des choses, il est impératif d'examiner de plus près les options du firmware du W200. Sur l'interface web locale (généralement accessible via l'IP attribuée par votre routeur DHCP), la section "Avancée" regorge de paramètres cruciaux pour l'intégration de la chaudière. Vous y trouverez l'hystérésis réglable, la temporisation minimale d'allumage (pour protéger les compresseurs des pompes à chaleur) et la calibration des sondes de température.

#### Calibration des sondes de température internes

Un thermostat mural est par définition sujet aux courants d'air et à la chaleur qu'il dégage lui-même (surtout un appareil équipé d'un microcontrôleur puissant et d'un écran OLED ou LCD). Le W200 génère environ 1,5 à 2 watts en fonctionnement continu, ce qui fausse légèrement la mesure de la température ambiante de sa propre sonde interne (souvent de +1 à +1,5 degré Celsius par rapport à la température réelle au centre de la pièce). Heureusement, le firmware propose un offset de calibration. 

Je recommande de placer une sonde Zigbee déportée et fiable (type thermomètre de précision à encre électronique) au milieu de la pièce pendant au moins 48 heures. Comparez la courbe de chauffe du W200 avec celle de la sonde de référence dans votre tableau de bord domotique. Une fois l'écart moyen déterminé, appliquez le correctif négatif dans l'interface du W200. Certains systèmes domotiques avancés permettent de forcer le W200 à ignorer sa propre sonde pour utiliser exclusivement la valeur remontée par le capteur déporté. Ce mode "Sonde Externe" est la configuration ultime pour un confort thermique parfaitement équilibré.

#### Gestion des PID (Proportionnel, Intégral, Dérivé)

Plutôt que de fonctionner en simple "Tout ou Rien" (On/Off basique), le W200 gère un algorithme PID (Proportionnel, Intégral, Dérivé). Cela signifie qu'il anticipe l'inertie thermique de la pièce. Au lieu de chauffer jusqu'à atteindre la consigne puis de s'arrêter (ce qui entraîne souvent un dépassement désagréable de 1 ou 2 degrés, surtout avec un chauffage au sol ou des radiateurs en fonte très massifs), le W200 réduit l'apport de chaleur à mesure qu'il s'approche de la température cible.

Les paramètres P, I et D sont ajustables. 
- La valeur "Proportionnelle" agit sur la puissance de chauffe en fonction de l'écart immédiat avec la consigne.
- La valeur "Intégrale" corrige l'erreur résiduelle (si la pièce stagne à 19°C alors que la consigne est à 19,5°C à cause de déperditions constantes).
- La valeur "Dérivée" freine la chauffe pour anticiper le dépassement lié à l'inertie.

Si vous possédez un plancher chauffant, l'inertie est gigantesque. Il faudra augmenter significativement la valeur "D" et réduire la valeur "P" pour lisser la montée en température sur plusieurs heures. Pour des convecteurs électriques très réactifs, c'est l'inverse. Le fait de pouvoir régler ces constantes PID en local fait toute la différence par rapport aux thermostats grand public bridés.

### Configuration du flux vidéo G350 (ONVIF et RSTP)

Revenons à la G350. La configuration de son NPU (l'unité de traitement IA) nécessite quelques ajustements pour éviter les faux positifs causés par les animaux de compagnie ou les changements de luminosité (phares de voiture balayant le mur).

Dans les paramètres de la caméra, vous avez accès à une grille de masquage de confidentialité et à des zones de détection polygonales. Il est crucial de délimiter précisément les zones où le mouvement humain doit déclencher une action domotique. Ne sélectionnez pas toute l'image. Concentrez l'analyse sur le couloir, le pas de la porte ou la zone centrale du salon.

De plus, la sensibilité de l'algorithme est ajustable (de 1 à 100). Un réglage autour de 75 offre généralement un excellent compromis entre la détection rapide d'une personne immobile et le filtrage des petits animaux (chats ou chiens de moins de 15 kg).

Si vous souhaitez enregistrer les séquences vidéo sur un serveur local, la G350 expose un flux RSTP secondaire en 1080p, en plus du flux principal 2K. Je conseille d'utiliser le flux 1080p (souvent H.264) pour la détection de mouvement logicielle tierce si vous n'utilisez pas le NPU intégré, et de réserver le flux 2K (H.265, plus gourmand en ressources processeur) pour l'enregistrement continu ou la visualisation en direct.

La sécurité de ces flux est primordiale. Ne laissez jamais l'accès ONVIF ouvert sans authentification. Créez un utilisateur spécifique dans l'interface de la G350, avec des droits de lecture seule, exclusivement dédié à votre serveur NVR.

### Conclusion sur l'architecture réseau unifiée

L'association du Thermostat Hub W200 et de la Caméra Hub G350 illustre parfaitement la maturité grandissante du matériel domotique en 2026. L'époque où nous devions jongler avec cinq passerelles propriétaires différentes, toutes dépendantes d'un serveur distant, est révolue pour quiconque prend le temps de concevoir son infrastructure intelligemment.

En confiant le rôle de routeur et de coordinateur aux éléments fixes et constamment alimentés de la maison (le thermostat au centre, la caméra en périphérie), on bâtit un réseau Zigbee et Thread incroyablement robuste, capable de résister aux pannes internet, aux coupures de cloud et aux perturbations électromagnétiques de la bande 2.4 GHz. La convergence matérielle est la clé d'un système domotique fiable, performant et réellement respectueux de la vie privée.
