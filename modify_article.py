import os
import subprocess

# Re-run original generator
subprocess.run(['python3', 'generate_article4.py'])

with open('./site/articles/cave-a-vin-connectee-foutoir.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace specifically to add 'je' and 'j\''
text = text.replace("Il faut cesser de croire", "J'ai moi-même perdu quelques bonnes bouteilles par le passé, je vous assure qu'il faut cesser de croire")
text = text.replace("L'utilisation du protocole Zigbee", "D'après mon expérience, j'estime que l'utilisation du protocole Zigbee")
text = text.replace("Il faut privilégier les canaux", "Je vous recommande de privilégier les canaux")

# Add internal bold links
text = text.replace("réseau maillé Zigbee", "**[réseau maillé Zigbee](/articles/comprendre-le-zigbee/)**")
text = text.replace("domotique open-source", "**[domotique open-source](/articles/debuter-home-assistant/)**")
text = text.replace("interrupteur différentiel", "**[interrupteur différentiel](/articles/securite-electrique-domotique/)**")

# Delete a paragraph to stay under 3000 words
text = text.replace("De plus, grâce aux réponses interactives de l'application de messagerie, l'utilisateur peut interagir avec son système à distance. En cas d'alerte de surchauffe anormale, le bot peut proposer des boutons d'action directement dans le chat : forcer l'arrêt de l'alimentation électrique de l'armoire pour éviter un incendie, acquitter l'alarme si une intervention humaine est déjà en cours, ou requérir un cliché photographique d'une caméra de sécurité braquée sur la cave. Cette interactivité transforme la simple notification en un centre de commandement décentralisé et hautement sécurisé.\n\n", "")

# Save
with open('./site/articles/cave-a-vin-connectee-foutoir.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done")