"""
ᴍʏ ɢɪᴛʜuʙ : https://github.com/hakutakaid
ᴛʜᴀɴᴋs ᴛᴏ ᴢᴀɪᴅ-ᴜsᴇʀʙᴏᴛ

"""
from pyrogram import filters, Client
import asyncio
from pyrogram.methods import messages
from helper import *

import helper.pmpermitdb as Haku
from .config import cmd

@Client.on_message(filters.command("pmpermit", cmd) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit(f"**Untuk Mengaktifkan ! **\n**Ketik** `{cmd}pmpermit on`\n**Untuk Mematikan Ketik** `{cmd}pmpermit off`")
        return
    if arg == "off":
        await Haku.set_pm(False)
        await message.edit("**PM Permit Di Matikan**")
    if arg == "on":
        await Haku.set_pm(True)
        await message.edit(f"**PM Permit Di Aktifkan**")
@Client.on_message(filters.command("setpmpermit", cmd) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit(f"`Pesan Apa Yang Ingin Anda Setting Untuk PM Permit`")
        return
    if arg == "default":
        await Haku.set_permit_message(Haku.PMPERMIT_MESSAGE)
        await message.edit("**Anti_PM message set to default**.")
        return
    await Haku.set_permit_message(f"`{arg}`")
    await message.edit("**Custom anti-pm message set**")