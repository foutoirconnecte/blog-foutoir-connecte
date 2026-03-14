---
layout: article.njk
title: "Raspberry Pi 5 et domotique en 2026 : le guide définitif pour bâtir sa maison connectée souveraine"
date: 2026-03-14
tags: ["diy-and-tutoriels", "home assistant", "raspberry pi"]
image: "/images/raspberry-pi-domotique.webp"
summary: "Faut-il encore choisir le Raspberry Pi pour sa domotique en 2026 ? Comparatif Pi 4 vs Pi 5, le rôle crucial du SSD, l'intégration des protocoles Zigbee/Z-Wave/Matter, et les avantages de l'IA locale : tout ce qu'il faut savoir pour une installation pérenne et souveraine."
---

### Introduction : La reconquête de nos foyers numériques

On ne va pas se mentir, le petit jeu des assistants vocaux qui écoutent en permanence et des services cloud qui ferment boutique du jour au lendemain, ça commence à bien faire. En 2026, l'heure n'est plus à la confiance aveugle envers des solutions propriétaires qui transforment nos maisons en simples produits de consommation. La tendance de fond, c'est la reconquête, la souveraineté numérique. C'est l'idée de reprendre le contrôle de nos données, de nos scénarios, de notre infrastructure.

Au cœur de cette révolution silencieuse, on retrouve un champion inattendu : le Raspberry Pi. Cette petite carte, initialement conçue pour l'éducation, est devenue le cerveau de milliers d'installations domotiques résilientes et privées. Avec l'arrivée du Raspberry Pi 5, on ne parle plus d'un gadget pour bidouilleurs, mais d'une plateforme matérielle sérieuse, capable de rivaliser avec des mini-PC bien plus onéreux. Il offre la puissance nécessaire pour non seulement orchestrer des centaines d'appareils, mais aussi pour faire tourner des intelligences artificielles locales, coupant définitivement le cordon avec les serveurs de la Silicon Valley. Ce guide est là pour ça : vous montrer pourquoi et comment le Pi 5 est la pierre angulaire d'une domotique qui vous appartient vraiment.

### L'infrastructure matérielle : Le Pi 5, simple évolution ou révolution ?

Le Raspberry Pi 4 a longtemps été le roi incontesté de la domotique DIY. Fiable, abordable, et juste assez puissant pour faire tourner Home Assistant et ses compagnons. Mais l'arrivée du Pi 5 a rebattu les cartes. Est-ce juste une mise à jour mineure ou un véritable changement de paradigme ?

#### Rant : "Mon Pi 4 suffit, le 5 c'est du luxe !"

C'est une rengaine qu'on entend souvent. "Pourquoi dépenser plus pour un Pi 5 alors que mon Pi 4 gère mes 50 appareils sans broncher ?" L'argument est recevable... si votre vision de la domotique se limite à allumer des lumières et à lire des températures. Mais dès que l'on commence à empiler les services – AdGuard Home, un serveur de musique, la gestion de caméras, et surtout, l'IA locale – le Pi 4 montre ses limites. Les redémarrages de Home Assistant deviennent poussifs, l'interface a des hoquets, et compiler un firmware ESPHome prend une éternité. On se retrouve à optimiser, à traquer le moindre processus gourmand, bref, à passer plus de temps à maintenir la machine qu'à profiter de sa maison.

#### Fix : Comparatif des forces en présence

Mettons les choses au clair. Le Pi 5 n'est pas "un peu" plus rapide. C'est un monstre de puissance comparé à son aîné.

