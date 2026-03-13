---
layout: article.njk
title: "Voice-over-IP Local : piloter sa maison à la voix sans un gramme de Cloud avec l'IA"
date: 2026-03-13
tags: ["article", "domotique", "intelligence_artificielle", "home-assistant", "vie-privee", "voix"]
image: "/images/voip-local-ia.webp"
summary: "Abandonner les assistants connectés de Google ou Amazon pour une solution 100% locale, basée sur des LLM et du VoIP, afin d'assurer la confidentialité et la résilience totale du contrôle vocal de sa maison."
---

Le contrôle vocal de la maison intelligente a longtemps été dominé par des écosystèmes centralisés et dépendants du cloud. Les assistants vocaux comme Amazon Alexa ou Google Assistant capturent nos voix, transmettent les enregistrements sur des serveurs distants, analysent nos requêtes via des modèles propriétaires, puis renvoient la commande à nos équipements locaux. Cette dépendance pose un problème majeur de confidentialité, de latence et de résilience. Si la connexion internet tombe, la maison devient silencieuse. Si le service cloud décide de modifier ses conditions d'utilisation, l'utilisateur est pris en otage.

Il est désormais possible de reprendre le contrôle. L'intégration des technologies Voice-over-IP (VoIP) avec des modèles de langage (LLM) exécutés localement permet de créer un assistant vocal performant, rapide et totalement déconnecté d'internet. Ce guide technique détaille la conception et la mise en œuvre d'une architecture voix sur IP locale couplée à l'intelligence artificielle pour le pilotage d'une installation domotique basée sur Home Assistant.

## Le problème : la dépendance au Cloud

La promesse initiale de la maison intelligente était de simplifier la vie quotidienne tout en conservant le contrôle de son environnement. L'arrivée des assistants vocaux a introduit une faille structurelle dans cette philosophie. Les enceintes connectées agissent comme des microphones ouverts en permanence, attendant un mot de réveil. Une fois déclenchés, ils enregistrent la conversation et l'envoient à un serveur externe.

Ce modèle présente des défauts techniques et éthiques. Sur le plan technique, l'aller-retour vers le cloud ajoute une latence incompressible, allant de plusieurs centaines de millisecondes à plusieurs secondes. Les pannes de serveurs externes paralysent l'infrastructure locale. Éthiquement, l'analyse des requêtes permet aux entreprises de profiler les utilisateurs, de comprendre leurs habitudes, de connaître les horaires de présence et même d'extrapoler leur niveau de vie en fonction des équipements contrôlés.

J'ai personnellement subi les conséquences d'une panne serveur d'un géant du cloud qui m'a empêché de fermer les volets de la maison depuis mon canapé pendant quarante-huit heures, me forçant à repenser intégralement l'architecture de contrôle. Une installation domotique fiable doit être autonome.

## La solution : l'architecture VoIP et l'IA locale

La solution consiste à recréer la chaîne de traitement vocal en interne. L'architecture repose sur trois piliers : la capture de l'audio via un réseau VoIP local, la transcription de la voix en texte (Speech-to-Text), le traitement de la commande par une intelligence artificielle, et la génération d'une réponse audio (Text-to-Speech).

### Capture de l'audio : Le protocole SIP

Le protocole SIP (Session Initiation Protocol) est le standard de l'industrie pour la voix sur IP. Dans notre infrastructure, nous utilisons des téléphones IP matériels, des softphones ou des microcontrôleurs ESP32 configurés comme terminaux SIP. Ces appareils s'enregistrent sur un serveur PBX local, souvent Asterisk ou FreePBX.

L'avantage du SIP réside dans sa robustesse et sa flexibilité. Un combiné téléphonique SIP sur le bureau ou un interphone mural devient un point d'entrée direct vers le système domotique. L'audio est transmis sans compression destructive, garantissant une qualité optimale pour l'étape de transcription. Le flux audio reste confiné au réseau local (LAN), généralement isolé dans un VLAN dédié (VLAN IoT) pour des raisons de sécurité. L'isolation du réseau est une pratique de conception que j'applique systématiquement pour limiter la surface d'attaque.

