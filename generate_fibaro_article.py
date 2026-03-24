import os
import sys
from google import genai
from google.genai import types

def generate():
    client = genai.Client(api_key="AIzaSyDMyiTunvzGZt7axsEoLBV3cziZhY7Okpc")
    prompt = """
Tu es le rédacteur expert du blog "Le Foutoir Connecté".
Ton objectif est de rédiger un article complet sur le thème de la marque "Fibaro", connue pour ses modules domotiques haut de gamme (Z-Wave), leur fiabilité, leur design soigné mais aussi leur prix élevé. Faut-il encore investir dans du Fibaro en 2026 face à Shelly, Sonoff et l'essor de Zigbee/Matter ?
L'article DOIT faire entre 2500 et 3000 mots. C'est crucial. Ne t'arrête pas avant.
Le contenu doit être formaté en Markdown.

CONSIGNES STRICTES :
1. Le Persona et le Ton
*   **Identité :** Un expert pragmatique de la domotique. Il a de l'expérience, il a fait les erreurs de débutant, et son but est d'éviter à ses lecteurs de perdre du temps et de l'argent.
*   **Ton :** Professionnel, direct, utile et didactique. Pas de vulgarité, pas de familiarité excessive ("balles", "brol" interdits). On ne ramène pas tout à soi.
*   **Règle du "Je" :** Le pronom "je/j'" doit être utilisé de manière légère (environ 2 à 3 fois par article) pour asseoir votre crédibilité. Le reste est orienté lecteur.

2. Contraintes de Format
*   **Longueur et Accessibilité :** Entre 2500 et 3000 mots. L'article doit être un guide de référence (pillar content) extrêmement approfondi, mais totalement accessible aux débutants. Vulgarise les concepts (ex: Z-Wave, maillage, routage, neutre).
*   **Structure Rant/Fix/Verdict :**
    *   *Le Problème (Rant) :* L'explosion de la domotique low-cost (Zigbee, Wi-Fi) qui fait passer Fibaro pour un dinosaure hors de prix.
    *   *La Solution (Fix) :* Pourquoi Fibaro (et le Z-Wave) reste le roi de la fiabilité pour les installations encastrées critiques, et dans quels cas l'utiliser (ou l'éviter). Analyse technique des modules (Roller Shutter, Dimmer, capteurs).
    *   *Le Verdict :* Une conclusion pragmatique et définitive sur la place de Fibaro en 2026.
*   Intégrer 2 à 3 liens internes (ex: [Shelly Pro](/articles/shelly-pro-2026/) ou [Domotique tableau électrique](/articles/domotique-tableau-electrique-rail-din/)).

3. Le Filtre Anti-IA (Mots à bannir)
INTERDICTION d'utiliser :
*   "Plongeons dans..." / "Naviguer dans le paysage..." / "Découvrir le potentiel..."
*   "Il est crucial de souligner..." / "En fin de compte..." / "Il convient de noter..."
*   "En effet", "De plus", "Ainsi", "Par conséquent"
*   "Symphonie", "Révolutionner", "Un véritable jeu d'enfant", "L'allié idéal", "Polyvalent".
*   "Dans ce monde numérique en constante évolution..."
*   Pas d'émojis dans le texte.

4. Frontmatter
Inclus le frontmatter exact (en haut) :
---
layout: article.njk
title: "Fibaro en 2026 : Le roi déchu ou l'investissement indispensable ?"
date: '2026-03-17'
tags: ["matériel", "domotique", "capteurs"]
image: "/images/fibaro-domotique.webp"
summary: "Face à l'avalanche de modules Zigbee et Wi-Fi low-cost, la marque premium Fibaro justifie-t-elle encore son prix stratosphérique ? Analyse technique et verdicts."
---

L'article doit être exceptionnellement long, détaillé, technique mais compréhensible, en évitant les phrases creuses. Rentre dans les détails électriques, les schémas de câblage sans neutre (Dimmer 2), la portée du Z-Wave vs Zigbee, la qualité des plastiques et des borniers. Fais ~2500 mots.
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=8192
        )
    )
    with open("/root/.openclaw/workspace/blog_domotique/site/articles/fibaro-domotique-2026.md", "w") as f:
        f.write(response.text)
    print("Article généré avec succès.")

if __name__ == "__main__":
    generate()
