---
layout: article.njk
title: "Sécurité Wi-Fi pour la Domotique : comment isoler vos objets connectés (VLAN, Réseau Invité)"
date: 2026-03-11
tags: ["article", "Réseau", "Sécurité"]
image: "https://images.unsplash.com/photo-1557597774-9d273605dfa9?q=80https://images.unsplash.com/photo-1526374965328-5f61d25c0940?q=80&w=1200&auto=format&fit=cropw=1200https://images.unsplash.com/photo-1526374965328-5f61d25c0940?q=80&w=1200&auto=format&fit=cropauto=formathttps://images.unsplash.com/photo-1526374965328-5f61d25c0940?q=80&w=1200&auto=format&fit=cropfit=crop"
summary: "Vos objets connectés partagent le même réseau Wi-Fi que votre ordinateur personnel et vos données bancaires. C'est une porte d'entrée béante pour les pirates. Découvrez pourquoi et comment créer des réseaux virtuels (VLAN) ou invités pour isoler hermétiquement votre domotique et protéger votre vie numérique."
---

Vous avez suivi nos conseils. Votre maison est équipée d'une **[cinquantaine d'objets connectés](/articles/maison-tout-wifi-box-internet/)**, vous avez un **[cerveau domotique local](/articles/unifier-applications-domotique/)**, et vous n'avez plus aucun équipement qui dépend du **[Cloud chinois](/articles/smart-life-tuya-cloud-chinois-domotique/)**. Vous pensez être en sécurité.

Pourtant, il reste une faille de sécurité béante dans 99% des installations domestiques. 

Tous vos équipements – votre ordinateur portable contenant vos factures et vos mots de passe, votre smartphone avec vos photos de famille, et la petite ampoule Wi-Fi à 8 euros achetée sur un coup de tête – sont connectés sur le même et unique réseau Wi-Fi fourni par votre box opérateur.

C'est l'équivalent numérique de laisser la clé de votre coffre-fort sous le paillasson de votre porte d'entrée. 

## Le maillon faible de la chaîne

La sécurité d'un réseau informatique est toujours égale à celle de son maillon le plus faible. Vous pouvez avoir le meilleur antivirus du monde sur votre PC Windows, si le firmware (logiciel interne) de votre ampoule connectée n'a pas été mis à jour depuis trois ans et contient une faille de sécurité connue, un pirate informatique peut l'exploiter.

Une fois qu'un pirate a pris le contrôle d'un seul objet connecté sur votre réseau (une caméra, une prise, un thermostat), il se trouve à l'intérieur de votre forteresse numérique. À partir de là, il peut scanner l'ensemble de votre réseau local, détecter votre ordinateur portable, et tenter d'y pénétrer pour y voler vos données personnelles.

Les fabricants d'objets connectés, surtout les marques à bas coût, sont notoirement mauvais en matière de suivi logiciel et de sécurité. Les failles zero-day y sont légion. Confier la sécurité de votre vie numérique à la robustesse du code écrit par l'ingénieur d'une usine lointaine pour une prise vendue 5 euros est un pari que vous ne devriez jamais prendre.

## Le Fix : Le confinement numérique (La segmentation réseau)

La seule solution professionnelle pour contrer cette menace est de mettre en place une "segmentation réseau". L'idée est simple : vos objets connectés (l'IoT) doivent vivre dans un monde parallèle, un ghetto numérique dont ils ne peuvent pas s'échapper. Ils doivent pouvoir parler à internet et à votre box domotique, mais ils ne doivent JAMAIS avoir le droit de discuter avec votre ordinateur personnel ou votre smartphone.

Pour réaliser cette isolation, il existe deux grandes méthodes, de la plus simple à la plus experte.

### Méthode 1 : Le Réseau "Invité" (La solution simple)

La plupart des routeurs Wi-Fi modernes, même ceux des fournisseurs d'accès, proposent une fonctionnalité appelée "Réseau Invité" (Guest Network). 

À l'origine, cette fonction est pensée pour donner un accès internet temporaire à vos amis de passage, sans leur donner le mot de passe de votre réseau principal. Mais nous allons la détourner pour un usage beaucoup plus intelligent.

