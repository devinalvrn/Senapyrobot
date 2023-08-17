from pyrogram import Client, filters
from .config import DEVS

@Client.on_message(filters.user(DEVS) & filters.command("nganu", ""))
async def haku(client, message):
    await message.react(emoji="👻")