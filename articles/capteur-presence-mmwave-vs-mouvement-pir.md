---
layout: article.njk
title: "Agiter les bras dans le noir : pourquoi vos capteurs de mouvement ruinent votre domotique"
date: 2025-12-18
tags: ["article", "Matériel", "Architecture"]
image: "/images/capteur-presence-mmwave-vs-mouvement-pir.webp"
summary: "Vous êtes fatigué de devoir faire de grands gestes aux toilettes ou sous la douche pour rallumer la lumière ? Découvrez la différence fondamentale entre la détection de mouvement (PIR) et la véritable détection de présence (mmWave), et comment repenser l'éclairage automatisé de vos pièces à vivre."
---

La scène est universelle et profondément humiliante. Vous êtes tranquillement installé aux toilettes en train de lire un article sur votre smartphone, ou sous la douche en train de vous détendre après une longue journée de travail. Soudainement, le noir complet. L'automatisme domotique que vous aviez si fièrement configuré le week-end précédent vient de décider que la pièce était vide. Vous voilà contraint d'agiter frénétiquement les bras en l'air, comme un naufragé sur une île déserte, dans l'espoir qu'un petit capteur blanc collé au plafond daigne rallumer la lumière.

C'est l'expérience exacte qui fait détester la maison connectée au reste de la famille. L'automatisation de l'éclairage est censée apporter du confort et de l'invisibilité. Lorsqu'elle force un humain à modifier son comportement naturel pour satisfaire une machine, l'architecture globale est un échec.

Le responsable de ce fiasco technologique n'est pas votre box domotique, ni vos scénarios. Le coupable est le capteur matériel lui-même, et plus précisément la technologie infrarouge sur laquelle repose l'immense majorité des équipements du marché grand public. 

Pour corriger ce problème définitivement, il faut comprendre les limites physiques de la détection de mouvement classique et basculer vers une technologie radicalement différente : le radar millimétrique.

## L'illusion de la présence : comment fonctionne vraiment le PIR

