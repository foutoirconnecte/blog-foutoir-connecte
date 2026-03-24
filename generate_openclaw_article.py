import os
import sys
from google import genai
from google.genai import types

def generate():
    client = genai.Client(api_key="AIzaSyDMyiTunvzGZt7axsEoLBV3cziZhY7Okpc")
    prompt = """
Tu es le rédacteur expert du blog "Le Foutoir Connecté".
Ton objectif est de rédiger un article complet sur le thème : "OpenClaw et la domotique : L'IA locale qui reprend le contrôle de votre maison en 2026."
L'article DOIT faire entre 2500 et 3000 mots. C'est CRUCIAL. Ne t'arrête pas avant, développe massivement chaque point technique avec des exemples.
Le contenu doit être formaté en Markdown.

CONSIGNES STRICTES :
1. Le Persona et le Ton
*   **Identité :** Un expert pragmatique de la domotique. Il a de l'expérience, il a fait les erreurs de débutant.
*   **Ton :** Professionnel, direct, utile et didactique. Pas de vulgarité ("balles", "brol" interdits).
*   **Règle du "Je" :** Le pronom "je/j'" doit être utilisé de manière légère (environ 2 à 3 fois par article) pour asseoir votre crédibilité. Le reste est orienté lecteur.

2. Contraintes de Format
*   **Longueur et Accessibilité :** Entre 2500 et 3000 mots. Vulgarise les concepts (LLM, RAG, agents locaux, inférence sur Raspberry Pi, intégration Home Assistant).
*   **Structure Rant/Fix/Verdict :**
    *   *Le Problème (Rant) :* Les assistants vocaux cloud (Alexa, Google Home) qui ne comprennent rien, espionnent, nécessitent internet et sont fermés.
    *   *La Solution (Fix) :* OpenClaw. Comment cet agent IA open-source fonctionnant en local révolutionne l'interaction avec la maison. Exemples de scénarios, intégration avec Home Assistant (par exemple via des skills), exécution de commandes complexes (ex: "éteins la lumière du salon mais laisse le couloir à 20% si l'alarme est armée"). Les prérequis matériels (NPU, RAM, Raspberry Pi 5).
    *   *Le Verdict :* Une conclusion pragmatique sur la maturité d'OpenClaw en 2026 pour le grand public.
*   Intégrer 2 à 3 liens internes pertinents. **ATTENTION FORMATAGE : Tous les liens (internes et externes) DOIVENT OBLIGATOIREMENT être mis en gras** avec cette syntaxe : `**[Texte du lien](/articles/url/)**`. (ex: **[Maison prédictive avec l'IA](/articles/maison-predictive-ia-2026/)** ou **[Les limites d'Alexa](/articles/domotique-commande-vocale-alexa-google-home/)** ou **[Raspberry Pi en domotique](/articles/raspberry-pi-domotique/)**).

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
title: "OpenClaw et la domotique : L'IA locale au service de votre maison intelligente"
date: '2026-03-17'
tags: ["openclaw", "ia-domotique", "cloud-vs-local", "home-assistant"]
image: "/images/openclaw-domotique.webp"
summary: "Fini les assistants vocaux limités et dépendants du cloud. Découvrez comment OpenClaw permet d'intégrer une véritable IA conversationnelle et locale à votre installation domotique."
---

Assure-toi de faire plus de 2500 mots en détaillant l'architecture logicielle, le respect de la vie privée (pas d'audio envoyé sur les serveurs GAFAM), et des cas d'usage avancés de type "Agent" (où l'IA prend des décisions multi-étapes basées sur les capteurs de la maison).
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=8192
        )
    )
    with open("/root/.openclaw/workspace/blog_domotique/site/articles/openclaw-ia-locale-domotique.md", "w") as f:
        f.write(response.text)
    print("Article généré avec succès.")

if __name__ == "__main__":
    generate()
