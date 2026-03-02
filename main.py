import json
import asyncio
from telegram.ext import ApplicationBuilder
from scripts.handlers import register  # fonctions pour /start et auto-reply

async def main():
    # Charger tous les bots depuis bots.json
    with open("bots.json") as f:
        bots = json.load(f)

    apps = []
    for bot in bots:
        # Créer une application pour chaque bot
        app = ApplicationBuilder().token(bot["8604971770:AAH_N3tJuiWbERYHBWi1SgPSKkcPDk5_zQI"]).build()
        
        # Ajouter les handlers (commandes /start, réponses automatiques)
        register(app)
        
        # Démarrer le bot
        await app.initialize()
        await app.start()
        print(f"✅ {bot['elino1000_bot']} actif")
        apps.append(app)

    # Garde tous les bots actifs
    await asyncio.Event().wait()

if __elino1000_bot__ == "__main__":
    asyncio.run(main())
