---
layout: article.njk
title: "Tablettes murales domotiques : la fausse bonne idée (et comment bien le faire)"
date: 2026-03-11
tags: ["article", "Architecture", "Matériel"]
image: "https://images.unsplash.com/photo-1585338107529-13afc5f02586?q=80&w=1200&auto=format&fit=crop"
summary: "Accrocher un vieil iPad au mur du salon pour piloter toute la maison est le fantasme de tout domoticien. C'est aussi le projet qui échoue le plus souvent. Découvrez les erreurs fatales qui détruisent la batterie de la tablette et les solutions professionnelles pour créer un vrai tableau de bord de contrôle."
---

C'est l'image d'Épinal de la maison du futur, celle que l'on voit dans tous les films de science-fiction et sur les brochures des constructeurs immobiliers : le grand écran tactile fixé au mur de l'entrée, affichant un magnifique plan 3D de la maison, la météo, le flux des caméras de sécurité et le contrôle absolu de chaque ampoule.

Portés par cette vision, de nombreux passionnés décident de recycler une vieille tablette Android ou un iPad vieillissant. Ils achètent un support d'impression 3D sur internet, collent l'écran au mur du salon, et laissent l'application de leur box domotique affichée en permanence. 

L'effet "Wahou" auprès des invités est garanti. Pourtant, six mois plus tard, la tablette est souvent éteinte, débranchée, ou pire, sa batterie a tellement gonflé qu'elle a fendu l'écran. 

La mise en place d'un "Dashboard" (tableau de bord) mural est l'un des projets les plus complexes à réaliser proprement. Ce n'est pas un problème logiciel, c'est un problème matériel et d'ergonomie (le fameux **[WAF - Wife Acceptance Factor](/articles/waf-domotique-acceptation-famille/)**).

## L'erreur fatale : la gestion désastreuse de l'alimentation

Le premier responsable de la mort prématurée des tablettes murales est le câble de charge. 

Une tablette grand public (Apple ou Samsung) n'est absolument pas conçue pour être branchée sur le secteur 24 heures sur 24, 7 jours sur 7. Les batteries au lithium-ion détestent être maintenues en permanence à 100% de charge. Sous cette contrainte constante, la chaleur s'accumule à l'intérieur du châssis collé contre le mur. 

Au bout de quelques mois d'alimentation ininterrompue, la réaction chimique à l'intérieur des cellules de la batterie dégénère. La batterie se met à dégager du gaz, elle gonfle (on appelle cela le *spicy pillow*), et finit par faire exploser la vitre de la tablette ou déformer la coque. C'est un risque d'incendie bien réel qui est totalement sous-estimé par les débutants.

Pour éviter cela, il existe deux approches d'ingénierie viables :

### La solution logicielle : Le cycle de charge domotisé
Puisque vous installez un écran domotique, utilisez la domotique pour le protéger ! 
Branchez le chargeur USB de la tablette sur une **[prise connectée ou un micromodule de bonne qualité](/articles/danger-domotique-pas-cher-incendie/)**. 

