---
date: '2026-03-12'
image: /images/volets-roulants-radio-somfy-vs-filaire-domotique.webp
layout: article.njk
summary: Votre menuisier vous propose des volets roulants radio avec télécommande
  car c'est 'plus moderne' ? Découvrez pourquoi c'est un piège technologique qui vous
  enfermera dans un écosystème fermé, et pourquoi le moteur filaire classique est
  la seule véritable option pour une domotique libre.
tags:
- cloud-vs-local
- diy-and-tutoriels
- débutant-en-domotique
- waf-and-famille
title: 'Le piège des volets roulants radio : pourquoi exiger des moteurs filaires'
---


Le scénario est un classique absolu de la construction neuve ou de la rénovation lourde. Vous faites appel à un menuisier ou à un façadier pour changer l'ensemble de vos menuiseries et installer des volets roulants motorisés. Le chantier est important, le budget se compte en milliers d'euros. Au moment d'affiner le devis, l'artisan vous pose une question qui semble relever du simple détail pratique : *"Pour la motorisation, je vous mets des moteurs radio avec une petite télécommande sans fil pour chaque fenêtre, ou bien on part sur des moteurs filaires avec un interrupteur classique encastré dans le mur ?"* 

Séduit par la perspective alléchante de ne pas avoir de saignées disgracieuses à faire dans vos murs neufs, et par l'idée confortable de piloter vos volets depuis votre lit avec une petite télécommande blanche, vous optez presque machinalement pour la technologie radio. L'artisan est généralement ravi de ce choix : l'installation est infiniment plus rapide et plus simple pour lui, puisqu'il n'a qu'à tirer un simple câble d'alimentation électrique vers le coffre du volet, sans se soucier de redescendre vers un point de commande manuel à hauteur d'homme. C'est du temps de main d'œuvre gagné.

Vous venez pourtant, sans le savoir, de commettre l'une des erreurs d'architecture domotique les plus coûteuses et les plus complexes à rattraper par la suite. Vous venez littéralement d'enfermer la gestion de vos ouvertures — sans doute l'élément le plus critique pour la sécurité et la régulation thermique de votre foyer — dans une prison technologique propriétaire et hermétique. 

L'intégration d'un système radio natif dans un volet roulant est une hérésie pour quiconque souhaite construire une maison connectée fiable, pérenne et interopérable. Décryptage d'un faux ami technologique et retour aux fondamentaux de l'électricité.

## Le mirage de la modernité et l'enfermement propriétaire (Vendor Lock-in)

L'argument principal de vente des moteurs de volets radio (dominés sur le marché européen par des géants comme Somfy ou Bubendorff) est la modernité et la simplicité apparente. La réalité technique est radicalement différente : il s'agit d'un modèle économique basé sur le verrouillage commercial absolu, un concept connu en ingénierie sous le nom de "Vendor Lock-in".

Lorsqu'un constructeur intègre un récepteur radio directement à l'intérieur du cylindre du moteur de votre volet roulant, il utilise un langage de communication qui lui est propre. Prenons l'exemple du très répandu protocole "IO Homecontrol", massivement poussé par Somfy, Velux et Atlantic. Ce protocole a été spécifiquement conçu par un consortium de marques pour être un système fermé, hautement chiffré et exclusif. 

Le jour où vous décidez de franchir le cap de la vraie domotique — par exemple, pour fermer automatiquement les volets des façades sud en été lorsque le soleil tape, ou pour baisser l'ensemble des ouvrants lorsque l'alarme est armée — vous découvrez brusquement l'ampleur du problème. Votre superbe **[superviseur domotique local (Home Assistant, Homey Pro ou Apple HomeKit)](/articles/unifier-applications-domotique/)**, qui est pourtant capable de communiquer avec des milliers d'appareils différents via des standards ouverts comme le Zigbee, le Z-Wave ou Matter, se retrouve totalement incapable de parler avec vos volets. Les ondes radio de ces moteurs sont verrouillées par des clés cryptographiques privées auxquelles vous n'avez pas accès.

