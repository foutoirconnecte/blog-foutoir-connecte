---
layout: article.njk
title: "Raspberry Pi 5 et domotique en 2026 : le guide définitif pour bâtir sa maison connectée souveraine"
date: 2026-03-14
tags: ["diy-and-tutoriels", "home assistant", "raspberry pi"]
image: "/images/raspberry-pi-domotique.webp"
summary: "Faut-il encore choisir le Raspberry Pi pour sa domotique en 2026 ? Comparatif Pi 4 vs Pi 5, le rôle crucial du SSD, l'intégration des protocoles Zigbee/Z-Wave/Matter, et les avantages de l'IA locale : tout ce qu'il faut savoir pour une installation pérenne et souveraine."
---

En 2026, l'idée d'une maison connectée entièrement dépendante du cloud d'un géant de la tech commence à sentir le rance. Les pannes de service à répétition, les changements de politique tarifaire unilatéraux et le siphonnage constant de nos données personnelles ont eu raison de notre patience. La tendance est au retour en force du local, du "self-hosted". Il ne s'agit plus seulement de confort, mais de souveraineté numérique. C'est dans ce contexte que le Raspberry Pi, et plus particulièrement sa cinquième itération, s'impose non plus comme un jouet de bidouilleur, but comme le cerveau d'une maison intelligente, résiliente et respectueuse de notre vie privée. Oubliez les box propriétaires qui deviendront des briques le jour où le fabricant décidera de couper les serveurs. L'avenir est open-source, local, et il tourne sur un nano-ordinateur de la taille d'une carte de crédit. Ce guide complet explore pourquoi et comment le Raspberry Pi 5 est aujourd'hui la pierre angulaire d'une domotique pérenne et maîtrisée.

## L'infrastructure matérielle : Le Pi 5, une évidence ?

Le Raspberry Pi 4 a longtemps été le roi incontesté de la domotique DIY. Fiable, abordable, et juste assez puissant pour faire tourner Home Assistant et ses dépendances. Mais l'arrivée du Pi 5 a rebattu les cartes. Est-ce une simple mise à jour ou un véritable bond en avant justifiant une migration ?

**Rant :** Soyons clairs, si votre installation sur Pi 4 fonctionne parfaitement, ne vous précipitez pas. La domotique, c'est la quête de la stabilité. On ne change pas un système qui gagne sur un coup de tête. Mais pour toute nouvelle installation, ou si vous commencez à sentir les limites de votre Pi 4 (lenteurs de l'interface, redémarrages qui s'éternisent, difficultés avec des addons gourmands comme Frigate), le Pi 5 n'est plus une option, c'est la nouvelle norme.

**Fix :** Le gain de performance est indéniable. Le processeur ARM Cortex-A76 quad-core à 2.4GHz du Pi 5 offre une puissance de calcul 2 à 3 fois supérieure à celle du Pi 4. Pour Home Assistant, cela se traduit par une fluidité déconcertante. Les redémarrages, qui prenaient parfois plusieurs minutes, sont maintenant une affaire de secondes. L'interface est instantanée, les automations complexes s'exécutent sans latence. Mais le vrai changement se situe au niveau des I/O (entrées/sorties). Le Pi 5 intègre un contrôleur I/O RP1, une puce conçue par la fondation Raspberry Pi elle-même, qui décharge le processeur principal et offre des débits bien supérieurs. Le port USB 3.0, par exemple, peut maintenir des débits élevés simultanément, là où le Pi 4 pouvait s'essouffler.

Et puis, il y a le Graal : l'interface PCIe 2.0. Officiellement destinée aux HATs (Hardware Attached on Top), elle ouvre la voie à ce qui manquait cruellement au Pi : un stockage natif ultra-rapide. Nous y reviendrons.

Côté alimentation, le Pi 5 est plus exigeant. Il requiert une alimentation officielle USB-C de 27W (5V/5A) pour délivrer son plein potentiel. Une alimentation de Pi 4 (5V/3A) fonctionnera, mais limitera le courant disponible pour les ports USB, ce qui peut poser problème avec des SSD ou des dongles radio gourmands. Ne faites pas l'impasse sur une alimentation de qualité, c'est le gage de la stabilité.

Enfin, la question qui fâche : le refroidissement. Le Pi 5 chauffe plus que son prédécesseur. Un simple dissipateur ne suffit plus. L'Active Cooler officiel est efficace, mais son petit ventilateur peut devenir audible. Pour une installation domotique destinée à tourner 24/7 dans un salon, le silence est d'or. Heureusement, les fabricants tiers comme Argon40 ou Flirc proposent des boîtiers passifs en aluminium qui dissipent la chaleur de manière totalement silencieuse et efficace.

