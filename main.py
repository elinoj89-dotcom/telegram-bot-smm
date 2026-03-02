import telebot
import json
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from rich.console import Console

# --- CONFIGURATION ---
import config
bot = telebot.TeleBot(config.BOT_TOKEN)
console = Console()
DATA_FILE = "bots.json"

# --- FONCTIONS UTILITAIRES ---
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"keys": {}}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# --- COMMANDES BOT ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Bienvenue ! Utilisez /auth <clé> pour vous connecter.")

@bot.message_handler(commands=['auth'])
def authenticate(message):
    try:
        key = message.text.split()[1]
        data = load_data()
        
        if key in data["keys"] and data["keys"][key]["status"] == "active":
            bot.reply_to(message, "✅ Clé valide ! Accès autorisé.")
            # Ici, tu peux lancer les fonctionnalités du bot
        else:
            bot.reply_to(message, "❌ Clé invalide ou désactivée.")
    except IndexError:
        bot.reply_to(message, "⚠️ Usage: /auth <votre_clé>")

# --- COMMANDES ADMIN ---
@bot.message_handler(commands=['toggle'])
def toggle_key(message):
    if message.from_user.id != config.ADMIN_ID:
        bot.reply_to(message, "🚫 Commande réservée à l'administrateur.")
        return

    try:
        key = message.text.split()[1]
        data = load_data()
        
        if key in data["keys"]:
            new_status = "inactive" if data["keys"][key]["status"] == "active" else "active"
            data["keys"][key]["status"] = new_status
            save_data(data)
            bot.reply_to(message, f"🔄 Clé {key} est maintenant : {new_status}")
        else:
            bot.reply_to(message, "⚠️ Clé introuvable.")
    except IndexError:
        bot.reply_to(message, "⚠️ Usage: /toggle <clé>")

# --- LANCEMENT ---
if __name__ == "__main__":
    console.print("[bold green]🤖 Bot SMM Pro lancé ![/bold green]")
    bot.infinity_polling()
        