Installez une application compagnon sur la tablette (comme l'excellente application officielle *Home Assistant Companion* pour Android). Cette application est capable de lire le pourcentage de batterie de la tablette et de l'envoyer à votre cerveau domotique. 

Il ne vous reste plus qu'à créer l'automatisation de survie :
*   *SI la batterie de la tablette descend en dessous de 20%, ALORS allumer la prise connectée du chargeur.*
*   *SI la batterie de la tablette atteint 80%, ALORS éteindre la prise connectée du chargeur.*

Grâce à ce simple scénario, la tablette effectuera des cycles de charge/décharge naturels, exactement comme si vous l'utilisiez sur votre canapé. Sa durée de vie sera décuplée et le risque de gonflement totalement écarté.

### La solution matérielle radicale : Le retrait de la batterie
Pour les plus bricoleurs qui souhaitent une installation définitive, la solution ultime consiste à ouvrir la tablette (souvent de vieilles tablettes Android comme les Amazon Fire HD), déconnecter physiquement la batterie au lithium, et la remplacer par un petit module convertisseur de tension abaissant le courant d'une alimentation fixe à la tension exacte requise par la carte mère (généralement autour de 4 volts). 
La tablette devient un véritable moniteur mural câblé en dur, sans aucune batterie, écartant 100% des risques d'incendie.

## Le problème de l'écran toujours allumé

La deuxième erreur consiste à laisser l'écran allumé au maximum de sa luminosité de jour comme de nuit. 

Au-delà de la consommation électrique absurde et du fait que la tablette se transformera en un puissant phare éblouissant le salon à 3 heures du matin, cela pose un problème technique majeur si votre tablette utilise un écran OLED (comme certaines Samsung Galaxy Tab). Une image fixe, affichée en continu pendant des jours, finira par "brûler" la dalle (le fameux effet de *burn-in*). Les icônes de votre tableau de bord resteront fantomatiques sur l'écran pour toujours.

La bonne pratique architecturale consiste à gérer l'allumage de la tablette comme on gère la lumière d'une pièce : avec de **[véritables capteurs de mouvement](/articles/capteur-presence-mmwave-vs-mouvement-pir/)**.

L'écran de la tablette doit être éteint ou en veille profonde par défaut. Vous utilisez la caméra frontale de la tablette (via des applications comme *Fully Kiosk Browser* sur Android), ou un capteur PIR situé dans l'entrée, pour détecter l'approche d'un être humain. Dès que quelqu'un passe à moins de deux mètres de l'écran, la tablette se réveille instantanément pour afficher les commandes. 

## L'échec ergonomique : Trop d'informations tuent l'information

Même avec une tablette parfaitement alimentée et un écran qui s'allume intelligemment, le projet peut échouer à cause de ce qui est affiché à l'écran.

Les technophiles ont la fâcheuse habitude de vouloir afficher **tout** ce que leur système sait faire. Le premier tableau de bord ressemble souvent à un cockpit d'avion de ligne : 45 boutons minuscules, la température du processeur du routeur Wi-Fi, la courbe de variation du taux d'humidité de la cave, et l'espace libre sur le disque dur du NAS.

C'est fascinant pour celui qui l'a programmé, mais c'est totalement illisible pour le reste de la famille. Quand quelqu'un veut éteindre la lumière du couloir, il ne veut pas avoir à chercher une icône de 5 millimètres au milieu d'un graphique de consommation électrique.

Pour réussir l'intégration de votre écran mural, vous devez respecter le design "UI/UX" (Expérience Utilisateur) :

1.  **Gros boutons, actions simples :** La page d'accueil ne doit contenir que les actions critiques et quotidiennes. Un énorme bouton pour armer l'alarme en partant. Un bouton pour éteindre toutes les lumières. Un bouton d'ouverture du portail. L'icône doit faire au minimum la taille d'une pièce de 2 euros pour être frappée sans regarder.
2.  **L'approche conditionnelle :** Un bon tableau de bord domotique ne vous montre pas les boutons qui ne servent à rien. Le bouton "Fermer les volets" ne devrait apparaître à l'écran que lorsque le soleil est couché. Le flux de la caméra de sécurité ne devrait apparaître en grand que si quelqu'un a sonné à la porte. 
3.  **Reléguons la complexité :** Si vous voulez garder vos jolis graphiques de température de la cave pour votre propre plaisir de technicien, placez-les sur une "page 2", accessible uniquement en glissant le doigt vers la droite. La page 1 doit rester d'une pureté absolue.

## Le verdict : Un bon bouton poussoir vaut souvent mieux

Avant de vous lancer dans la découpe de votre mur (placo) pour y incruster une alimentation USB et une tablette 10 pouces, posez-vous sérieusement la question du besoin réel.

L'immense majorité des actions quotidiennes dans une maison connectée (allumer, éteindre, fermer les volets) se fait de manière beaucoup plus intuitive, rapide et fiable avec un petit bouton sans fil posé sur un meuble (type bouton connecté Aqara ou télécommande Hue). Vous n'avez pas besoin de regarder un bouton physique pour appuyer dessus en passant la porte. Vous devez en revanche vous arrêter, fixer l'écran tactile mural, et viser la bonne case pour faire la même chose.

La tablette murale n'a de sens que pour la visualisation de données complexes (vérifier l'identité de la personne qui sonne au portail, consulter la météo complète du lendemain avant de s'habiller, ou ajuster de manière chirurgicale la température de plusieurs zones de chauffage). 

Si c'est pour remplacer vos interrupteurs, abandonnez le projet de la tablette murale. Si c'est pour créer un véritable poste de contrôle centralisé et épuré, armez-vous de patience, d'une prise connectée pour la charge, et d'un grand sens de la simplicité visuelle.