Pour réussir à franchir ce mur artificiel, le fabricant a la solution toute trouvée : il vous impose d'acheter sa propre passerelle internet propriétaire (comme la box Tahoma ou Connexoon chez Somfy), vendue entre 150 et 300 euros. Vous êtes alors forcé d'ajouter un boîtier supplémentaire sur votre meuble TV, de créer un énième compte utilisateur avec mot de passe, de télécharger une application de plus sur votre smartphone, et surtout, vous créez une dépendance directe et extrêmement dangereuse à leurs serveurs Cloud. 

Dans cette configuration, lorsque Home Assistant veut fermer un volet, il doit envoyer une requête via internet aux serveurs cloud du fabricant (souvent hébergés à des milliers de kilomètres), qui transmettent ensuite l'ordre à votre box propriétaire locale, qui envoie enfin le signal radio au volet. Si la passerelle du fabricant plante, si votre connexion internet saute, ou pire, si le constructeur décide un jour de couper ses serveurs Cloud ou de rendre son API payante, vos automatisations globales s'effondrent immédiatement. Vous avez payé le matériel au prix fort, mais le contrôle local absolu vous échappe.

## L'absence cruelle du retour d'état : Le drame du protocole RTS

Si vous avez opté pour la génération légèrement plus ancienne (et ironiquement encore moins chère) de moteurs radio, fonctionnant sur le célébrissime protocole RTS de Somfy (Radio Technology Somfy), la situation est techniquement encore pire.

Le protocole RTS fonctionne sur une fréquence de 433 MHz. C'est un protocole strictement unidirectionnel. Cela signifie que la télécommande — ou la box domotique qui parvient à imiter le signal — est capable d'envoyer l'ordre "Descendre" au moteur. Le moteur reçoit l'ordre et s'exécute. Mais à aucun moment, jamais, le moteur ne renvoie un signal pour confirmer qu'il a bien accompli sa tâche. Il n'y a aucun "retour d'état". C'est l'équivalent numérique de jeter une bouteille à la mer.

Imaginez les conséquences sur une installation domotique digne de ce nom. Dans l'interface de votre système, vous cliquez sur le bouton pour fermer le volet de la baie vitrée du salon. Le signal radio part. Mais si un meuble de jardin a été oublié sur le trajet du volet et bloque la descente, si le moteur s'est mis en sécurité thermique après plusieurs manipulations successives, ou si une simple interférence radio (un voisin utilisant un casque sans fil sur la même fréquence) a brouillé le signal d'origine, le volet reste physiquement ouvert. Pourtant, votre application smartphone, aveugle et sourde à ce qui se passe réellement dans le monde physique, affichera avec une certitude trompeuse que le volet est "Fermé à 100%".

Construire des scénarios de sécurité (fermeture nocturne, simulation de présence) ou de régulation thermique stricte sur un système matériel qui ment sur sa position mécanique est une aberration architecturale. La domotique a un besoin viscéral de certitudes factuelles, pas de suppositions statistiques. 

Les protocoles radio fermés plus récents (comme le IO Homecontrol mentionné plus haut) ont corrigé ce défaut en devenant bidirectionnels, offrant un retour d'état. Mais ils conservent leur nature propriétaire et leur dépendance mortifère au Cloud via leurs passerelles imposées. Le problème n'est donc déplacé que d'un cran.

## La question de la maintenance : Le coût caché du tout-en-un

L'intégration poussée a un prix caché très lourd. Fusionner l'intelligence (la carte électronique de réception radio et de traitement du signal) et le muscle (le gros bloc moteur tubulaire mécanique) dans le même cylindre étanche au fond du coffre de votre fenêtre pose un immense problème de maintenance et de réparabilité à long terme.

Il faut être pragmatique : l'électronique grand public vieillit presque toujours beaucoup plus vite que la grosse mécanique. Les condensateurs d'une carte de réception radio soumis à des écarts de températures importants (dans un coffre de volet exposé au soleil de plomb en été et au gel en hiver) finissent par fatiguer. Si la carte de réception radio de votre volet grille à cause d'une surtension sur le réseau électrique ou d'une simple usure des composants, ou si la télécommande propriétaire indispensable au réglage des fins de course tombe en panne et n'est mystérieusement plus fabriquée par la marque cinq ans plus tard, le moteur mécanique en lui-même fonctionne encore de manière parfaitement fluide. 

