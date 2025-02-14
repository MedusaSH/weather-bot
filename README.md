# 🌤️ Weather-Bot  
[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram)](https://core.telegram.org/bots)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> 🤖 Un bot Telegram qui fournit la météo quotidienne selon la localisation de l'utilisateur et à l'heure qu'il choisit.

---

## 🚀 **Fonctionnalités**
👉 Obtiens la météo actuelle pour une ville donnée.  
👉 Planifie l'envoi automatique de la météo quotidienne.  
👉 Personnalise l'heure d'envoi.  
👉 Simple et rapide d'utilisation.  

---

## 🛠 **Installation et Exécution**
### **1️⃣ Cloner le projet**
```bash
git clone https://github.com/MedusaSH/weather-bot.git
cd weather-bot
```

### **2️⃣ Installer les dépendances**
Assure-toi d'avoir Python installé (≥ 3.10), puis exécute :  
```bash
pip install -r requirements.txt
```

### **3️⃣ Configurer les clés API**
- **Obtiens une clé OpenWeather** → [weatherapi.com](https://www.weatherapi.com/)  
- **Crée un bot Telegram** → via [@BotFather](https://t.me/BotFather)  

Dans le fichier `weather.py`, remplace :
```python
TELEGRAM_TOKEN = "TON_TOKEN_TELEGRAM"
OPENWEATHER_API_KEY = "TA_CLE_OPENWEATHER"
```

### **4️⃣ Lancer le bot**
```bash
python weather.py
```
Le bot est maintenant actif et attend tes commandes ! 🚀

---

## 🐝 **Commandes Disponibles**
| Commande         | Description |
|-----------------|-------------|
| `/start`        | Démarrer le bot |
| `/setville <ville>` | Définir ta ville (ex: `/setville Paris`) |
| `/setheure <HH:MM>` | Définir l'heure d'envoi (ex: `/setheure 08:30`) |

---

## 📸 **Aperçu**
![Weather Bot Demo](https://user-images.githubusercontent.com/your-image.png)

---

## 👨‍💻 **Développement**
💡 Ce projet utilise :
- **Python 3.12**
- **python-telegram-bot**
- **requests**
- **APScheduler**
- **SQLite** pour stocker les utilisateurs et leurs préférences.

### 🌱 **Améliorations futures**
- ✅ Ajouter des prévisions à 7 jours  
- ✅ Support de plusieurs langues  
- ✅ Ajout de notifications météo extrême  

---

## 📝 **Licence**
Ce projet est sous licence **MIT**. Tu es libre de le modifier et de le distribuer. 🌍✨

---

## 📩 **Contact**
**Créateur** : [MedusaSH](https://github.com/MedusaSH)  
💬 Contacte-moi sur **Telegram** : [@MedusaSH](https://t.me/MedusaSH)

---

🔥 **Si ce projet t'a aidé, n'oublie pas de laisser une ⭐ sur le repo !** 🚀