*   **CPU :** Le processeur Cortex-A76 du Pi 5 est 2 à 3 fois plus performant que le Cortex-A72 du Pi 4. Pour Home Assistant, cela se traduit par des redémarrages quasi instantanés, une interface d'une fluidité parfaite même avec des dizaines de tableaux de bord, et une capacité à gérer des centaines d'automatisations complexes sans jamais ralentir.
*   **I/O (Entrées/Sorties) :** C'est LA révolution silencieuse du Pi 5. Grâce à la puce RP1, les performances USB sont enfin stables et rapides, et surtout, on dispose d'une interface **PCIe 2.0**. On y reviendra dans la section stockage, mais c'est un game-changer absolu pour la fiabilité. Fini les goulots d'étranglement des adaptateurs USB-SATA.
*   **Consommation et chaleur :** Qui dit puissance, dit consommation. Le Pi 5 est plus gourmand, nécessitant une alimentation officielle de 5V/5A (25W) pour fonctionner à plein régime. Il chauffe aussi beaucoup plus. Oubliez les petits dissipateurs passifs du Pi 4. Pour le Pi 5, un refroidissement actif (comme le ventilateur officiel) ou un boîtier entièrement passif mais massif (type Flirc ou Argon) est non-négociable. Le silence a un prix, et dans le cas d'un boîtier passif, il est thermique et financier.

#### Verdict : Le Pi 5 est le choix de la pérennité

En 2026, choisir un Raspberry Pi 4 pour une nouvelle installation, c'est un peu comme acheter un smartphone sans 5G. Ça fonctionne, mais on se prive de l'avenir. Le surcoût du Pi 5 et de son alimentation est largement justifié par le confort d'utilisation, la fluidité, et surtout, les portes qu'il ouvre pour l'avenir de votre domotique. C'est l'assurance de ne pas avoir à changer de matériel dans deux ans quand vous voudrez explorer les assistants vocaux locaux ou l'analyse d'images. C'est un investissement pour une base saine et durable.

### Gestion du stockage : L'adieu définitif à la carte SD

Si le processeur est le cerveau de votre domotique, le stockage en est le cœur. Et pendant des années, on a laissé ce cœur entre les mains d'un composant fragile, lent et totalement inadapté : la carte microSD.

#### Rant : La carte SD, cette bombe à retardement

C'est l'erreur du débutant par excellence. On suit un tuto, on flashe Home Assistant OS sur une carte SD, et on oublie. Six mois, un an, parfois deux ans plus tard, c'est le drame. La domotique ne répond plus, impossible de redémarrer. La raison ? La carte SD est morte. Corrompue. Foutue. Il faut comprendre qu'une carte SD n'est pas conçue pour les écritures constantes générées par un système d'exploitation et une base de données comme celle de Home Assistant. Chaque log, chaque changement d'état, chaque enregistrement d'historique lime un peu plus sa durée de vie. Utiliser une carte SD pour sa domotique, c'est construire sa maison sur du sable mouvant. On a beau faire des sauvegardes, la panne arrive toujours au pire moment. C'est un sujet que l'on a déjà abordé en parlant de [pannes de courant et la résilience domotique](/articles/pannes-de-courant-et-la-resilience-domotique), mais la corruption de données est un ennemi tout aussi redoutable.

#### Fix : Le SSD, une évidence devenue la norme

La solution est simple : un SSD (Solid State Drive). C'est plus rapide, et surtout, infiniment plus fiable car conçu pour des cycles d'écriture/lecture intensifs.

*   **Avec un Raspberry Pi 4 :** La méthode éprouvée consiste à utiliser un boîtier externe USB 3.0 pour un SSD SATA au format 2.5". C'est une solution robuste qui a fait ses preuves. Le gain en réactivité par rapport à la carte SD est spectaculaire. Les bases de données répondent au doigt et à l'œil, et les sauvegardes sont bien plus rapides.
*   **Avec un Raspberry Pi 5 :** C'est ici que le Pi 5 change la donne. Grâce à son port PCIe, on peut connecter un SSD NVMe via un "HAT" (une carte d'extension). Le NVMe est encore plus rapide que le SATA, mais le véritable avantage est la connexion directe au bus PCIe, éliminant la couche de conversion USB qui peut parfois être une source de problèmes. Des solutions comme le Pineberry Pi Hat ou le Pimoroni NVMe Base permettent une intégration propre et des performances dignes d'un vrai PC.

N'oubliez pas les sauvegardes ! Avoir un SSD ne vous dispense pas d'une stratégie de backup solide. L'addon "Google Drive Backup" pour Home Assistant est un must-have. Il automatise la sauvegarde de votre configuration complète vers le cloud, vous assurant de pouvoir tout restaurer en quelques minutes en cas de problème majeur.

