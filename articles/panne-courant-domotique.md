---
layout: article.njk
title: "La panne de courant : que devient votre maison intelligente quand le 230V s'arrête ?"
date: 2026-03-12
tags: ["article", "architecture", "sécurité"]
image: "/images/panne-courant-domotique.webp"
summary: "Une domotique qui s'éteint avec la lumière, ce n'est pas une maison intelligente. Découvrez pourquoi l'onduleur (UPS) est l'investissement de sécurité le plus critique pour la stabilité de votre réseau et de vos données."
---

La domotique est souvent perçue comme un ajout de confort : on pilote ses lumières, on régule son chauffage, on surveille son entrée. Mais à mesure que notre installation grandit, la dépendance de notre confort (et de notre sécurité) envers le réseau électrique augmente. Que se passe-t-il réellement dans votre maison le jour où une tempête, un accident de transformateur ou une maintenance locale coupe brusquement le courant 230V ?

Pour la plupart des gens, la maison s'éteint, tout simplement. On sort une bougie, on attend que ça revienne. Mais pour un foyer domotisé, une panne de courant est une agression majeure. Vos modules Zigbee perdent leur coordinateur, vos serveurs perdent leurs données, vos bases de données domotiques se corrompent, et vos caméras de sécurité s'éteignent.

Une maison intelligente ne doit pas être le premier maillon à céder lors d'une panne. Elle doit être le dernier rempart, capable de maintenir ses fonctions vitales pendant que le quartier est dans le noir. Voici comment transformer votre installation pour qu'elle devienne invulnérable aux coupures de courant.

## L'onduleur (UPS) : Le cœur battant de votre infrastructure

Dans le monde de l'informatique, l'UPS (*Uninterruptible Power Supply* ou onduleur) est la règle d'or. En domotique, c'est l'investissement le plus négligé, et pourtant le plus vital.

Un onduleur est un appareil qui se place entre votre prise murale et vos équipements sensibles. Il contient une batterie interne et un onduleur statique. En temps normal, il filtre le courant, le nettoie des parasites, et recharge sa batterie. En cas de coupure de courant, il prend le relais en quelques millisecondes, garantissant une alimentation constante à vos équipements.

### Ce qu'il faut protéger en priorité
Tout n'a pas besoin d'être sur onduleur. Il faut établir une hiérarchie :
1. **La Box Internet / Modem :** Sans internet, pas de communication avec vos périphériques distants et pas de mise à jour horaire.
2. **Le Serveur Domotique (Home Assistant, Homey) :** Il est le cerveau. S'il s'éteint brutalement lors d'une coupure, sa base de données (SQLite ou autre) peut se corrompre, rendant votre installation inutilisable au rétablissement du courant.
3. **Le coordinateur Zigbee :** Si vous utilisez une clé USB Zigbee, elle doit rester alimentée. Si le coordinateur s'éteint, votre réseau maillé tombe instantanément.
4. **Le NAS :** Si vous utilisez un NAS pour la vidéosurveillance, il est impératif qu'il s'éteigne proprement en cas de coupure prolongée, sous peine de perdre vos vidéos.

## L'onduleur : Bien plus qu'une simple batterie

Un onduleur moderne communique avec votre superviseur domotique. C'est là que la magie opère. En utilisant des protocoles comme NUT (Network UPS Tools) ou simplement des intégrations natives, votre onduleur envoie son état à votre serveur (Home Assistant).

Cela vous permet de créer des automatisations intelligentes en cas de panne :
*   *SI la coupure dépasse 5 minutes, ALORS envoyer une notification critique sur tous les smartphones.*
*   *SI le niveau de batterie de l'onduleur passe sous 20%, ALORS envoyer un ordre d'extinction propre à tous les appareils gourmands (NAS, gros serveurs) pour éviter de vider la batterie.*
*   *SI le courant revient, ALORS rétablir les services automatiquement.*

Cette gestion fine vous permet de transformer une simple panne en un événement maîtrisé. Votre domotique, elle, reste totalement opérationnelle. Vous pouvez continuer à recevoir les alertes des capteurs (qui eux, sont sur pile), et votre réseau Zigbee continue de relayer les informations des capteurs de fuite d'eau ou des détecteurs de fumée.

## La résilience du réseau maillé : Pourquoi le Zigbee survit