Pourtant, dans un système radio tout-en-un, vous êtes quasiment systématiquement contraint de remplacer l'intégralité du bloc moteur. C'est une opération lourde, qui nécessite d'ouvrir le caisson (parfois tapissé ou plâtré), de démonter l'axe métallique, de régler à nouveau les attaches, et de dépenser entre 150 et 350 euros pour un moteur neuf, simplement parce qu'une minuscule puce de communication valant deux euros a rendu l'âme. 

J'ai vu des installations domotiques entières paralysées parce qu'une télécommande "maître" centralisée avait été cassée par un enfant, et que la procédure de réappairage d'une nouvelle télécommande nécessitait des manipulations incroyablement fastidieuses (du type "couper le courant au disjoncteur général pendant 2 secondes, rallumer 10 secondes, couper 2 secondes" pour réinitialiser la mémoire des moteurs). C'est une conception punitive pour l'utilisateur final.

## La solution radicale : Le retour au moteur filaire standard à 4 fils

Face à cette somme de contraintes artificielles et de coûts cachés, la seule véritable option pour construire une maison connectée robuste, évolutive et réellement vôtre, semble contre-intuitive pour un débutant : il faut consciemment exiger de votre installateur la technologie la plus ancienne, la plus basique et la plus "bête" du marché. Le bon vieux moteur de volet roulant filaire classique.

Un moteur filaire pur jus ne possède aucune carte électronique de communication complexe, aucune antenne radio, aucune mémoire d'appairage. Il s'agit d'un pur composant électromécanique de puissance. Son fonctionnement repose sur un câble standard contenant quatre fils électriques bien distincts :
1.  **Le fil de Terre (Vert/Jaune) :** Pour la sécurité électrique de l'armature métallique.
2.  **Le fil de Neutre (Bleu) :** Pour le retour du courant.
3.  **Le fil de Phase (souvent Marron) pour la montée :** Si du courant 230V passe dans ce fil, le moteur tourne dans un sens et lève le tablier.
4.  **Le fil de Phase (souvent Noir) pour la descente :** Si du courant 230V passe dans ce fil, le moteur tourne dans le sens inverse et baisse le tablier.

C'est une norme électrotechnique universelle et inébranlable depuis plus d'un demi-siècle. L'intelligence ne réside pas dans le moteur, le moteur se contente d'exécuter bêtement un ordre électrique physique. 

Cette rusticité est son plus grand atout. C'est un matériel quasiment indestructible s'il est bien dimensionné. Il est réparable et compréhensible par absolument n'importe quel électricien professionnel, sans avoir besoin d'une certification spécifique à une marque. Et surtout, c'est un matériel totalement interopérable. Vous n'êtes lié à aucune marque spécifique pour le reste de sa durée de vie. Un moteur filaire d'entrée de gamme à 40 euros acheté dans un magasin de bricolage fonctionnera exactement sur le même principe physique de base qu'un moteur de grande marque allemande à 200 euros.

## Le cerveau caché dans le mur : Les micromodules encastrés

Si le moteur est volontairement "bête", où se trouve l'intelligence qui permet de l'automatiser depuis un smartphone ou un système complexe ? Elle se déporte. Elle quitte le coffre étouffant du volet pour venir se cacher dans vos murs, juste derrière un interrupteur mural filaire tout à fait classique (idéalement de type "bouton poussoir bistable" ou "poussoir double" haut/bas).

C'est là que réside le génie d'une architecture séparée. L'électricien tire le câble à 4 fils du moteur jusqu'à une boîte d'encastrement murale classique (qu'il faut impérativement prévoir profonde, au minimum 50mm, idéalement avec une poche spécifique pour la domotique, ce qu'on appelle les boîtes "à chaussette" type BLM). Dans cette petite boîte en plastique, vous allez glisser un micromodule domotique spécialement conçu pour la gestion des ouvrants.

