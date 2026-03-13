---
date: '2026-03-08'
image: /images/maison-tout-wifi-box-internet.webp
layout: article.njk
summary: Trop d'objets connectés tuent le réseau. Découvrez pourquoi votre box internet
  opérateur n'est pas taillée pour supporter cinquante prises intelligentes, et comment
  le réseau maillé (Zigbee/Thread) peut sauver vos soirées Netflix.
tags:
- diy-and-tutoriels
- débutant-en-domotique
- wi-fi-and-réseau
- zigbee-and-matter
title: 'La Box Internet qui Suffoque : Le Syndrome de la Maison Tout Wi-Fi'
---



L'enthousiasme des débuts pousse souvent à une erreur fatale. Vous découvrez les joies de la domotique avec une première prise connectée. Le mois suivant, vous équipez tout le salon d'ampoules intelligentes. Six mois plus tard, la maison compte une cinquantaine de périphériques bon marché, tous connectés au réseau sans fil. 

Et c'est là que les problèmes commencent. 

Netflix se met à saccader en pleine soirée. Vos appels vidéo professionnels figent sans raison. La box internet de votre opérateur redémarre mystérieusement au milieu de la nuit. La famille s'impatiente et blâme la mauvaise qualité de la fibre optique. Le coupable est pourtant sous vos yeux, branché sur vos prises murales. Vous êtes victime du syndrome du "tout Wi-Fi".

L'accumulation frénétique d'objets connectés en Wi-Fi détruit silencieusement les fondations de votre réseau domestique. Il est urgent de revoir cette architecture avant que l'ensemble de la maison ne devienne incontrôlable.

## Les limites matérielles de la box opérateur

