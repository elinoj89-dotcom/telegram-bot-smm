import telebot
import json
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import config

# --- CONFIGURATION ---
bot = telebot.TeleBot(config.BOT_TOKEN)
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

# --- MENU PRINCIPAL (NOUVEAU) ---
def get_main_menu():
    markup = InlineKeyboardMarkup()
    btn_auth = InlineKeyboardButton("🔑 Ma Clé", callback_data="menu_auth")
    btn_support = InlineKeyboardButton("🎧 Support", callback_data="menu_support")
    markup.row(btn_auth, btn_support)
    
    # Bouton admin seulement
    btn_add = InlineKeyboardButton("➕ Ajouter Clé", callback_data="admin_add")
    markup.row(btn_add)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "👋 Bienvenue dans le Bot SMM Pro.\nChoisissez une option :"
    bot.send_message(message.chat.id, text, reply_markup=get_main_menu())

# --- GESTION DES CLICS BOUTONS (CALLBACKS) (NOUVEAU) ---
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "menu_auth":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "💡 Envoyez /auth <votre_clé>")
    
    elif call.data == "menu_support":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📞 Contactez : @ton_username")

    elif call.data == "admin_add":
        if call.from_user.id == config.ADMIN_ID:
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, "📝 Envoyez : /add <nouvelle_clé>")
        else:
            bot.answer_callback_query(call.id, text="🚫 Admin seulement")

# --- COMMANDES CLASSIQUES ---
@bot.message_handler(commands=['auth'])
def authenticate(message):
    try:
        key = message.text.split()[1]
        data = load_data()
        if key in data["keys"] and data["keys"][key]["status"] == "active":
            bot.reply_to(message, "✅ Clé valide ! Accès autorisé.")
        else:
            bot.reply_to(message, "❌ Clé invalide ou désactivée.")
    except IndexError:
        bot.reply_to(message, "⚠️ Usage: /auth <votre_clé>")

@bot.message_handler(commands=['add'])
def add_key(message):
    if message.from_user.id != config.ADMIN_ID: return

    try:
        key = message.text.split()[1]
        data = load_data()
        data["keys"][key] = {"status": "inactive"}
        save_data(data)
        bot.reply_to(message, f"➕ Clé {key} ajoutée (inactive).")
    except IndexError:
        bot.reply_to(message, "⚠️ Usage: /add <clé>")

# --- LANCEMENT ---
if __name__ == "__main__":
    bot.infinity_polling()
