---
layout: article.njk
title: "Le piège des volets roulants radio : pourquoi exiger des moteurs filaires"
date: 2026-03-12
tags: ["article", "Architecture", "Matériel"]
image: "https://images.unsplash.com/photo-1513694203232-719a280e022f?q=80&w=1200&auto=format&fit=crop"
summary: "Votre menuisier vous propose des volets roulants radio avec télécommande car c'est 'plus moderne' ? Découvrez pourquoi c'est un piège technologique qui vous enfermera dans un écosystème fermé, et pourquoi le moteur filaire classique est la seule véritable option pour une domotique libre."
---

Le scénario est un classique de la construction neuve ou de la grosse rénovation. Vous faites appel à un menuisier pour changer l'ensemble de vos fenêtres et installer des volets roulants motorisés. 

Au moment du devis, l'artisan vous pose une question qui semble anodine : *"Je vous mets des moteurs radio avec une petite télécommande sans fil, ou des moteurs filaires avec un interrupteur au mur ?"* 

Séduit par la perspective de ne pas avoir de câbles disgracieux à tirer et par l'idée de piloter vos volets depuis votre canapé, vous optez machinalement pour la technologie radio (souvent de marque Somfy, avec les protocoles RTS ou IO Homecontrol). L'artisan est ravi, l'installation est plus rapide pour lui.

Vous venez pourtant de commettre l'une des erreurs d'architecture domotique les plus coûteuses et les plus difficiles à rattraper. Vous venez d'enfermer la gestion de vos ouvertures dans une prison technologique propriétaire.

## L'illusion du "sans fil" et le Vendor Lock-in

L'argument principal de vente des volets radio est la modernité. La réalité technique est toute autre : c'est un modèle de verrouillage commercial absolu (Vendor Lock-in).

Lorsqu'un moteur de volet roulant intègre son propre récepteur radio, il parle une langue que seul son constructeur comprend. Le protocole IO Homecontrol, par exemple, a été conçu par un consortium de marques (dont Somfy et Velux) pour être fermé et chiffré. 

Le jour où vous décidez de rendre votre maison réellement intelligente (pour fermer les volets automatiquement au coucher du soleil ou en cas de canicule), vous découvrez l'ampleur du problème. Votre superbe **[superviseur domotique local (Home Assistant, Homey ou Apple HomeKit)](/articles/unifier-applications-domotique/)** est incapable de communiquer directement avec vos volets. Les ondes radio sont cryptées.

Pour franchir ce mur, le fabricant vous impose d'acheter sa propre passerelle (la box Tahoma ou Connexoon chez Somfy), vendue plusieurs centaines d'euros. Vous ajoutez un boîtier supplémentaire sur votre réseau, une application de plus sur votre téléphone, et vous créez une dépendance directe à leurs serveurs Cloud. Si la box propriétaire plante ou si internet coupe, vos automatisations globales échouent. Le matériel vous appartient, mais le contrôle vous échappe.

## L'absence cruelle du retour d'état (Le drame du RTS)

