"""
• • • • • • • • • • • • • • • • • • • • • • • •
• Created By hakutakaid@github.com •
• Thanks To Pyroman-Userbot • 
• Thanks To Naya-Pyro •
• Thanks To Zaid-Userbot •
• • • • • • • • • • • • • • • • • • •• • • • • •
"""
import os
from pyromek import *
from .config import *

@Client.on_message(filters.me & filters.command("delbl", cmd))
async def delete_file_command(client, message):
    try:
        os.remove("gcast.env")
        await message.reply(f"Berhasil Di Hapus")
    except Exception as e:
        await message.reply(f"Maaf Tidak Ada Blacklist Gcast")