import os
import sys
from google import genai
from google.genai import types

def generate():
    client = genai.Client(api_key="AIzaSyDMyiTunvzGZt7axsEoLBV3cziZhY7Okpc")
    prompt = """
Tu es le rédacteur expert du blog "Le Foutoir Connecté".
Ton objectif est de rédiger un article complet sur le thème : "Le frigo connecté : Révolution familiale ou gadget hors de prix ?"
L'article DOIT faire entre 2500 et 3000 mots. C'est CRUCIAL. Développe massivement chaque aspect technique et pratique pour atteindre cette longueur (gestion des stocks, consommation électrique, domotisation maison, obsolescence).
Le contenu doit être formaté en Markdown. Ne mets SURTOUT PAS de balises ```markdown au début et ``` à la fin de ta réponse. Commence directement par le frontmatter "---".

CONSIGNES STRICTES :
1. Le Persona et le Ton
*   **Identité :** Un expert pragmatique de la domotique, qui est AUSSI un père de famille gérant le quotidien d'une tribu.
*   **Ton :** Professionnel, direct, utile et didactique, ancré dans la réalité familiale. Pas de familiarité excessive.
*   **Règle du "Je" :** Le pronom "je/j'" doit être utilisé de manière légère (2-3 fois) pour asseoir la crédibilité de père de famille.
*   **MOTS OBLIGATOIRES :** Tu DOIS impérativement intégrer de façon naturelle les mots "fraises" et "carte de fidélité" dans le texte.

2. Contraintes de Format
*   **Longueur et Accessibilité :** Entre 2500 et 3000 mots. Vulgarise les concepts.
*   **Structure Rant/Fix/Verdict :**
    *   *Le Problème (Rant) :* La promesse marketing des frigos à 3000€ avec écran géant intégré. La réalité de l'obsolescence programmée (un écran Android obsolète en 3 ans sur un frigo censé durer 15 ans). Le gadget de la caméra interne.
    *   *La Solution (Fix) :* Comment vraiment connecter un frigo intelligemment et utilement pour une famille ? Placer un capteur de température Zigbee à l'intérieur pour les alertes de porte mal fermée. Monitorer la consommation avec une prise connectée (ex: Shelly). Gérer les listes de courses via un vrai dashboard mural (Grocy, Home Assistant) scannant les codes-barres, plutôt que l'écran du frigo.
    *   *Le Verdict :* Faut-il craquer pour un frigo connecté natif ou "domotiser" un frigo standard ?
*   Intégrer 2 à 3 liens internes pertinents. **ATTENTION FORMATAGE : Tous les liens DOIVENT OBLIGATOIREMENT être mis en gras** avec cette syntaxe exacte : `**[Texte du lien](/chemin/vers/article/)**`. Exemples : **[Acceptation par la famille (WAF)](/articles/waf-domotique-acceptation-famille/)** ou **[Créer un dashboard mural](/articles/tablette-murale-domotique-dashboard/)** ou **[Modules Shelly](/articles/shelly-pro-2026/)**.

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
title: "Frigo connecté en 2026 : Révolution pour la famille ou gadget à 3000€ ?"
date: 2026-03-22
tags: ["matériel", "waf-and-famille", "domotique"]
image: "/images/frigo-connecte-famille.webp"
summary: "Le réfrigérateur intelligent promet de métamorphoser la gestion des repas familiaux. Entre l'écran tactile intégré et la réalité du quotidien, découvrez si l'investissement en vaut la peine."
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
    with open("/root/.openclaw/workspace/blog_domotique/site/articles/frigo-connecte-famille.md", "w") as f:
        f.write(response.text)
    print("Article généré avec succès.")

if __name__ == "__main__":
    generate()
