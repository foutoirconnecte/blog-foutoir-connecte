---
date: 2026-03-12
image: /images/linky-teleinfo-local.webp
layout: article.njk
summary: Ne laissez plus Enedis être le seul à connaître votre consommation électrique.
  Découvrez comment récupérer la donnée TIC (Télé-Information Client) en temps réel
  pour domotiser votre délestage et optimiser votre facture.
tags:
- cloud-vs-local
- diy-and-tutoriels
- débutant-en-domotique
- économies-d'énergie
title: 'Le Linky bavard : comment exploiter la télé-info sans passer par l''app Enedis'
---

Le compteur communicant Linky, déployé massivement dans tous les foyers français, est souvent perçu comme un simple outil de facturation à distance pour le gestionnaire du réseau, Enedis. On le regarde avec méfiance, on s'inquiète des ondes CPL, on peste contre les coupures de courant à distance, mais on oublie un détail technique fondamental : ce boîtier est une mine d'or d'informations pour quiconque possède une installation domotique.

Au cœur du Linky se cache une interface méconnue du grand public mais vénérée par les ingénieurs : la TIC (Télé-Information Client). C'est un port de communication série qui crache, en temps réel et avec une précision à la seconde, l'intégralité de ce qui se passe sur votre installation électrique. 

En 2026, si vous payez encore pour consulter votre consommation via l'application ou le site web d'Enedis, qui affiche des données avec 24 à 48 heures de retard, vous passez à côté de la véritable puissance de votre maison intelligente. La domotique, ce n'est pas seulement piloter des ampoules, c'est maîtriser l'énergie de son foyer.

## La Télé-Information Client (TIC) : Le pouls de votre maison

La TIC est le protocole de communication standardisé utilisé par le compteur Linky pour transmettre les informations de consommation et de tarification à votre équipement domotique. 

### Pourquoi c'est révolutionnaire
Le site Enedis et son application officielle vous fournissent une vue "rétrospective" : vous voyez combien vous avez consommé hier, ou la semaine dernière. C'est utile pour la comptabilité, mais totalement inutile pour la gestion domotique. 

