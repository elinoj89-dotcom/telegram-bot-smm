# --- COMMANDES ADMIN ---
@bot.message_handler(commands=['activate'])
def activate_key(message):
    # Vérifie si c'est toi l'admin
    if message.from_user.id != config.ADMIN_ID:
        bot.reply_to(message, "🚫 Commande réservée à l'administrateur.")
        return

    try:
        key = message.text.split()[1]
        data = load_data()
        
        if key in data["keys"]:
            data["keys"][key]["status"] = "active"
            save_data(data)
            bot.reply_to(message, f"✅ Clé {key} activée avec succès.")
        else:
            bot.reply_to(message, "⚠️ Clé introuvable.")
    except IndexError:
        bot.reply_to(message, "⚠️ Usage: /activate <clé>")

@bot.message_handler(commands=['deactivate'])
def deactivate_key(message):
    if message.from_user.id != config.ADMIN_ID:
        bot.reply_to(message, "🚫 Commande réservée à l'administrateur.")
        return

    try:
        key = message.text.split()[1]
        data = load_data()
        
        if key in data["keys"]:
            data["keys"][key]["status"] = "inactive"
            save_data(data)
            bot.reply_to(message, f"❌ Clé {key} désactivée avec succès.")
        else:
            bot.reply_to(message, "⚠️ Clé introuvable.")
    except IndexError:
        bot.reply_to(message, "⚠️ Usage: /deactivate <clé>")
        
