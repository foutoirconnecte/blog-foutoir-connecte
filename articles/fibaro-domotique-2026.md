---
layout: article.njk
title: "Fibaro en 2026 : Le roi déchu ou l'investissement indispensable ?"
date: '2026-03-17'
tags: ["matériel", "domotique", "capteurs"]
image: "/images/fibaro-domotique.webp"
summary: "Face à l'avalanche de modules Zigbee et Wi-Fi low-cost, la marque premium Fibaro justifie-t-elle encore son prix stratosphérique ? Analyse technique et verdicts."
---

## Le dilemme de l'interrupteur : 60 € contre 15 €

Imaginez la scène. Vous êtes en pleine rénovation ou simplement désireux d'automatiser votre éclairage. Vous ouvrez une boutique en ligne et cherchez un micromodule à encastrer derrière votre interrupteur. D'un côté, un module Fibaro Dimmer 2, affiché à un tarif qui frôle les 60 €. De l'autre, un module Zigbee d'une marque comme Sonoff ou Aqara à 15 €, ou un module Wi-Fi Shelly à peine plus cher. La différence est abyssale. Quatre fois le prix.

Instinctivement, la question s'impose : qui, en 2026, peut encore justifier un tel écart ? La domotique s'est démocratisée à une vitesse folle. Les étagères, virtuelles comme physiques, débordent d'alternatives fonctionnelles et abordables. Les protocoles ouverts comme Zigbee et, plus récemment, le standard Matter, promettent un monde où tout communique avec tout, sans se ruiner.

Dans ce contexte, Fibaro, avec son positionnement premium et son protocole historique Z-Wave, ressemble à une relique d'un autre temps. Une sorte de Nokia de la domotique, autrefois roi incontesté, aujourd'hui perçu comme un dinosaure coûteux et rigide. Les forums et les groupes de discussion regorgent de nouveaux convertis au "tout-Shelly" ou au "tout-Zigbee", vantant les mérites d'installations complètes pour le prix de quelques modules polonais.

Cette perception est-elle justifiée ? Fibaro est-il devenu un simple produit de luxe pour puristes nostalgiques, ou cette différence de prix cache-t-elle une supériorité technique tangible, toujours pertinente aujourd'hui ? C'est le cœur du problème. Tenter de défendre un produit quatre fois plus cher expose au ridicule si les arguments ne sont pas solides, techniques et vérifiables. L'objectif de cet article n'est pas de vous vendre du Fibaro, mais de disséquer la technologie pour vous donner une grille de lecture claire. Vous pourrez ainsi décider si cet investissement est une dépense superflue ou l'assurance d'une tranquillité à long terme.

## L'architecture de la fiabilité : pourquoi Z-Wave reste une référence

Pour comprendre la valeur de Fibaro, il faut d'abord comprendre le véhicule qu'il utilise : le protocole Z-Wave. C'est un point non négociable. Contrairement au Wi-Fi ou au Zigbee, le Z-Wave n'est pas qu'une technologie, c'est un écosystème contrôlé et certifié.

### Z-Wave : la voie royale de la radiofréquence

Le premier élément fondamental est la fréquence radio. En Europe, le Z-Wave opère sur la bande des 868 MHz. Le Wi-Fi et le Zigbee, eux, se partagent la bande très encombrée des 2.4 GHz, aux côtés du Bluetooth, des fours à micro-ondes et d'une myriade d'autres appareils.

**Vulgarisation :** Imaginez que la bande 2.4 GHz est une autoroute à six voies constamment embouteillée aux heures de pointe. Vos commandes domotiques sont des voitures qui tentent de se frayer un chemin. Le Z-Wave, lui, dispose d'une route nationale privée, quasi déserte. Même si la vitesse de pointe est plus faible (le débit de données du Z-Wave est bien inférieur à celui du Wi-Fi), l'information arrive à destination de manière plus prévisible et sans interférences. Dans un appartement où une vingtaine de réseaux Wi-Fi voisins se disputent les canaux, cette distinction est capitale.

De plus, la physique des ondes est têtue : une fréquence plus basse pénètre mieux les obstacles solides. Le signal à 868 MHz traverse plus efficacement les murs en briques ou en béton que le signal à 2.4 GHz. Pour des modules encastrés dans des boîtiers profonds au cœur de la maçonnerie, cet avantage physique peut faire la différence entre un réseau stable et un réseau capricieux.

### Le maillage Z-Wave : une intelligence collective et certifiée

