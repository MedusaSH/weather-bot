import logging
import re
import requests
import sqlite3
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, filters, CallbackContext
from apscheduler.schedulers.background import BackgroundScheduler
import asyncio


TELEGRAM_TOKEN = ""
KEY = ""


app = Application.builder().token(TELEGRAM_TOKEN).build()
scheduler = BackgroundScheduler()
scheduler.start()


conn = sqlite3.connect("meteo_users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, city TEXT, hour TEXT, minute TEXT)")
conn.commit()


def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={KEY}&q={city}&lang=fr"
    response = requests.get(url)
    data = response.json()

    
    if "error" in data:
        return "❌ Ville non trouvée. Essaye encore !"

  
    if "current" not in data or "temp_c" not in data["current"]:
        return "❌ Impossible de récupérer la météo pour cette ville."

    temp = data["current"]["temp_c"]
    description = data["current"]["condition"]["text"]

   
    if temp >= 7:
        return f"👋 Tu peux te permettre de te passer de ton manteau 🙌 (Température : {temp}°C)"
    elif temp <= 5:
        return f"🛑 Sors pas sans manteau, tu vas attraper la PESTE ! (Température : {temp}°C)"

    return f"🌍 {city.capitalize()} \n🌡 Température : {temp}°C \n⛅ {description}"



async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Salut ! Ce Robot te serviras d'alerte Météo il te previendras a chaque heure:minutes précisé la Météo\n\nVoici les commandes disponibles:\n\n- /setville [Entre la ville pour laquel tu te sers de ce Robot :)] 🌆\n- /setheure [Entre l'heure que tu souhaite pour ton alerte] 🕒\n- /info [Renverra tes Information actuellement définis dans la base de données] 🙎")


async def set_city(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    city = " ".join(context.args)

    if not city:
        await update.message.reply_text("❌ Tu dois indiquer une ville. Ex : /setville Paris")
        return

    cursor.execute("INSERT OR REPLACE INTO users (id, city) VALUES (?, ?)", (user_id, city))
    conn.commit()
    await update.message.reply_text(f"✅ Ville enregistrée : {city}")

async def my_info(update: Update, context: CallbackContext):
    user_id = update.message.chat_id

    cursor.execute("SELECT city, hour, minute FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()

    if result:
        city, hour, minute = result
        await update.message.reply_text(f"📌 Ton profil météo :\n🌆 Ville : {city}\n⏰ Heure d'envoi : {hour}:{minute}")
    else:
        await update.message.reply_text("❌ Tu n'as pas encore enregistré de ville ou d'heure. Utilise `/setville` et `/setheure`.")





async def set_hour(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    hour = " ".join(context.args)

 
    if not re.match(r"^([01]?\d|2[0-3]):([0-5]?\d)$", hour):
        await update.message.reply_text("❌ Donne une heure valide au format HH:MM. Ex : /setheure 22:30")
        return

   
    hour, minute = hour.split(":")
    
    cursor.execute("UPDATE users SET hour = ?, minute = ? WHERE id = ?", (hour, minute, user_id))
    conn.commit()

    await update.message.reply_text(f"✅ Heure enregistrée : {hour}:{minute}")

  
    schedule_jobs()


async def send_daily_weather(user_id, city):
    weather_info = get_weather(city)
    await app.bot.send_message(chat_id=user_id, text=weather_info)


def schedule_jobs():
    cursor.execute("SELECT id, city, hour, minute FROM users WHERE hour IS NOT NULL AND minute IS NOT NULL")
    users = cursor.fetchall()


    scheduler.remove_all_jobs()

    for user_id, city, hour, minute in users:
        scheduler.add_job(
            lambda u_id=user_id, c=city: asyncio.run(send_daily_weather(u_id, c)),  
            "cron",
            hour=int(hour),
            minute=int(minute)
        )


def main():
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setville", set_city))
    app.add_handler(CommandHandler("setheure", set_hour))
    app.add_handler(CommandHandler("info", my_info))

    schedule_jobs()
    
    print("🤖 Bot météo lancé...")
    app.run_polling()

if __name__ == "__main__":
    main()