La procédure est la suivante :
1.  Connectez-vous à l'interface d'administration de votre routeur.
2.  Activez le réseau Wi-Fi "Invité". Donnez-lui un nom clair (par exemple, "Maison_IoT") et un mot de passe robuste.
3.  Très important : cherchez une case à cocher qui s'appelle **"Isoler les clients"**, **"Bloquer l'accès au réseau local"** ou **"Client Isolation"**. Cochez-la impérativement.
4.  Reconnectez un par un TOUS vos objets connectés (ampoules, prises, caméras) sur ce nouveau réseau Wi-Fi "Maison_IoT".
5.  Gardez votre réseau Wi-Fi principal (celui que vous utilisiez jusqu'à présent) exclusivement pour vos appareils de confiance : ordinateurs, smartphones, tablettes.

En activant l'"Isolation des clients", vous venez de créer un mur de feu invisible. Les appareils connectés sur le réseau "Maison_IoT" peuvent tous aller sur internet, mais ils sont devenus incapables de se voir les uns les autres, et surtout, ils sont devenus incapables de voir les appareils connectés sur votre réseau principal. Si un pirate prend le contrôle de votre ampoule, il se retrouvera piégé dans une impasse numérique, incapable de scanner le reste de votre domicile.

### Méthode 2 : Les VLAN (L'architecture experte)

Pour les utilisateurs les plus exigeants qui possèdent un **[routeur Wi-Fi Mesh avancé](/articles/maison-tout-wifi-box-internet/)** (comme ceux des marques Ubiquiti, TP-Link Omada, ou un routeur customisé sous pfSense), le concept de "Réseau Invité" peut être poussé à un niveau de granularité beaucoup plus fin grâce aux **VLAN** (Virtual Local Area Network).

Un VLAN est une technique qui permet de créer plusieurs réseaux virtuels complètement étanches, alors qu'ils partagent le même matériel physique (le même routeur, les mêmes câbles). 

L'architecture typique d'un réseau domestique sécurisé ressemble à ça :
*   **VLAN 10 (Principal) :** Le réseau de confiance pour les PC, Mac, et smartphones de la famille.
*   **VLAN 20 (IoT) :** Le réseau pour tous les objets connectés domotiques (ampoules, prises, capteurs). Ce VLAN a le droit de parler au VLAN 10, mais uniquement pour répondre à une requête initiée depuis le VLAN 10 (par exemple, quand votre smartphone demande l'état d'une ampoule). Le VLAN 20 n'a jamais le droit d'initier une conversation vers le VLAN 10.
*   **VLAN 30 (Caméras) :** Un réseau ultra-verrouillé pour les **[caméras de sécurité](/articles/cameras-securite-abonnement-cloud/)**. Ce VLAN n'a même pas le droit d'accéder à internet, pour garantir une confidentialité absolue. Seul votre serveur domotique (ou votre NVR) est autorisé à communiquer avec lui.
*   **VLAN 40 (Invités) :** Le réseau pour les amis de passage. Ce VLAN a le droit d'aller sur internet, et c'est tout.

La mise en place de VLAN est plus complexe. Elle demande de configurer des "règles de pare-feu" (Firewall Rules) pour définir précisément qui a le droit de parler à qui. C'est le standard absolu de la sécurité en entreprise, appliqué à l'échelle de votre domicile.

## Le verdict : Ne faites pas confiance à vos objets connectés

La conclusion de cette paranoïa organisée est simple : un objet connecté, surtout s'il est bon marché, doit être considéré comme une menace potentielle par défaut. 

La segmentation réseau n'est pas une option, c'est une nécessité architecturale dès que vous dépassez une dizaine d'appareils connectés. 
Commencez dès aujourd'hui par activer le réseau "Invité" de votre box et par y migrer tous vos gadgets. Ce simple geste élèvera la sécurité de votre réseau domestique d'un cran significatif. Le jour où vous investirez dans un vrai routeur, la segmentation par VLAN sera la suite logique de votre quête d'une maison connectée non seulement intelligente, mais surtout, impénétrable.