La TIC, elle, vous donne la consommation **instantanée** (en Watts) avec une fréquence de rafraîchissement très élevée (de l'ordre de la seconde). C'est cette donnée en temps réel qui change tout. Vous ne gérez plus votre consommation après coup ; vous gérez votre puissance électrique *pendant* qu'elle est consommée.

### Ce que la TIC vous révèle
Le flux de données TIC est très bavard. Il vous donne en permanence :
*   **La puissance apparente (VA) et la puissance active (W) :** La mesure exacte de ce que la maison consomme en ce moment précis.
*   **L'index de consommation (Wh) :** Votre compteur kilométrique électrique.
*   **La période tarifaire :** Savoir si vous êtes en Heures Pleines ou Heures Creuses instantanément.
*   **Le dépassement de puissance :** Le compteur vous prévient avant de disjoncter si vous dépassez votre abonnement (le seuil de déclenchement).

## Le Fix : Comment brancher son cerveau domotique sur le compteur

Récupérer ces données n'est pas complexe, mais demande un petit matériel dédié. Le Linky dispose d'une prise dédiée, généralement protégée par un petit capot vert ou gris, nommée "TIC".

### Option 1 : Le dongle USB dédié (Recommandé)
C'est l'approche la plus stable. Vous achetez un petit adaptateur USB-TIC (souvent basé sur une puce FTDI ou un convertisseur série). Vous branchez deux fils de cuivre (torsadés) sur les bornes I1 et I2 du compteur Linky, et vous reliez le côté USB à votre serveur domotique (Home Assistant ou autre). 
Dans Home Assistant, une simple intégration dédiée détectera le port série et commencera à afficher instantanément votre consommation en Watts.

### Option 2 : La solution sans fil (Zigbee/Wi-Fi)
Si votre tableau électrique est trop loin de votre serveur domotique pour tirer un câble, il existe des modules Zigbee (comme le module TIC de chez Lixee ou Sonoff) qui se clipsent directement sur le compteur et envoient les données sans fil vers votre réseau Zigbee. 
C'est la solution idéale pour les maisons où le tableau électrique est dans le garage ou à l'extérieur. L'autonomie est généralement très bonne, et l'intégration dans Home Assistant est transparente via Zigbee2MQTT.

## Automatiser pour économiser : Le délestage dynamique

Une fois que votre domotique "voit" la consommation en temps réel, vous pouvez passer à l'automatisation intelligente. L'application la plus rentable est sans doute le **délestage électrique dynamique**.

La plupart des abonnements électriques sont calés sur une puissance de 6 kVA ou 9 kVA. Si vous dépassez cette puissance, votre disjoncteur général saute et toute la maison se retrouve dans le noir. 

Au lieu de payer un abonnement plus cher (12 kVA ou 15 kVA) par peur des coupures, vous pouvez utiliser la domotique pour piloter votre puissance appelée. 
*   **La règle d'or :** Si votre installation domotique détecte que la consommation totale de la maison approche de la limite de votre abonnement, elle coupe automatiquement les appareils non essentiels. 
*   **Scénario type :** "Si la consommation globale dépasse 5500W, alors couper immédiatement le chauffage électrique du garage et le lave-linge."
*   **Le résultat :** Votre maison évite le black-out, et vous pouvez rester sur un abonnement électrique moins coûteux. Vous gagnez sur tous les tableaux.

## L'optimisation solaire : Le nerf de la guerre

Si vous avez des panneaux photovoltaïques, la TIC est indispensable. L'objectif est d'utiliser un maximum de votre production solaire pour vos besoins internes plutôt que de la revendre à prix réduit à votre fournisseur.

C'est ce qu'on appelle "l'autoconsommation". 
Avec la donnée TIC en temps réel, vous pouvez automatiser la mise en route des appareils gourmands uniquement quand vos panneaux produisent un surplus.
*   *SI (Production Solaire > 2000W) ET (Consommation de la maison < 500W) ALORS Allumer le chauffe-eau.*
*   *SI le nuage passe et que la production chute, ALORS couper le chauffe-eau.*

Sans cette mesure en temps réel, vous chauffez votre eau à vos frais le soir au lieu de le faire gratuitement la journée avec votre propre électricité solaire.

## Pourquoi éviter l'application Enedis ?

L'application Enedis est un outil de service public. Elle est conçue pour la conformité et la facturation, pas pour la vie quotidienne. 

1. **La latence :** Enedis collecte les données, les traite, les envoie vers ses serveurs. La donnée n'est disponible que le lendemain. Pour un délestage ou pour charger votre voiture électrique au moment où le soleil tape fort, 24 heures de délai, c'est l'éternité.
2. **Le respect de la vie privée :** En connectant vos services domotiques à l'API Enedis, vous donnez accès à votre historique de consommation à une entreprise tierce. En utilisant la TIC locale, la donnée ne quitte jamais les murs de votre maison. Vous êtes le seul propriétaire de la lecture de vos compteurs.
3. **La stabilité :** Les APIs d'Enedis sont régulièrement mises à jour et peuvent être indisponibles. Votre port TIC local, lui, est immuable. Il fonctionne depuis 1990 et fonctionnera toujours en 2040. C'est le standard ultime de la fiabilité.


## Comprendre les trames TIC : Plongée dans les données brutes

Pour les plus technophiles, il est fascinant de comprendre ce que le Linky envoie réellement. La TIC communique via un protocole série simple (à 1200 bauds en mode historique, ou 9600 bauds en mode standard). 

Chaque seconde, le compteur envoie des "trames". Une trame est une succession de caractères ASCII qui contient des étiquettes (ex: `BASE`, `PAPP`, `HCHC`) suivies d'une valeur et d'un code de vérification (checksum).

*   `PAPP` : Puissance apparente (en VA). C'est votre consommation instantanée.
*   `HCHC` / `HCHP` : Heures Creuses / Heures Pleines. L'index de votre compteur.
*   `ADCO` : L'adresse de votre compteur (pour identifier votre installation).
*   `IMAX` : La puissance maximale atteinte depuis la dernière mise à zéro.

En décodant ces trames, vous n'avez plus seulement une "consommation" globale, vous avez une base de données temporelle capable de tracer la signature énergétique de chaque appareil de votre maison. Avec un peu d'analyse de données (sur Home Assistant), vous pouvez même détecter quand votre réfrigérateur se déclenche, quand la pompe à chaleur s'enclenche, ou quand une ampoule est allumée. La TIC, c'est l'ADN énergétique de votre maison.

## Guide de dépannage : Quand la télé-info ne répond pas

Si votre installation ne remonte aucune donnée dans Home Assistant, ne paniquez pas. C'est souvent un problème de configuration. Voici les pannes les plus fréquentes :

1. **Inversion des fils :** Bien que ce soit un signal alternatif, certains modules TIC sont sensibles à la polarité. Si ça ne marche pas, essayez d'inverser les deux fils sur les bornes I1 et I2 du Linky.
2. **Le capot du Linky :** Il arrive que le capot vert/gris du Linky soit mal clipsé, ou qu'il ne fasse pas bien contact. Assurez-vous qu'il est parfaitement en place.
3. **Le débit (Baud Rate) :** Comme mentionné, le mode "Standard" nécessite une vitesse de transmission beaucoup plus élevée. Vérifiez si votre module TIC supporte le mode 9600 bauds. Si vous avez un vieux module uniquement compatible avec le mode historique (1200 bauds), il ne verra rien en mode standard.
4. **Distance et blindage :** Si vous utilisez une rallonge de plus de 5 mètres, il est impératif d'utiliser du câble blindé pour éviter que le signal ne soit parasité par le champ électromagnétique des câbles de puissance qui passent à proximité.

En suivant ces étapes, vous résoudrez 99% des problèmes de remontée d'information.

## Vers une gestion proactive : Le délestage dynamique et intelligent

Nous avons parlé du délestage binaire (couper tout si ça dépasse), mais le futur de la domotique est à l'ajustement dynamique. Si votre superviseur domotique connaît votre consommation en temps réel et votre production solaire, il peut ajuster finement la puissance de vos appareils.

Par exemple, au lieu de couper complètement une pompe de piscine, vous pouvez réduire la vitesse de son variateur de fréquence. Au lieu de couper un chauffage, vous pouvez réduire la température de consigne d'un degré. C'est ce qu'on appelle le "lissage de courbe de charge". C'est là que la TIC devient un outil puissant : vous transformez une installation statique en un système dynamique qui s'adapte à la contrainte électrique du moment, sans jamais sacrifier brutalement votre confort.


## Le verdict : Reprenez la main sur votre compteur

Le compteur Linky n'est pas votre ennemi. C'est un instrument de mesure incroyablement précis, à condition que vous l'utilisiez à votre avantage. 

La Télé-Information Client est le seul moyen de construire une domotique énergétique intelligente. Si vous voulez réduire vos factures, arrêter les coupures de courant dues aux surcharges, ou optimiser votre production d'énergie solaire, vous devez impérativement passer par une lecture locale de votre TIC. 

C'est une installation qui coûte moins de 50 euros, qui se fait en dix minutes, et qui transforme totalement la gestion de votre foyer. Une fois que vous verrez les Watts de votre maison défiler en direct sur votre écran, vous ne pourrez plus jamais revenir en arrière. Vous ne serez plus un simple "consommateur" passif, vous serez devenu un gestionnaire actif de votre énergie.


## Les erreurs fréquentes dans la mise en place de la télé-info

La mise en place de la télé-info semble simple, mais beaucoup d'utilisateurs font des erreurs de débutant qui rendent la donnée inutilisable. 

La première est la longueur du câble. La TIC transmet une donnée série sur un signal faible. Si vous utilisez un câble trop fin, trop long (plus de 20-30 mètres sans protection) ou mal blindé, vous aurez des erreurs de trame : les données reçues seront corrompues, votre superviseur domotique affichera des valeurs aberrantes, et les automatisations seront impossibles. Utilisez toujours du câble blindé (type paire torsadée blindée, le câble Ethernet est parfait pour cela) pour relier les bornes I1 et I2 du Linky à votre boîtier adaptateur TIC.

Une autre erreur classique est de mal serrer les fils dans les borniers du compteur. Un faux contact, même minime, provoquera des coupures intempestives des données. Assurez-vous d'avoir un contact franc, surtout si votre tableau électrique subit des vibrations.

Enfin, certains utilisateurs oublient de configurer leur superviseur domotique pour interpréter correctement le mode de la TIC. Le Linky peut fonctionner en mode "historique" (standard ancien) ou en mode "standard" (nouveau protocole plus riche en données). Si votre module TIC est configuré pour l'un mais que le compteur émet en mode "standard", vous ne recevrez rien. Assurez-vous que votre module et votre compteur parlent exactement la même langue avant de chercher une panne logicielle qui n'existe pas.

## Sécurité informatique : Pourquoi la TIC est plus sûre qu'une app cloud

Un point souvent négligé est la sécurité informatique intrinsèque de la télé-info. En utilisant une connexion directe filaire entre votre compteur et votre serveur local, vous supprimez tout vecteur d'attaque distant.

Les applications Cloud (Enedis, ou les applications de fournisseurs d'énergie) reposent sur un serveur centralisé vulnérable aux attaques par force brute ou aux failles de sécurité de la plateforme Cloud. Si vous utilisez un service qui agrège les données de milliers d'utilisateurs, vous dépendez de la sécurité globale de ce service.

Avec la TIC locale, même si votre réseau domestique est attaqué, l'attaquant ne peut pas "lire" votre consommation historique globale sur un serveur central. Il ne peut lire que ce que vous lui donnez accès, et en local, vous avez le contrôle total sur qui peut voir cette donnée. C'est une architecture de sécurité "by design" que tout passionné de domotique devrait privilégier.

## L'apport de la domotique locale : Une vision globale de l'énergie

En combinant les données TIC avec d'autres capteurs (capteurs de température dans chaque pièce, détecteurs d'ouverture aux fenêtres, mesures de puissance sur les prises), vous construisez un modèle énergétique global de votre foyer. 

Vous pouvez comparer, par exemple, la consommation électrique réelle d'un radiateur au degré Celsius près à l'intérieur. Vous pouvez calculer le rendement réel de votre chauffage en corrélant la température extérieure (récupérée via une API météo) et votre consommation électrique globale. 

C'est là que la domotique dépasse la simple statistique : elle vous donne les clés pour comprendre l'efficacité thermique réelle de votre bâtiment. Vous ne cherchez plus à deviner pourquoi la facture explose, vous avez la réponse exacte en Watts. C'est le pouvoir de la donnée locale : elle vous transforme d'un spectateur inquiet en un acteur serein de votre propre transition énergétique. La TIC n'est pas juste un câble, c'est l'instrument de mesure d'un mode de vie plus sobre.
