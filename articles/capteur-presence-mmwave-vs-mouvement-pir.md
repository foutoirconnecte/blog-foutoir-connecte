---
date: '2026-02-24'
image: /images/capteur-presence-mmwave-vs-mouvement-pir.webp
layout: article.njk
summary: La lumière qui s'éteint alors que vous lisez tranquillement dans le canapé
  est le premier facteur de rejet de la domotique. Découvrez la révolution des capteurs
  mmWave qui détectent votre présence immobile.
tags:
- comparatif-2026
- diy-and-tutoriels
- débutant-en-domotique
- éclairage-connecté
title: 'Capteurs de présence vs Mouvement : pourquoi votre salon vous oublie sur le
  canapé'
---


C’est un classique de la vie en maison connectée : vous êtes confortablement installé dans votre canapé, plongé dans un livre passionnant ou en train de regarder un film, et soudainement, la lumière du salon s'éteint brusquement. Vous agitez les bras dans le vide en espérant que la domotique se rende compte de votre présence, vous vous levez pour marcher, et finalement, la lumière daigne se rallumer.

Cette situation est non seulement frustrante, mais elle est aussi le premier facteur de rejet massif de la domotique par le reste de la famille (le fameux WAF - Wife/Husband Acceptance Factor). Si la technologie rend votre maison moins confortable qu'elle ne l'était avant, elle échoue à sa mission première.

La faute ne revient pas à votre programmation, mais à une erreur architecturale fondamentale sur le choix du capteur. Pendant quinze ans, nous avons essayé de domotiser la "présence" humaine avec des capteurs de "mouvement" (PIR). C'est comme essayer de mesurer la température avec une règle : l'outil n'est tout simplement pas fait pour ça.

## Le mensonge du capteur PIR (Mouvement)

La quasi-totalité des capteurs que vous trouvez dans les rayons domotique (ou chez les marques comme Aqara ou Sonoff basiques) sont des capteurs infrarouges passifs (PIR - Passive Infrared).

### Comment ça marche ?
Un capteur PIR possède une lentille de Fresnel (cette coque en plastique blanc qui ressemble à un dôme) qui segmente le champ de vision en plusieurs zones. Il détecte uniquement la différence de température entre deux zones. Si un corps chaud (vous) traverse une zone "froide" puis une zone "chaude" devant la lentille, le capteur génère une impulsion électrique : "Mouvement détecté".

### La limite fatale
Le capteur PIR ne détecte pas une "présence", il détecte un "déplacement". 
Si vous entrez dans une pièce et que vous vous asseyez sur le canapé pour ne plus bouger, le capteur PIR ne détecte plus aucune variation de chaleur entre les secteurs de sa lentille. Pour lui, la pièce est vide. Il va donc déclencher sa temporisation (souvent réglée sur 2, 5 ou 10 minutes) puis couper la lumière.

