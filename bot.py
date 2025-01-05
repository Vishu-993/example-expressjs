import os
from pyrogram import Client, idle
from flask import Flask

app = Flask(__name__)

@app.route('/')
def health_check():
    return 'OK', 200

# Start Flask in the background
import threading
def run_flask():
    app.run(host="0.0.0.0", port=8080)

# Load environment variables
API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Initialize the bot
bot = Client(
    "InstaLoader",  
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

async def main():
    # Start the Flask app in a separate thread
    threading.Thread(target=run_flask).start()
    await bot.start()  # Start the bot
    print("Bot is running...")
    await idle()  # Keep the bot running

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