Comme le Zigbee, le Z-Wave est un réseau maillé (mesh network). Chaque module alimenté sur secteur (interrupteur, prise, module de volet) agit comme un répéteur. Il ne se contente pas de recevoir des ordres, il les relaie aux autres modules plus éloignés du contrôleur principal (la box domotique).

Là où Z-Wave se distingue, c'est au niveau de la certification. Pour qu'un fabricant puisse apposer le logo Z-Wave sur son produit, il doit passer une série de tests stricts définis par la Z-Wave Alliance. Cette certification garantit non seulement une interopérabilité quasi parfaite entre les marques, mais aussi que le module se comportera correctement en tant que routeur au sein du maillage.

C'est un point que de nombreux débutants sous-estiment avec le Zigbee. Vous pouvez acheter une prise connectée Zigbee à bas prix qui, une fois intégrée, s'avère être un piètre routeur, affaiblissant la stabilité de tout votre réseau. Avec Z-Wave, ce risque est quasiment éliminé. Le réseau est auto-réparant : si un module tombe en panne, le réseau recalcule automatiquement les routes les plus efficaces pour que les messages continuent de passer. C'est cette gestion rigoureuse du maillage qui constitue le fondement de la réputation de "roc" du Z-Wave.

### La sécurité comme prérequis

Depuis plusieurs années, la norme de sécurité S2 est obligatoire pour la certification des nouveaux produits Z-Wave. Elle offre un chiffrement de niveau bancaire (AES-128) et des mécanismes de protection contre les attaques par déni de service ou de type "man-in-the-middle". Si la domotique Wi-Fi a fait d'énormes progrès, elle reste dépendante de la sécurité globale de votre réseau Wi-Fi, tandis que le Zigbee a connu des vulnérabilités par le passé. L'approche Z-Wave est de considérer la sécurité comme une brique fondamentale du protocole lui-même.

## Anatomie d'un module Fibaro : l'ingénierie au service du détail

Passons maintenant de la théorie du protocole à la pratique du matériel. Qu'est-ce qui, concrètement, justifie le prix d'un module Fibaro quand on le tient en main et qu'on l'installe ?

### La qualité de fabrication : un gage de sécurité et de longévité

Au premier contact, la différence est palpable. Les plastiques utilisés par Fibaro sont denses, de haute qualité et souvent classés pour leur résistance au feu. Les borniers de connexion sont un excellent exemple. Sur de nombreux modules bon marché, les vis des borniers sont fragiles, le pas de vis s'abîme vite et la cage de serrage peine à maintenir fermement les fils rigides de 1.5 mm² ou 2.5 mm².

Sur un Fibaro, les borniers sont robustes. Ils permettent un serrage franc et sécurisé, essentiel pour un appareil électrique destiné à être scellé dans un mur pendant plus d'une décennie. Un mauvais contact électrique n'est pas seulement une source de panne, c'est un risque d'échauffement et, dans le pire des cas, d'incendie. Payer plus cher pour des borniers de qualité n'est pas un luxe, c'est une assurance.

La miniaturisation est un autre point fort historique de la marque. Les modules Fibaro sont parmi les plus compacts du marché, ce qui facilite grandement leur installation dans des boîtes d'encastrement européennes standards (40 mm de profondeur), souvent déjà encombrées de fils.

### L'intelligence embarquée : le cas du Dimmer 2 et du Roller Shutter 3

C'est au niveau des fonctionnalités que Fibaro creuse l'écart. Prenons deux exemples emblématiques.

**1. Le Fibaro Dimmer 2 (FGD-212) : Le sauveur des rénovations**

Ce module est une petite merveille d'ingénierie pour une raison principale : sa capacité à fonctionner **sans fil de neutre**.

**Vulgarisation du neutre :** Dans un circuit électrique simple, le courant arrive par un fil (la Phase) et repart par un autre (le Neutre) pour "fermer la boucle". Or, dans de nombreuses installations anciennes, seul le fil de phase est coupé par l'interrupteur. Le neutre, lui, va directement à l'ampoule. Un module domotique standard a besoin de la phase et du neutre pour s'auto-alimenter en permanence.

Le Dimmer 2 contourne ce problème en faisant passer un courant infime et imperceptible à travers le filament de l'ampoule pour s'alimenter. Cette prouesse technique est complétée par un algorithme d'auto-calibration intelligent. Au premier démarrage, il teste la charge connectée (LED, halogène, ampoule à incandescence) et adapte son mode de fonctionnement (leading-edge ou trailing-edge) pour offrir une variation de lumière stable, sans scintillement ("flickering"), même à très basse intensité.