Le marché regorge de références d'une fiabilité exceptionnelle. On pense immédiatement aux modules Shelly Plus 2PM (qui fonctionnent en Wi-Fi local de manière très robuste), ou aux excellents modules Legrand Netatmo, Fibaro Roller Shutter 3 et NodOn (qui fonctionnent sur des réseaux maillés Zigbee ou Z-Wave). 

Le principe de câblage est rigoureux mais logique. Le micromodule est alimenté en permanence par le réseau électrique de la maison (Phase et Neutre). Les deux fils de commande du moteur (le marron de la montée et le noir de la descente) viennent se visser sur les sorties de puissance (Output) du module. Enfin, les fils venant de l'interrupteur mécanique manuel que vous touchez avec vos doigts viennent se brancher sur les entrées logiques (Input/Switch) du module.

La séparation des pouvoirs devient alors absolue et protectrice : le moteur tubulaire ne fournit plus que la force brute de levage. Le micromodule encastré agit comme le cerveau numérique intelligent, connecté à votre réseau. L'interrupteur mural en plastique agit comme l'interface humaine prioritaire et infaillible d'urgence.

## Le calibrage, le retour d'état réel et le graal du positionnement absolu

En adoptant cette combinaison (moteur "bête" + micromodule intelligent), vous ne faites pas que contourner la prison des écosystèmes propriétaires. Vous débloquez des capacités de contrôle d'une finesse impossible à atteindre autrement.

La quasi-totalité des bons micromodules pour volets intègrent une puce de mesure de consommation électrique en temps réel (le *Power Monitoring*). C'est ce détail technique qui change absolument tout.