Pour comprendre l'origine du naufrage, il faut analyser le matériel qui gère votre réseau. Les fournisseurs d'accès internet (qu'il s'agisse d'Orange, Free, Proximus ou Voo) fournissent des routeurs d'entrée de gamme, souvent appelés "box". Ces boîtiers sont conçus pour un usage domestique standard, calibré sur les besoins d'il y a dix ans.

Une box internet gère parfaitement deux ordinateurs, trois smartphones et une télévision connectée. Elle n'a absolument pas la puissance processeur ni la mémoire vive (RAM) nécessaires pour maintenir cinquante connexions Wi-Fi simultanées et permanentes. 

Chaque objet connecté, même s'il n'envoie qu'une toute petite quantité de données, oblige le routeur à maintenir un canal de communication ouvert. Le processeur de la box passe son temps à vérifier que chaque ampoule est toujours là. Sous cette charge constante, le matériel s'étouffe. Il surchauffe. Les paquets de données se perdent, créant de la latence pour vos usages classiques comme la navigation web ou le streaming.

J'ai fait l'erreur de saturer le routeur de mon opérateur avec des dizaines de modules Wi-Fi premier prix avant de voir l'ensemble de mon réseau informatique s'effondrer lamentablement sous la charge. C'est une leçon d'architecture qu'on n'oublie pas.

## L'épuisement du DHCP et le cauchemar des conflits IP

Le problème matériel s'accompagne d'un problème logiciel majeur : la gestion des adresses IP.

Votre box internet intègre un service appelé serveur DHCP. Son rôle est de distribuer une adresse IP unique à chaque appareil qui rejoint le réseau. Sur beaucoup de routeurs fournis par les opérateurs, ce pool d'adresses est limité par défaut ou mal géré sur la durée. 

Quand vous ajoutez massivement des interrupteurs, des prises et des capteurs, le serveur DHCP est sollicité en permanence. Les baux DHCP expirent, se renouvellent, se croisent. Les conflits d'adresses IP apparaissent rapidement. Votre smartphone tente de se connecter en rentrant du travail, la box lui attribue par erreur l'adresse IP déjà utilisée par une prise connectée du salon. Résultat : le téléphone refuse d'afficher internet, et la prise connectée disparaît de votre application domotique. 

La maison connectée devient un environnement instable où les appareils jouent aux chaises musicales avec les adresses réseau. C'est aussi pour cela qu'il est crucial de **[passer au contrôle local et délaisser le Cloud](/articles/domotique-sans-internet-cloud/)**.

## L'embouteillage de la bande des 2.4 GHz

Le troisième clou dans le cercueil de l'architecture "tout Wi-Fi" concerne les fréquences radio. 

L'immense majorité du matériel domotique Wi-Fi utilise exclusivement la bande de fréquence des 2.4 GHz. C'est une bande très ancienne, choisie parce qu'elle traverse bien les murs et coûte très peu cher à intégrer dans des puces électroniques. Le revers de la médaille est catastrophique : c'est une véritable autoroute à une seule voie, déjà saturée par votre four à micro-ondes, le babyphone, le Bluetooth et les multiples réseaux Wi-Fi de vos voisins.

Quand cinquante ampoules et relais essaient de crier "Je suis allumé" en même temps sur cette même voie congestionnée, les signaux se percutent (on parle de collisions de paquets). Le réseau passe son temps à demander aux appareils de répéter leurs messages. La réactivité de votre domotique s'effondre. Vous appuyez sur un bouton dans l'application, et la lumière s'allume trois secondes plus tard.

## Le Fix : L'isolation et le passage au Zigbee

La solution professionnelle consiste à séparer les flux et à utiliser le bon outil pour le bon usage. Il faut impérativement réserver votre réseau Wi-Fi aux appareils qui ont un réel besoin de bande passante. 

Un ordinateur portable téléchargeant des gros fichiers ou une caméra de surveillance diffusant un flux vidéo haute définition ont besoin de la puissance du Wi-Fi. Un capteur d'ouverture de fenêtre qui doit juste dire "ouvert" ou "fermé" n'a rien à faire sur ce réseau.

L'alternative indispensable s'appelle Zigbee (ou le récent protocole Thread). Ce sont des standards radio spécialement inventés pour la domotique. Ils consomment une énergie dérisoire et ne dialoguent pas en Wi-Fi.

Contrairement au Wi-Fi où chaque appareil tape directement et lourdement sur la box internet, le Zigbee crée son propre réseau maillé parallèle. Les appareils communiquent entre eux. Seule la passerelle principale (le coordinateur Zigbee branché à votre serveur domotique) est reliée à votre réseau principal. Au lieu d'avoir cinquante connexions Wi-Fi instables qui saturent votre routeur, vous n'avez plus qu'une seule connexion réseau propre. Le trafic s'effondre et votre connexion internet retrouve sa fluidité immédiate.

## Renforcer l'infrastructure Wi-Fi pour les équipements inévitables

Parfois, l'usage du Wi-Fi reste indispensable en domotique. C'est le cas si vous optez pour des **[micromodules encastrés d'excellente qualité comme les Shelly](/articles/ampoules-connectees-hors-ligne/)**, ou si vous multipliez les assistants vocaux et les caméras.

Si vous dépassez la vingtaine d'appareils Wi-Fi à domicile, la box de votre opérateur doit être reléguée au rang de simple modem. Son antenne Wi-Fi intégrée doit être désactivée définitivement.

L'architecture pérenne exige l'installation d'un véritable système Wi-Fi Mesh dédié (comme les solutions TP-Link Deco, Amazon Eero, Ubiquiti ou Netgear Orbi). Ces routeurs multi-bornes embarquent des processeurs multicœurs et beaucoup de mémoire vive. Ils sont capables de gérer plus de cent ou deux cents périphériques simultanément sans sourciller. Ils répartissent intelligemment la charge sur plusieurs points d'accès dans la maison.

De plus, ces routeurs avancés permettent de créer des réseaux isolés (des VLAN ou des réseaux invités). Vous pouvez ainsi confiner tous vos objets connectés Wi-Fi sur un réseau parallèle. Ils n'auront plus aucun moyen de communiquer avec votre ordinateur personnel ou votre smartphone, bloquant ainsi toute faille de sécurité potentielle liée à une ampoule bas de gamme.

## Le verdict

Une installation domotique fiable repose avant tout sur des fondations réseau irréprochables. Arrêtez de saturer la pauvre box de votre fournisseur d'accès avec des dizaines d'objets connectés inutiles sur le canal 2.4 GHz. 

Basculez massivement votre éclairage, vos interrupteurs et vos capteurs vers le protocole Zigbee pour soulager votre bande passante. Si votre environnement ou vos choix matériels exigent une forte densité d'appareils Wi-Fi, acceptez d'investir dans un vrai routeur maillé conçu pour cet usage intensif. Votre domotique gagnera en réactivité instantanée et toute votre famille retrouvera un internet fonctionnel pour ses loisirs. C'est la base de la paix sociale dans une maison connectée.
