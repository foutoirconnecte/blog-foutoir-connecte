import os
import sys
from google import genai
from google.genai import types

def generate():
    client = genai.Client(api_key="AIzaSyDMyiTunvzGZt7axsEoLBV3cziZhY7Okpc")
    prompt = """
Tu es le rédacteur expert du blog "Le Foutoir Connecté".
Ton objectif est de rédiger un article complet sur le thème : "Panneaux solaires en 2026 : L'autonomie énergétique de votre maison connectée."
L'article DOIT faire entre 2500 et 3000 mots. C'est CRUCIAL. Développe massivement chaque aspect technique et pratique.
Le contenu doit être formaté en Markdown.

CONSIGNES STRICTES :
1. Le Persona et le Ton
*   **Identité :** Un expert pragmatique de la domotique, qui a testé et expérimenté. Il partage ses conseils sans jargon excessif.
*   **Ton :** Professionnel, direct, utile et didactique. Pas de familiarité excessive.
*   **Règle du "Je" :** Le pronom "je/j'" doit être utilisé de manière légère (2-3 fois) pour asseoir la crédibilité, le reste est orienté lecteur.

2. Contraintes de Format
*   **Longueur et Accessibilité :** Entre 2500 et 3000 mots. Guide de référence accessible aux débutants, mais techniquement approfondi. Vulgarise les concepts (type de panneaux, onduleurs, batteries, TWh, autoconsommation, revente, aides de l'état, intégration domotique).
*   **Structure Rant/Fix/Verdict :**
    *   *Le Problème (Rant) :* La complexité apparente de l'installation, les coûts initiaux élevés, les aides administratives parfois opaques, le manque de retour sur investissement clair.
    *   *La Solution (Fix) :* Comment choisir le bon matériel, optimiser son installation pour l'autoconsommation (gestion des appareils connectés), comprendre les aides financières, les bénéfices sur le long terme (économique et écologique), l'intégration avec un système domotique (ex: **[Home Assistant](/articles/home-assistant/)** pour gérer la charge des batteries ou les appareils énergivores).
    *   *Le Verdict :* Une conclusion pragmatique sur la viabilité et l'intérêt des panneaux solaires en 2026 pour une maison connectée.
*   Intégrer 2 à 3 liens internes pertinents. **ATTENTION FORMATAGE : Tous les liens (internes et externes) DOIVENT OBLIGATOIREMENT être mis en gras** avec cette syntaxe : `**[Texte du lien](/chemin/vers/article/)**`.

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
title: "Panneaux solaires en 2026 : L'autonomie énergétique de votre maison connectée"
date: 2026-03-18T00:00:00Z
tags: ["matériel", "domotique", "économies-dénergie"]
image: "/images/panneaux-solaires-maison-2026.webp"
summary: "Explorez comment les panneaux solaires transforment votre maison en un centre d'énergie autonome, optimisée par la domotique, et devenez maître de votre consommation et de vos factures."
---

Sois très détaillé sur les aspects techniques et financiers. Explique les différents types de panneaux (monocristallin, polycristallin, silicium amorphe), les onduleurs (string, micro-onduleurs, hybrides), les systèmes de stockage (batteries au lithium, technologie Flow), l'autoconsommation, la loi d'orientation des énergies renouvelables (loi ENE). Donne des conseils concrets pour bien choisir son installateur et son matériel.
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=8192
        )
    )
    with open("/root/.openclaw/workspace/blog_domotique/site/articles/panneaux-solaires-maison-2026.md", "w") as f:
        f.write(response.text)
    print("Article généré avec succès.")

if __name__ == "__main__":
    generate()