**Verdict :** Pour une nouvelle installation, le Raspberry Pi 5 est le choix logique et pérenne. Sa puissance de calcul et surtout ses I/O améliorées offrent une base solide pour les années à venir, notamment pour l'intégration de l'intégration de l'[IA locale](/articles/ia-locale-voix-2026). Pour les possesseurs de Pi 4, la migration n'est pas une urgence, mais deviendra une évidence si vous souhaitez explorer des usages plus avancés.

## Le stockage : Dites adieu aux cartes SD

Si un seul conseil devait être retenu de ce guide, ce serait celui-ci : n'utilisez PAS de carte SD pour faire tourner votre système domotique. Jamais.

**Rant :** La carte SD est le talon d'Achille de la domotique sur Raspberry Pi depuis ses débuts. Home Assistant, avec ses bases de données d'historique, ses logs et ses écritures constantes, est un véritable tueur de cartes SD. La question n'est pas *si* votre carte va lâcher, mais *quand*. Et ça arrivera toujours un dimanche soir, en plein hiver, alors que vous êtes en vacances, laissant votre maison dans le noir et le froid. La corruption de données est la première cause d'abandon des débutants et une source de frustration immense.

**Fix :** La solution est simple : un SSD. Jusqu'au Pi 4, la seule option était de brancher un SSD SATA via un adaptateur USB 3.0. C'est une solution fiable et déjà bien plus performante qu'une carte SD. Le boot sur USB est maîtrisé depuis longtemps et la stabilité est au rendez-vous.

Mais le Raspberry Pi 5 change la donne avec son port PCIe. Grâce à des cartes d'extension (des "HATs") comme le Pineberry Pi HatDrive! ou le Pimoroni NVMe Base, on peut désormais connecter un SSD NVMe directement sur le bus PCIe. La différence est spectaculaire. Là où un SSD USB 3.0 plafonne autour de 400-450 Mo/s, un SSD NVMe sur le Pi 5 peut atteindre des vitesses de 800-900 Mo/s.

Concrètement pour Home Assistant ? Les sauvegardes (snapshots) sont quasi instantanées. La base de données Recorder, qui peut devenir énorme, répond au doigt et à l'œil. L'accès à l'historique, même sur de longues périodes, est immédiat. C'est un confort d'utilisation qui change tout et, surtout, une fiabilité à toute épreuve.

Quelle que soit la solution choisie (USB ou NVMe), la stratégie de sauvegarde reste primordiale. Home Assistant propose un outil de sauvegarde simple et efficace. Automatisez une sauvegarde complète au moins une fois par semaine et configurez l'envoi vers un emplacement externe : un NAS, un service cloud (via un addon comme Google Drive Backup ou Samba Backup). C'est votre assurance vie en cas de pépin matériel. Une bonne domotique est une domotique résiliente, comme on l'a vu pour les [pannes de courant et la résilience domotique](/articles/panne-courant-domotique).

**Verdict :** Le SSD est non négociable. Pour un Pi 4, un bon SSD SATA en USB 3.0 fait parfaitement l'affaire. Pour un Pi 5, investir dans un HAT et un petit SSD NVMe est le meilleur investissement que vous puissiez faire pour la performance et la tranquillité d'esprit. La carte SD ne doit servir qu'à une seule chose : l'installation initiale du système d'exploitation avant de le transférer sur le SSD.

## Les protocoles sans-fil : Unifier le chaos

Une domotique, ce sont des capteurs et des actionneurs qui communiquent. Et dans le monde du sans-fil, c'est souvent la jungle. Zigbee, Z-Wave, et maintenant Matter sur Thread, comment s'y retrouver ?

**Rant :** Le Wi-Fi, c'est bien pour votre ordinateur, pas pour vos capteurs de température. Chaque appareil Wi-Fi est un client de plus sur votre réseau, consommant de l'énergie (adieu les capteurs sur pile) et une adresse IP. Pour la domotique, on a besoin de protocoles basse consommation, créant leur propre réseau maillé (mesh) pour une meilleure portée et fiabilité.