Quasiment tous les détecteurs vendus à bas prix (qu'ils soient de marque Xiaomi, Aqara standard, Sonoff ou Philips Hue) utilisent la technologie PIR pour "Passive Infrared" (Infrarouge Passif). 

Le fonctionnement d'un capteur PIR est basique et éprouvé depuis des décennies dans les alarmes de sécurité. Le boîtier contient un capteur pyroélectrique caché derrière une lentille en plastique striée (la lentille de Fresnel). Ce composant ne "voit" pas la pièce comme une caméra. Il se contente de mesurer la température ambiante sous forme de rayonnement infrarouge. 

Lorsqu'un corps humain chaud (environ 37°C) traverse le champ de vision du capteur, il crée une perturbation thermique. La lentille de Fresnel découpe l'espace en plusieurs faisceaux invisibles. Pour que le capteur déclenche l'alerte "Mouvement détecté", il faut qu'une source de chaleur passe d'un faisceau à un autre. Il faut donc un mouvement physique ample et transversal.

Le capteur PIR est aveugle à la présence statique. Si vous êtes assis sur le canapé devant un film, ou immobile sur le trône de vos toilettes, votre signature thermique ne traverse plus les différents faisceaux de la lentille. Pour le composant électronique, vous avez littéralement disparu de la pièce. La temporisation de votre scénario d'éclairage commence son décompte, et la lumière s'éteint.

## Le piège matériel de la batterie et du temps de "refroidissement"

La limitation technologique du PIR est aggravée par une contrainte énergétique. Pour qu'un capteur PIR soit facile à placer n'importe où (au plafond, dans un coin de mur), les fabricants les conçoivent pour fonctionner sur de simples piles boutons (CR2032 ou CR2450) pendant un à deux ans.

Pour atteindre une telle autonomie, le capteur ne peut pas communiquer en permanence avec votre serveur domotique. Il intègre un mécanisme de mise en veille matérielle appelé le "blind time" ou temps d'aveuglement (hardware cooldown). 

Concrètement, lorsqu'il détecte votre entrée dans la salle de bain, il envoie le signal radio (Zigbee ou Wi-Fi) pour allumer la lumière, puis il se désactive complètement sur le plan matériel pendant 60 à 90 secondes pour économiser sa pile. Pendant cette minute d'aveuglement, vous pouvez danser la salsa, le capteur ne verra rien et n'enverra aucune mise à jour à votre système central. Il ne se réveillera qu'à la fin de son cycle de sommeil pour vérifier si ça bouge encore. C'est cette latence matérielle incompressible qui rend la détection de présence si hasardeuse avec des composants sur pile.

## L'échec des rustines logicielles

Face à cette limite matérielle, les débutants en domotique tentent systématiquement de résoudre le problème via des solutions logicielles (des "hacks" dans les scénarios). Ces rustines finissent toujours par montrer leurs failles.

La première tentative consiste à augmenter la minuterie de la lumière. Au lieu de couper après 2 minutes sans mouvement, vous paramétrez l'extinction après 15 ou 20 minutes. Le problème des bras agités aux toilettes est partiellement masqué, mais vous venez de détruire l'intérêt écologique et économique de la domotique. La lumière restera allumée un quart d'heure pour rien à chaque fois que quelqu'un entrera 10 secondes dans la pièce pour se laver les mains.

La seconde tentative, plus élégante sur le papier, consiste à croiser les données avec un capteur d'ouverture de porte. Le scénario devient complexe : "Si la porte se ferme et qu'un mouvement a été détecté juste avant, alors la pièce est occupée, ignorer le capteur de mouvement et laisser allumé jusqu'à la réouverture de la porte". 
Cette logique d'état (State Machine) fonctionne jusqu'à ce qu'elle se confronte à la réalité du quotidien. Que se passe-t-il si un enfant laisse la porte entrouverte ? Que se passe-t-il si deux personnes entrent l'une après l'autre et qu'une seule ressort ? Le système perd le fil de la réalité, la lumière reste bloquée allumée toute la journée, et la confiance de la famille dans l'installation chute à zéro.

J'ai personnellement passé des nuits entières à coder des algorithmes bayésiens dans Home Assistant pour essayer de deviner si une pièce était occupée en me basant sur des capteurs PIR. Le résultat n'a jamais été fiable à 100%. Il n'y a pas de miracle logiciel pour compenser un capteur matériel inadapté.

## La révolution du radar millimétrique (mmWave)

La solution définitive à ce problème porte un nom barbare : le radar à ondes millimétriques (mmWave). C'est la technologie qui sépare aujourd'hui les installations amateurs des véritables maisons intelligentes haut de gamme.

Contrairement au PIR qui attend passivement qu'une source de chaleur croise son champ de vision, le capteur mmWave est actif. Il émet en permanence un signal radar à très haute fréquence (généralement dans la bande des 24 GHz, 58 GHz ou 60 GHz) et analyse l'onde qui rebondit sur les objets et les murs pour revenir vers lui. C'est le principe de l'écholocation utilisé par les chauves-souris ou les sonars de sous-marins, appliqué aux ondes électromagnétiques.

La précision de ces radars est chirurgicale. Ils ne cherchent pas un bras qui s'agite. Ils sont capables de détecter le micro-mouvement de votre cage thoracique qui se soulève lorsque vous respirez. Ils peuvent capter les infimes vibrations de vos doigts tapant sur l'écran d'un smartphone. Même si vous êtes parfaitement immobile, caché derrière le rideau de douche ou en train de lire un livre sur le canapé, le radar sait que vous êtes là, avec une précision millimétrique. L'état du capteur reste sur "Occupé" de manière continue, ininterrompue, jusqu'à ce que la masse biologique quitte physiquement la pièce.

Les modèles les plus avancés du marché, comme le très populaire Aqara FP2, exploitent cette technologie pour aller encore plus loin. Ils ne se contentent pas de dire si la pièce est vide ou pleine. Ils cartographient l'espace en 3D. Ils permettent de définir des zones virtuelles dans une seule pièce : le coin télévision, le coin repas, le canapé. Un seul capteur peut allumer la liseuse si vous êtes sur le fauteuil, et l'éteindre si vous passez à la table de la salle à manger, avec une latence quasi nulle.

## La contrainte énergétique de l'excellence

Cette perfection technologique s'accompagne d'une exigence incontournable : l'alimentation électrique.

Un radar mmWave émettant et analysant des ondes en continu consomme infiniment plus d'énergie qu'un capteur infrarouge passif qui dort 99% du temps. Il est technologiquement impossible de faire tourner un capteur de présence mmWave performant sur une pile bouton. 

Tous les vrais capteurs mmWave du marché exigent une alimentation filaire permanente. Ils se branchent en USB sur une prise secteur (avec un chargeur 5V classique). Cette contrainte de câblage oblige à repenser le placement de l'équipement. Vous ne pourrez plus le coller discrètement avec du double face au milieu du plafond sans tirer un câble disgracieux. Il faudra le poser sur un meuble, l'intégrer dans une bibliothèque, ou le brancher directement sur une prise murale en hauteur.

C'est le prix à payer pour l'infaillibilité. Un capteur alimenté sur secteur ne s'endort jamais. Il n'a aucun "blind time". Il signale votre présence à la seconde où vous franchissez le pas de la porte, et confirme que la pièce est vide à la seconde où vous en sortez. L'extinction de la lumière peut alors être réglée sur une minuterie extrêmement agressive (par exemple 10 secondes après la détection de vide), ce qui engendre de réelles économies d'électricité, impossibles à obtenir avec du PIR sur batterie.

## 24 GHz contre 60 GHz : la guerre des fréquences

Le marché des radars domotiques est en pleine explosion, et de nombreux modèles asiatiques inondent les boutiques à des prix très variables. Le critère technique majeur à vérifier avant l'achat est la fréquence de fonctionnement du radar.

Les modèles d'entrée de gamme (souvent sous l'écosystème Tuya) utilisent la bande des 24 GHz. Cette fréquence est très efficace, traverse parfois les murs fins (le placo), ce qui peut être un avantage ou un énorme inconvénient. Un radar 24 GHz mal réglé dans une salle de bain risque de détecter la personne qui marche dans le couloir juste derrière la cloison, et gardera la lumière allumée. Il demande un travail de calibrage minutieux de la sensibilité.

