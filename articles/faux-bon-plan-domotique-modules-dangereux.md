---
date: '2026-03-04'
image: /images/faux-bon-plan-domotique-modules-dangereux.webp
layout: article.njk
summary: Il est tentant de commander des modules électriques domotiques anonymes sur
  les plateformes asiatiques pour faire des économies. Découvrez pourquoi c'est un
  jeu dangereux pour la sécurité de votre réseau, et surtout, pour la sécurité incendie
  de votre maison.
tags:
- diy-and-tutoriels
- sécurité-and-caméras
- wi-fi-and-réseau
- économies-d'énergie
title: 'Le Faux Bon Plan Domotique : Les Dangers Cachés des Modules Électriques à
  2 Euros'
---



La domotique est un hobby qui peut rapidement coûter cher. Lorsqu'un débutant réalise qu'il a besoin d'une trentaine de micromodules pour domotiser l'ensemble des lumières et des volets roulants de sa maison, la facture théorique grimpe vite au-delà des 600 euros s'il choisit des marques réputées comme Shelly, Fibaro, Legrand ou NodOn.

C'est à ce moment-là que la tentation d'aller sourcer son matériel sur les grandes plateformes de e-commerce asiatiques (AliExpress, Temu, Banggood) devient presque irrésistible. 

Sur ces sites, les algorithmes vous proposent des "Smart Switch Zigbee" ou Wi-Fi sans aucune marque apparente (du *no-name*), vendus entre 2 et 4 euros l'unité. Sur le papier et sur les photos, ils font exactement la même chose que le module européen vendu 25 euros. Ils sont compatibles Tuya, parfois reconnus par Home Assistant, et rentrent dans vos boîtes d'encastrement.

Vous pensez avoir fait l'affaire du siècle. En réalité, vous venez d'introduire un risque majeur au cœur même des murs de votre maison.

Il y a une différence fondamentale entre économiser sur un thermomètre de table de nuit, et économiser sur un composant électronique qui va commuter du courant alternatif à 230 Volts, 24 heures sur 24, caché derrière une cloison en placo.

## L'illusion de la certification CE

Le premier réflexe d'un acheteur prudent est de chercher le fameux logo "CE" (Conformité Européenne) sur la fiche produit. La quasi-totalité des modules électroniques à bas coût vendus depuis l'Asie l'affichent fièrement. 

Cependant, il faut comprendre une faille béante du système de certification. Le marquage CE n'est pas un label de qualité délivré par un organisme indépendant. Dans l'immense majorité des cas, il s'agit d'une démarche d'**auto-certification**. Le fabricant appose lui-même le logo en déclarant sur l'honneur que son produit respecte les normes européennes.

Sur un module *no-name* vendu 2 euros sans véritable entité juridique traçable, ce logo n'a aucune valeur technique. C'est simplement une impression sur un bout de plastique pour passer les douanes. Pire, il existe un logo esthétiquement presque identique (avec un espacement très légèrement différent entre le C et le E) qui signifie "China Export". 

En cas de sinistre électrique, votre assurance habitation missionnera un expert. Si cet expert trouve l'origine du départ de feu dans une boîte d'encastrement contenant un module électronique non certifié acheté hors des circuits de distribution officiels européens, votre compagnie d'assurance sera en droit de refuser toute indemnisation.

## L'anatomie d'un module bas de gamme (Le risque d'incendie)

La différence de prix entre un module à 3 euros et un module à 25 euros ne réside pas seulement dans la marge commerciale. Elle se trouve à l'intérieur du boîtier, sur le circuit imprimé.

Pour casser les prix, les usines rognent sur les composants vitaux :
1.  **Les Relais :** C'est la pièce mécanique qui "claque" pour faire passer le courant. Les modules *no-name* utilisent des micro-relais sous-dimensionnés. Si vous branchez un appareil qui demande une forte puissance au démarrage (un gros moteur de volet, un radiateur électrique ou des gros panneaux LED), les contacts métalliques à l'intérieur du relais vont créer un arc électrique, s'échauffer, fondre, et finir par se souder entre eux de manière permanente (le module reste bloqué sur "Allumé").
2.  **L'isolation galvanique :** Un bon module sépare physiquement le circuit "Basse tension" (la puce radio, l'antenne) du circuit "Haute tension" (le 230V de la maison) avec des optocoupleurs de qualité. Dans un module à très bas coût, cette séparation est minimale. Une surtension sur le réseau peut littéralement faire exploser la puce Zigbee.
3.  **Le manque de protection thermique :** Une marque comme Shelly intègre un capteur de température directement *à l'intérieur* de chacun de ses modules. Si le composant détecte qu'il dépasse les 90°C (à cause d'une mauvaise connexion ou d'une surcharge), il coupe immédiatement le courant par sécurité logicielle. Un module à 2 euros n'a aucune protection thermique. Il continuera de fonctionner jusqu'à prendre feu.