Lors de la première installation, vous lancez une procédure de "Calibration" depuis l'application de votre module. Le module va envoyer le courant sur la phase de montée. Il va mesurer un pic de consommation électrique au démarrage du moteur (la force d'arrachement), puis une consommation stable pendant quelques secondes (le volet s'enroule). Au moment précis où le volet arrive tout en haut de sa course et percute sa butée mécanique haute, le moteur se bloque. La consommation électrique chute brutalement à zéro. Le module détecte informatiquement cette chute, coupe immédiatement le relais pour protéger le moteur, et mémorise : *"La position haute m'a pris exactement 14,3 secondes de course"*. Il fait la même chose pour la descente.

Grâce à cette mesure mathématique précise, votre système possède un véritable "Retour d'état absolu". Le module sait en temps réel, grâce au temps de trajet électrique écoulé, où se trouve physiquement le tablier du volet. Vous ne donnez plus des ordres vagues comme "Monte un peu". Vous pouvez exiger à votre système domotique de positionner le volet roulant de la baie vitrée ouest à exactement 42% de fermeture, pour filtrer précisément le soleil direct de 14h00 sur votre canapé sans plonger la pièce dans le noir. Et le volet s'exécutera avec une précision chirurgicale, jour après jour. C'est le graal de la régulation thermique passive.

## Sauver le WAF et rationaliser la maintenance à long terme

Au-delà de la précision technique, l'architecture filaire associée aux micromodules résout les deux plus gros points de friction de la domotique résidentielle : l'acceptation par les autres membres du foyer (le fameux **[WAF - Wife/Husband Acceptance Factor](/articles/waf-domotique-acceptation-famille/)**) et les coûts de réparation.

Concernant l'ergonomie quotidienne, le module se contente de lire les impulsions électriques de l'interrupteur mural filaire. Cela signifie que vous conservez de véritables interrupteurs cliquables et physiques sur vos murs. Pas de télécommandes propriétaires qui se perdent sous les coussins du salon, pas de piles bouton CR2032 à changer tous les deux ans. Quiconque entre dans une chambre — vos invités, vos enfants, la personne qui fait le ménage — saura intuitivement comment baisser le volet en appuyant sur le bouton près de la porte. L'interface manuelle d'urgence fonctionne toujours, instantanément, sans aucune latence, et surtout, elle fonctionne même si votre serveur domotique central (Home Assistant ou autre) est éteint pour mise à jour, ou si votre Wi-Fi est en panne. C'est la définition même de la résilience.

Sur le front de la maintenance, la démonstration financière est écrasante. Si la foudre s'abat près de chez vous et provoque une forte surtension, ou si l'électronique de communication finit par rendre l'âme au bout de huit ans, le gros moteur tubulaire à 200 euros coincé dans l'axe de la fenêtre n'aura strictement rien subi, car l'électronique fragile n'est pas logée à l'intérieur. C'est le petit relais électromagnétique du micromodule caché dans la cloison murale qui aura fondu pour encaisser le choc. 

Il vous suffira de couper le courant au tableau électrique de la maison, de retirer la plaque de l'interrupteur mural avec vos doigts, de dévisser les fils avec un petit tournevis plat, de jeter le module carbonisé et d'en brancher un nouveau à 25 euros. Une opération de maintenance curative qui prend environ douze minutes chrono, qui ne salit pas les murs, qui ne nécessite aucun démontage de menuiserie, et qui coûte dix fois moins cher qu'une intervention sur un volet radio tout-en-un.

Mieux encore, si le monde technologique évolue massivement dans cinq ans et que le protocole Zigbee actuel est définitivement abandonné au profit d'un nouveau standard révolutionnaire, vous ne serez pas prisonnier d'une flotte de volets obsolètes. Vos murs et vos moteurs resteront inchangés. Vous changerez uniquement les petits cerveaux cachés derrière les plastiques de vos interrupteurs, au fur et à mesure de votre budget, pour migrer doucement votre maison vers la nouvelle décennie technologique. L'architecture séparée est la définition même du "Future-Proof".

## Le verdict : Résistez aux installateurs et reprenez le contrôle

Les entreprises de menuiserie, les artisans façadiers et la plupart des constructeurs de maisons individuelles standards détestent viscéralement les moteurs filaires traditionnels. 

La raison est purement logistique et financière pour eux. Tirer un câble électrique 4 fils depuis le haut du coffre de chaque fenêtre, redescendre dans le mur en réalisant des saignées dans la brique ou le placo, intégrer des boîtes d'encastrement profondes, et câbler des interrupteurs manuels demande un temps de main d'œuvre considérable, une véritable expertise en câblage électrique et génère de la poussière. À l'inverse, fixer un moteur radio qui n'a besoin que d'une simple arrivée électrique 230V repiquée n'importe où dans le plafond, puis vous tendre une télécommande en plastique blanc à la fin du chantier prend montre en main cinq minutes par fenêtre.

Leur intérêt de rentabilité à court terme sur votre chantier est diamétralement opposé à la viabilité, l'ouverture et la réparabilité de votre installation domotique à long terme. 

Si vous avez la chance de faire construire, d'entreprendre une rénovation électrique lourde, ou même de simplement faire changer vos menuiseries, soyez absolument intransigeant lors des devis. Refusez catégoriquement, fermement, et avec le sourire les fameuses "options radio modernes IO/RTS", même (et surtout) si le vendeur vous jure solennellement que *"c'est dernier cri et que c'est parfaitement compatible avec votre smartphone via notre application dédiée"*. Vous savez désormais que cette phrase est synonyme de prison technologique cloud et de surcoûts injustifiés.

Exigez noir sur blanc sur le contrat de travaux la pose de moteurs filaires standards à 4 fils de bonne qualité mécanique (Somfy propose d'excellents moteurs filaires mécaniques purs par exemple, il s'agit de la gamme Ilmo ou Solus, tout comme Becker ou d'autres marques historiques). Demandez le tirage des lignes de commande vers des interrupteurs encastrés situés près des fenêtres ou à l'entrée des pièces. 

Le surcoût initial de main d'œuvre lié à l'intervention de l'électricien pour tirer ces quelques mètres de câbles sera sans l'ombre d'un doute le meilleur investissement architectural que vous ferez. Vous payez une fois pour garantir la liberté, l'intelligence, la fiabilité et la longévité de votre maison connectée pour les vingt prochaines années.