C'est un capteur binaire : mouvement = actif, calme = vide. Ce n'est pas un capteur de présence. Utiliser un PIR pour automatiser un éclairage de salon, de bureau ou de salle de bain est voué à l'échec technique. C'est une technologie parfaite pour un couloir (où l'on ne fait que passer), mais totalement inadaptée pour une pièce de vie.

## La révolution mmWave : Le capteur qui voit tout

La domotique a basculé dans une nouvelle ère avec l'arrivée des capteurs de présence basés sur la technologie millimétrique (mmWave - Millimeter Wave).

### Le radar domestique
Contrairement au PIR qui regarde les variations thermiques, le capteur mmWave émet des ondes radio à haute fréquence. Ces ondes rebondissent sur les surfaces de la pièce et reviennent vers le capteur. 
Le processeur interne analyse la signature de ces ondes réfléchies. Si un humain est présent, même s'il ne bouge pas, son corps provoque des micro-modifications de ces ondes réfléchies. 
Le mouvement de votre cage thoracique dû à votre respiration, le battement de votre cœur, ou le très léger tressaillement d'un membre suffisent au capteur pour comprendre qu'il y a une masse biologique qui occupe l'espace.

Le résultat est stupéfiant. Vous pouvez lire, dormir, ou rester concentré sur votre écran d'ordinateur pendant des heures sans bouger, la lumière restera allumée. La domotique bascule enfin d'une gestion "par mouvement" à une gestion "par présence".

## Les enjeux techniques des capteurs mmWave

Si le mmWave est supérieur, pourquoi ne l'utilise-t-on pas partout ? Parce que cette technologie est beaucoup plus complexe et sensible que le PIR.

### 1. La sensibilité aux interférences
Le radar mmWave est tellement sensible qu'il peut détecter des mouvements parasites. 
*   **Les ventilateurs de plafond :** Un ventilateur qui tourne peut être confondu avec une présence humaine par des modèles bas de gamme.
*   **Les rideaux :** Un rideau qui bouge au vent peut tromper le capteur.
*   **Les animaux de compagnie :** Un gros chat ou un chien qui bouge peut maintenir la zone "présente" activée indéfiniment.

Il faut donc paramétrer la zone de détection dans le capteur. La plupart des capteurs mmWave modernes (comme l'Aqara FP2) permettent de définir des "zones d'exclusion". Vous pouvez dire au capteur d'ignorer la zone du ventilateur, ou la zone où se trouve le bac à chat, tout en restant vigilant sur votre zone de canapé. C'est une configuration qui demande quelques minutes, mais qui garantit une précision de chirurgien.

### 2. Le câblage et l'alimentation
Le PIR fonctionne sur pile bouton pendant deux ans. Le mmWave, à cause du traitement numérique en temps réel du signal radar, consomme beaucoup trop pour une pile. Ces capteurs doivent être branchés sur le secteur (généralement via un connecteur USB). 

Cela impose une contrainte d'aménagement : il faut une prise électrique ou un point d'alimentation proche de l'endroit où vous voulez installer le capteur. C'est une contrainte, certes, mais c'est le prix à payer pour l'intelligence de présence.

## Choisir le bon capteur : Le guide d'usage

La domotique n'est pas une solution universelle. Vous devez mixer les technologies pour créer un réseau robuste.

### Où utiliser le PIR (Mouvement)
Le capteur PIR reste un outil indispensable pour les zones de passage :
- **Couloirs :** Un PIR suffit largement à allumer la lumière quand vous passez.
- **Entrées :** Pour une détection rapide lors de votre arrivée.
- **Escaliers :** Idéal pour accompagner votre montée/descente sans allumer toute la maison.
- **Garages :** Détecter une entrée rapide.
Ils sont peu chers, faciles à cacher, et leur batterie dure une éternité.

### Où utiliser le mmWave (Présence)
Le mmWave est indispensable dans les pièces où vous restez statique :
- **Salons :** Pour lire ou regarder la télévision sans que tout s'éteigne.
- **Bureaux :** Pour automatiser le chauffage ou l'éclairage de travail en fonction de votre présence devant l'écran.
- **Salles de bain :** Pour éviter que la lumière ne s'éteigne pendant que vous êtes sous la douche ou sur vos toilettes.
- **Chambres à coucher :** Pour automatiser des scènes "nuit" sans risque de réveil inopiné.

## L'architecture logicielle : Fusionner les deux

La méthode d'architecte domotique consiste à utiliser les deux technologies ensemble pour une redondance parfaite.

Dans une pièce de vie, vous pouvez placer un capteur mmWave au centre pour gérer la présence statique (le canapé, le coin lecture), et un PIR à l'entrée pour gérer la réactivité. 
En utilisant des outils comme Home Assistant, vous créez un groupe de capteurs. 
*   *SI (PIR détecte mouvement) OU (mmWave détecte présence) ALORS Allumer lumière.*

Cela permet d'avoir la rapidité de déclenchement du PIR (0,5s) alliée à la constance de la présence du mmWave. Vous avez le meilleur des deux mondes.

## L'avenir du mmWave : Vers la reconnaissance de posture

La technologie mmWave ne s'arrête pas à la détection de présence immobile. La nouvelle génération de capteurs, qui commence à arriver sur le marché en 2026, intègre des fonctions de "reconnaissance de posture".

En analysant de manière encore plus fine les ondes radar, le processeur du capteur peut maintenant faire la différence entre une personne qui est debout, une personne assise sur un canapé, et une personne allongée sur le sol. 

Pourquoi est-ce révolutionnaire ? 
*   **Sécurité des personnes âgées :** Le capteur peut détecter une chute. Contrairement aux caméras qui posent des problèmes de vie privée, le radar mmWave détecte une position anormale (allongé sur le sol dans une zone de non-mouvement) et envoie une alerte critique sans jamais filmer quoi que ce soit. C'est la solution ultime pour le maintien à domicile.
*   **Automatisation de sommeil :** Le capteur peut savoir que vous êtes allongé dans votre lit. Il peut alors déclencher une automatisation "Sommeil" (fermeture des volets, extinction totale, armement de l'alarme périmétrique) de manière automatique, sans aucune intervention de votre part.

Cette technologie de reconnaissance de posture va transformer les futurs capteurs domotiques en véritables gardiens de la santé et du confort, bien au-delà de la simple gestion de l'éclairage.

## Installation et intégration : Quelques conseils d'expert

Installer un capteur mmWave ne se fait pas au hasard. La plupart des capteurs fonctionnent par émission d'un cône de détection. 

1. **Hauteur optimale :** Contrairement au PIR qu'on place souvent en hauteur, le mmWave gagne souvent à être placé à hauteur d'homme ou légèrement au-dessus (entre 1m50 et 2m). 
2. **Zones d'exclusion :** Si votre capteur voit une fenêtre avec un rideau qui bouge, ou un ventilateur de plafond, il va déclencher une présence permanente. Prenez le temps de configurer les zones d'exclusion dans votre application domotique. C'est une étape de configuration obligatoire.
3. **Le "Sensitivity level" (Sensibilité) :** La plupart des capteurs ont un réglage de sensibilité de 1 à 10. Ne mettez pas systématiquement 10. Si vous le mettez trop haut, le capteur pourra détecter des mouvements derrière un mur fin ou à travers une porte entrouverte. Commencez par une sensibilité moyenne (5 ou 6) et affinez selon les besoins.

En domotique, la précision vient toujours de la patience lors de la configuration. Le matériel est impressionnant, mais c'est votre capacité à ajuster ces paramètres qui fera la différence entre une automatisation magique et un comportement erratique. 

## Le verdict : La fin du mouvement pour la présence

En 2026, l'utilisation de simples capteurs PIR pour automatiser les pièces de vie est une erreur de débutant. Si votre maison ne sait pas que vous êtes assis, elle est "connectée", mais elle n'est pas "intelligente". 

La technologie mmWave est l'une des rares avancées domotiques de ces dernières années qui a un impact immédiat, visible et positif sur le confort de tous les occupants de la maison. En adoptant ces radars miniatures, vous passez de la détection brutale au pilotage fin. Vous offrez à votre maison la capacité de comprendre que vous êtes là, que vous êtes calme, et que vous n'avez pas besoin d'être interrompu dans votre lecture.

C'est cet aspect "humain" de la technologie, cette capacité à respecter le calme tout en assurant le service, qui définit la réussite d'une installation domotique moderne. Oubliez vos vieux PIR pour le salon et passez à la détection de présence réelle. C'est, sans aucun doute, le changement le plus spectaculaire que vous pouvez apporter à votre installation dès aujourd'hui.