### Transcription : Speech-to-Text avec Whisper

Une fois le flux audio capturé par le serveur PBX, il doit être converti en texte. Nous utilisons l'intégration VoIP de Home Assistant couplée à un moteur de transcription. L'intégration de la technologie Whisper, développée par OpenAI, permet d'exécuter la transcription localement, souvent via un add-on sur le serveur Home Assistant ou sur une machine dédiée (par exemple, un conteneur Docker utilisant la puissance d'un GPU ou d'un NPU pour accélérer l'inférence).

Le modèle Whisper base (ou small pour une meilleure précision) offre un compromis idéal entre rapidité d'exécution et taux de reconnaissance correcte, même avec des accents ou du bruit de fond. La transcription s'effectue en quelques centaines de millisecondes, rendant la latence quasiment imperceptible.

### Intelligence Artificielle : Le cerveau local

La chaîne classique de Home Assistant se contentait de comparer le texte transcrit à une liste de phrases prédéfinies. Cette approche rigide ne permet pas la flexibilité d'un véritable assistant. L'intégration de modèles de langage (LLM) en local change la donne.

Nous utilisons des outils comme Ollama ou LM Studio pour héberger des modèles ouverts tels que Llama 3 ou Mistral sur un serveur local. Home Assistant dialogue avec ce modèle via une API locale. Le LLM reçoit le texte transcrit ainsi que le contexte de la maison (l'état des lumières, la température des pièces, le statut des capteurs). Il analyse l'intention de l'utilisateur, même si la phrase est formulée de manière imprécise ("Il fait un peu sombre ici", "Baisse la température de la chambre"), et génère l'action correspondante à envoyer à Home Assistant, accompagnée d'une réponse textuelle.

### Réponse : Text-to-Speech avec Piper

La réponse textuelle générée par le LLM ou par Home Assistant doit être convertie en audio pour être renvoyée au terminal VoIP. Piper est un moteur Text-to-Speech neuronal conçu spécifiquement pour une exécution locale rapide, y compris sur des architectures ARM comme le Raspberry Pi. Piper produit des voix naturelles, bien loin des synthèses vocales robotiques des décennies précédentes. Le flux audio est ensuite renvoyé via la connexion SIP au combiné ou au haut-parleur.

## Mise en œuvre technique

La mise en place de cette architecture requiert plusieurs composants matériels et logiciels.

### Matériel requis

*   Un serveur robuste (ex: Intel NUC, Mini PC avec un processeur récent, idéalement avec un GPU Nvidia ou un accélérateur Coral TPU) pour héberger Home Assistant, Asterisk, et les modèles d'IA.
*   Des terminaux VoIP : téléphones fixes SIP (Grandstream, Yealink), interphones SIP, ou des dispositifs personnalisés basés sur des ESP32 (ex: ESP32-S3-BOX-3) avec firmware ESPHome.
*   Un commutateur réseau (switch) gérable pour configurer des VLANs.

### Logiciels et configuration

1.  **Home Assistant OS ou Supervised :** La base du système.
2.  **Serveur SIP (Asterisk) :** Déployé sous forme de conteneur Docker ou d'add-on. Configuration des extensions (comptes SIP) pour chaque terminal.
3.  **Wyoming Protocol :** Home Assistant utilise le protocole Wyoming pour communiquer de manière fluide et rapide avec les services vocaux locaux.
4.  **Wyoming Whisper :** Installation de l'add-on ou du conteneur pour le Speech-to-Text. Choix du modèle linguistique adapté à la langue et à la puissance du serveur.
5.  **Wyoming Piper :** Installation du service Text-to-Speech. Configuration de la voix française désirée.
6.  **Ollama (optionnel mais recommandé) :** Hébergement du LLM localement.
7.  **Home Assistant VoIP Integration :** Configuration de l'intégration dans Home Assistant. Il faut renseigner l'adresse IP du serveur SIP et configurer un pont pour rediriger les appels entrants vers le pipeline vocal.

### Le flux d'exécution (Pipeline)

Dans Home Assistant, le pipeline vocal est la colonne vertébrale du système. Il définit l'enchaînement des opérations :
1.  **Entrée :** La source audio (le flux SIP entrant).
2.  **STT (Speech-to-Text) :** Le service Wyoming Whisper convertit l'audio en texte.
3.  **Intention :** Le moteur de conversation, soit l'analyseur intégré de Home Assistant, soit un LLM local externe, identifie l'action.
4.  **TTS (Text-to-Speech) :** Le service Wyoming Piper génère l'audio de la réponse.
5.  **Sortie :** L'audio est renvoyé vers le flux SIP.

L'optimisation des paramètres, notamment la détection de la fin de parole (VAD - Voice Activity Detection), est cruciale pour réduire la latence. Un VAD trop sensible coupera l'utilisateur en plein milieu d'une phrase, tandis qu'un VAD trop permissif ajoutera un délai artificiel avant le début du traitement.

## Sécurisation et bonnes pratiques

Déployer un serveur SIP sur un réseau local impose des règles de sécurité strictes. Un serveur Asterisk mal configuré est une cible privilégiée pour les attaques de force brute.

*   **VLAN dédié :** Placer tous les équipements VoIP et le serveur Asterisk dans un VLAN isolé, sans accès à internet. Les règles de pare-feu doivent limiter les flux au strict minimum (ports SIP 5060/5061, plage de ports RTP, accès HTTP(S) vers l'API Home Assistant).
*   **Mots de passe forts :** Les identifiants SIP (secrets) doivent être longs et générés aléatoirement.
*   **Fail2Ban :** Déployer un outil de bannissement automatique pour bloquer les adresses IP tentant de se connecter avec des identifiants incorrects, bien que ce risque soit mitigé par l'isolation du VLAN.

## Résolution des problèmes fréquents

La mise en place du VoIP local peut présenter des défis, principalement liés au routage de l'audio (RTP) et à la gestion des codecs.

*   **Audio unidirectionnel (One-Way Audio) :** Le problème le plus courant en VoIP. Il est généralement causé par un problème de routage NAT (Network Address Translation) ou des règles de pare-feu bloquant le flux RTP dans un sens. L'utilisation d'un serveur STUN local ou une configuration précise des plages de ports RTP dans le pare-feu résout le problème.
*   **Latence excessive :** La latence peut provenir du réseau (mauvaise gestion de la qualité de service QoS) ou de la surcharge du serveur hébergeant Whisper/Piper. Assurez-vous que le serveur dispose de ressources suffisantes et, si possible, déportez les services gourmands en CPU vers une machine dotée d'un accélérateur matériel. Le choix d'un codec audio léger comme le G.711 (PCMA/PCMU) ou Opus est également déterminant.

## Le Verdict

La construction d'un assistant vocal local basé sur le VoIP et l'IA demande un investissement initial en temps, en compétences techniques et en matériel. Elle exige de configurer un serveur Asterisk, de gérer des modèles linguistiques et d'affiner des paramètres réseau souvent complexes.

La récompense justifie largement cet effort. Le résultat est un système domotique qui obéit instantanément, qui comprend le contexte, et qui garantit une confidentialité absolue. Aucune donnée vocale ne quitte le réseau local. Le système reste fonctionnel même si la liaison fibre de votre domicile est coupée par un pelleteuse. Cette résilience est la définition même d'une architecture informatique mature. En supprimant la dépendance aux serveurs de la Silicon Valley, l'utilisateur retrouve la pleine souveraineté sur son environnement technologique. J'en ai la conviction après avoir opéré cette transition : l'avenir de la domotique exige des infrastructures locales robustes, où l'intelligence artificielle est un outil sous notre contrôle total, et non un point de défaillance externe. Lisez également mon guide sur [le choix du protocole Zigbee ou Thread](/articles/zigbee-ou-thread) pour compléter votre compréhension des réseaux locaux, ou explorez l'importance du fil neutre dans [notre dossier sur le câblage électrique](/articles/importance-neutre-domotique) pour préparer vos installations. La maison intelligente locale est la seule approche pérenne.
