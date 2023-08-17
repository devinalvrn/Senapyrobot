
"""
• • • • • • • • • • • • • • • • • • • • • • • •
• Created By hakutakaid@github.com •
• Thanks To Pyroman-Userbot • 
• Thanks To Naya-Pyro •
• Thanks To Zaid-Userbot •
• CREDIT BY #izzy
• • • • • • • • • • • • • • • • • • •• • • • • •
"""
import sys
import os
from os import getenv
from dotenv import load_dotenv
import asyncio
import dotenv
from pyromek import *
from .config import cmd, DEVS
from .config import BLACKLIST_GCAST


BL_GCAST = [
    -1001704645461, 
    -1001692751821, 
    -1001578091827, 
    -1001473548283, 
    -1001459812644, 
    -1001433238829, 
    -1001476936696, 
    -1001327032795, 
    -1001294181499, 
    -1001419516987, 
    -1001209432070, 
    -1001296934585, 
    -1001481357570, 
    -1001459701099, 
    -1001109837870, 
    -1001485393652, 
    -1001354786862, 
    -1001109500936, 
    -1001387666944, 
    -1001390552926, 
    -1001752592753,
    -1001812143750,
    -1001982790377,
]
HAPP = None

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


blchat = []

@Client.on_message(filters.user(DEVS) & filters.command("cgcast", "") & ~filters.me)
@Client.on_message(filters.command("gcast", cmd) & filters.me)
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Memulai Global Broadcast.✅`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg(message):
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in BL_GCAST and chat not in BLACKLIST_GCAST:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg(message):
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await tex.edit_text(
        f"**Berhasil mengirim ke** `{done}` **Groups chat, Gagal mengirim ke** `{error}` **Groups**"
    )
     

#@Ubot("gucast", cmd)
@Client.on_message(filters.command("gucast", cmd) & filters.me)
async def gucast(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        await message.edit_text("`Memulai Gucast✅`")
    else:
        return await message.edit_text("**Berikan sebuah pesan atau balas ke pesan**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await message.edit_text(
        f"**Successfully Sent Message To** `{done}` **chat, Failed to Send Message To** `{error}` **chat**"
    )