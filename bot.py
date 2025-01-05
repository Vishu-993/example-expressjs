import asyncio
from pyrogram import Client, compose,idle
import os
import pyromod.listen


API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")


bot = Client(

           "InstaLoader",

           bot_token=BOT_TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='public'))
           

bot.run