Si vous avez opté pour la génération précédente de moteurs radio (le protocole RTS de Somfy, encore massivement vendu aujourd'hui), la situation est pire sur le plan technique.

Le RTS est un protocole unidirectionnel. La télécommande envoie l'ordre de descendre, mais le moteur ne confirme jamais qu'il a bien exécuté l'action. Il n'y a aucun "retour d'état". 

Dans l'interface de votre système domotique, vous cliquez sur le bouton pour fermer le volet de la chambre. L'ordre part. Mais si un meuble bloquait la descente, si le moteur s'est mis en sécurité thermique, ou si une interférence radio a brouillé le signal, le volet reste grand ouvert. Votre application, aveugle, affichera pourtant le volet comme étant "Fermé".

Construire des scénarios de sécurité ou de régulation thermique sur un système qui ment sur sa position réelle est une hérésie architecturale. La domotique a besoin de certitudes, pas de suppositions.

## La maintenance : le prix du tout-en-un

Fusionner l'intelligence (le récepteur radio) et le muscle (le moteur tubulaire) dans le même cylindre au fond du coffre de votre fenêtre pose un immense problème de maintenance à long terme.

L'électronique vieillit généralement beaucoup plus vite que la mécanique. Si la carte de réception radio de votre volet grille à cause d'une surtension, ou si la télécommande propriétaire tombe en panne et n'est plus fabriquée, le moteur mécanique, lui, fonctionne encore parfaitement. 

Pourtant, dans un système radio tout-en-un, vous êtes souvent contraint de remplacer l'intégralité du moteur, une opération qui nécessite d'ouvrir le coffre, de démonter l'axe, et de dépenser plusieurs centaines d'euros pour une simple puce grillée. 

J'ai vu des installations entières paralysées parce qu'une télécommande maître avait rendu l'âme et que la procédure de réappairage d'une nouvelle télécommande nécessitait des manipulations fastidieuses impliquant de couper le courant au tableau électrique dans un ordre très précis.

## La solution : Le retour au moteur filaire standard

La seule véritable option pour une maison connectée robuste est contre-intuitive pour un débutant : il faut exiger la technologie la plus ancienne et la plus "bête" du marché. Le moteur filaire classique à 4 fils.

Un moteur filaire ne possède aucune carte électronique complexe. Il possède quatre câbles :
1.  Un fil de Terre.
2.  Un fil de Neutre.
3.  Un fil de Phase pour la montée.
4.  Un fil de Phase pour la descente.

C'est une norme universelle depuis un demi-siècle. Si vous envoyez du courant sur le fil de montée, le moteur tourne dans un sens. Si vous envoyez du courant sur le fil de descente, il tourne dans l'autre sens. 

C'est simple, indestructible, réparable par n'importe quel électricien, et surtout, c'est totalement interopérable. Vous n'êtes lié à aucune marque. Un moteur filaire d'entrée de gamme fonctionnera exactement sur le même principe qu'un moteur hors de prix.

## L'intelligence déportée : Le micromodule

Si le moteur est bête, où se trouve l'intelligence ? Elle se cache dans le mur, derrière un interrupteur filaire classique.

C'est là que réside le génie de cette architecture. L'électricien tire les câbles du moteur jusqu'à une boîte d'encastrement profonde (ou idéalement **[directement jusqu'au tableau électrique](/articles/domotique-tableau-electrique-rail-din/)**). Dans cette boîte, vous installez un micromodule domotique spécialisé pour volets roulants.

Les références du marché sont les modules Shelly 2PM Plus (en Wi-Fi) ou les modules Legrand, NodOn et Fibaro (en Zigbee ou Z-Wave). 

Le module est branché sur le secteur. Les deux fils de phase du moteur viennent se brancher sur les sorties du module. L'interrupteur mécanique de votre mur vient se brancher sur les entrées du module.

La séparation des pouvoirs est totale : le moteur fournit la force brute, le micromodule fournit le cerveau, et l'interrupteur fournit l'interface humaine d'urgence.

## Les immenses avantages de la séparation matérielle

En adoptant cette architecture filaire + micromodule, vous débloquez des capacités techniques impossibles à obtenir avec des systèmes radio propriétaires :

1.  **Liberté de protocole :** Vous choisissez la langue de votre maison. Vous préférez un réseau maillé **[Zigbee pour économiser votre Wi-Fi](/articles/maison-tout-wifi-box-internet/)** ? Vous achetez un module Zigbee. Dans dix ans, si le standard Matter domine le marché, vous changerez le petit module à 30 euros sans jamais toucher au moteur du volet.
2.  **Calibrage et Retour d'état absolu :** Les micromodules mesurent la consommation électrique en temps réel (power monitoring). Lorsqu'ils envoient le courant pour descendre le volet, ils détectent le pic de consommation au démarrage, puis la chute de tension lorsque le volet arrive en butée mécanique. Le système sait exactement où se trouve le volet, au pourcent près. Si vous demandez une ouverture à 34% pour filtrer le soleil de midi, le volet s'exécutera avec une précision redoutable.
3.  **Le WAF (Wife/Husband Acceptance Factor) parfait :** Le module conserve l'usage de l'interrupteur filaire collé au mur. Pas de télécommande qui se perd sous les coussins du canapé, pas de piles à changer. Quiconque entre dans la pièce saura comment lever le volet en appuyant sur le bouton physique, même si votre serveur domotique est éteint.
4.  **Maintenance facile :** Si la foudre grille l'électronique de votre maison, le moteur dans le volet sera protégé. Seul le petit relais du micromodule dans le mur aura fondu. Vous le remplacerez vous-même avec un tournevis en dix minutes, pour une vingtaine d'euros.

## Le verdict : Résistez aux vendeurs de menuiseries

Les installateurs de fenêtres détestent les moteurs filaires. Tirer un câble depuis le haut de la fenêtre jusqu'à l'interrupteur, percer les murs et faire des saignées demande du temps, de l'expertise électrique et génère de la poussière. Poser un moteur radio et vous tendre une télécommande prend cinq minutes.

Leur intérêt à court terme est diamétralement opposé à la viabilité de votre installation domotique à long terme. 

Si vous construisez ou rénovez, soyez intransigeant. Refusez fermement les options radio, même si on vous assure que "c'est compatible smartphone". Exigez des moteurs filaires standards à 4 fils. Le surcoût initial lié au tirage des câbles par un électricien sera le meilleur investissement que vous ferez pour garantir la liberté, la fiabilité et la longévité de votre maison connectée.