#### Verdict : SSD non-négociable, NVMe recommandé

En 2026, démarrer une installation domotique sur une carte SD est une faute professionnelle. Le débat n'est plus "SD ou SSD", mais "SATA ou NVMe". Pour un Raspberry Pi 4, un bon SSD SATA en USB 3.0 reste une excellente option. Mais pour un Pi 5, il serait dommage de se priver de la vitesse et de l'élégance d'une solution NVMe sur PCIe. C'est le duo gagnant pour une fiabilité et des performances à toute épreuve.

### Protocoles sans fil : Mettre de l'ordre dans le chaos des ondes

Zigbee, Z-Wave, Wi-Fi, Bluetooth, et maintenant Matter over Thread... Le monde des objets connectés est un champ de bataille de protocoles. Choisir le bon cheval et la bonne infrastructure est crucial pour une expérience stable et réactive.

#### Rant : "Le Wi-Fi, c'est plus simple !"

L'attrait du Wi-Fi est compréhensible. Pas besoin de clé ou de pont supplémentaire, on connecte l'appareil à son réseau et c'est tout. Simple, en apparence. Mais rapidement, c'est la catastrophe. Chaque appareil Wi-Fi est un client de plus sur votre routeur, consommant une adresse IP et de la bande passante. Avec 10, 20, 50 appareils, votre réseau Wi-Fi, initialement conçu pour quelques ordinateurs et smartphones, s'effondre. Les appareils se déconnectent, la latence explose, et votre conjoint(e) vous maudit car Netflix se met en mémoire tampon. De plus, la plupart des appareils Wi-Fi dépendent du cloud de leur fabricant. Une panne de leurs serveurs, et votre maison devient idiote.

#### Fix : La puissance des réseaux maillés

La solution réside dans les protocoles conçus pour la domotique : Zigbee et Z-Wave, rejoints par le prometteur Thread.

*   **Zigbee :** C'est le plus populaire et le plus abordable. Il existe une myriade de capteurs et d'actionneurs à des prix défiant toute concurrence. Son principal avantage est son réseau maillé (mesh) : chaque appareil alimenté sur secteur (ampoule, prise connectée) agit comme un répéteur, étendant la portée et la fiabilité du réseau. Le choix du coordinateur (la clé USB qui dialogue avec les appareils) est crucial. Les modèles Sonoff (ZBDongle-E), Conbee II/III ou le SkyConnect officiel de Home Assistant sont des valeurs sûres. Attention aux interférences avec le Wi-Fi 2.4 GHz ! Utilisez une rallonge USB pour éloigner le coordinateur du Pi et choisissez un canal Zigbee qui ne chevauche pas votre canal Wi-Fi.
*   **Z-Wave :** Souvent perçu comme plus "premium" et plus robuste, Z-Wave utilise une fréquence plus basse (~868 MHz en Europe), ce qui le rend moins sujet aux interférences et lui donne une meilleure pénétration à travers les murs. Il est également réputé pour sa sécurité. Le ticket d'entrée est plus cher, mais pour des éléments critiques (serrures, alarmes), c'est un choix rassurant.
*   **Matter over Thread :** C'est le "futur" qui se fait attendre mais qui arrive enfin. Matter est une surcouche applicative qui promet l'interopérabilité. Thread est le protocole réseau sous-jacent, un réseau maillé basse consommation comme Zigbee, mais basé sur IPv6. L'avantage ? Pas de pont propriétaire, et une communication locale et standardisée. Le Raspberry Pi 5, avec un coordinateur multiprotocole comme le SkyConnect, peut agir comme un **Routeur de Bordure Thread (Thread Border Router)**, connectant votre réseau domotique Thread au reste de votre réseau local.

#### Verdict : Le trio gagnant Zigbee, Thread et un bon Wi-Fi