**Fix :** Le protocole le plus populaire est sans conteste le **Zigbee**. C'est un standard ouvert, avec un écosystème immense et des appareils très abordables (merci Aqara, Sonoff, et Tuya). Le principe est simple : un coordinateur (une clé USB branchée sur le Pi) crée un réseau. Chaque appareil alimenté sur secteur (ampoule, prise connectée) agit comme un routeur, étendant le réseau. Les appareils sur pile (capteurs) se connectent au point le plus proche.
Le choix du coordinateur est crucial. Les clés Sonoff (basées sur une puce Texas Instruments) sont devenues une référence pour leur stabilité et leur compatibilité avec ZHA (l'intégration native de Home Assistant) et Zigbee2MQTT (une alternative plus puissante et flexible). Les Conbee II et SkyConnect (la clé officielle de Home Assistant) sont aussi d'excellentes options.
Le principal écueil du Zigbee est sa fréquence (2.4 GHz), la même que le Wi-Fi. Pour éviter les interférences, il faut choisir un canal Zigbee qui ne chevauche pas vos canaux Wi-Fi et utiliser une rallonge USB pour éloigner le coordinateur du Raspberry Pi, qui est une source de parasites électromagnétiques.

Le **Z-Wave** est l'alternative historique. Il opère sur une fréquence plus basse (~868 MHz en Europe), ce qui lui évite les interférences du Wi-Fi et lui confère une meilleure pénétration dans les murs. Il est réputé pour sa fiabilité et sa sécurité (certification obligatoire), mais les appareils sont souvent plus chers.

Et **Matter** dans tout ça ? Annoncé comme le standard qui allait unifier la domotique, Matter est une couche applicative qui peut fonctionner sur différents réseaux, dont le Wi-Fi et **Thread**. Thread, comme Zigbee, est un protocole radio basse consommation qui crée un réseau maillé. L'idée de Matter est de rendre les appareils interopérables, peu importe le fabricant. En 2026, l'écosystème Matter est encore en construction, mais il prend de l'ampleur. Pour utiliser Matter sur Thread, il vous faut un "Thread Border Router". Bonne nouvelle : Home Assistant sur un Pi 4 ou 5, avec la clé SkyConnect, peut jouer ce rôle.

**Verdict :** Pour démarrer, le Zigbee offre le meilleur rapport qualité/prix/choix. Une clé Sonoff et quelques capteurs Aqara suffisent à se lancer. Ne négligez pas la planification de votre réseau maillé : ajoutez des prises connectées ou des ampoules à des endroits stratégiques pour renforcer le signal. Gardez un œil sur Matter/Thread. L'avenir est probablement là, mais en 2026, Zigbee reste le choix le plus pragmatique et le plus riche en termes de périphériques disponibles.

## Intelligence Locale : L'IA au service de la maison

La vraie puissance d'une domotique locale ne réside pas seulement dans le contrôle de ses lumières depuis son canapé, mais dans sa capacité à être véritablement "intelligente" et proactive, sans dépendre d'un cloud. Le Raspberry Pi 5, avec sa puissance accrue, est la machine parfaite pour héberger cette intelligence.

**Rant :** Les assistants vocaux du commerce sont des mouchards. Chaque "Ok Google" ou "Alexa" est une conversation qui part sur des serveurs pour y être analysée. Les automations "intelligentes" des plateformes cloud sont basiques et leur exécution dépend d'une connexion internet. Si votre ADSL tombe, votre maison devient bête. Inacceptable.

**Fix :** Home Assistant a fait des pas de géant pour rapatrier l'intelligence à la maison. Le projet "Voice" permet de créer son propre assistant vocal, 100% local. Le Pi 5 est capable de faire tourner les briques logicielles nécessaires :
- **STT (Speech-to-Text) :** L'addon "Whisper" peut tourner localement sur le CPU du Pi 5 pour transcrire vos commandes vocales avec une précision bluffante.
- **Intent Recognition :** Le moteur de Home Assistant analyse la transcription pour comprendre votre demande ("Allume la lumière du salon").
- **TTS (Text-to-Speech) :** L'addon "Piper" génère une réponse vocale naturelle, toujours localement, avec des voix de très haute qualité en français.
Il suffit d'un petit micro (comme le ReSpeaker 2-Mics Pi HAT) pour créer des satellites vocaux dans toute la maison, qui ne communiquent qu'avec votre Home Assistant local.

Au-delà de la voix, la puissance du Pi 5 ouvre la porte à des automations prédictives. En analysant l'historique de vos capteurs (présence, température, luminosité, consommation via le suivi du [Linky en local](/articles/linky-teleinfo-local)), Home Assistant peut apprendre vos habitudes. Il peut anticiper que vous allez bientôt vous coucher et commencer à baisser le chauffage, ou détecter une absence anormale et vous envoyer une alerte.
Des addons comme "Frigate NVR" peuvent utiliser un accélérateur IA (comme une clé USB Google Coral) pour analyser en temps réel les flux de vos caméras et détecter des personnes, des voitures ou des animaux, sans jamais envoyer une seule image sur le cloud. Le Pi 5, avec son port USB 3.0 rapide, est parfait pour gérer ces flux vidéo et ces analyses en parallèle.

L'étape suivante, déjà accessible, est l'intégration de LLMs (Large Language Models) locaux. Des modèles comme Llama 3 ou Mistral peuvent être interrogés par Home Assistant pour générer des notifications plus humaines, résumer l'état de la maison, ou même aider à créer des automations complexes en langage naturel.

**Verdict :** Le Raspberry Pi 5 transforme Home Assistant d'un simple chef d'orchestre d'automations en un véritable cerveau pour la maison. L'IA locale n'est plus un fantasme. Elle permet une interaction plus naturelle (voix), des actions plus pertinentes (prédiction) et une sécurité renforcée (analyse vidéo locale), le tout en gardant le contrôle total sur vos données.

## Sécurité et Résilience : Verrouiller sa forteresse numérique

Une domotique puissante et connectée est une porte d'entrée potentielle sur votre réseau local. La sécuriser n'est pas une option.

**Rant :** Exposer son instance Home Assistant directement sur internet en ouvrant un port sur sa box (port forwarding) est une hérésie. C'est comme laisser la porte de sa maison grande ouverte avec une pancarte "Entrez !". Les bots scannent en permanence les adresses IP à la recherche de services vulnérables.

**Fix :** La première étape est la segmentation du réseau. Vos objets connectés, surtout les appareils Wi-Fi de marques exotiques dont le firmware est une boîte noire, ne devraient pas pouvoir communiquer avec vos ordinateurs ou votre NAS. La solution s'appelle les **VLANs** (Virtual LANs). La plupart des routeurs un peu avancés (Ubiquiti, Mikrotik, ou même un routeur open-source comme OPNsense) permettent de créer des réseaux virtuels étanches. On crée un VLAN "IoT" pour tous les objets connectés, qui n'a le droit de communiquer qu'avec Home Assistant, et pas avec le reste de votre réseau, ni avec Internet (sauf si nécessaire pour une mise à jour).

Pour l'accès à distance, plusieurs solutions sécurisées existent. La plus simple est d'utiliser le service Nabu Casa, un abonnement payant (et modique) proposé par les développeurs de Home Assistant qui crée un tunnel chiffré et sécurisé vers votre instance. C'est la solution "plug-and-play" qui soutient en plus le projet.
Pour une solution auto-hébergée, on peut monter un **VPN** (WireGuard est aujourd'hui la référence pour sa simplicité et ses performances) sur son routeur ou sur un autre appareil. Il faut alors se connecter au VPN depuis son smartphone pour accéder à son réseau local, et donc à Home Assistant, comme si on était à la maison.
Une autre alternative de plus en plus populaire est le **Cloudflare Tunnel**. C'est un service gratuit qui permet d'exposer un service local (comme Home Assistant) sur internet via un tunnel sécurisé, sans ouvrir le moindre port. C'est facile à mettre en place (via un addon) et très robuste.

**Verdict :** La sécurité par l'obscurité n'est pas une stratégie. Prenez le temps de segmenter votre réseau avec des VLANs et utilisez une méthode d'accès à distance sécurisée. Nabu Casa pour la simplicité, un tunnel Cloudflare ou un VPN WireGuard pour un contrôle total. Bannissez le port forwarding.

## Conclusion

En 2026, le Raspberry Pi 5 n'est plus seulement un choix pertinent pour la domotique ; il en est le cœur battant. Il offre la puissance nécessaire pour une expérience fluide, la flexibilité pour s'adapter à tous les protocoles, et la capacité de faire tourner des intelligences artificielles localement, ce qui était impensable il y a quelques années sur ce type de matériel. Bâtir sa maison connectée sur un Raspberry Pi, c'est faire le choix de la durabilité, de l'indépendance face aux géants du web, et de la confidentialité. C'est reprendre le contrôle. C'est affirmer que sa maison, et les données qu'elle génère, n'appartiennent qu'à soi.