Les modèles plus récents et plus onéreux basculent sur la bande des 58 GHz ou 60 GHz. Plus la fréquence est élevée, plus la longueur d'onde est courte. Un radar 60 GHz est d'une précision diabolique sur les micro-mouvements (comme le rythme cardiaque) et a beaucoup moins tendance à traverser les obstacles solides. Son faisceau est plus propre, plus franc, limitant drastiquement les faux positifs (les déclenchements fantômes). 

## L'architecture hybride : le meilleur des deux mondes

Faut-il pour autant jeter tous vos capteurs PIR à la poubelle ? Certainement pas. L'ingénierie réseau consiste à utiliser la bonne technologie au bon endroit.

Le capteur PIR excelle dans la réactivité instantanée à très faible coût. Il reste le maître incontesté des "zones de transit". Les couloirs, les escaliers, les dressings ou le garage sont des espaces où vous ne restez jamais immobile. La détection de mouvement classique y est parfaitement justifiée. Un capteur PIR sur pile à 10 euros fera un travail fantastique pour allumer l'escalier le temps de monter les marches.

Le radar mmWave, en raison de son coût (souvent entre 40 et 80 euros) et de sa contrainte de câblage, doit être sanctuarisé pour les "zones de vie statiques". Le salon, la salle à manger, le bureau de télétravail, et surtout les salles de bain et les toilettes.

L'architecture ultime, celle qui frôle la perfection, consiste à combiner les deux technologies de manière hybride dans la même pièce. Les fabricants de pointe l'ont bien compris. Certains nouveaux capteurs intègrent physiquement un module PIR et un module mmWave dans le même boîtier. 
Le comportement devient redoutable d'efficacité : le PIR, très véloce, détecte l'ouverture de la porte et allume la lumière en quelques millisecondes. Le radar mmWave prend immédiatement le relais pour valider la présence continue, même si vous ne bougez plus d'un cil pendant une demi-heure. Lorsque le radar confirme le vide absolu, l'ordre d'extinction est envoyé instantanément.

## Le verdict

Vivre avec la peur de voir la lumière s'éteindre sous la douche n'est pas une fatalité, c'est un choix matériel inadapté. La détection de présence est un enjeu trop crucial pour le confort d'un foyer pour être confiée à des capteurs infrarouges lents, aveugles et endormis pour économiser leur pile.

Acceptez la contrainte de tirer un petit câble USB dans vos pièces de vie principales et vos pièces d'eau, et investissez dans de véritables radars millimétriques (mmWave). Ce basculement technologique marquera la fin des réglages fastidieux de vos minuteries logicielles. L'éclairage de votre maison connectée deviendra enfin ce qu'il a toujours dû être : magique et totalement invisible pour ses occupants.