C'est ici que l'architecture Zigbee prouve sa supériorité. Contrairement à une ampoule Wi-Fi qui s'éteint si la box ou l'électricité coupe, un capteur de température ou d'ouverture Zigbee ne se "déconnecte" jamais du réseau. Il attend patiemment le retour du coordinateur.

En cas de panne, si votre serveur domotique reste alimenté par un onduleur, votre réseau reste actif. Vos capteurs de fuite d'eau, vos détecteurs de mouvement et vos boutons poussoirs continuent de fonctionner et de remonter des alertes à votre serveur (tant que le serveur lui-même est sur onduleur). Votre maison intelligente reste donc "intelligente" et capable de vous alerter sur des dangers majeurs (incendie, inondation), même en cas de coupure de courant générale du quartier.

C'est une résilience que le Wi-Fi ne pourra jamais atteindre.

## La maintenance des onduleurs

L'onduleur est un équipement vivant. Sa batterie interne a une durée de vie limitée, généralement de 2 à 4 ans. 

Ne faites pas l'erreur d'acheter un onduleur et de l'oublier sous votre bureau. 
1. **Surveillance :** Votre superviseur doit surveiller l'état de santé de la batterie. Si votre logiciel affiche "Battery replaced", ne tardez pas.
2. **Qualité :** Privilégiez des marques reconnues comme APC, Eaton, ou CyberPower. Un onduleur bas de gamme peut être bruyant, dégager des odeurs de plastique chaud, ou pire, ne pas assurer le passage sur batterie en cas de besoin.
3. **Tests :** Une fois par an, simulez une coupure en débranchant la prise murale de l'onduleur pour vérifier que vos équipements ne redémarrent pas. La tranquillité d'esprit a un prix, celui de la rigueur.


## Onduleur ou Batterie de secours : Les dangers du lithium en appartement

L'achat d'un onduleur impose une contrainte physique. Les batteries au plomb, lourdes et encombrantes, sont la norme. Pourquoi pas de batterie au lithium ? 

Le problème réside dans la gestion de la charge et de la température. Une batterie au lithium, surtout si elle est stockée près d'un NAS ou d'un serveur domotique, peut être dangereuse si le système de gestion de la batterie (BMS) est de mauvaise qualité. 

Contrairement aux batteries au plomb, le lithium est beaucoup plus sensible à une décharge profonde ou à une surchauffe. Si vous n'avez pas un équipement de qualité certifiée pour votre domicile, restez sur le plomb scellé (VRLA). C'est beaucoup plus sûr dans un appartement. De plus, la durée de vie est mieux documentée, et le remplacement est simple. 

Il existe aujourd'hui des solutions "EcoFlow" ou "Bluetti" qui sont des centrales d'énergie portables. Ces machines sont incroyables pour les coupures prolongées (plusieurs heures) mais ne remplacent pas un onduleur informatique, car elles n'ont pas la fonction "pass-through" (protection contre les surtensions) assez rapide pour le matériel domotique sensible. Si vous voulez une résilience totale, cumulez les deux : un petit onduleur informatique pour la box et le serveur, et une station d'énergie pour le reste.

## La question du bruit et de l'installation physique

Si vous installez un onduleur dans votre logement, il ne doit pas être bruyant. Les ventilateurs de certains onduleurs "pro" sont assourdissants, surtout en pleine nuit. 

Privilégiez des onduleurs conçus pour le bureau (gammes "Desktop" ou "SOHO"). Ils sont souvent fanless (sans ventilateur) et conçus pour être placés dans un environnement de travail. 

Assurez-vous également que l'endroit où vous placez l'onduleur est bien ventilé. Les batteries chauffent durant la charge. Un onduleur enfermé dans un placard étroit, sans aucune circulation d'air, verra la durée de vie de ses batteries divisée par deux. 

## Protéger le réseau domotique au-delà de l'onduleur : La foudre

Enfin, si l'onduleur vous protège des coupures de courant et des micro-coupures, il ne vous protège pas contre la foudre. Une surtension induite par la foudre sur le réseau électrique de votre maison peut détruire votre onduleur, votre serveur, et toutes vos clés domotiques en quelques microsecondes. 

La solution complémentaire est l'installation d'un parasurtenseur (parafoudre) directement dans votre tableau électrique général. C'est un composant indispensable qui dévie l'énergie excessive des surtensions vers la terre. Si vous vivez dans une zone sujette aux orages, l'onduleur couplé à un parafoudre au tableau est l'assurance tous risques la plus efficace. Une installation domotique bien protégée est une installation qui survit aux aléas climatiques les plus extrêmes. 

