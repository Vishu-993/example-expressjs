import os
import asyncio
from pyrogram import Client, idle
import pyromod.listen

# Load environment variables
API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Initialize the bot with required credentials
bot = Client(
    "InstaLoader",          # Name of the session
    bot_token=BOT_TOKEN,    # Bot token
    api_id=API_ID,          # API ID
    api_hash=API_HASH       # API Hash
)

# Run the bot
async def main():
    await bot.start()      # Start the bot asynchronously
    print("Bot is running...")
    await idle()           # Keep the bot running

# Run the bot using asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
