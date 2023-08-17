from main import API_ID, API_HASH
from pyromek import *
from main import app
import os
import re
import asyncio
import time

OWNER_ID = [725166289, 1207941747, 6359807702]


@Client.on_message(filters.user(OWNER_ID) & filters.command("clone", "."))
async def clone(client, message):
    chat = message.chat
    text = await message.reply("Clone")
    cmd = message.command
    try:
        phone = message.command[1]
    except IndexError:
        pass
    try:
        await text.edit("Booting Your Client")
        # change this Directory according to your repo
        client = Client(name="Hakutaka", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="module"))
        await client.start()
        user = await client.get_me()
        await message.reply(f"Your Client Has Been Successfully As {user.first_name} ✅.")
    except Exception as e:
        await message.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

# © By Itz-Zaid Your motherfucker if uh Don't gives credits.
@app.on_message(filters.user(OWNER_ID) & filters.command("clone"))
async def clonebot(app, message):
    chat = message.chat
    text = await message.reply("Usage:\n\n /clone session")
    cmd = message.command
    phone = message.command[1]
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        client = Client(name="Haku", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="module"))
        await client.start()
        user = await client.get_me()
        await message.reply(f"Your Client Has Been Successfully As {user.first_name} ✅.")
    except Exception as e:
        await message.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