En combinant un onduleur de qualité, une bonne gestion des notifications de batterie, et une protection foudre au tableau, vous construisez un système domotique capable de tenir des années dans un environnement domestique imprévisible. C'est l'ultime preuve que votre système est devenu une véritable infrastructure de bâtiment, robuste et professionnelle.


## Le verdict : L'onduleur, votre meilleure assurance domotique

La domotique n'est pas qu'une question de confort ou d'économie d'énergie. C'est une question de fiabilité. Une installation qui s'effondre à la moindre petite variation de tension est une installation mal conçue.

Si vous avez investi du temps et de l'argent dans des modules, des capteurs, et une box domotique, vous devez protéger cet investissement. Un onduleur n'est pas un accessoire de luxe, c'est la fondation de votre infrastructure. Il protège votre matériel, il préserve vos données, il garantit la continuité de votre sécurité, et il vous évite de devoir tout reconfigurer après une corruption de base de données. 

Votre maison connectée doit être un système fiable, qui ne vous laisse pas tomber au moment où vous en avez le plus besoin. Investir dans un onduleur est le geste le plus professionnel qu'un passionné de domotique puisse faire pour sa maison. C'est l'assurance vie de votre projet.


## Les différents types d'onduleurs : Lequel choisir ?

Dans le monde des onduleurs, il y a des différences techniques fondamentales qui impactent directement la durée de vie et la compatibilité de vos équipements.

### 1. Onduleurs "Off-line" (ou Standby)
C'est l'entrée de gamme. En temps normal, le courant passe directement depuis la prise vers vos appareils. En cas de coupure, la batterie prend le relais en quelques millisecondes. C'est suffisant pour une box internet basique, mais la qualité du courant délivré est médiocre et la bascule peut être trop lente pour certains équipements informatiques très sensibles.

### 2. Onduleurs "Line-Interactive" (Le standard recommandé)
Ces modèles stabilisent la tension électrique en temps réel, même quand le courant passe. Ils possèdent un régulateur de tension (AVR) qui corrige les petites surtensions ou sous-tensions sans utiliser la batterie. C'est l'investissement idéal pour un serveur domotique ou un NAS. C'est le meilleur compromis prix-performance pour la domotique.

### 3. Onduleurs "On-line" (ou Double conversion)
C'est le haut de gamme professionnel. Le courant est converti en continu puis en alternatif en permanence. Le courant en sortie est parfait, pur, sans aucune micro-coupure à la bascule. C'est indispensable pour les équipements informatiques de mission critique, mais c'est overkill pour une installation domotique standard. Le coût, le bruit des ventilateurs et la consommation électrique supplémentaire ne justifient pas cet investissement dans un cadre résidentiel.

## Comment dimensionner votre onduleur ?

Ne vous faites pas avoir par les chiffres marketing des onduleurs. On parle souvent en VA (Volt-Ampères). Pour savoir quel onduleur choisir, additionnez la consommation maximale de tous vos appareils que vous souhaitez protéger (en Watts). 

Pour une box internet, un serveur domotique (type Raspberry Pi ou mini-PC) et une clé Zigbee, un onduleur de 500 ou 600 VA est largement suffisant et vous donnera une autonomie de plus de 30 minutes, ce qui couvre 95% des coupures sur le réseau électrique.

## La gestion de l'onduleur dans Home Assistant

Si vous utilisez Home Assistant, l'intégration est un jeu d'enfant. Connectez l'onduleur à votre serveur via le câble USB fourni. Home Assistant détectera automatiquement l'onduleur via le module NUT (Network UPS Tools). Vous aurez alors accès à toutes les données de santé de votre onduleur : charge de la batterie, tension d'entrée, autonomie restante estimée. 

C'est là que vous pouvez créer des scènes complexes : "S'il reste moins de 10 minutes de batterie, alors arrête le NAS proprement, puis éteins le serveur domotique pour préserver l'intégrité des disques durs". C'est cette automatisation de fin de vie qui fait toute la différence entre un système qui survit et un système qui s'abîme prématurément. Votre domotique ne doit pas seulement être fiable lors de son fonctionnement, elle doit être élégante et sécurisée jusque dans son extinction.