Une installation domotique saine en 2026 repose sur une combinaison intelligente. Le Zigbee pour la majorité des capteurs et actionneurs grâce à son excellent rapport qualité/prix. Matter over Thread pour les nouveaux appareils compatibles, afin de construire un écosystème pérenne et interopérable. Et le Wi-Fi ? On le réserve pour les appareils qui nécessitent une bande passante élevée (caméras, assistants vocaux) en s'assurant d'avoir une infrastructure réseau solide (points d'accès, VLANs...). C'est cette diversification qui garantit une maison connectée réactive, fiable et prête pour l'avenir.

### Intelligence locale : Quand votre maison commence à réfléchir

La vraie révolution de la domotique ne réside pas dans le contrôle à distance, mais dans l'autonomie et l'intelligence. Grâce à la puissance du Raspberry Pi 5, cette intelligence n'a plus besoin de résider sur des serveurs distants, mais directement chez vous.

#### Rant : L'IA dans le cloud, une fausse bonne idée

On nous a vendu le rêve d'assistants vocaux omniscients. La réalité est plus amère : des micros qui écoutent en permanence, des données envoyées on ne sait où, et une dépendance totale à une connexion internet. Votre voix, vos habitudes, les conversations de vos enfants... tout est analysé, stocké, et potentiellement utilisé. Et que se passe-t-il quand le service change ses conditions ou met la clé sous la porte ? Vos scénarios vocaux, si pratiques, cessent de fonctionner. Le summum de l'absurdité : "Ok Google, allume la lumière du salon", une commande qui fait un aller-retour de plusieurs milliers de kilomètres pour allumer une ampoule à deux mètres de vous. Il est temps de rapatrier notre [IA locale](/articles/ia-locale) et de la faire travailler pour nous, et uniquement pour nous.

#### Fix : Le Pi 5, un mini-serveur d'IA

Le Pi 5 a les muscles nécessaires pour faire tourner localement des briques logicielles d'IA qui étaient auparavant l'apanage de serveurs dédiés. Home Assistant a massivement investi dans ce domaine avec son projet "Voice".

*   **STT (Speech-to-Text) :** Le projet "Whisper" d'OpenAI, dans sa version open-source, peut tourner sur le Pi 5. Il permet de transcrire vos commandes vocales en texte avec une précision bluffante, sans qu'aucun son ne quitte votre domicile.
*   **Intention Recognition :** Home Assistant analyse ensuite ce texte pour comprendre ce que vous voulez faire ("allume", "lumière", "salon").
*   **TTS (Text-to-Speech) :** Une fois l'action effectuée, l'assistant peut vous répondre. Des moteurs comme "Piper" permettent de générer une voix de synthèse de très haute qualité, toujours en local. Adieu les voix robotiques et bonjour les retours naturels et instantanés.
*   **LLM (Large Language Models) :** C'est la nouvelle frontière. Des modèles de langage comme Llama 3 ou le français Mistral, dans leurs versions optimisées, peuvent commencer à tourner sur un Pi 5. On ne parle pas encore de remplacer ChatGPT, mais de permettre des interactions plus complexes et naturelles avec votre maison. "Mets une ambiance tamisée dans le salon et joue ma playlist de soirée" deviendra une commande standard, comprise et exécutée entièrement localement.

Au-delà de la voix, cette puissance de calcul permet des automatisations prédictives. En croisant les données de vos capteurs (présence, luminosité, température, calendrier), le système peut apprendre vos habitudes et anticiper vos besoins : baisser les volets avant que le soleil ne surchauffe une pièce, préchauffer la salle de bain avant votre réveil, ou vous alerter si vous partez en oubliant une fenêtre ouverte.

#### Verdict : L'IA locale est la prochaine étape logique

L'IA locale n'est plus un fantasme de geek. C'est une réalité accessible grâce au Raspberry Pi 5. C'est la garantie d'une confidentialité absolue, d'une réactivité inégalée (les commandes sont exécutées en millisecondes) et d'une résilience à toute épreuve, même sans connexion internet. Mettre en place son propre assistant vocal local demande un peu de configuration, mais le jeu en vaut la chandelle. C'est la dernière étape pour une maison véritablement intelligente et souveraine.

### Sécurité et résilience : Fortifier votre château numérique

Avoir une maison intelligente, c'est bien. S'assurer qu'elle ne devienne pas une porte d'entrée pour des personnes malveillantes, c'est mieux. Une domotique souveraine se doit d'être sécurisée.

#### Rant : L'enfer du Port Forwarding

La solution de facilité pour accéder à son Home Assistant depuis l'extérieur ? Le "port forwarding" ou redirection de port. On dit à sa box internet : "tout ce qui arrive sur le port 8123, envoie-le à mon Raspberry Pi". C'est simple, rapide, et c'est une très, très mauvaise idée. C'est l'équivalent numérique de laisser sa porte d'entrée grande ouverte avec une pancarte "servez-vous". Votre instance Home Assistant est directement exposée sur Internet, à la merci des bots qui scannent en permanence les adresses IP à la recherche de la moindre faille. Même avec un mot de passe solide, vous vous exposez à des attaques et des vulnérabilités zero-day.

#### Fix : L'accès distant sécurisé et la segmentation réseau

Plusieurs solutions robustes et sécurisées existent pour éviter cet écueil.

*   **VPN (Virtual Private Network) :** C'est la méthode la plus sûre. Vous montez un serveur VPN chez vous (WireGuard est excellent pour ça et peut tourner sur le Pi ou votre routeur). Pour vous connecter à votre domotique, vous activez le VPN sur votre smartphone, créant un tunnel chiffré et sécurisé directement vers votre réseau local. C'est comme si vous étiez à la maison. C'est la méthode que je privilégie pour sa sécurité sans compromis.
*   **Cloudflare Tunnel :** Une alternative plus simple à mettre en place. Un petit service tourne sur votre Pi et crée un tunnel sortant sécurisé vers les serveurs de Cloudflare. Vous accédez à votre Home Assistant via une adresse web personnalisée, et c'est Cloudflare qui fait le pont, sans que vous ayez besoin d'ouvrir le moindre port. C'est une excellente solution qui combine sécurité et simplicité.
*   **Nabu Casa :** Le service payant (quelques euros par mois) des développeurs de Home Assistant. C'est la solution la plus simple ("plug-and-play"), qui gère pour vous l'accès distant sécurisé et l'intégration avec les assistants vocaux cloud (si vous en avez encore besoin). En plus, vous soutenez financièrement le développement du projet.

En interne, la segmentation de votre réseau avec des **VLANs** est une bonne pratique. Vous pouvez créer un réseau virtuel isolé juste pour vos objets connectés. Ainsi, même si un appareil est compromis, il ne pourra pas accéder au reste de votre réseau (vos ordinateurs, votre NAS...). C'est un niveau de sécurité supplémentaire qui vaut la peine d'être exploré si votre matériel réseau le permet. Et bien sûr, une bonne domotique est une domotique qui sait comment se comporter quand le [suivi de consommation Linky en local](/articles/linky-en-local) indique une coupure de courant.

#### Verdict : Zéro port ouvert sur l'extérieur

La règle d'or est simple : aucun port ne doit être ouvert directement sur internet pour votre domotique. Les solutions comme WireGuard ou Cloudflare Tunnel sont matures, gratuites et infiniment plus sécurisées. Prenez le temps de les mettre en place. La tranquillité d'esprit n'a pas de prix.

### Conclusion : Le Pi, plus que jamais le cœur de la maison intelligente

Alors, en 2026, le Raspberry Pi est-il toujours le bon choix pour sa domotique ? La réponse est un oui franc et massif. Mais plus n'importe lequel : le Raspberry Pi 5 s'impose comme la nouvelle référence. Il n'est plus seulement un "cerveau" pour orchestrer des appareils, mais une véritable plateforme de "edge computing" domestique.

En l'associant à un stockage fiable (SSD NVMe), à des protocoles radio éprouvés (Zigbee) et d'avenir (Thread), et en exploitant sa puissance pour l'IA locale, on ne construit pas simplement une maison connectée. On bâtit une maison souveraine : privée, résiliente, rapide, et qui nous appartient vraiment. C'est un petit investissement en temps et en argent, mais qui garantit une domotique pérenne, loin des caprices des géants de la tech.