De nombreux modules Zigbee ou Wi-Fi qui prétendent fonctionner sans neutre nécessitent un "bypass" (un condensateur à installer en parallèle de l'ampoule) pour fonctionner correctement avec des LED de faible puissance. Le Dimmer 2, dans la majorité des cas, s'en passe. Pour quiconque rénove un logement ancien sans vouloir retirer des câbles, ce module n'est pas "une" option, il est souvent **la** solution.

**2. Le Fibaro Roller Shutter 3 (FGR-223) : La précision absolue**

Un module de volet roulant basique se contente d'envoyer du courant pendant une durée déterminée pour monter ou descendre. Le Roller Shutter 3 va bien plus loin. Il intègre une mesure de la consommation électrique. Lors d'un cycle de calibration, il "apprend" le comportement du moteur : il détecte le pic de consommation lorsque le volet arrive en butée (haute ou basse) et mesure le temps de parcours.

Grâce à cela, il peut positionner le volet avec une précision au pourcentage près. La commande "Mets le volet du salon à 50%" devient une réalité, et non une approximation. Il peut aussi détecter des obstacles et protéger le moteur. Cette mesure de consommation est également précieuse pour suivre ses dépenses énergétiques.

Ces fonctionnalités avancées, couplées à la gestion de scènes (un double-clic sur le bouton de l'interrupteur peut, par exemple, fermer tous les volets de la maison), transforment un simple module en un véritable centre de contrôle local.

## Confrontation directe : Fibaro face à la concurrence en 2026

Analysons maintenant les forces et faiblesses de Fibaro face à ses principaux rivaux.

### Fibaro (Z-Wave) vs. Shelly (Wi-Fi)

Shelly a bâti sa réputation sur des produits innovants, ouverts (firmware modifiable) et très compétitifs. La gamme [Shelly Pro](/articles/shelly-pro-2026/) sur rail DIN est une alternative redoutable pour la [domotique au tableau électrique](/articles/domotique-tableau-electrique-rail-din/).

*   **Avantage Shelly :** Le prix, évidemment. L'absence de hub dédié est aussi un argument, chaque module se connectant directement à votre Wi-Fi. L'écosystème est riche et la communauté très active.
*   **Inconvénient Shelly :** La dépendance au Wi-Fi est son talon d'Achille. Une installation avec 30 ou 40 modules Shelly met à rude épreuve un routeur grand public. Chaque module est un client de plus, ce qui peut engendrer des latences, des déconnexions et une saturation du réseau. Une panne de routeur ou un changement de mot de passe Wi-Fi paralyse toute l'installation.
*   **Verdict du duel :** Pour des applications ponctuelles ou pour une gestion centralisée au tableau électrique, Shelly est une option exceptionnelle. Pour une infrastructure d'éclairages et de volets encastrés dans toute la maison, la robustesse d'un réseau Z-Wave dédié, indépendant du Wi-Fi, offre une sérénité et une stabilité que le Wi-Fi peine à égaler à grande échelle.

### Fibaro (Z-Wave) vs. Aqara/Sonoff (Zigbee)

Le Zigbee est le champion du rapport qualité/prix, surtout pour les capteurs sur batterie.

*   **Avantage Zigbee :** Le coût est imbattable. L'écosystème est gigantesque, avec une variété de capteurs (température, mouvement, inondation, vibration...) à des prix dérisoires.
*   **Inconvénient Zigbee :** L'interférence avec le Wi-Fi 2.4 GHz est un risque réel. La qualité du maillage est très hétérogène et dépend de la qualité de vos routeurs (les modules sur secteur). L'interopérabilité, bien qu'améliorée avec Zigbee 3.0, peut encore réserver des surprises entre les marques. La portée perçue est souvent inférieure à celle du Z-Wave en raison de la moins bonne pénétration des murs par la fréquence de 2.4 GHz.
*   **Verdict du duel :** Le Zigbee est le roi incontesté des capteurs sur batterie et des applications non critiques. Il serait financièrement absurde de payer un capteur de porte Fibaro Z-Wave à 45 € quand un équivalent Aqara Zigbee à 10 € fait parfaitement le travail. Cependant, pour les modules encastrés qui forment l'ossature de l'installation, les arguments en faveur de la stabilité et de la portée du Z-Wave restent valables.

### Et Matter dans tout ça ?

Matter est souvent présenté comme la solution miracle. C'est une sur-couche logicielle conçue pour unifier la communication entre les appareils, pas un protocole radio. Matter fonctionne sur des réseaux existants comme le Wi-Fi et le Thread (un autre protocole maillé à 2.4 GHz, concurrent du Zigbee).

En 2026, Matter simplifie la vie de l'utilisateur en permettant à un appareil A de parler à un écosystème B. Cependant, il ne résout pas les problèmes physiques sous-jacents. Un module Wi-Fi Matter continuera de congestionner votre réseau Wi-Fi. Un module Thread Matter sera toujours sujet aux interférences sur la bande 2.4 GHz. La Z-Wave Alliance a développé un pont Z-Wave vers Matter, ce qui signifie que l'écosystème Fibaro ne sera pas isolé. Matter est une avancée formidable pour l'interopérabilité, mais il ne rend pas la physique des ondes radio obsolète.

## Le verdict : faut-il encore investir dans Fibaro en 2026 ?

Après cette analyse technique, la réponse n'est pas un "oui" ou un "non" simpliste. C'est une réponse stratégique qui dépend de vos priorités et de la nature de votre projet.

**Investissez dans Fibaro (et le Z-Wave) SANS HÉSITER pour :**

1.  **L'infrastructure critique encastrée.** Pour tous les modules qui contrôlent l'éclairage, les volets roulants, et qui sont destinés à rester dans vos murs pendant 15 ans. Leur fiabilité, la qualité de leur fabrication et la stabilité du réseau Z-Wave justifient l'investissement initial. C'est la fondation de votre maison connectée. Une fondation se doit d'être solide.
2.  **Les rénovations sans neutre.** Le Fibaro Dimmer 2 reste, à mon sens, la solution la plus élégante, la plus fiable et la plus sûre du marché pour les circuits d'éclairage dépourvus de neutre à l'interrupteur. Tenter d'économiser sur ce point précis est souvent le début de problèmes de scintillement et de pannes.
3.  **Les environnements radio-pollués.** Si vous vivez dans un immeuble où des dizaines de réseaux Wi-Fi se chevauchent, créer un réseau domotique sur une fréquence dédiée et propre comme le Z-Wave est un choix de raison pour garantir une réactivité et une fiabilité à toute épreuve.

**Évitez Fibaro (ou panachez intelligemment) pour :**

1.  **Les capteurs et les actionneurs non critiques.** Pour les capteurs de température, d'ouverture de porte, de mouvement, les prises connectées pour des lampes d'appoint... l'écosystème Zigbee offre un rapport performance/prix imbattable. Il est plus judicieux de dépenser 100 € pour dix capteurs Zigbee que pour deux capteurs Z-Wave.
2.  **Les budgets très contraints.** Si votre budget est le critère numéro un, une installation entièrement basée sur Shelly (Wi-Fi) ou Sonoff (Wi-Fi/Zigbee) sera fonctionnelle. Il faudra simplement être conscient des limites potentielles en termes de stabilité à grande échelle et accepter de devoir peut-être intervenir plus souvent sur le système.
3.  **Les applications spécifiques au tableau électrique.** La gamme Shelly Pro, conçue pour le rail DIN, est souvent plus adaptée et plus économique pour piloter des circuits de puissance directement depuis le tableau.

### La stratégie hybride : le choix de l'expert

La conclusion la plus pragmatique en 2026 n'est pas de choisir un camp, mais de tirer le meilleur de chaque monde. Une installation domotique mature et résiliente est une installation hybride.

*   **Le squelette en Z-Wave :** Utilisez des modules Fibaro pour tous vos points d'éclairage et volets roulants encastrés. C'est votre investissement dans la fiabilité à long terme.
*   **Le système nerveux en Zigbee :** Déployez un large réseau de capteurs Zigbee (Aqara, Sonoff, etc.) pour collecter des informations (présence, température, humidité, état des portes). Ils sont économiques, efficaces et discrets.
*   **Les muscles en Wi-Fi :** Employez des modules Shelly pour des tâches spécifiques : piloter une porte de garage, un contacteur de chauffe-eau au tableau électrique, ou une prise connectée nécessitant une mesure de puissance précise.

Le tout est orchestré par une box domotique puissante et agnostique comme Home Assistant, Jeedom ou Homey, capable de faire dialoguer ces protocoles de manière transparente.

Fibaro n'est donc pas un roi déchu. Il a simplement été contraint de céder une partie de son territoire. Il n'est plus le souverain absolu de la domotique, mais il reste le maître incontesté de son domaine de prédilection : l'infrastructure encastrée, fiable et durable. Le considérer comme un simple produit de luxe, c'est ignorer la profondeur de l'ingénierie qui justifie son prix. Le choix d'investir dans Fibaro n'est pas une question de budget, mais une décision sur le niveau de fiabilité que vous exigez pour le cœur de votre maison.
