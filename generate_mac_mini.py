import os
import sys
from google import genai
from google.genai import types

def generate():
    client = genai.Client(api_key="AIzaSyDMyiTunvzGZt7axsEoLBV3cziZhY7Okpc")
    prompt = """
Tu es le rédacteur expert du blog "Le Foutoir Connecté".
Ton objectif est de rédiger un article complet sur le thème : "Mac mini M4 : Le serveur domotique ultime pour votre maison connectée ?"
L'article DOIT faire entre 2500 et 3000 mots. C'est CRUCIAL. Développe massivement chaque aspect technique (architecture ARM, consommation watts, Docker, Home Assistant, silence).
Le contenu doit être formaté en Markdown. Ne mets SURTOUT PAS de balises ```markdown au début et ``` à la fin de ta réponse. Commence directement par le frontmatter "---".

CONSIGNES STRICTES :
1. Le Persona et le Ton
*   **Identité :** Un expert pragmatique de la domotique.
*   **Ton :** Professionnel, direct, utile et didactique.
*   **Règle du "Je" :** Le pronom "je/j'" doit être utilisé de manière légère (2-3 fois).

2. Contraintes de Format
*   **Longueur et Accessibilité :** Entre 2500 et 3000 mots.
*   **Structure Rant/Fix/Verdict :**
    *   *Le Problème (Rant) :* Les serveurs PC classiques qui consomment 100W, font du bruit et chauffent. Les Raspberry Pi qui sont super mais parfois limités pour de la vidéo ou de l'IA locale lourde.
    *   *La Solution (Fix) :* Le Mac mini (surtout les puces Apple Silicon M1/M2/M4). Rapport performance/watt imbattable. Silence absolu. Comment l'utiliser comme serveur (Home Assistant en VM ou Docker, Plex/Jellyfin, Frigate pour les caméras). Le coût initial vs l'économie d'électricité sur 5 ans.
    *   *Le Verdict :* Est-ce overkill ou le meilleur investissement pérenne ?
*   Intégrer 2 à 3 liens internes pertinents. **ATTENTION FORMATAGE : Tous les liens DOIVENT OBLIGATOIREMENT être mis en gras** avec cette syntaxe exacte : `**[Texte du lien](/chemin/vers/article/)**`. Exemples : **[Raspberry Pi en domotique](/articles/raspberry-pi-domotique/)** ou **[IA locale et voix](/articles/ia-locale-voix-2026/)**.

3. Le Filtre Anti-IA (Mots à bannir)
INTERDICTION d'utiliser : "Plongeons dans...", "Révolutionner", "Symphonie", "En effet", "De plus". Pas d'émojis dans le texte.

4. Frontmatter
Inclus le frontmatter exact (en haut) et commence ta réponse par "---" :
---
layout: article.njk
title: "Mac mini M4 : Le serveur domotique ultime ou un luxe inutile ?"
date: 2026-03-22
tags: ["matériel", "google-/-apple-/-amazon", "domotique"]
image: "/images/mac-mini-serveur.webp"
summary: "Oubliez les gros serveurs bruyants. Le Mac mini et sa puce Apple Silicon pourraient bien être la clé de voûte silencieuse et surpuissante de votre maison connectée."
---
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=8192
        )
    )
    with open("/root/.openclaw/workspace/blog_domotique/site/articles/mac-mini-serveur.md", "w") as f:
        f.write(response.text)
    print("Article généré avec succès.")

if __name__ == "__main__":
    generate()