J'ai personnellement démonté un vieux module bas de gamme qui gérait l'éclairage de mon garage après avoir senti une légère odeur de plastique brûlé. Le plastique autour du bornier de phase était noirci et complètement fondu. Ce module est passé à quelques degrés près de déclencher un feu de cloison.

## L'instabilité réseau (Les routeurs toxiques)

Le danger n'est pas que physique, il est aussi numérique. Comme nous l'avons expliqué dans notre article sur **[l'optimisation des piles Zigbee](/articles/autonomie-piles-capteurs-domotique/)**, chaque module branché sur le secteur fait office de "Routeur" (répéteur) pour vos autres appareils.

C'est une excellente chose... à condition que ce routeur soit compétent.

Le firmware (logiciel interne) des puces Zigbee *no-name* est souvent bâclé et jamais mis à jour par le fabricant (qui a souvent disparu six mois après la mise en vente du produit). Ces modules "toxiques" ont la fâcheuse habitude d'accepter les connexions des capteurs sur pile environnants, puis de "perdre" ou d'oublier de relayer leurs messages vers la box domotique. 

Vous vous retrouvez alors avec des détecteurs de mouvement qui ne répondent plus de manière aléatoire. Vous pensez que votre box Home Assistant ou Homey a un problème, alors que le coupable est le petit relais de mauvaise qualité caché derrière l'interrupteur, qui détruit le maillage de tout votre réseau.

## Sur quoi pouvez-vous vraiment faire des économies ?

Ce constat alarmant ne signifie pas qu'il faut fuir l'ensemble du matériel asiatique. Il existe d'excellentes marques chinoises extrêmement réputées (comme Aqara ou Sonoff) qui fabriquent du matériel fantastique à des prix très compétitifs.

L'ingénierie domotique demande d'appliquer la règle du bon sens : **ne faites jamais d'économie sur ce qui touche directement au courant alternatif 230V.**

Voici comment répartir votre budget intelligemment :

*   **Ce qu'il faut acheter chez des marques certifiées (Shelly, Fibaro, Legrand, NodOn) :** Les micromodules encastrés, les disjoncteurs connectés pour le tableau électrique, les relais pour ballon d'eau chaude, les prises connectées de forte puissance. Ces équipements gèrent la sécurité de la maison. Le prix fort se justifie.
*   **Ce que vous pouvez acheter à petit prix (Marques asiatiques ou no-name) :** Tout ce qui fonctionne sur pile bouton ou basse tension (5V USB). Les capteurs d'ouverture de porte, les thermomètres, les **[détecteurs de présence](/articles/capteur-presence-mmwave-vs-mouvement-pir/)**, les petits boutons poussoirs sans fil à poser sur la table de nuit.

Si un thermomètre *no-name* à 3 euros prend feu (ce qui est physiquement presque impossible avec une pile 3V), au pire, il fera un petit trou noir sur votre mur. Si un relais 230V *no-name* de 3000 Watts prend feu derrière une cloison en bois, les conséquences ne sont plus du tout les mêmes.

## Le verdict

La sécurité de votre foyer et de votre famille ne vaut pas une économie de quelques centaines d'euros sur un budget global de rénovation électrique. 

Considérez les modules de commutation domotique comme du matériel électrique à part entière, au même titre qu'un disjoncteur différentiel sur votre tableau général. Vous ne confieriez pas la sécurité de votre tableau électrique à une marque inconnue achetée sans garantie sur un site lointain. Appliquez exactement la même logique aux composants qui se cachent derrière vos interrupteurs muraux. Achetez de la qualité européenne certifiée pour la puissance électrique, et gardez le *low-cost* asiatique pour les petits capteurs inoffensifs.
