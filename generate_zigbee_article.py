import os
import sys
from google import genai
from google.genai import types

def generate():
    client = genai.Client(api_key="AIzaSyDMyiTunvzGZt7axsEoLBV3cziZhY7Okpc")
    prompt = """
Tu es le rédacteur expert du blog "Le Foutoir Connecté".
Ton objectif est de rédiger un article complet sur le thème : "Comprendre le Zigbee : Le protocole indispensable de la maison connectée."
L'article DOIT faire entre 2500 et 3000 mots. C'est CRUCIAL. Développe massivement chaque aspect technique et pratique pour atteindre cette longueur.
Le contenu doit être formaté en Markdown. Ne mets SURTOUT PAS de balises ```markdown au début et ``` à la fin de ta réponse. Commence directement par le frontmatter "---".

CONSIGNES STRICTES :
1. Le Persona et le Ton
*   **Identité :** Un expert pragmatique de la domotique, qui a testé et expérimenté.
*   **Ton :** Professionnel, direct, utile et didactique. Pas de familiarité excessive.
*   **Règle du "Je" :** Le pronom "je/j'" doit être utilisé de manière légère (2-3 fois) pour asseoir la crédibilité.

2. Contraintes de Format
*   **Longueur et Accessibilité :** Entre 2500 et 3000 mots. Vulgarise les concepts (réseau maillé / mesh, routeur, end-device, coordinateur, fréquence 2.4 GHz vs Wi-Fi, consommation d'énergie).
*   **Structure Rant/Fix/Verdict :**
    *   *Le Problème (Rant) :* Pourquoi empiler des ampoules et prises Wi-Fi finit par tuer la box internet et créer une maison connectée instable et gourmande en énergie.
    *   *La Solution (Fix) :* Le Zigbee. Explique l'architecture (Coordinateur, Routeur, End Device), le maillage (mesh network), la différence avec le Wi-Fi/Bluetooth, l'impact sur les piles (capteurs qui durent 2 ans), le matériel nécessaire (clé Sonoff, passerelle Aqara), l'écosystème ouvert (ZHA, Zigbee2MQTT).
    *   *Le Verdict :* Conclusion claire sur pourquoi le Zigbee reste le standard roi en 2026.
*   Intégrer 2 à 3 liens internes pertinents. **ATTENTION FORMATAGE : Tous les liens (internes et externes) DOIVENT OBLIGATOIREMENT être mis en gras** avec cette syntaxe exacte : `**[Texte du lien](/chemin/vers/article/)**`. Exemples de liens à intégrer : **[Aqara vs Sonoff](/articles/aqara-vs-sonoff-2026/)** ou **[Zigbee vs Matter](/articles/zigbee-vs-matter-2026/)**.

3. Le Filtre Anti-IA (Mots à bannir)
INTERDICTION d'utiliser :
*   "Plongeons dans..." / "Naviguer dans le paysage..." / "Découvrir le potentiel..."
*   "Il est crucial de souligner..." / "En fin de compte..." / "Il convient de noter..."
*   "En effet", "De plus", "Ainsi", "Par conséquent"
*   "Symphonie", "Révolutionner", "Un véritable jeu d'enfant", "L'allié idéal", "Polyvalent".
*   "Dans ce monde numérique en constante évolution..."
*   Pas d'émojis dans le texte.

4. Frontmatter
Inclus le frontmatter exact (en haut) et commence ta réponse par "---" :
---
layout: article.njk
title: "Qu'est-ce que le Zigbee ? Le guide complet pour les débutants en domotique"
date: 2026-03-19
tags: ["zigbee", "débutant-en-domotique", "réseau"]
image: "/images/comprendre-le-zigbee-debutant.webp"
summary: "Oubliez les appareils Wi-Fi qui saturent votre box internet. Découvrez le Zigbee, le protocole réseau maillé basse consommation qui fait tourner 90% des maisons intelligentes fiables."
---

Sois exhaustif sur la topologie du réseau, l'interopérabilité (ou l'absence d'interopérabilité chez certains constructeurs), l'importance des routeurs sur secteur (ampoules, prises) pour étendre la portée, et les canaux Zigbee vs Wi-Fi pour éviter les interférences.
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=8192
        )
    )
    with open("/root/.openclaw/workspace/blog_domotique/site/articles/comprendre-le-zigbee-debutant.md", "w") as f:
        f.write(response.text)
    print("Article généré avec succès.")

if __name__ == "__main__":
    generate()
